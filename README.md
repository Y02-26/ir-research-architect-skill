# IR Research Architect Skill

> 把一个国际关系选题，推进成清楚、可检验、能写成论文的研究设计。

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-green)](https://agentskills.io)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue)](#安装方法)
[![Research Methods](https://img.shields.io/badge/IR-Research%20Methods-purple)](#它能帮你做什么)

这是一个面向国际关系、政治学、区域国别研究、国家安全研究的 Codex / Agent Skill。

它不是简单帮你“润色论文”，而是像一个研究方法助手一样，帮你把模糊想法一步步拆成：

`选题 -> 研究问题 -> 文献综述设计 -> 因果解释 -> 假设 -> 变量 -> 操作化 -> 假设检验 -> 论文结构`

这个 skill 的知识库基于《国际关系研究实用方法》的方法框架整理而成，但不是原书全文，也不包含原始 PDF。它更适合用来做研究设计、论文开题、选题压缩、假设生成、变量设计和方法论检查。

## 安装方法

macOS / Linux:

```bash
git clone https://github.com/Y02-26/ir-research-architect-skill ~/.codex/skills/ir-research-architect
```

Windows PowerShell:

```powershell
git clone https://github.com/Y02-26/ir-research-architect-skill "$env:USERPROFILE\.codex\skills\ir-research-architect"
```

## 示例用法

```text
Use IR Research Architect to turn "US-China technology competition" into a feasible thesis topic.
```

```text
Use IR Research Architect to revise my hypothesis and list alternative explanations.
```

```text
Use IR Research Architect to organize these reading notes into a literature-review design.
```

你也可以直接用中文提问，例如：

```text
用 IR Research Architect 帮我把“中美技术竞争”改成一个可以写论文的研究问题。
```

```text
用 IR Research Architect 检查我的因果机制、变量和假设有没有问题。
```

## 它能帮你做什么

| 能力 | 说明 |
|---|---|
| 选题压缩 | 把宽泛主题改成具体、真实、有意义、能回答的研究问题。 |
| 研究问题 | 帮你写出清楚、可回答、有理论价值的 why / how / under what conditions 问题。 |
| 文献综述设计 | 根据你已有的文献、笔记、摘要或材料，整理争论地图、解释类型和研究缺口。 |
| 因果解释 | 搭建 X -> 机制 -> Y 的解释链，并检查反事实、范围条件和竞争解释。 |
| 假设生成 | 把想法改写成有方向、有条件、有可观察含义的研究假设。 |
| 变量设计 | 区分自变量、因变量、中介变量、调节变量、混杂变量、撞子变量和控制变量。 |
| 操作化测量 | 把抽象概念转成指标、数据来源、编码规则和效度/信度检查。 |
| 假设检验 | 设计案例比较、过程追踪、定量检验或混合方法路径。 |
| 论文结构 | 组织导论、文献综述、理论、方法、经验分析和结论。 |

## 重要边界

- 它不会自动替你做文献搜索。
- 它不会凭空编造文献、作者、年份或引用。
- 文献综述必须基于你提供的文献、摘要、阅读笔记、书目或另行明确搜索得到的资料。
- 它是研究方法助手，不替代导师、同行评审和你自己的判断。
- 它提供的是整理后的方法知识库，不是原书全文。

## 目录结构

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

## 可复用脚本

```bash
python scripts/ir_research_design.py --topic "US-China technology competition" --out design.md
python scripts/ir_research_design.py --topic "regional organizations and conflict mediation" --mode checklist
```

## 适合谁

- 正在写国际关系、政治学、区域国别研究论文的学生
- 准备开题、选题、研究设计或方法论章节的人
- 想把“我有一个想法”推进成“我有一个可检验研究设计”的人
- 需要检查因果机制、变量、假设、操作化和论文结构的人

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=Y02-26/ir-research-architect-skill&type=Date)](https://www.star-history.com/#Y02-26/ir-research-architect-skill&Date)
