# Principles

Shibui is a low-surface design system. It is restrained, not empty: every remaining element has a clear job, and structure remains visible without decorative scaffolding.

## 1. Show less by default

Begin with the information required for the current task. Remove speculative context and move large secondary content to a focused destination. Low density is an information-architecture decision, not merely extra padding.

## 2. Reveal detail on demand

Use navigation, dedicated detail views, native disclosure controls, or explicit actions. A project list should help someone choose a project; activity and metadata belong on the chosen project's view.

Disclosure must remain discoverable. Label the action by what it reveals—“Show archived projects” is better than an unlabeled chevron.

## 3. One screen, one primary task

State the view's purpose as a verb: choose a setting, find a project, understand a project, or update an organization. Supporting actions may exist, but they must not compete with that purpose.

## 4. Structure through space

Build hierarchy in this order:

1. Whitespace
2. Alignment
3. Typography
4. Background
5. Border

Do not skip directly to a box. Proximity groups related controls; larger intervals separate sections; a shared edge makes relationships legible.

## 5. Draw only meaningful containers

A container earns a visible treatment when it communicates state, interaction, or a semantic boundary. Selection can use a subtle background. An input needs a boundary. A generic content grouping usually needs neither.

Prefer `Page`, `Section`, `Region`, `Group`, `Stack`, `Row`, and `Divider` over a generic `Card` primitive.

## 6. Keep the visual language quiet

- Never use shadows, elevation, or decorative gradients.
- Limit backgrounds to canvas, region, and selected states.
- Keep geometry rectilinear; reserve pills for controls whose shape carries meaning.
- Use one accent and restrained semantic colors.
- Let text carry information; add icons only when they improve recognition or enable an icon-only action.

## 7. Preserve affordance and access

Restraint must not make controls ambiguous. Inputs may have borders, keyboard focus must be conspicuous, interactive targets must be usable, and meaning must never depend on color alone. Progressive disclosure must preserve a direct route to hidden content.
