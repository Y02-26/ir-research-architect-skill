#!/usr/bin/env python3
"""Generate an IR research design scaffold or checklist."""

from __future__ import annotations

import argparse
from pathlib import Path


def scaffold(topic: str) -> str:
    return f"""# 国际关系研究设计草案

## 主题

{topic}

## 1. 研究困惑

- 观察到的异常、变化或对比：
- 为什么这个现象值得解释：
- 与既有研究或常识的张力：

## 2. 研究问题

- 核心问题：
- 时间范围：
- 空间/案例范围：
- 分析单位：

## 3. 文献综述设计矩阵

> 仅整理你已经提供的文献、摘要、书目或读书笔记；不要在这里编造真实文献。

| 已提供材料/作者 | 研究问题 | 解释机制 | 方法/证据 | 局限 | 对本文用途 |
|---|---|---|---|---|---|
| | | | | | |

## 4. 因果解释

| 要素 | 内容 |
|---|---|
| 因变量 Y | |
| 自变量 X | |
| 因果机制 M | |
| 范围条件 S | |
| 竞争性解释 R | |
| 可观察含义 O | |

## 5. 假设

- H1:
- H2:
- 竞争性假设:

## 6. 概念操作化与测量

| 变量 | 概念定义 | 维度 | 指标 | 数据来源 | 测量等级 | 效度/信度风险 |
|---|---|---|---|---|---|---|
| Y | | | | | | |
| X | | | | | | |

## 7. 检验设计

- 案例/样本选择：
- 方法：
- 控制变量/控制策略：
- 过程追踪证据：
- 能削弱本文假设的证据：

## 8. 论文结构

1. 导论：
2. 文献综述设计/回顾：
3. 理论与假设：
4. 研究设计：
5. 经验检验：
6. 结论：
"""


CHECKLIST = """# 国际关系研究设计检查清单

- [ ] 研究问题清楚、真实、有意义、能回答。
- [ ] 因变量 Y 明确，且不是泛泛主题。
- [ ] 自变量 X 明确，且与 Y 有时间先后。
- [ ] 因果机制不是一句“影响”，而是有步骤。
- [ ] 范围条件说明结论适用于哪些案例/时期。
- [ ] 文献回顾形成争论地图，而不是逐篇摘要。
- [ ] 核心概念有定义、维度和指标。
- [ ] 指标有数据来源和编码规则。
- [ ] 假设有方向、条件和可观察含义。
- [ ] 竞争性解释被认真纳入检验。
- [ ] 控制变量有理论理由。
- [ ] 方法与问题、证据和案例数量匹配。
- [ ] 结论不超出证据支持范围。
"""


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate an IR research design scaffold.")
    parser.add_argument("--topic", default="待定主题", help="Research topic.")
    parser.add_argument("--mode", choices=["scaffold", "checklist"], default="scaffold")
    parser.add_argument("--out", help="Optional output Markdown path.")
    args = parser.parse_args()

    text = CHECKLIST if args.mode == "checklist" else scaffold(args.topic)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
