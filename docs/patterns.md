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

Add `data-column-divider` to a two-column group only when its functional boundary needs an explicit separator. Its second direct child is the content column and owns a `::before` pseudo-element. The 1px line sits at the center of the gap using `--column-gap`, which also controls the grid spacing. Its ends are inset by `--column-divider-inset` (8px by default). No JavaScript or measurement is required.

The line follows the content column's height, even if the navigation column is shorter. Keep `align-items: start` so a taller sidebar does not stretch the content and its separator. For the outer layout, the content column is `.app-main`; for nested settings it is `.settings-content`.

The outer shell supplies 3rem top and 2rem bottom padding (1.5rem top on mobile), so the line cannot cut through the page edges. The sidebar keeps its natural height and scrolls with the content. When columns stack, their vertical separator disappears; no full-width horizontal replacement is added. Content changes, wrapping, and font loading naturally resize the CSS line along with its content column.

### Spacing depends on roles and visual balance

A line's presence does not determine its surrounding spacing. Choose the gap for the relationship of the regions, then center the line inside it. Menu and content are different functional roles, so both workspace navigation and local settings navigation use the wide region gap. Small peer items use the compact gap. Editing and immediate results also have different roles, but their tight task coupling calls for a nearer gap. Nesting depth or apparent size alone does not determine spacing.

| Context | Total column gap | Space on each side of the line |
| --- | --- | --- |
| Workspace sidebar and main task | 6rem | Approximately 3rem |
| Local settings navigation and controls | 6rem | Approximately 3rem |
| Project hours editing and Capacity results | 3rem | Approximately 1.5rem |
| Homepage principle columns | 2rem | Approximately 1rem |

`--gap-region` supplies the 6rem gap for menu/content boundaries at both navigation levels. `--gap-peer` supplies the 2rem gap for comparable items such as homepage principles. Each layout assigns the appropriate token to `--column-gap`; the divider remains centered automatically.

These values are reference defaults, not mandatory dimensions. Check the rendered composition: menus and content should feel distinct, peer items should still form a group, and inputs and text should retain comfortable widths. Tune the local gap or stack columns if wider spacing causes crowding or excessive wrapping; avoid empty space that makes related regions feel disconnected. Keep the divider centered in the resulting gap. When local settings navigation stacks, use the compact gap between it and the controls because the horizontal composition has changed.

The homepage opts into `data-separators="columns"` on `.principle-grid`. Its 1px rules sit between items in each three-column row, inset 8px at the ends. There is no line before the first item of a row, across the row gap, or after the last item. At the existing single-column breakpoint, the rules disappear. The pseudo-elements take no layout space, so adding them does not change item widths or spacing.

### Editing and immediate results

The GUI tool opts into `data-column-divider` on `.workspace-grid`. Project hours and Capacity form one editing/feedback loop: a 1px line clarifies their roles while the existing 3rem gap keeps comparison close. The line belongs to Capacity, follows its height, and is inset 8px at both ends. At 44rem and below, the sections stack with their existing 2rem gap and the vertical line disappears. This treatment is CSS-only; calculation behavior is unchanged.

## Shared page and tool structure

Reading examples use `.shell.page` with a `.reading` article. Task examples use `.shell.page.workspace`, or `.app-main.workspace` inside `.app-shell` when navigation columns are needed. The shell owns the available layout width; `.workspace` changes task typography and header spacing, not content width. All examples use `.page-header`. Do not add a narrow wrapper around an entire task to fix a misplaced action.

Use `.reading` for article line length and `.lede` for introductory reading copy. GUI descriptions use ordinary paragraphs. A header spans the task region, and `.split` aligns its actions with that region's edge before stacking on small screens.

Both project lists use `.table-wrap` for accessible horizontal scrolling and `.project-table` for the same column and row treatment. Both settings forms use `.setting-row` for label/control alignment and responsive stacking. The allocation tool keeps `.allocation-table` because editable numeric cells have different requirements. `.settings-columns` and `.workspace-grid` describe different column roles, not different generations of components.

Settings, Detail, and Form use the available task width without `.page-content` or a form-wide maximum. Ordinary detail sections use headings and whitespace; the destructive form boundary spans its task region. A genuinely constrained input or text block may have a local width chosen for its content, but that must not silently constrain the surrounding header, actions, or other regions.
