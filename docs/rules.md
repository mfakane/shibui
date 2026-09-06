# Review rules

Use these near-binary checks after establishing the view's primary task. An exception is acceptable only when its purpose is recorded.

## Information architecture

- **IA-01 — Primary task:** The page title, first content section, and primary action support one stated task.
- **IA-02 — Secondary content:** Large secondary content is absent by default or available through an explicit drill-down/disclosure.
- **IA-03 — Persistent panels:** No inspector, activity feed, metadata panel, or filters remain visible unless required for the primary task.
- **IA-04 — Discoverability:** Every hidden region has a descriptive trigger and a logical focus/navigation path.

## Structure

- **ST-01 — Grouping order:** Related content is grouped by spacing and alignment before backgrounds or borders.
- **ST-02 — Semantic containers:** Every visibly drawn container communicates interaction, selection, warning, input, or another named meaning.
- **ST-03 — Nested surfaces:** No surface is nested inside another surface merely to create hierarchy.
- **ST-04 — Dividers:** Each divider separates regions that remain ambiguous without it.

## Visual language

- **VI-01 — Effects:** `box-shadow`, `text-shadow`, filter-based shadows, and decorative gradients are absent.
- **VI-02 — Surface limit:** A view uses no more than canvas, region, and selected background levels.
- **VI-03 — Borders:** Borders are limited to inputs, focus indicators, explicit separators, and meaningful warning/destructive boundaries.
- **VI-04 — Radius:** Default radius is zero; small radii or pills are used only for affordance or semantic shape.
- **VI-05 — Color:** The interface uses one accent; semantic color adds information and does not act as decoration.
- **VI-06 — Typography:** Page and section hierarchy uses size, placement, and whitespace; body copy is not needlessly bold.

## Components and content

- **CO-01 — Cards:** Generic cards are absent. Card-like treatment has a documented interaction or semantic purpose.
- **CO-02 — Status:** Status is text-first; a dot or color is added only when faster recognition matters.
- **CO-03 — Tags:** Every tag represents a genuine category, filter, or action.
- **CO-04 — Icons:** Every icon supports navigation, an icon-only action, type recognition, or meaningful system status.
- **CO-05 — Helper text:** Helper text explains information a reasonable user cannot infer from the label, value, or surrounding context.
- **CO-06 — Forms:** Fields are grouped by topic and use a boundary only to establish input affordance.

## Accessibility

- **AC-01 — Focus:** All interactive elements expose a visible `:focus-visible` indicator.
- **AC-02 — Color independence:** Text or another non-color cue communicates selection, status, errors, and warnings.
- **AC-03 — Semantics:** Landmarks, headings, lists, tables, labels, and native controls match their meaning.
- **AC-04 — Motion:** Essential behavior does not depend on animation, and reduced-motion preferences are respected.

## Review output

For each failure, report: rule ID, observed issue, why it competes with the primary task, and a specific simpler replacement. Prioritize architecture before cosmetic cleanup.
