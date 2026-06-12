# Hypothesis Testing And Variable Control

Use this file when the user needs a test design, case selection, variable control, process tracing, or inference critique.

## Testing Logic

Hypothesis testing asks whether empirical evidence supports the main explanation better than rival explanations. A test plan should specify:

- Main hypothesis.
- Rival hypotheses.
- Observable implications.
- Evidence/data.
- Case selection logic.
- Variable control strategy.
- Criteria for support, revision, or rejection.

## Qualitative Testing

Qualitative research often uses:

- **Case study**: deep analysis of one or several cases.
- **Comparative case study**: compare similar or different cases to isolate key variables.
- **Process tracing**: examine within-case evidence for the causal mechanism.
- **Counterfactual reasoning**: ask what would plausibly happen without X.
- **Most-similar systems**: cases similar on background factors but different on X/Y.
- **Most-different systems**: cases different on background factors but sharing X/Y relation.

## Process Tracing Checklist

For a mechanism X -> M -> Y:

- Identify each step in the mechanism.
- Specify what evidence each step should leave.
- Check temporal order.
- Search for evidence that should not appear if the mechanism is false.
- Compare against rival mechanisms.
- Avoid selecting only confirming evidence.

Output table:

| Mechanism step | Expected trace | Evidence found | Rival explanation | Assessment |
|---|---|---|---|---|

## Quantitative Testing

Quantitative testing is useful when:

- The variables can be measured across many observations.
- The unit of analysis is consistent.
- Data availability and quality are sufficient.
- The hypothesis expects systematic variation.

State model logic in plain language before equations:

- What outcome is modeled?
- What is the key independent variable?
- Which controls address confounding?
- What signs or magnitudes are expected?
- What robustness checks matter?

## Variable Control

Variable control improves causal inference by addressing rival explanations and confounding.

Principles:

- Control confounders that affect both X and Y.
- Do not control mediators if estimating total effect.
- Be careful controlling colliders, because this can create spurious association.
- Match control strategy to theory, not just software defaults.
- Explain why each control variable belongs in the design.

## Common Control Problems

| Problem | Meaning | Risk |
|---|---|---|
| Omitted confounder | A common cause of X and Y is ignored | Spurious or biased estimate |
| Overcontrol | Mediator is controlled | Real causal effect is hidden |
| Collider control | Common effect is conditioned on | Artificial association appears |
| Bad comparison | Cases differ on too many relevant factors | Rival explanations remain |
| Selection bias | Cases selected based on outcome or available evidence | Inference is distorted |

## Uncertainty

Report uncertainty explicitly:

- Data uncertainty: missing, biased, strategically produced, or inconsistent data.
- Measurement uncertainty: indicator validity/reliability problems.
- Model uncertainty: alternative specifications or mechanisms.
- Historical uncertainty: incomplete records, retrospective interpretation.
- Scope uncertainty: whether findings apply beyond selected cases.

## Evidence Strength

Rank evidence:

- Strong: directly observes predicted mechanism and weakens rivals.
- Moderate: consistent with hypothesis but also compatible with rivals.
- Weak: anecdotal, post hoc, or only loosely connected.
- Negative: contradicts expected timing, mechanism, or implication.

## Output Pattern

Use this table:

| Hypothesis | Observable implication | Evidence/data | Test method | Controls/rivals | Result criteria |
|---|---|---|---|---|---|

Then add:

- Main inference risk.
- What evidence would falsify or seriously weaken the claim.
- Minimum next evidence to collect.
