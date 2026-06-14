# IR Research Architect Skill

> Turn an international relations topic into a research design that is answerable, testable, and writable.

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-green)](https://agentskills.io)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue)](#installation)
[![Research Methods](https://img.shields.io/badge/IR-Research%20Methods-purple)](#what-it-helps-with)

IR Research Architect is an Agent Skill for international relations, political science, national security studies, and area studies. It organizes a paraphrased methods knowledge base into a practical workflow:

`topic -> research question -> literature-review design -> causal explanation -> hypotheses -> variables -> operationalization -> hypothesis testing -> thesis structure`

It does not search the web for literature and does not invent citations. It helps structure the topic, notes, sources, and research materials the user already has.

## Installation

```bash
git clone https://github.com/Y02-26/ir-research-architect-skill ~/.codex/skills/ir-research-architect
```

Windows PowerShell:

```powershell
git clone https://github.com/Y02-26/ir-research-architect-skill "$env:USERPROFILE\.codex\skills\ir-research-architect"
```

## Example Prompts

```text
Use IR Research Architect to turn "US-China technology competition" into a feasible thesis topic.
```

```text
Use IR Research Architect to revise my hypothesis and list alternative explanations.
```

```text
Use IR Research Architect to organize these reading notes into a literature-review design.
```

## What It Helps With

| Capability | What it does |
|---|---|
| Topic narrowing | Turns a broad area into a concrete phenomenon, case range, time frame, and puzzle. |
| Research questions | Produces clear, meaningful, answerable why/how/under-what-conditions questions. |
| Literature-review design | Organizes user-provided sources into debate maps, explanation types, and gaps. |
| Causal explanation | Builds X -> mechanism -> Y explanations with counterfactuals, scope conditions, and alternatives. |
| Hypotheses | Turns ideas into directional, conditional, testable causal hypotheses. |
| Variables | Distinguishes independent, dependent, mediating, moderating, confounding, collider, and control variables. |
| Operationalization | Turns concepts into dimensions, indicators, data sources, and coding rules. |
| Hypothesis testing | Designs case comparison, process tracing, quantitative tests, or mixed-method strategies. |
| Thesis structure | Organizes introduction, literature, theory, method, empirical chapters, and conclusion. |

## Repository Structure

```text
ir-research-architect-skill/
|-- SKILL.md
|-- agents/
|   `-- openai.yaml
|-- references/
|   |-- knowledge-map.md
|   |-- research-workflow.md
|   |-- research-orientation.md
|   |-- question-and-literature.md
|   |-- causal-explanation.md
|   |-- operationalization-measurement.md
|   |-- hypothesis-testing.md
|   |-- thesis-writing.md
|   `-- checklists.md
`-- scripts/
    `-- ir_research_design.py
```

## Quick Scaffold

```bash
python scripts/ir_research_design.py --topic "US-China technology competition" --out design.md
python scripts/ir_research_design.py --topic "regional organizations and conflict mediation" --mode checklist
```

## Boundaries

- This is a methods assistant, not a substitute for supervisors, peer review, or source collection.
- It does not conduct literature search by itself.
- Literature-review outputs should be based on user-provided sources or a separate explicit search workflow.
- The knowledge base is paraphrased from OCR-assisted notes; exact wording and page references should be checked against the original book.
- The repository does not contain the original PDF or the full book text.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Y02-26/ir-research-architect-skill&type=Date)](https://www.star-history.com/#Y02-26/ir-research-architect-skill&Date)
