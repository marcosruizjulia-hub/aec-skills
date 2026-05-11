# Vitruvian Method Diagnostic Claude Skill

A compact, downloadable Agent Skill for applying a procedural diagnostic method distilled from Vitruvian architectural heuristics.

This is **not** a Vitruvius reference skill. It is a method-extraction and design-diagnostic skill.

## What it does

Use it to review:

- Architecture and urban design briefs.
- Facade and material substitutions.
- Site selection or climate-fit decisions.
- Water/source and building-service proposals.
- Public/private spatial organization.
- Mechanical or constructability concepts.
- Design proposals that need risk triage, test plans, or a decision framework.

## Package structure

```text
vitruvian-method-diagnostic/
├── SKILL.md
├── README.md
├── LICENSE.txt
├── references/
│   ├── method-cards.md
│   ├── domain-checklists.md
│   ├── source-map.md
│   └── boundaries-and-failure-modes.md
├── assets/
│   └── output-templates.md
└── evals/
    ├── evals.json
    └── rubric.md
```

## Install in Claude.ai

1. Upload `vitruvian-method-diagnostic-skill.zip` in Claude’s Skills settings.
2. Enable the skill.
3. Test with: `Diagnose this facade substitution using the Vitruvian method: ...`

## Install in Claude Code

Copy the folder into your skills directory so the path is:

```text
~/.claude/skills/vitruvian-method-diagnostic/SKILL.md
```

For a project-local installation, use:

```text
.claude/skills/vitruvian-method-diagnostic/SKILL.md
```

## Security posture

This skill is instruction-only. It includes no scripts, no executables, no network calls, and no embedded source book. It is designed for low operational risk and efficient progressive disclosure.

## Suggested test prompt

```text
We want to replace the specified facade board with a cheaper similar-looking product on a wet coastal office building. Diagnose whether that is acceptable using the Vitruvian method.
```

Expected behavior: Claude should classify the task as facade/materials plus climate/cost, apply the triad gate, flag coastal exposure and fixing/moisture risks, require verification, and give a test-first or revise verdict.
