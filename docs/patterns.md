# Patterns

## Page and GUI tool

Compare `examples/page.html` and `examples/tool.html`. Both concern a project plan and use the same tokens and components.

| | Reading page | GUI tool |
| --- | --- | --- |
| Task | Understand the planning method | Compare and adjust allocations |
| Structure | Article with sequential headings | Editable table and live capacity summary |
| Density | Comfortable line length and section spacing | Related values and controls visible together |
| Disclosure | Optional background notes | Only calculation notes; inputs and results stay visible |
| Small screens | Reflow text | Stack the summary and keep the table in a labeled scroll region |

The tool's persistent result region belongs to the primary task. It is not an exception to progressive disclosure. Edits are local to the demo and are not saved.

## Focused index

Present categories as a quiet list of links with short descriptions. Navigate to a dedicated view instead of rendering every category's controls on one settings page. See `examples/settings.html`.

## List to detail

Keep list columns limited to identification, decision-critical state, and recency. Make names direct links. Put ownership history, activity, and extended metadata on the detail page. See `examples/list.html` and `examples/detail.html`.

## Optional form fields

Show fields required for the common path. Put infrequent configuration in a labeled native `details` disclosure. Keep actions adjacent to the form they submit. See `examples/form.html`.

## Status text

Use plain text by default. Opt in with `data-marker="dot"` only where scanning several states is central to the task. Do not put routine status inside a pill-shaped background.

## Meaningful region

Use the region background for content that has a distinct semantic role, such as contextual guidance or selection. Do not nest another surface inside it. Prefer a heading and whitespace for ordinary sections.

## Destructive action

Keep destructive actions quiet while inactive, separate them from the primary workflow, and require clear confirmation. Use semantic red for the action text or a meaningful warning boundary—not for an entire decorative panel.
