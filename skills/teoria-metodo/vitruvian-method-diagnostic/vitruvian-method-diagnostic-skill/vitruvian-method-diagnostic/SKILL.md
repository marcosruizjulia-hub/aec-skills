---
name: vitruvian-method-diagnostic
description: Apply a procedural diagnostic method distilled from Vitruvian building heuristics. Use for architecture, facade, site, material, water/service, machine/system, design-brief, or proposal reviews; method extraction; heuristic critique; risk triage; design checklists; and test plans. Do not use for pure historical/reference questions unless the user asks to apply the method.
license: CC0-1.0 for original skill text; source text not bundled
compatibility: No scripts or network access required. Works in Claude.ai, Claude Code, and skills-compatible agents that support Agent Skills folders.
metadata:
  version: "1.0.0"
  source_basis: "Project Gutenberg EPUB of Vitruvius, De architectura, treated as procedural source material rather than reference material."
---

# Vitruvian Method Diagnostic

## Purpose

Use this skill to turn a design, site, material choice, building system, service proposal, machine, or brief into a practical diagnostic review. Treat the source tradition as a repertoire of procedures and warning signs, not as authority for modern approval.

The skill’s job is to extract and apply reusable moves: classify the problem, test adequacy, check fit to place/use/means, identify hidden risks, and end with the next concrete test or decision.

## Trigger discipline

Use this skill when the user asks for any of the following:

- Diagnose, review, critique, stress-test, or red-team a design proposal.
- Convert a design tradition, book, precedent, or brief into methods, heuristics, checklists, or tests.
- Evaluate a site, facade, material substitution, water/service source, spatial layout, or mechanical device.
- Produce a decision framework or inspection checklist for architecture, construction, envelope, or built-environment problems.

Do not activate for simple historical questions such as “Who was Vitruvius?” or “What are the ten books?” unless the user asks to apply or extract a method.

## Non-negotiable guardrails

- Do not treat ancient advice as modern engineering, public-health, fire, accessibility, structural, or code approval.
- For high-stakes building, safety, water, structural, fire, environmental, or legal decisions, recommend review by qualified professionals and modern standards.
- Separate **stated facts**, **reasonable inferences**, and **unknowns**.
- Make a best-effort diagnosis with missing information listed; do not stop at clarification questions unless action would be unsafe.
- Prefer observable tests, mockups, calculations, inspections, and stakeholder checks over abstract opinions.
- Avoid lengthy historical exposition. Use the method.

## Core operating loop

1. **Classify the problem.** Choose the primary domain: site, function, structure, envelope/materials, proportion/form, water/services, machines/systems, cost/supply, public/private use, or maintenance.
2. **Run the triad gate.** Evaluate the proposal through stability, usefulness, and delight/legibility. A proposal that succeeds only visually is not adequate.
3. **Check fit to place.** Test climate, sun, wind, moisture, water, ground, hazards, surrounding context, access, and local material conditions.
4. **Check fit to users and use.** Ask who uses it, for what routines, with what public/private status, comfort needs, access needs, maintenance burden, and budget logic.
5. **Check fit to means.** Compare the desired solution with available materials, supply chain, transport, craft skill, budget, time, replacement cycles, and maintenance capacity.
6. **Look for diagnostic signs.** Identify visible symptoms, precedent evidence, sample tests, mockups, measurements, or small experiments before full commitment.
7. **Probe hidden risks.** For buried, wet, enclosed, loaded, pressurized, mechanical, or life-safety systems, require testing before entry, closure, loading, distribution, or commissioning.
8. **Find the governing module.** For form, facades, grids, components, or machines, identify the controlling unit, center, bay, ratio, lever arm, tolerance, or rhythm.
9. **Stress-test substitutions.** If an ideal material, detail, location, or configuration is unavailable, propose the nearest acceptable substitute and name the performance tradeoff.
10. **Conclude with action.** End with one of: proceed, revise, test first, or reject. Include the smallest next test that could change the decision.

## Default output

Use this format unless the user asks for another one:

```markdown
## Diagnostic verdict
[Proceed / revise / test first / reject] — [one-sentence reason]

## Classification
Primary domain: [...]
Secondary domains: [...]

## Evidence status
- Stated: [...]
- Inferred: [...]
- Unknown: [...]

## Three-part adequacy test
| Test | Finding | Confidence | What to verify |
|---|---|---:|---|
| Stability | ... | High/Med/Low | ... |
| Usefulness | ... | High/Med/Low | ... |
| Delight / legibility | ... | High/Med/Low | ... |

## Method moves applied
1. [Move]: [why it matters here]
2. [Move]: [why it matters here]
3. [Move]: [why it matters here]

## Risks and diagnostic signs
- [Risk]: [visible sign, measurement, mockup, calculation, or inspection]

## Smallest useful next test
[Concrete test / calculation / mockup / site check / stakeholder check]
```

## Method moves to apply

Use these move names consistently:

- **Triad gate:** Stability, usefulness, and delight/legibility must all pass.
- **Site-before-form:** Diagnose exposure, water, ground, access, and local hazards before judging design form.
- **Use-specific distribution:** Do not universalize a prestigious layout; fit spatial hierarchy to users, routines, and public/private role.
- **Local means discipline:** Prefer available, buildable, maintainable choices unless importation clearly improves performance enough to justify risk.
- **Material sample test:** Verify material claims through samples, mockups, compatibility checks, and exposure-specific tests.
- **Environmental adaptation:** Orientation, openings, rooms, finishes, and systems should respond to sun, wind, humidity, and thermal variation.
- **Water/source verification:** Prove source quality, capacity, protection, and reliability before designing distribution.
- **Hidden hazard probe:** Test invisible dangers before entering, sealing, loading, or commissioning concealed systems.
- **Commissioning by failure points:** Add inspection points, cleanouts, isolation, test ports, relief, or monitoring where failure is likely.
- **Module/coherence test:** Identify the governing module, ratio, grid, center, or detail logic; flag arbitrary or incoherent borrowing.
- **Substitution discipline:** When replacing a material/detail/site choice, name the lost and gained performance, not just cost or appearance.
- **Mechanics by centers and ratios:** For machines and movable systems, analyze force through centers, arms, rotations, ratios, supports, and stops.

## When to load supporting files

- Read `references/method-cards.md` when the problem needs more detailed prompts for a specific move.
- Read `references/domain-checklists.md` when generating a checklist for site, facade, materials, water/services, machines, or public/private buildings.
- Read `references/source-map.md` only when the user asks how the procedure was extracted from the Vitruvian source.
- Read `references/boundaries-and-failure-modes.md` for safety limits, misuse patterns, and modern-professional review triggers.
- Read `assets/output-templates.md` when the user asks for a compact checklist, decision memo, comparison matrix, test plan, or red-team review.
- Use `evals/evals.json` and `evals/rubric.md` only to test or improve the skill, not during normal diagnostic answers.

## Quality bar

A good answer from this skill:

- Makes a clear provisional decision.
- Shows which diagnostic moves were applied.
- Names missing facts without becoming paralyzed by them.
- Recommends concrete verification steps.
- Distinguishes method-derived insight from modern compliance or engineering approval.
- Avoids turning into a summary of Vitruvius.
