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


def question(topic: str, lang: str) -> str:
    if lang == "zh":
        return f"""# 从主题到研究问题

## 初始主题

{topic}

## 先不要写假设

第一步不是直接提出自变量或因果机制，而是先确定要解释的结果：因变量 / 待解释结果 Y。

## 可能的待解释结果

| 可能的 Y | 可观察的变化或差异 | 可能证据 |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

## 候选研究问题

| 类型 | 研究问题草案 | 还缺什么信息 |
|---|---|---|
| Why 问题 | 为什么 [Y] 在 [案例/时间] 中出现差异？ | |
| How 问题 | [过程/因素] 如何影响 [Y]？ | |
| 条件问题 | 在什么条件下，[X] 更可能导致 [Y]？ | |

## 诊断问题

- 这个主题现在是研究领域、政策议题，还是已经有明确的研究问题？
- 你真正想解释的结果是什么？
- 这个结果是否在国家、组织、事件、时间段或政策领域之间存在差异？
- 哪个结果最容易找到证据？
- 选择这个结果后，案例和时间范围应该如何收窄？

## 下一步

先选择一个待解释结果 Y，再讨论自变量 X、因果机制 M、范围条件和假设。不要把其他案例或示例中的机制直接搬到这个主题上。
"""

    return f"""# From Topic To Research Question

## Initial Topic

{topic}

## Do Not Write Hypotheses Yet

First identify the outcome to explain: the dependent variable / outcome Y.

## Possible Outcomes

| Possible Y | Observable variation | Possible evidence |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

## Candidate Research Questions

| Type | Draft question | Missing information |
|---|---|---|
| Why question | Why does [Y] vary across [cases/time]? | |
| How question | How does [process/factor] affect [Y]? | |
| Conditional question | Under what conditions does [X] produce [Y]? | |

## Next Step

Choose one outcome before discussing independent variables or causal mechanisms. Do not reuse mechanisms from other cases.
"""


def diagnose(topic: str, lang: str) -> str:
    if lang == "zh":
        return f"""# 研究设计诊断表

主题或草稿：{topic}

先找最弱环节，再修改文本。

| 环节 | 诊断问题 | 当前问题 | 修正动作 |
|---|---|---|---|
| 主题 | 是否只是领域标签？ | | 收窄到行动者、结果、时间、空间和变化。 |
| 研究问题 | 因变量 / 待解释结果 Y 是否清楚？ | | 先列出可能 Y，再选择一个。 |
| 文献综述设计 | 是否只是作者罗列？ | | 按解释类型、机制、方法、证据和局限分组。 |
| 因果解释 | 是否有机制，而不只是理论标签？ | | 从行动者、激励、信念、资源、信息、约束重建机制。 |
| 假设 | 是否有方向、条件和可检验证据？ | | 改成可被证据支持或削弱的句子。 |
| 变量 | 自变量、因变量、中介、混杂、撞子是否区分？ | | 先画因果图，再决定变量角色。 |
| 操作化 | 概念是否转成指标和编码规则？ | | 写定义、维度、指标、来源、规则、效度风险。 |
| 检验 | 是否只找支持证据？ | | 写出替代解释和反驳证据。 |
| 结构 | 章节是否服务研究问题？ | | 按问题、文献、理论、方法、证据、结论重排。 |
"""

    return f"""# Research Design Diagnosis

Topic or draft: {topic}

Find the weakest link before rewriting.

| Link | Diagnostic question | Current problem | Repair move |
|---|---|---|---|
| Topic | Is this only a field label? | | Narrow actor, outcome, time, place, and variation. |
| Research question | Is the dependent variable/outcome Y clear? | | List possible Y values, then choose one. |
| Literature-review design | Is this only author-by-author summary? | | Group by explanation, mechanism, method, evidence, and limitation. |
| Causal explanation | Is there a mechanism, not only a theory label? | | Rebuild from actors, incentives, beliefs, resources, information, and constraints. |
| Hypotheses | Are direction, condition, and observable implication clear? | | Make the claim testable and able to fail. |
| Variables | Are X, Y, mediator, confounder, and collider separated? | | Draw a causal diagram before deciding controls. |
| Operationalization | Are concepts translated into indicators and coding rules? | | Define dimensions, indicators, sources, rules, and validity risks. |
| Testing | Does the design seek only confirming evidence? | | Add alternatives and disconfirming evidence. |
| Structure | Does every chapter serve the question? | | Reorder around question, literature, theory, method, evidence, conclusion. |
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True, help="Research topic")
    parser.add_argument("--lang", choices=["en", "zh"], default="en")
    parser.add_argument("--mode", choices=["scaffold", "checklist", "question", "diagnose"], default="scaffold")
    parser.add_argument("--out", help="Optional output file")
    args = parser.parse_args()

    if args.mode == "scaffold":
        text = scaffold(args.topic)
    elif args.mode == "checklist":
        text = checklist(args.topic)
    elif args.mode == "question":
        text = question(args.topic, args.lang)
    else:
        text = diagnose(args.topic, args.lang)

    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
