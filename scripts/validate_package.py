#!/usr/bin/env python3
"""Static checks for the standalone Baimiao Skill."""

from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "LICENSE",
    "README.md",
    "PRODUCT.md",
    "agents/openai.yaml",
    "references/guided-methods.md",
    "references/review-rubric.md",
    "tests/glm-cases.json",
    "tests/glm-results.json",
    "tests/glm-evaluation-report.md",
    "scripts/run_glm_evaluation.py",
    "showcase/index.html",
    "assets/baimiao-writing-hero.png",
    "assets/baimiao-writing-hero.prompt.md",
]
FORBIDDEN_PUBLIC = (
    "SAY",
    "SHOW",
    "PRIVATE",
    "GAP",
    "自然口播",
    "说话人：",
    "观众：",
)


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or not re.search(r"(?m)^name:\s*baimiao\s*$", skill):
        errors.append("invalid SKILL.md frontmatter")
    for phrase in ("默认只需要原文", "硬门", "二十五种", "零新增", "默认只输出"):
        if phrase not in skill:
            errors.append(f"SKILL.md missing contract: {phrase}")

    public_paths = [ROOT / "SKILL.md", ROOT / "README.md", ROOT / "showcase/index.html"]
    for path in public_paths:
        text = path.read_text(encoding="utf-8")
        for token in FORBIDDEN_PUBLIC:
            if token in text:
                errors.append(f"obsolete video contract in {path.relative_to(ROOT)}: {token}")
        for secret in ("/home/wang", "sk-"):
            if secret in text:
                errors.append(f"private token in {path.relative_to(ROOT)}: {secret}")

    cases = json.loads((ROOT / "tests/glm-cases.json").read_text(encoding="utf-8"))
    results = json.loads((ROOT / "tests/glm-results.json").read_text(encoding="utf-8"))
    if len(cases) != 8 or len(results.get("results", [])) != 8:
        errors.append("GLM regression suite must contain 8 cases and 8 results")
    contract = results.get("request_contract", {})
    if contract.get("max_tokens") != "omitted" or contract.get("client_timeout") != "not_set":
        errors.append("GLM request contract changed")
    notice = next((item for item in results.get("results", []) if item.get("id") == "constraint-notice"), None)
    if notice and notice.get("input") != notice.get("output"):
        errors.append("high-constraint notice was modified")

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print(json.dumps({"status": "PASS", "glm_cases": 8, "high_constraint": "unchanged", "license": "Apache-2.0"}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
