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

Diagnostic prompts:

- What is the observable phenomenon, not only the broad field?
- What varies across cases, actors, or time?
- Why is this pattern surprising relative to theory, expectation, or another case?
- What evidence could realistically be collected?

Common mistakes:

- Treating a country relation, region, or issue area as a research question.
- Starting from a preferred conclusion rather than an observed puzzle.
- Making the scope so broad that no evidence strategy can cover it.

## 2. Research Question

| Item | Draft |
|---|---|
| Research puzzle | |
| Core question | |
| Outcome / dependent variable Y | |
| Cases and time frame | |
| Question type | why / how / under what conditions / with what effect |
| Answerability evidence | |

Question repair pattern:

```text
Why/how/under what conditions does [X or mechanism] affect [Y] in [cases/time]?
```

Common mistakes:

- Asking several questions without one main Y.
- Asking a normative policy question when the project needs explanation.
- Asking a question whose answer is already assumed in the wording.

## 3. Literature-Review Design

Use only user-provided sources, abstracts, bibliographies, excerpts, or reading notes. Do not invent citations.

| Provided source | Question addressed | Core explanation | Method/evidence | Scope | Limitation | Use in this project |
|---|---|---|---|---|---|---|
| | | | | | | |

Literature-review design prompts:

- Which explanations compete with each other?
- Which sources share a mechanism, assumption, or method?
- Which gap is conceptual, causal, empirical, methodological, or scope-related?
- How does this project build on strengths rather than only criticize limits?

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

Mechanism diagnostics:

- Who are the actors or entities in each step?
- What changes: beliefs, incentives, resources, information, institutions, or constraints?
- Why does each step generate the next step?
- What evidence would we observe if this step occurred?
- What rival mechanism would predict a different trace?

## 5. Hypotheses

| Hypothesis | Direction/condition | Mechanism | Observable implication | Possible disconfirming evidence |
|---|---|---|---|---|
| H1 | | | | |
| H2 | | | | |
| Alternative hypothesis | | | | |

Hypothesis repair pattern:

```text
H1: When [scope condition], higher/lower [X] increases/decreases [Y] because
[mechanism]. If this is correct, we should observe [observable implication].
```

## 6. Variables

| Variable | Role | Conceptual definition | Expected role | Link to mechanism | Possible indicators |
|---|---|---|---|---|---|
| Y | Dependent variable | | | | |
| X | Independent variable | | | | |
| M | Mediator/mechanism element | | | | |
| C | Confounder/control | | | | |
| D | Collider, if relevant | Common result of X and Y in the book's Figure 5.5 pattern | Do not control casually | | |

Variable diagnostics:

- Is X measured before Y?
- Is M a mechanism step rather than a control variable?
- Is any proposed control actually a mediator or collider?
- Does each variable have a conceptual definition before indicators are chosen?

## 7. Operationalization And Measurement

| Concept | Definition | Dimensions | Indicators | Data source | Coding rule | Validity risk | Reliability check |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Operationalization diagnostics:

- Does the indicator measure the concept or only a convenient proxy?
- Would another coder apply the rule in the same way?
- Is the measure comparable across cases and time?
- What missing data or source bias could change the conclusion?

## 8. Hypothesis Testing

| Hypothesis | Observable implication | Evidence/data | Method | Alternative explanation | Support criterion | Disconfirming evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

Testing diagnostics:

- Does the method match the hypothesis?
- What would support the mechanism, not only the X-Y association?
- What evidence would weaken the claim?
- How will the design address alternative explanations?
- Are cases selected because they are theoretically useful, not merely familiar?

## 9. Thesis Structure

1. Introduction: puzzle, question, argument, method, contribution.
2. Literature review: explanation types, debate map, gap.
3. Theory: concepts, causal mechanism, hypotheses.
4. Research design: cases/data, variables, operationalization, method.
5. Empirical analysis: evidence organized around hypotheses or mechanism steps.
6. Conclusion: answer the question, state contribution, limits, implications.

Chapter-level checks:

- Introduction creates the puzzle and states the answer.
- Literature review maps debates and opens the gap.
- Theory turns the gap into a mechanism and hypotheses.
- Method explains how evidence can evaluate the hypotheses.
- Empirical chapters test claims rather than only narrate events.
- Conclusion separates support, uncertainty, limits, and implications.
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

## Common Failure Signals

- [ ] The draft has a topic but no puzzle.
- [ ] The research question contains several dependent variables.
- [ ] The literature review lists authors instead of explanation families.
- [ ] The mechanism jumps from X to Y without actors, activities, or sequence.
- [ ] Hypotheses are too vague to be wrong.
- [ ] Indicators are chosen before concepts are defined.
- [ ] Controls are added without checking mediators or colliders.
- [ ] Evidence is organized only by chronology.
- [ ] The conclusion says "prove" when the design only supports a claim.

## Repair Moves

- Narrow the topic by actor, outcome, time, place, and variation.
- Rewrite the question around one main Y.
- Group literature by explanation type, mechanism, method, evidence, or scope.
- Add a stepwise mechanism with observable implications.
- Rewrite hypotheses with direction, condition, mechanism, and failure evidence.
- Build an operationalization table before collecting data.
- Draw a causal diagram before deciding controls.
- Organize empirical sections by hypothesis or mechanism step.
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
