---
name: shibui
description: Implement or review quiet, structured, low-surface user interfaces using the Shibui Design System. Use for UI architecture, semantic HTML, CSS, component design, page simplification, progressive disclosure, accessibility review, or critiques that should avoid cards, shadows, gradients, excessive borders, nested surfaces, badges, and decorative icons.
---

# Shibui

Build hierarchy through information architecture and structure rather than decoration.

## Load references

- Read `../docs/principles.md` before making structural decisions.
- Read `../docs/rules.md` when reviewing an existing UI or validating an implementation.
- Read `../docs/patterns.md` when choosing a disclosure, list, detail, or form pattern.
- Inspect `../shibui.yaml` when machine-readable constraints or automation are useful.
- Compare relevant files in `../examples/` before introducing a new pattern.

Resolve all paths relative to this file. If the skill is copied outside this repository, locate the equivalent bundled reference files or apply the workflow below directly.

## Implement

1. State the current view's primary task as one verb phrase.
2. List only information and actions required to complete that task.
3. Move substantial secondary content to drill-down views or labeled disclosure controls.
4. Mark up landmarks, headings, lists, tables, labels, and controls semantically.
5. Group with whitespace and shared alignment.
6. Establish hierarchy with restrained type size and placement.
7. Add a region background only when it communicates meaning or state.
8. Add a border only for input affordance, explicit separation, focus, or danger.
9. Keep geometry rectilinear. Use small radii or pills only where shape communicates affordance.
10. Remove shadows, elevation, decorative gradients, generic cards, ornamental icons, and decorative chips.
11. Verify keyboard focus, color-independent meaning, usable labels, responsive layout, and reduced motion.
12. Run the review workflow before finishing.

Use plain CSS and semantic HTML unless project constraints require a framework. Reuse the project's existing conventions rather than importing a new dependency solely to obtain styling primitives.

## Review

1. Identify the intended primary task from the artifact; flag ambiguity rather than inventing certainty.
2. Review architecture before visual details.
3. Evaluate every rule in `../docs/rules.md` as pass, fail, exception, or not applicable.
4. For each failure, provide the rule ID, evidence, task impact, and a concrete simpler replacement.
5. Order recommendations by leverage: information removal, drill-down, structure, typography, backgrounds, then borders.
6. Preserve necessary affordances and accessibility while simplifying.
7. End with the smallest high-impact change set; do not merely list violations.

Use `review.md` as the compact checklist and response template.

## Guardrails

- Do not equate Shibui with empty screens or oversized spacing.
- Do not hide required information merely to reduce density.
- Do not remove visible focus, input boundaries, labels, or error explanations in the name of restraint.
- Do not replace cards with equally decorative floating panes, gradients, or colored blocks.
- Do not treat the reference examples as a mandatory application shell; preserve product-specific navigation and workflows.
- Document a justified exception when task clarity or accessibility requires breaking a visual rule.
