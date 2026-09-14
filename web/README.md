# Frontend Decisions

## Toolchain

- React, TypeScript, and Vite for the application UI.
- Bun 1.3.13 for dependency management, TypeScript checking, Vite development, and builds.
- `bun.lock` is the only frontend dependency lockfile. Install with `bun install --frozen-lockfile`.
- Run commands from `web/`: `bun run dev`, `bun run build`, and `bun run test:e2e`.
- Playwright is invoked through Bun scripts but currently uses its Node CLI. Keep Node 22 available for browser tests; the Python API uses the repository virtual environment.
- Backend setup, authentication, and development boundaries: [workspace guide](../workspace_app/README.md).

## UI Foundation

Tailwind CSS uses its official Vite plugin. `src/app.css` defines shared color tokens and imports the existing page CSS into the components layer so utilities can override it predictably. This is an incremental migration, not a claim that every legacy selector has been converted.

`src/components/ui/` contains locally owned, shadcn-style Button and Dialog components backed by Radix Slot/Dialog. These are custom implementations, not an installed shadcn starter or an untouched registry export. Radix manages dialog semantics, focus trapping, Escape dismissal, and background interaction. Tailwind owns their appearance. Lucide supplies icons.

## Library Review

Reviewed September 2026. Popularity is an adoption signal, not proof of design quality or a universal vote for "best."

| Option | Evidence | Decision |
| --- | --- | --- |
| shadcn/ui | Roughly 124k GitHub stars observed; customizable, locally owned component source | Use its composition/ownership approach, with deliberate application-specific styling |
| Mantine | Roughly 32k GitHub stars observed; broad styled React component suite | Credible alternative, but avoid adding another styling system alongside Tailwind |
| React Aria | Adobe's accessible, customizable interaction primitives | Credible alternative; do not duplicate the Radix interaction layer in this increment |

Sources: [shadcn repository](https://github.com/shadcn-ui/ui), [shadcn introduction](https://ui.shadcn.com/docs), [Mantine repository](https://github.com/mantinedev/mantine), [React Aria](https://react-aria.adobe.com/), [Radix Dialog](https://www.radix-ui.com/primitives/docs/components/dialog), [Tailwind with Vite](https://tailwindcss.com/docs/installation/using-vite).

## Design Constraints

- Table-first job discovery and source-linked evidence review; no marketing hero or ornamental dashboard template.
- Compact type, neutral surfaces, green action accents, and distinct warning/error colors.
- One visual hierarchy, restrained borders, and a maximum 8px corner radius.
- No gradient decoration, oversized statistics, stacked cards, or unnecessary animation.
- Prefer native controls for simple inputs and proven primitives for complex interactions.
- Verify real button interactions, dialog bounds, keyboard navigation, and overflow across desktop/mobile before committing UI changes.
