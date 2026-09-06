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

## Application columns

`examples/columns.html` uses `.app-shell` to place workspace navigation beside a project list. `examples/columns-settings.html` nests `.settings-columns` inside the task area for a third column of local section links. Global navigation changes destinations; local navigation moves to named sections of the current settings view. Both remain ordinary keyboard-accessible links.

The sidebar supports movement between workspace tasks. The local column is useful when users revisit several settings sections. These are optional patterns, not a required shell for reading pages or focused tools. Navigation columns need no separate background. Selection uses the selected background plus heavier text and `aria-current`. These examples opt into a restrained boundary between adjacent navigation and content regions.

At 68rem and below, local navigation moves above the settings. At 48rem and below, workspace navigation moves above the main content and the sample identity is omitted. At 36rem and below, field labels stack above controls. Required inputs and section links remain available. Only the project table scrolls horizontally when needed, through a named, focusable region.

The settings example is a live control preview without persistence or a save action. Keep the reference source expanded and run `npm run format` after edits.

### Content-length column dividers

Add `data-column-divider` to a two-column group only when the navigation/content boundary needs an explicit separator. Its second direct child is the content column and owns a `::before` pseudo-element. The 1px line sits at the center of the gap using `--column-gap`, which also controls the grid spacing. Its ends are inset by `--column-divider-inset` (8px by default). No JavaScript or measurement is required.

The line follows the content column's height, even if the navigation column is shorter. Keep `align-items: start` so a taller sidebar does not stretch the content and its separator. For the outer layout, the content column is `.app-main`; for nested settings it is `.settings-content`.

The outer shell supplies 3rem top and 2rem bottom padding (1.5rem top on mobile), so the line cannot cut through the page edges. The sidebar keeps its natural height and scrolls with the content. When columns stack, their vertical separator disappears; no full-width horizontal replacement is added. Content changes, wrapping, and font loading naturally resize the CSS line along with its content column.
