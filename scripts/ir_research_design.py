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

## 2. Research Question

| Item | Draft |
|---|---|
| Research puzzle | |
| Core question | |
| Outcome / dependent variable Y | |
| Cases and time frame | |
| Question type | why / how / under what conditions / with what effect |
| Answerability evidence | |

Before naming a cause, theory family, country, or strategic posture, list multiple neutral possible outcomes Y.

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
- [ ] Broad-topic conversion offered multiple neutral question families instead of one familiar IR frame.
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
| 政策采纳或不采纳 | | |
| 投票行为 | | |
| 条约参与 | | |
| 监管变化 | | |
| 危机反应 | | |
| 资源配置 | | |
| 制度遵守 | | |
| 公开叙事 | | |
| 合作强度 | | |
| 冲突升级或降级 | | |

## 候选研究问题类型

| 类型 | 中性问题框架 | 还缺什么信息 |
|---|---|---|
| 差异问题 | 在相似外部条件下，为什么 Y 在不同案例之间不同？ | |
| 过程问题 | X 通过什么过程产生 Y？ | |
| 条件问题 | 在什么条件下，X 更可能产生 Y？ | |
| 时间问题 | 为什么 Y 在某一时间之后发生，而不是之前发生？ | |
| 比较问题 | 为什么案例 A 与案例 B 呈现不同的 Y？ | |

## 下一步

先选择一个待解释结果 Y，再讨论自变量 X、因果机制 M、范围条件和假设。不要把其他案例或示例中的问题框架直接搬到这个主题上。
"""

    return f"""# From Topic To Research Question

## Initial Topic

{topic}

## Do Not Write Hypotheses Yet

First identify the outcome to explain: the dependent variable / outcome Y.

## Possible Neutral Outcomes

| Possible Y | Observable variation | Possible evidence |
|---|---|---|
| policy adoption or non-adoption | | |
| voting behavior | | |
| treaty participation | | |
| regulatory change | | |
| crisis response | | |
| resource allocation | | |
| institutional compliance | | |
| public framing | | |
| cooperation intensity | | |
| conflict escalation or de-escalation | | |

## Question Families

| Family | Generic question frame | Missing information |
|---|---|---|
| Variation | Under a similar external condition, why does Y vary across cases? | |
| Process | Through what process does X generate Y? | |
| Condition | Under what conditions does X produce Y rather than not-Y? | |
| Timing | Why did Y occur after time T rather than before? | |
| Comparison | Why did case A and case B produce different values of Y? | |

## Next Step

Choose one outcome before discussing independent variables or causal mechanisms. Do not reuse question frames or mechanisms from other cases.
"""


def diagnose(topic: str, lang: str) -> str:
    if lang == "zh":
        return f"""# 研究设计诊断表

主题或草稿：{topic}

先找最弱环节，再修改文本。

| 环节 | 诊断问题 | 当前问题 | 修正动作 |
|---|---|---|---|
| 主题 | 是否只是领域标签？ | | 收窄到行动者、结果、时间、空间和变化。 |
| 研究问题 | 因变量 / 待解释结果 Y 是否清楚？ | | 先列出可能的 Y，再选择一个。 |
| 文献综述设计 | 是否只是作者罗列？ | | 按解释类型、机制、方法、证据和局限分组。 |
| 因果解释 | 是否有机制，而不只是理论标签？ | | 从行动者、激励、信念、资源、信息、约束重建机制。 |
| 假设 | 是否有方向、条件和可检验证据？ | | 改成可被证据支持或削弱的句子。 |
| 变量 | 自变量、因变量、中介、混杂、撞子变量是否区分？ | | 先画因果图，再决定变量角色。 |
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
| Variables | Are X, Y, mediator, confounder, and collider separated? | | Draw a causal diagram before deciding controls. |
"""


def validate_prompts() -> str:
    return """# Validation Prompts

Use these prompts for light regression testing.

## Broad Topic

Prompt:

```text
External pressure and small-state policy change. Help me design a research question.
```

Expected behavior:

- List possible dependent variables/outcomes first.
- Offer several question families: variation, process, condition, timing, and comparison.
- Do not impose a fixed strategic-choice frame.

## Mechanism Construction

Prompt:

```text
My topic is why international organization mediation sometimes succeeds and sometimes fails. Help me write a causal mechanism.
```

Expected behavior:

- Clarify success/failure, cases, and time period.
- Rebuild the mechanism from actors, incentives, resources, information, and constraints.
- Do not copy a mechanism from an example.

## Draft Diagnosis

Prompt:

```text
External pressure and small-state policy change. What is wrong with it?
```

Expected behavior:

- Diagnose the weakest link first.
- Identify that the dependent variable and variation are unclear.
- Offer possible outcomes before proposing mechanisms.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", default="Untitled topic", help="Research topic")
    parser.add_argument("--lang", choices=["en", "zh"], default="en")
    parser.add_argument("--mode", choices=["scaffold", "checklist", "question", "diagnose", "validate-prompts"], default="scaffold")
    parser.add_argument("--out", help="Optional output file")
    args = parser.parse_args()

    if args.mode == "scaffold":
        text = scaffold(args.topic)
    elif args.mode == "checklist":
        text = checklist(args.topic)
    elif args.mode == "question":
        text = question(args.topic, args.lang)
    elif args.mode == "diagnose":
        text = diagnose(args.topic, args.lang)
    else:
        text = validate_prompts()

    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
