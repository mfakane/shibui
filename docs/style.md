# Standard style

This is Shibui's default visual profile, implemented by `css/tokens.css`, `css/base.css`, and `css/components.css`. It is separate from the shared [principles](principles.md).

- No shadows, elevation, or decorative gradients.
- At most three background roles: canvas, region, and selected.
- Rectilinear geometry: zero default radius, 2px for small control radii, semantic pills only.
- One accent, with semantic colors used to convey information.
- Borders for inputs, focus, explicit separators, and meaningful warning boundaries.
- Text-first status; functional tags and icons only.

Density is task-dependent, not a visual conformity score. Both page and tool examples use this profile.

## Light and dark appearance

The standard profile follows the system light/dark preference without JavaScript.
To override it, set `data-theme="light"` or `data-theme="dark"` on the root
`<html>` element. Omit the attribute to follow the system again. Native controls
follow the same color scheme.

Both appearances share the same visual rules, including the three background
roles. The dark palette adapts [Stream Pointer Overlay’s dark profile](https://github.com/mfakane/stream-pointer-overlay/blob/master/DESIGN.md):
blue-black canvas, quiet secondary regions, and one lime accent for actions and
focus. Keep content, controls, and states on semantic CSS tokens so they work in
either appearance. Product-specific effects such as the overlay’s preview grid
are not part of the shared profile.

## Explicit treatments

`.status` is plain text. Add `data-marker="dot"` only when scanning states benefits from a redundant marker; retain the text label. `data-state="active"` sets the marker's color but does not enable it.

`.principle` has no rule by default. Add `data-separator="top"` only where the section boundary is otherwise ambiguous. Ordinary headers and footers remain unruled.

Column spacing uses `--gap-region` (6rem) for distinct menu/content roles and `--gap-peer` (2rem) for comparable items. The editing/results tool retains a 3rem gap because its regions are closely coupled. These are adjustable defaults; choose by role, task coupling, and visual balance, not outer versus inner nesting. See [column patterns](patterns.md#spacing-depends-on-roles-and-visual-balance).

## Product profiles

To use another profile, declare its name and overrides in the product's design notes, then apply its tokens or CSS after the standard styles. For example, rounded control geometry can be a deliberate product default. Record the reason once rather than treating every instance as an exception. Review visual rules against the selected profile and always review structure and accessibility against the shared principles.

`shibui.yaml` separates `principles`, `information`, and `accessibility` from `style_profiles.standard`. Tools consuming the previous top-level `visual` or `components` keys must use the profile keys in version 0.2.0. The repository CSS validator checks this repository's standard profile; it is not a universal validator for every Shibui product profile.
