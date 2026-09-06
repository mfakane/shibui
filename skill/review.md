# Shibui review checklist

## Context

- Primary task:
- Interaction model (page / GUI tool):
- Required simultaneous context:
- Style profile and declared overrides:
- Required content:
- Secondary content:

## Check

- [ ] One primary task is evident, with required context and controls available together.
- [ ] Large secondary content is disclosed or moved to a focused view.
- [ ] Persistent panels are essential to the primary task.
- [ ] Spacing, alignment, and typography do the grouping first.
- [ ] Every visible container boundary carries meaning.
- [ ] Surface nesting is not used merely to create hierarchy.
- [ ] Visual checks below use the selected profile; standard defaults omit shadows, elevation, and decorative gradients.
- [ ] Background levels do not exceed canvas, region, and selected.
- [ ] Borders and radii follow the selected profile; status dots and section rules are opt-in.
- [ ] Status is text-first; tags and icons are functional.
- [ ] Helper text adds non-obvious information.
- [ ] Focus is visible and meaning does not depend on color.
- [ ] Semantics, labels, keyboard flow, responsive behavior, and reduced motion work.

## Finding format

```text
[rule ID] Short finding
Evidence: What is present in the artifact.
Impact: How it obscures or competes with the primary task.
Replace with: A specific, simpler structure.
```

Prioritize architecture-changing findings. Finish with the smallest ordered change set that resolves the highest-impact failures.
