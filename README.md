# IR Research Architect.skill

> *把一个国际关系选题，搭成一篇能被检验、能被答辩、能被写完的研究。*

[![Agent Skills](https://img.shields.io/badge/Agent%20Skills-Standard-green)](https://agentskills.io)
[![Codex Skill](https://img.shields.io/badge/Codex-Skill-blue)](#安装)
[![Research Methods](https://img.shields.io/badge/IR-Research%20Methods-purple)](#它能帮你做什么)

**IR Research Architect** 是一个面向国际关系、政治学与区域国别研究的 Agent Skill。它把《国际关系研究实用方法（第三版）》的方法论整理成可调用的研究设计知识库，帮你从“我有一个大概想法”走到“我有一个清晰问题、因果机制、变量方案、检验路径和论文结构”。

它不是替你堆材料，也不是替你写空泛综述。它的核心任务是：**把研究做成一个有结构、可检验、能推进的设计。**

[效果示例](#效果示例) · [安装](#安装) · [它能帮你做什么](#它能帮你做什么) · [工作原理](#工作原理) · [仓库结构](#仓库结构)

---

## 效果示例

```text
用户 ❯ 我想研究中美技术竞争，但题目太大了

IR Research Architect ❯
先不要急着写“中美技术竞争研究”。这个题目现在还是主题，不是问题。

可以把它压成三个可研究的问题：

1. 为什么美国对华技术限制在某些领域更强，在某些领域更弱？
2. 为什么同样面对美国限制，中国企业的适应结果不同？
3. 技术联盟如何改变中美竞争中的第三方国家选择？

如果你想写论文，我建议优先选第 2 个。
它有明确因变量：企业适应结果。
它能比较案例：华为、TikTok、半导体设备企业。
它能建立机制：外部压力 -> 资源重组 -> 替代能力形成 -> 适应差异。
```

```text
用户 ❯ 我的假设是“国际组织能促进冲突调停”，这样可以吗？

IR Research Architect ❯
这还不是一个好假设，它缺少三个东西：条件、机制、可观察含义。

可以改成：

H1：当国际组织具备较高制度授权和成员国资源支持时，其调停更可能降低冲突复发概率。

机制是：
制度授权提高承诺可信度，成员国资源提供执行能力，两者共同降低冲突方违约预期。

可观察含义包括：
- 调停协议是否包含监督机制；
- 成员国是否提供维和、资金或制裁承诺；
- 冲突方是否在协议后减少军事动员。
```

```text
用户 ❯ 我的文献综述总像读书笔记

IR Research Architect ❯
把“逐篇介绍”改成“解释类型地图”。

可以分成三组：

1. 权力结构解释：强调大国能力分布和威慑关系。
2. 国内政治解释：强调领导人、利益集团与制度约束。
3. 观念认知解释：强调威胁感知、身份和历史记忆。

每组只回答三个问题：
它解释了什么？
它解释不了什么？
你的研究准备补哪一块？
```

---

## 安装

### 方式一：一行命令

如果你的 runtime 支持通用 skills 安装器，可以运行：

```bash
npx skills add Y02-26/guoji-guanxi-yanjiu-fangfa-skill
```

### 方式二：手动安装到 Codex

```bash
git clone https://github.com/Y02-26/guoji-guanxi-yanjiu-fangfa-skill ~/.codex/skills/guoji-guanxi-yanjiu-fangfa
```

Windows PowerShell 可以改成你的 Codex skills 目录，例如：

```powershell
git clone https://github.com/Y02-26/guoji-guanxi-yanjiu-fangfa-skill "$env:USERPROFILE\.codex\skills\guoji-guanxi-yanjiu-fangfa"
```

### 方式三：作为研究模板使用

即使你的工具不支持 Agent Skills，也可以直接阅读：

- `SKILL.md`
- `references/`
- `scripts/ir_research_design.py`

它们本身就是一套国际关系研究设计工作流。

---

## 使用

安装后，可以这样对 Agent 说：

```text
用 IR Research Architect 帮我把“中美技术竞争”改成博士论文选题。
```

```text
用 IR Research Architect 检查我的开题报告，重点看研究问题、因果机制和变量操作化。
```

```text
用 IR Research Architect 给我做一个文献综述矩阵。
```

```text
用 IR Research Architect 把这个假设改成可检验版本，并列出竞争性解释。
```

---

## 它能帮你做什么

| 能力 | 说明 |
|---|---|
| **选题压缩** | 把宽泛主题改成清楚、真实、有意义、能回答的研究问题 |
| **文献综述** | 从读书笔记变成争论地图、解释类型和研究缺口 |
| **因果解释** | 建立 X -> 机制 -> Y 的解释链，并补充范围条件 |
| **假设生成** | 把想法改写成有方向、有条件、有可观察含义的假设 |
| **变量设计** | 明确自变量、因变量、中介变量、混杂变量和控制策略 |
| **操作化测量** | 把抽象概念变成指标、数据来源和编码规则 |
| **假设检验** | 设计案例比较、过程追踪、定量检验或混合方法路径 |
| **论文结构** | 组织导论、文献、理论、方法、经验检验和结论 |

---

## 工作原理

IR Research Architect 把研究设计拆成八个步骤：

1. 判断项目类型：理论研究、政策研究，还是混合项目。
2. 从研究兴趣中提炼研究困惑。
3. 把困惑压缩成明确研究问题。
4. 用文献回顾定位争论和缺口。
5. 构建因果解释和竞争性解释。
6. 设计假设与可观察含义。
7. 完成概念操作化、测量和变量控制。
8. 形成论文、开题报告或研究方案。

这套流程来自国际关系研究方法训练中的核心问题：**不是先问“我该写什么材料”，而是先问“我到底要解释什么”。**

---

## 仓库结构

```text
guoji-guanxi-yanjiu-fangfa-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── knowledge-map.md
│   ├── research-orientation.md
│   ├── question-and-literature.md
│   ├── causal-explanation.md
│   ├── operationalization-measurement.md
│   ├── hypothesis-testing.md
│   ├── thesis-writing.md
│   └── checklists.md
└── scripts/
    └── ir_research_design.py
```

`references/` 是知识库核心。Agent 会按任务需要读取对应文件，而不是一次性把所有内容塞进上下文。

---

## 快速生成研究设计模板

```bash
python scripts/ir_research_design.py --topic "中美技术竞争" --out design.md
```

生成检查清单：

```bash
python scripts/ir_research_design.py --topic "地区组织与冲突调停" --mode checklist
```

---

## 诚实边界

- 这个 skill 是方法论助手，不替代导师、同行评议或真实资料搜集。
- 知识库来自扫描 PDF 的 OCR 辅助整理，细节页码、原文表述和专名应以原书为准。
- 仓库不包含原始 PDF，也不包含整本书原文。
- 它能帮助你把研究设计变严谨，但不能保证观点一定成立。

---

## 背后的想法

很多论文卡住，不是因为作者不努力，而是因为一开始没有把“主题、问题、解释、变量、证据”分清楚。

**IR Research Architect** 想解决的就是这个问题：  
让一个研究从第一天起就有骨架。

一个好研究不是资料越多越好，而是每一份资料都知道自己在回答哪个问题。
