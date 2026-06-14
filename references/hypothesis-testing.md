# Hypothesis Testing

Use this file when the user needs a plan for testing hypotheses, selecting cases/data, controlling variables, comparing explanations, or assessing uncertainty.

## Testing Logic

Hypothesis testing is not the search for supportive evidence. It is a comparison between the main hypothesis, alternative explanations, and possible disconfirming evidence.

Ask:

- What hypothesis is being tested?
- What evidence should exist if it is true?
- What evidence would weaken it?
- What alternative explanation could produce the same outcome?
- What cases or data can distinguish between them?

## Evidence Chain

| Link | Question |
|---|---|
| Before X | Was the background condition present? |
| X | Did the proposed cause occur or vary? |
| Mechanism | Are there traces of the process from X to Y? |
| Y | Did the outcome occur or vary as expected? |
| Alternative | Could another explanation fit better? |

## Qualitative Testing

Use qualitative testing when cases are few, mechanisms matter, evidence is heterogeneous, or the project asks why/how.

Common strategies:

- single-case study;
- within-case comparison;
- most-similar case comparison;
- most-different case comparison;
- positive-negative case comparison;
- process tracing;
- counterfactual analysis.

Process tracing should test mechanism steps. It should not become a chronological narrative.

## Quantitative Testing

Use quantitative testing when:

- variables can be measured across many cases or time periods;
- the research question asks about patterns or average effects;
- comparable data are available;
- controls can be theoretically justified.

Quantitative significance does not by itself prove the mechanism. If the claim is causal, connect statistical results to mechanism and alternative explanations.

## Variable Control

Control variables should be theoretically justified.

| Variable type | Control? | Reason |
|---|---|---|
| Confounder | Usually yes | It may affect both X and Y. |
| Mediator | Usually no for total effect | It is part of the causal path from X to Y. |
| Collider | No | Conditioning on it can create bias. In the source's Figure 5.5 pattern: X -> Y, X -> D, Y -> D. |
| Background constant | Not needed if truly constant | It does not vary in the selected design. |

## Case Selection

| Strategy | Use when | Risk |
|---|---|---|
| Most-similar cases | Cases are similar but differ on X/Y. | Hidden differences may remain. |
| Most-different cases | Cases differ broadly but share X/Y. | Mechanisms may not be equivalent. |
| Positive-negative comparison | One case has Y and another lacks Y. | Negative cases may have thin evidence. |
| Same case over time | Explaining change. | Many things may change at once. |
| Crucial case | Testing a theory under favorable or difficult conditions. | Generalization is limited. |

## Testing Plan Table

| Hypothesis | Observable implication | Evidence/data | Method | Alternative explanation | Support criterion | Disconfirming evidence |
|---|---|---|---|---|---|---|
| | | | | | | |

## Common Inference Errors

- Selecting only cases where Y occurred.
- Treating narrative sequence as causal proof.
- Ignoring negative evidence.
- Controlling for a mediator.
- Controlling for a collider.
- Using a control variable without theoretical reason.
- Equating correlation with mechanism.
- Claiming proof when the evidence only supports plausibility.
