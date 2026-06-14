#!/usr/bin/env python3
"""Generate an international-relations research-design scaffold or checklist."""

from __future__ import annotations

import argparse
from pathlib import Path


def scaffold(topic: str) -> str:
    return f"""# International Relations Research Design Draft

## Topic

{topic}

## 1. Topic Narrowing

| Item | Draft |
|---|---|
| Initial topic | {topic} |
| Concrete phenomenon | |
| Actors/cases | |
| Time frame | |
| Spatial scope | |
| Variation, change, or anomaly | |
| Available evidence | |
| Research value | |

## 2. Research Question

| Item | Draft |
|---|---|
| Research puzzle | |
| Core question | |
| Outcome / dependent variable Y | |
| Cases and time frame | |
| Question type | why / how / under what conditions / with what effect |
| Answerability evidence | |

## 3. Literature-Review Design

Use only user-provided sources, abstracts, bibliographies, excerpts, or reading notes. Do not invent citations.

| Provided source | Question addressed | Core explanation | Method/evidence | Scope | Limitation | Use in this project |
|---|---|---|---|---|---|---|
| | | | | | | |

## 4. Causal Explanation

| Element | Draft |
|---|---|
| Cause / independent variable X | |
| Outcome / dependent variable Y | |
| Mediator or mechanism M | |
| Scope condition, if needed | |
| Alternative explanation | |
| Observable implication | |

Mechanism chain:

```text
X changes an actor's beliefs, incentives, resources, information, or constraints.
The actor chooses a strategy or behavior.
That behavior changes an interaction pattern, institution, or resource distribution.
The changed condition produces Y.
```

## 5. Hypotheses

| Hypothesis | Direction/condition | Mechanism | Observable implication | Possible disconfirming evidence |
|---|---|---|---|---|
| H1 | | | | |
| H2 | | | | |
| Alternative hypothesis | | | | |

## 6. Variables

| Variable | Role | Conceptual definition | Expected role | Link to mechanism | Possible indicators |
|---|---|---|---|---|---|
| Y | Dependent variable | | | | |
| X | Independent variable | | | | |
| M | Mediator/mechanism element | | | | |
| C | Confounder/control | | | | |
| D | Collider, if relevant | Common result of X and Y in the book's Figure 5.5 pattern | Do not control casually | | |

## 7. Operationalization And Measurement

| Concept | Definition | Dimensions | Indicators | Data source | Coding rule | Validity risk | Reliability check |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 8. Hypothesis Testing

| Hypothesis | Observable implication | Evidence/data | Method | Alternative explanation | Support criterion | Disconfirming evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

## 9. Thesis Structure

1. Introduction: puzzle, question, argument, method, contribution.
2. Literature review: explanation types, debate map, gap.
3. Theory: concepts, causal mechanism, hypotheses.
4. Research design: cases/data, variables, operationalization, method.
5. Empirical analysis: evidence organized around hypotheses or mechanism steps.
6. Conclusion: answer the question, state contribution, limits, implications.
"""


def checklist(topic: str) -> str:
    return f"""# Research Design Checklist

Topic: {topic}

- [ ] The topic is narrower than a field and broader than a single fact.
- [ ] The puzzle identifies an anomaly, contrast, change, or unresolved debate.
- [ ] The research question is clear, meaningful, and answerable.
- [ ] The dependent variable Y is explicit.
- [ ] The proposed cause X is explicit.
- [ ] Temporal order is plausible: X precedes Y.
- [ ] The causal mechanism is a chain of entities, activities, and generative links.
- [ ] Scope conditions are stated when the hypothesis is not universal.
- [ ] Alternative explanations and confounders are considered.
- [ ] Colliders are drawn accurately; in the book's Figure 5.5 pattern, X -> Y, X -> D, and Y -> D.
- [ ] Concepts are defined before indicators are selected.
- [ ] Operationalization includes dimensions, indicators, sources, and coding rules.
- [ ] Method and evidence match the hypothesis.
- [ ] The design names what evidence would weaken or falsify the hypothesis.
- [ ] Each thesis chapter serves the research question.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True, help="Research topic")
    parser.add_argument("--mode", choices=["scaffold", "checklist"], default="scaffold")
    parser.add_argument("--out", help="Optional output file")
    args = parser.parse_args()

    text = scaffold(args.topic) if args.mode == "scaffold" else checklist(args.topic)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
