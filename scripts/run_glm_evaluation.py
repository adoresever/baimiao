#!/usr/bin/env python3
"""Run independent Baimiao rewrite cases against an OpenAI-compatible API."""

from __future__ import annotations

import json
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES_PATH = ROOT / "tests/glm-cases.json"
RESULTS_PATH = ROOT / "tests/glm-results.json"


def load_skill() -> str:
    parts = [
        ROOT / "SKILL.md",
        ROOT / "references/guided-methods.md",
        ROOT / "references/review-rubric.md",
    ]
    return "\n\n".join(path.read_text(encoding="utf-8") for path in parts)


def rewrite(case: dict[str, str], skill: str, base_url: str, api_key: str, model: str) -> dict:
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "你正在执行下面这份完整的白描 Skill。严格遵循它。\n\n" + skill},
            {"role": "user", "content": f"文体：{case['genre']}\n\n请改写下面的文字，只输出改写后的完整文本：\n\n{case['input']}"},
        ],
        "temperature": 0.25,
    }
    request = urllib.request.Request(
        base_url.rstrip("/") + "/chat/completions",
        data=json.dumps(payload, ensure_ascii=False).encode("utf-8"),
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request) as response:
        data = json.loads(response.read().decode("utf-8"))
    return {**case, "output": data["choices"][0]["message"]["content"].strip(), "usage": data.get("usage", {})}


def main() -> int:
    api_key = os.environ.get("ADORE_API_KEY")
    if not api_key:
        raise SystemExit("ADORE_API_KEY is required")
    base_url = os.environ.get("ADORE_BASE_URL", "https://api.adoresever.com/v1")
    model = os.environ.get("ADORE_MODEL", "GLM-5.2")
    skill = load_skill()
    cases = json.loads(CASES_PATH.read_text(encoding="utf-8"))
    results: list[dict] = []
    with ThreadPoolExecutor(max_workers=4) as pool:
        futures = {pool.submit(rewrite, case, skill, base_url, api_key, model): case["id"] for case in cases}
        for future in as_completed(futures):
            results.append(future.result())
    order = {case["id"]: index for index, case in enumerate(cases)}
    results.sort(key=lambda item: order[item["id"]])
    report = {
        "model": model,
        "base_url": base_url,
        "request_contract": {
            "max_tokens": "omitted",
            "client_timeout": "not_set",
            "skill_files": ["SKILL.md", "references/guided-methods.md", "references/review-rubric.md"],
        },
        "created_at": datetime.now(timezone.utc).isoformat(),
        "results": results,
    }
    RESULTS_PATH.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"status": "completed", "model": model, "cases": len(results), "results": str(RESULTS_PATH)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
