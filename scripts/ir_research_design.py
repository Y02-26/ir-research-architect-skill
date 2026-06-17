#!/usr/bin/env python3
"""Generate non-template IR/political-science research-design worksheets."""

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
- What varies across cases, actors, institutions, issue areas, episodes, or time?
- Why is this pattern surprising relative to theory, expectation, or another case?
- What evidence could realistically be collected?

## 2. Research Question

Do not import a stock question frame. Derive the outcome from the user's own wording.

| Item | Draft |
|---|---|
| User's intended phenomenon | |
| Candidate outcome Y derived from the topic | |
| Observable variation in Y | |
| Cases and time frame | |
| Question wording | |
| Why it matters | |
| Evidence path | |

## 3. Literature-Review Design

Use only user-provided sources, abstracts, bibliographies, excerpts, or reading notes. Do not invent citations.

| Provided source | Question addressed | Core explanation | Method/evidence | Scope | Limitation | Use in this project |
|---|---|---|---|---|---|---|
| | | | | | | |

## 4. Causal Explanation

| Element | Draft |
|---|---|
| Outcome / dependent variable Y | |
| Cause / independent variable X | |
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
- [ ] The dependent variable Y is derived from the user's topic, not from a preset menu.
- [ ] The research question is clear, meaningful, and answerable.
- [ ] The proposed cause X is explicit only after Y is clear.
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
- [ ] Broad-topic conversion did not use a fixed outcome list or stock question frame.
"""


def question(topic: str, lang: str) -> str:
    if lang == "zh":
        return f"""# 从主题到研究问题

## 初始主题

{topic}

## 先不要写假设

第一步不是提出自变量或因果机制，而是从用户自己的题目里生成待解释结果 Y。

## 禁止固定菜单

不要从预设清单里选择 Y。下面这些只是诊断维度，不是答案选项。

| 诊断维度 | 现场生成 Y 时要问的问题 | 从用户题目生成的候选 Y |
|---|---|---|
| 行动或状态 | 题目里有什么行动、状态、关系或结果可能发生变化？ | |
| 差异或变化 | 这个结果在什么对象、时间、地点、议题或情境之间不同？ | |
| 程度或强度 | 是否存在强弱、频率、持续时间、投入程度或范围差异？ | |
| 方向或性质 | 结果的方向、性质、目标、对象或表达方式是否改变？ | |
| 时间顺序 | 结果为什么在某个时间点之前/之后出现或变化？ | |
| 可观察证据 | 什么材料能观察这个结果，而不是只靠判断？ | |

## 研究问题生成区

不要套用固定问题类型。请根据上面的候选 Y，写出 2-4 个只服务于当前题目的研究问题。

| 草案 | 这个问题解释的 Y | 所需案例/时间/证据 |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

## 下一步

先选择一个由当前题目生成的 Y，再讨论 X、M、范围条件和假设。不要把任何示例、清单或常见国关框架当作默认路径。
"""

    return f"""# From Topic To Research Question

## Initial Topic

{topic}

## Do Not Write Hypotheses Yet

First generate the outcome Y from the user's own topic. Do not choose from a preset list.

## No Fixed Menu

The rows below are diagnostic dimensions, not answer choices.

| Diagnostic dimension | Question for generating Y | Candidate Y generated from this topic |
|---|---|---|
| Action or state | What action, state, relation, or result in the user's topic could vary? | |
| Difference or change | Across what actors, cases, periods, issue areas, or contexts does it vary? | |
| Degree or intensity | Could the result vary by strength, frequency, duration, investment, or scope? | |
| Direction or character | Could the direction, target, meaning, or form of the result change? | |
| Timing | Why might the result appear before/after a specific moment? | |
| Observable evidence | What material would let us observe the result rather than only assert it? | |

## Research Question Generation Area

Do not apply fixed question families. Write 2-4 questions that fit only this topic and its generated Y.

| Draft question | Outcome Y it explains | Needed cases/time/evidence |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

## Next Step

Choose one Y generated from this topic before discussing X, M, scope conditions, or hypotheses. Do not treat any example, list, or common IR frame as the default path.
"""


def diagnose(topic: str, lang: str) -> str:
    if lang == "zh":
        return f"""# 研究设计诊断表

主题或草稿：{topic}

先找最弱环节，再修改文本。

| 环节 | 诊断问题 | 当前问题 | 修正动作 |
|---|---|---|---|
| 主题 | 是否只是领域标签？ | | 收窄到行动者、结果、时间、空间和变化。 |
| 研究问题 | Y 是否来自当前题目，而不是来自固定模板？ | | 根据题目现场生成 Y。 |
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
| Research question | Is Y generated from this topic rather than a fixed template? | | Generate candidate Y values from the topic. |
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
A broad international-relations topic with an unclear outcome. Help me design a research question.
```

Expected behavior:

- Do not provide a fixed outcome menu.
- Ask what action, state, relation, or result in the user's topic could vary.
- Generate candidate Y values from the topic itself.
- Write topic-specific questions only after Y is generated.

## Mechanism Construction

Prompt:

```text
My topic has an outcome that varies across cases. Help me write a causal mechanism.
```

Expected behavior:

- Clarify the outcome Y, cases, and time period.
- Rebuild the mechanism from actors, incentives, resources, information, and constraints.
- Do not copy a mechanism from an example.

## Draft Diagnosis

Prompt:

```text
A broad international-relations topic with an unclear outcome. What is wrong with it?
```

Expected behavior:

- Diagnose the weakest link first.
- Identify that Y and variation are not yet generated from the topic.
- Do not offer stock outcomes or stock question families.
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
