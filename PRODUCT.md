# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

需要把中文初稿改得自然、准确、有分寸和文采，同时保持原文用途的人。

## Product Purpose

白描接收一段中文，保留原意、事实和文体，通过取舍、重排、节奏与措辞润色，输出更成熟的人类写作版本。

## Positioning

白描是独立的通用中文改写与文采润色 Skill。清理 AI 痕迹只是其常见用途之一；用户通常只需提供原文。

## Operating Context

适用于文章、邮件、报告、产品介绍、社交媒体、知识解释、观点评论、故事和普通段落。

## Capabilities and Constraints

- 先检查高约束文字，再决定是否改写。
- 锁定事实、观点、数字、因果、责任与确定程度。
- 根据原文问题选择少量写作手法。
- 不增加原文没有提供的动作、场景、数字、引语、心理或情绪。
- 医疗、法律、安全、合同与责任文字默认逐字返回。
- 不负责事实研究、视频策划、配音、画面制作或发布。

## Brand Commitments

产品名为“白描 / Baimiao”。表达自然、克制、具体，不说教，不堆金句，不批量使用“不是……而是……”。

## Evidence on Hand

- `tests/glm-results.json`：GLM-5.2 的 8 类文本实测输出。
- `references/guided-methods.md`：25 种手法的信号、案例与撤销条件。
- 测试结论仅覆盖现有样本，不能代表所有模型和全部文体。

## Product Principles

- 先保真，再润色。
- 只改表达，不编事实。
- 文体各自成立，不统一改成口播。
- 手法由问题触发，没有信号就不用。
- 不改同样是一种正确结果。
