# Principles

Shibui builds quiet, structured interfaces by making relationships and actions clear. These principles apply to reading pages and GUI tools alike. Visual defaults are defined separately in [the standard style](style.md).

## 1. Preserve the information needed for the task

Start with the user's primary task. Keep the information and controls needed to complete it available together. Density follows the task: a reading page can be spacious; a comparison table or editor can be dense. Removing required context, or making users remember values between views, does not simplify the work.

## 2. Reveal secondary detail on demand

Move substantial secondary content to a focused destination or labeled disclosure. Keep required comparisons, editing controls, and immediate feedback visible. A persistent inspector is appropriate when editing the selected object is part of the main task.

Disclosure must remain discoverable, with descriptive triggers and logical keyboard navigation. Do not hide errors or prerequisites behind optional sections.

## 3. Give each view a clear purpose

State the purpose as a verb phrase: read a guide, choose a project, or compare and adjust a plan. A tool may need several coordinated regions to serve that purpose. One primary task does not mean one control or one visible region.

Choose the interaction model before the layout. Pages support reading and navigation; GUI tools support repeated manipulation, comparison, selection, and immediate feedback. A product may contain both. See [paired examples](patterns.md#page-and-gui-tool).

## 4. Structure through space

Build hierarchy with whitespace, alignment, and typography before adding backgrounds or borders. Use proximity to group related controls, larger intervals to separate sections, and shared edges to make relationships legible. Whitespace must preserve useful context and readable density. Let the roles of adjacent regions guide their separation: menu and content usually need more space than comparable peer items, even inside a nested layout. Refine that starting point against the rendered composition, including grouping, balance, wrapping, and usable content widths.

## 5. Draw only meaningful containers

A visible treatment should communicate interaction, selection, warning, input, or a boundary that would otherwise be ambiguous. Ordinary groups, page headers, and footers need no line by default. Prefer semantic sections, groups, rows, and regions over generic cards.

## 6. Preserve affordance and access

Controls must be recognizable, keyboard focus conspicuous, targets usable, and meaning independent of color. Use semantic HTML and native controls where appropriate. Preserve task context when adapting to smaller screens; stacking regions or allowing a labeled comparison table to scroll can be better than hiding required values.

## Principles and standard style

The principles above are shared requirements. The standard style supplies visual defaults, including rectilinear geometry and no shadows. Products can define a different named style without changing these principles. Record visual overrides once with their purpose; evaluate their usability against the principles. A rounded control is not automatically a structural failure, and an undecorated screen is not automatically usable.
