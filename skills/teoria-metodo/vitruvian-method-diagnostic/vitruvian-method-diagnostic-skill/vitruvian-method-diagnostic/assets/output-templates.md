# Output Templates

Use these templates when the user asks for a specific deliverable. Adapt them; do not fill every line if it is unnecessary.

## 1. Compact diagnostic memo

```markdown
# Diagnostic memo: [project/proposal]

## Verdict
[Test first / revise / proceed / reject] — [reason]

## Primary issue
[One sentence]

## Adequacy check
- Stability: [finding]
- Usefulness: [finding]
- Delight/legibility: [finding]

## Key risks
1. [risk] — [why it matters] — [verification]
2. [risk] — [why it matters] — [verification]
3. [risk] — [why it matters] — [verification]

## Decision-changing test
[smallest next test]
```

## 2. Comparison matrix

```markdown
| Option | Stability | Usefulness | Delight/legibility | Fit to place | Fit to means | Main risk | Verdict |
|---|---|---|---|---|---|---|---|
| A | ... | ... | ... | ... | ... | ... | ... |
| B | ... | ... | ... | ... | ... | ... | ... |
```

## 3. Material substitution review

```markdown
## Substitution verdict
[Accept / accept after tests / revise / reject]

## Original requirement
[What the original material/detail was probably solving]

## Substitute assessment
| Criterion | Original | Substitute | Risk |
|---|---|---|---|
| Durability | ... | ... | ... |
| Moisture/weathering | ... | ... | ... |
| Fire/code | ... | ... | ... |
| Appearance/module | ... | ... | ... |
| Installation/warranty | ... | ... | ... |
| Maintenance/lifecycle | ... | ... | ... |

## Required evidence before approval
- [test/mockup/document/review]
```

## 4. Site decision checklist

```markdown
## Site verdict
[Preferred site / test first / reject]

## Site risks
- Ground and water: [...]
- Climate and exposure: [...]
- Access and logistics: [...]
- Health and comfort: [...]
- Utilities and operations: [...]
- Cost of mitigation: [...]

## Tests before commitment
1. [test]
2. [test]
3. [test]
```

## 5. Red-team review

```markdown
## Most likely failure
[One sentence]

## Why the proposal is vulnerable
[Explanation]

## Failure chain
1. [condition]
2. [interaction]
3. [failure]
4. [consequence]

## Early warning signs
- [visible sign]
- [measurement]
- [complaint/operational symptom]

## Preventive change
[detail/design/test change]
```

## 6. Test plan

```markdown
## Test plan: [unknown]

## Hypothesis
[What we need to prove or disprove]

## Method
[Sample/mockup/measurement/calculation/inspection]

## Acceptance criteria
- [criterion]
- [criterion]

## Failure criteria
- [criterion]
- [criterion]

## Who should verify
[designer/engineer/supplier/lab/authority/user group]

## Decision after test
- If pass: [...]
- If fail: [...]
```
