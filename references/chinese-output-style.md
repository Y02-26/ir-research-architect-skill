# Chinese Output Style

Use this file when responding to Chinese users or producing Chinese proposal/thesis language.

## Preferred Terms

Use these Chinese academic-method terms by default when responding in Chinese:

| English | Chinese |
|---|---|
| research question | 研究问题 |
| research puzzle | 研究困惑 / 经验困惑 |
| dependent variable | 因变量 / 待解释结果 |
| independent variable | 自变量 / 核心解释变量 |
| causal mechanism | 因果机制 / 作用机制 |
| mediator | 中介变量 / 中介机制 |
| moderator | 调节变量 / 条件变量 |
| confounder | 混杂变量 / 混杂因素 |
| collider | 撞子变量 |
| scope condition | 范围条件 / 适用条件 |
| alternative explanation | 竞争性解释 / 替代性解释 |
| counterfactual | 反事实 |
| observable implication | 可观察含义 / 可检验证据 |
| operationalization | 操作化 |
| validity | 效度 |
| reliability | 信度 |
| hypothesis testing | 假设检验 |
| case selection | 案例选择 |
| process tracing | 过程追踪 |
| literature review | 文献综述 |
| variable control | 变量控制 |

## Forbidden Defaults, Not Forbidden Topics

不要默认把题目改写成“为什么某国对冲而不选边”。只有当用户明确提出“对冲、选边、联盟选择、大国竞争、中等国家、东盟、越南、中美竞争”等对象或结果时，才使用这些框架。这些不是禁用题目，而是禁用默认项。

Default Chinese broad-topic handling should be non-template:

1. 先判断题目是否还只是主题。
2. 根据用户自己的题目现场生成候选 Y，不要给固定结果清单。
3. 用诊断维度帮助生成问题，但不要把诊断维度当作固定问题菜单。
4. 暂时不要命名具体国家、地区、战略姿态或理论流派，除非用户已经给出。
5. 输出时说明：以下只是根据当前题目临时生成的候选方向，不是默认模板。

## Output Preferences

- Use Chinese prose first. Use X/Y/M only when it helps clarify a table, graph, or causal chain.
- When using X/Y/M, define them in Chinese: 因变量/待解释结果 Y, 自变量/核心解释变量 X, 因果机制 M.
- Use compact prose for early brainstorming.
- Use tables for research designs, proposal outlines, literature matrices, variable tables, measurement tables, and revision checklists.
- Do not over-format casual advice.
- Do not translate every methodological term literally if a standard Chinese term exists.
- Keep literature-review wording honest: if the user has not provided sources, say that the skill can design the review structure but cannot invent references.

## Chinese Broad-Topic Response Pattern

When the user gives a broad topic:

1. State that the topic is currently a field/theme, not yet a research question.
2. Generate candidate dependent variables / outcomes from the user's own wording.
3. Give two or three topic-specific research-question versions.
4. Recommend the easiest version to operationalize, with reasons.
5. State what cases, time range, evidence, or literature are still needed.

Do not propose a full causal mechanism before the outcome and scope are fixed. Do not use a fixed outcome list.

## Draft Diagnosis Pattern

When a Chinese user provides a title, abstract, proposal paragraph, or draft:

1. Identify the weakest link first.
2. Explain the problem using standard Chinese method terms.
3. Give a revised version only after the diagnosis.
4. If the draft is too broad, list possible Y values before suggesting X or M.

Useful compact phrasing:

```text
现在最弱的环节不是表达，而是因变量不清楚。这个题目还停留在主题层面，需要先确定你到底要解释什么结果。
```

```text
先不要急着写假设。这个阶段应该先从题目本身生成候选 Y，再决定案例、时间范围和证据来源。
```
