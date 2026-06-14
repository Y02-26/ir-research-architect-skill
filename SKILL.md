---
name: ir-research-architect
description: International relations and political science research-design assistant based on a paraphrased methods knowledge base from Practical Methods for International Relations Research, 3rd edition. Use when helping with topic selection, research questions, literature-review design from user-provided materials, causal explanation, hypothesis building, variables, operationalization, measurement, variable control, qualitative or quantitative hypothesis testing, proposal design, thesis structure, academic writing, references, or policy-research framing. Do not use as a literature-search skill or to invent real citations.
---

# IR Research Architect

Use this skill to help a user turn an international relations or political science idea into a rigorous, answerable, testable research design and thesis/report structure.

The bundled knowledge base is an OCR-assisted, paraphrased synthesis of a Chinese-language IR methods textbook. It does not include the full book text, and it should not quote the source at length.

## Core Workflow

Treat research design as a linked sequence:

1. Clarify whether the task is theoretical research, policy research, or a mixed project.
2. Move through the full chain: topic -> research question -> literature-review design -> causal explanation -> hypotheses -> variables -> operationalization -> hypothesis testing -> thesis structure.
3. Keep each link explicit. Do not let a topic substitute for a research question, a mechanism substitute for a hypothesis, or a variable name substitute for operationalization.
4. Produce a concrete artifact: research-design table, proposal outline, causal diagram, mechanism chain, variable/measurement table, testing plan, or revision checklist.

## Reference Selection

Load only the reference needed for the current task:

- `references/knowledge-map.md`: Read first for source scope, OCR caveats, and routing.
- `references/research-workflow.md`: Use for end-to-end research design from topic to thesis structure.
- `references/research-orientation.md`: Use for theory vs policy research, scientific method, research quality, and limits of IR research.
- `references/question-and-literature.md`: Use for topic narrowing, research puzzles/questions, and literature-review design based on user-provided sources. It does not provide literature search.
- `references/causal-explanation.md`: Use for causal relations, causal diagrams, mechanisms, counterfactuals, scope conditions, collider/confounder/mediator distinctions, causal hypotheses, and hypothesis revision.
- `references/operationalization-measurement.md`: Use for concept definition, dimensions, indicators, measurement levels, validity, and reliability.
- `references/hypothesis-testing.md`: Use for qualitative/quantitative testing logic, case selection, process tracing, controls, uncertainty, and inference errors.
- `references/thesis-writing.md`: Use for proposal/thesis structure, academic writing, notes, references, appendix, and final organization.
- `references/checklists.md`: Use when the user wants critique, grading, or compact revision guidance.

## Response Rules

- Respond in the user's language unless they ask otherwise. The skill files are in English to avoid encoding problems.
- For literature-review tasks, organize only user-provided titles, abstracts, bibliographies, excerpts, or reading notes. Do not invent citations or claim to have searched literature unless a separate search workflow is explicitly used.
- Separate research question, causal explanation, hypothesis, operationalization, and testing strategy.
- Start from the dependent variable/outcome when building causal explanations.
- Mark source-derived points vs methodological additions when precision matters.
- State uncertainty when a point is inferred from OCR-derived notes rather than directly verified source text.

## Reusable Script

Use `scripts/ir_research_design.py` to generate a research-design scaffold or checklist:

```bash
python scripts/ir_research_design.py --topic "US-China technology competition" --out design.md
python scripts/ir_research_design.py --topic "regional organizations and conflict mediation" --mode checklist
```

Patch the script if the user needs a customized template.
