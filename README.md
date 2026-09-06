# Shibui Design System

**Less surface. More structure.**

Shibui is a framework-independent design system for quiet, structured interfaces. It treats information architecture as part of visual design: show only what supports the current task, reveal secondary detail on demand, and establish hierarchy with space, alignment, and type before adding surfaces or borders.

## Start here

- Read the [principles](docs/principles.md) before designing a view.
- Use the [review rules](docs/rules.md) and machine-readable [`shibui.yaml`](shibui.yaml) as implementation constraints.
- Link [`css/tokens.css`](css/tokens.css), [`css/base.css`](css/base.css), and [`css/components.css`](css/components.css), in that order.
- Open [`index.html`](index.html) to browse four framework-free reference pages.
- Give Coding Agents [`skill/SKILL.md`](skill/SKILL.md) for implementation and review workflows.

## Reference pages

| Page | Primary task | Disclosure pattern |
| --- | --- | --- |
| [Settings](examples/settings.html) | Choose a settings category | Navigate to a focused category |
| [Projects](examples/list.html) | Find and open a project | Search/filter, then drill down |
| [Project detail](examples/detail.html) | Understand one project | Expand optional details |
| [Organization form](examples/form.html) | Update organization details | Reveal advanced fields on demand |

No build step or frontend dependency is required. Serve the repository with any static server, for example `python3 -m http.server 8000`.

## Browser support

The reference CSS targets current evergreen browsers. It respects reduced-motion preferences and uses native HTML controls wherever possible.

## License

[CC0 1.0 Universal](LICENSE)
