# Standard style

This is Shibui's default visual profile, implemented by `css/tokens.css`, `css/base.css`, and `css/components.css`. It is separate from the shared [principles](principles.md).

- No shadows, elevation, or decorative gradients.
- At most three background roles: canvas, region, and selected.
- Rectilinear geometry: zero default radius, 2px for small control radii, semantic pills only.
- One accent, with semantic colors used to convey information.
- Borders for inputs, focus, explicit separators, and meaningful warning boundaries.
- Text-first status; functional tags and icons only.

Density is task-dependent, not a visual conformity score. Both page and tool examples use this profile.

## Explicit treatments

`.status` is plain text. Add `data-marker="dot"` only when scanning states benefits from a redundant marker; retain the text label. `data-state="active"` sets the marker's color but does not enable it.

`.principle` has no rule by default. Add `data-separator="top"` only where the section boundary is otherwise ambiguous. Ordinary headers and footers remain unruled.

Column spacing uses `--gap-region` (6rem) for distinct menu/content roles and `--gap-peer` (2rem) for comparable items. These are adjustable defaults; choose by role and visual balance, not outer versus inner nesting. See [column patterns](patterns.md#spacing-depends-on-roles-and-visual-balance).

## Product profiles

To use another profile, declare its name and overrides in the product's design notes, then apply its tokens or CSS after the standard styles. For example, rounded control geometry can be a deliberate product default. Record the reason once rather than treating every instance as an exception. Review visual rules against the selected profile and always review structure and accessibility against the shared principles.

`shibui.yaml` separates `principles`, `information`, and `accessibility` from `style_profiles.standard`. Tools consuming the previous top-level `visual` or `components` keys must use the profile keys in version 0.2.0. The repository CSS validator checks this repository's standard profile; it is not a universal validator for every Shibui product profile.
