# Operationalization And Measurement

Use this file when the user needs to turn abstract concepts into observable indicators, data, coding rules, and measurement plans.

## Operationalization Logic

Operationalization turns a concept into something observable and comparable.

Sequence:

1. Define the concept.
2. Break it into dimensions.
3. Select indicators for each dimension.
4. Name data sources.
5. Write coding rules.
6. Assess validity and reliability.
7. State limitations and robustness checks.

The agent should slow the user down here. Many weak research designs fail not
because the theory is useless, but because the concept, indicator, data source,
and coding rule are silently treated as the same thing.

## Diagnostic Questions

Ask these before accepting an operationalization:

- What exactly is the concept, independent of its causes and consequences?
- Which part of the concept varies across cases, actors, or time?
- Is the concept one-dimensional, or does it contain several dimensions?
- Does each indicator directly observe a dimension, or only a convenient proxy?
- Could two researchers apply the coding rule and reach the same result?
- Does the data source observe the phenomenon, the actor's claim about the
  phenomenon, or a third party's interpretation of it?
- Is the measure comparable across cases, languages, institutions, and periods?
- Would the measure still make sense if the expected hypothesis were false?
- What missing data pattern would change the inference?

## Concept Definition

A good definition:

- is not circular;
- separates the concept from its causes and effects;
- matches the research question;
- is narrow enough to observe;
- can travel across selected cases without stretching too far.

Bad:

```text
Influence means having influence.
```

Better:

```text
Influence means the ability of actor A to change actor B's preference, behavior, or policy choice in a specified issue area.
```

## Dimensions And Indicators

| Concept | Dimension | Possible indicators |
|---|---|---|
| Institutional authority | Delegation | formal mandate, voting rules, enforcement power |
| Threat perception | Elite belief | speeches, strategy documents, classified/declassified assessments |
| Economic dependence | Trade/finance exposure | trade share, investment stock, supply-chain concentration |
| Compliance | Behavior | treaty implementation, violation count, reporting record |

## Indicator Selection Ladder

Use this ladder to help the user improve weak indicators:

| Level | Indicator type | Typical risk | Repair move |
|---|---|---|---|
| Direct behavioral trace | Observed action, vote, implementation, deployment, violation | May miss hidden motives | Add interpretive evidence if the concept includes intention. |
| Institutional record | Treaty text, legal mandate, budget, rule change | Formal rule may not equal practice | Pair with implementation evidence. |
| Actor statement | Speech, memoir, interview, strategy document | Strategic rhetoric or retrospective bias | Triangulate with behavior and context. |
| Expert coding | Dataset, index, expert survey | Coding assumptions may be opaque | Read codebook and report limitations. |
| Proxy | Trade share for dependence, media tone for perception | Proxy may capture adjacent concept | Justify why the proxy tracks the dimension. |
| Convenience count | Search hits, random frequency counts | Often weak validity | Use only with a clear sampling and coding rule. |

## Measurement Levels

| Level | Meaning | Example |
|---|---|---|
| Nominal | Categories without order | regime type, alliance membership |
| Ordinal | Ordered categories | low/medium/high institutionalization |
| Interval | Equal intervals, no true zero | index score |
| Ratio | Equal intervals with true zero | number of sanctions, trade volume |

## Validity And Reliability

Validity asks whether the indicator measures the intended concept.

Reliability asks whether the measurement procedure is consistent.

| Risk | Question | Fix |
|---|---|---|
| Concept-indicator mismatch | Does the indicator capture the concept? | Add dimensions or choose a better indicator. |
| Measurement overlap | Does the X indicator already include Y? | Define X independently of Y. |
| Source bias | Does the source systematically distort the evidence? | Triangulate with another source type. |
| Coding ambiguity | Would two coders code the case differently? | Write explicit coding rules. |

## Common Validity Problems

- **Conceptual stretching**: the concept is broadened until every case fits.
- **Outcome leakage**: the indicator for X already includes Y.
- **Cause-effect confusion**: the measure observes a consequence rather than the
  concept itself.
- **One-indicator shortcut**: a multidimensional concept is measured by one
  convenient number.
- **Elite-source bias**: official statements are treated as actual preferences
  without checking behavior or institutional constraints.
- **Time mismatch**: the indicator is measured after the outcome or at a time
  that cannot affect the outcome.
- **Case-specific coding**: rules are adjusted case by case, making comparison
  impossible.

## Reliability Checks

Use one or more of these:

- Write a codebook with inclusion, exclusion, and borderline-case rules.
- Test the coding rule on a few cases before using it across the whole design.
- Record source selection criteria, not only final sources.
- Use double coding or peer review when coding documents or events.
- Keep a decision log for ambiguous cases.
- Report missing, uncertain, or low-confidence observations instead of hiding
  them.

## Operationalization Repair Pattern

When the user's draft is vague, repair it in this order:

1. Replace the concept name with a sentence definition.
2. Split the definition into dimensions.
3. Assign at least one indicator to each dimension.
4. Name the exact source type for each indicator.
5. Write the coding rule in if-then language.
6. Name one validity risk and one reliability risk.

Example:

```text
Concept: alliance credibility.
Definition: the degree to which a target believes an ally will honor a
commitment under a specified contingency.
Dimensions: commitment clarity, capability, past follow-through, audience cost.
Indicators: treaty language, force posture, prior crisis behavior, public
leader statements.
Coding rule: code commitment clarity as high when the treaty names the
contingency and response obligation explicitly.
Validity risk: public treaty language may not reveal private reassurance.
Reliability check: compare coding against a second coder's reading of treaty
texts and declassified documents.
```

## Operationalization Table

| Concept | Definition | Dimensions | Indicators | Data source | Coding rule | Validity risk | Reliability check |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## Common Errors

- Choosing indicators only because they are easy to obtain.
- Defining X by Y, which creates circularity.
- Treating a case name as a variable.
- Using a vague concept as if it were directly observable.
- Hiding missing data or source bias.
- Treating official rhetoric as behavior without triangulation.
- Using a global index without checking whether its coding matches the user's
  concept.
- Measuring a concept at the wrong level of analysis, such as using national
  GDP for an elite-perception argument.
- Measuring the mediator as if it were a control variable.
- Reporting numbers without explaining how observations entered the dataset.
