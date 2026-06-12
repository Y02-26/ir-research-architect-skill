---
name: guoji-guanxi-yanjiu-fangfa
description: Practical international relations research-methods assistant based on the book "国际关系研究实用方法（第三版）". Use when helping with IR/political science research design, topic selection, organizing user-provided literature notes or bibliographies into review structures, causal explanation, hypothesis building, concept operationalization, measurement, variable control, qualitative or quantitative hypothesis testing, proposal design, thesis structure, academic writing, footnotes, references, or policy-research framing. Do not use as a literature-search skill or to invent real citations.
---

# 国际关系研究实用方法

Use this skill to help a user turn an international relations or political science idea into a rigorous, testable research design and thesis/report structure. The bundled knowledge base is an OCR-assisted, paraphrased synthesis of 孙学峰、阎学通、张聪《国际关系研究实用方法（第三版）》, organized for agent use. It does not include the full book text.

## Core Workflow

Treat research design as a sequence:

1. Clarify whether the task is **theoretical research**, **policy research**, or a mixed project.
2. Move through the full chain: **topic -> research question -> literature-review design -> causal explanation -> hypotheses -> variables -> operationalization -> hypothesis testing -> thesis structure**.
3. Keep each link explicit. Do not let a topic substitute for a question, a mechanism substitute for a hypothesis, or a variable name substitute for operationalization.
4. Produce a concrete artifact at the end: research design table, proposal outline, causal diagram, variable/measurement table, testing plan, or revision checklist.

## Reference Selection

Load only the reference needed for the user's current task:

- `references/knowledge-map.md`: Read first for book structure, OCR caveats, and which file to open.
- `references/research-workflow.md`: Use for end-to-end research design across topic, research question, literature-review design, causal explanation, hypotheses, variables, operationalization, testing, and thesis structure.
- `references/research-orientation.md`: Use for theory vs policy research, scientific method, limits of IR research, and research quality standards.
- `references/question-and-literature.md`: Use for choosing topics, forming research puzzles/questions, and organizing user-provided literature materials into review structures. It does not provide literature search.
- `references/causal-explanation.md`: Use for causal diagrams, mechanisms, causal hypotheses, variable roles, and rival explanations.
- `references/operationalization-measurement.md`: Use for concept operationalization, indicators, measurement level, validity, and reliability.
- `references/hypothesis-testing.md`: Use for qualitative/quantitative testing logic, case comparison, process tracing, variable control, and common inference errors.
- `references/thesis-writing.md`: Use for proposal and thesis/report structure, academic writing, notes, references, appendix, and index-like elements.
- `references/checklists.md`: Use when the user wants critique, revision, grading, or a compact checklist.

## How To Respond

- Work in Chinese by default unless the user asks otherwise.
- Prefer turning abstract advice into a concrete artifact: a research question, hypothesis set, variable table, causal graph in text/Mermaid, literature-material matrix based on user-provided sources, proposal outline, or revision checklist.
- Ask for the user's topic, cases, time period, dependent variable, and target output only when missing context prevents useful progress.
- If the user already has a draft, diagnose it against the workflow instead of rewriting blindly.
- For literature-review tasks, ask the user to provide article titles, abstracts, notes, bibliographies, or pasted excerpts. Do not invent citations or claim to have searched literature unless a separate web/academic-search workflow is explicitly used.
- Separate **research question**, **causal explanation**, **hypothesis**, **operationalization**, and **test strategy**. Do not let one substitute for another.
- State uncertainty when source text was OCR-derived or when a recommendation is a methodological inference rather than a direct book point.

## Reusable Script

Use `scripts/ir_research_design.py` to generate a structured research design scaffold or checklist:

```bash
python scripts/ir_research_design.py --topic "中美技术竞争" --out design.md
python scripts/ir_research_design.py --topic "地区组织与冲突调停" --mode checklist
```

Read or patch the script if a user needs a customized template.
