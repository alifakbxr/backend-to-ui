# Existing frontend: change safely, preserve the product

Works for **frontend-only**, full-stack and native apps. Lack of a backend does not prevent a real UX redesign; lack of an explicit stack decision *does* block UI file edits. See [stack-selection.md](stack-selection.md).

## Inspect what exists (scoped)

Identify only relevant:
- framework/renderer, package scripts, active route/page, reusable components;
- brand tokens, typography, layout conventions, localization and authentic assets;
- state and data owner (stores, page props, services, persistence, permissions);
- existing interactions (navigation, forms, keyboard/touch, loading/errors);
- current tests/screenshots or UI baselines.

Use an existing `UI_CONTRACT.json` if present. When absent, existing tokens and components are **observed evidence**, not automatic user approval; a small fix does not need a new file. If major design direction changes, consider a provisional source-backed contract (see [design-contract.md](design-contract.md)).

## Scope before editing

**Preservation map:** what must keep working vs what can change. No removal of unrelated routes, state, access controls or backend integration merely to simplify the UI. Avoid new frameworks, extra data owners, duplicate API calls, needless libraries and unrelated app shells.

- Small fix: patch the smallest component; reuse current visual identity and libraries.
- Feature: reuse routing/state patterns, verify changed user journey and existing related flows.
- Full redesign: inspect screens, establish domain-specific hierarchy and tokens, migrate incrementally while protecting working interactions.
- Backend-only: require selected stack and map actual handlers; no invented CRUD, metrics or permissions.

## Stack idioms

| Existing frontend | Preserve | Avoid |
| --- | --- | --- |
| Vue / Inertia / Nuxt | page props, composables, state, SSR and routing | re-fetching page props, deeply reactive giant lists |
| React / Next / Remix | route boundaries, installed state/query libraries, SSR | redundant client/server requests, global rerenders |
| Angular / Svelte / Solid / Astro | existing DI/reactivity, loaders, lifecycle | unnecessary replatforming/hydration |
| WordPress / Django / Rails / HTMX | templates, navigation and progressive enhancement | replacing everything with a SPA |
| Plain HTML/CSS/JS | semantic markup, current styling and accessible events | adding a framework without approval |
| Flutter / SwiftUI / Compose / React Native | native controls, lifecycle, accessibility | assuming browser/CSS primitives |

Other frameworks are supported through their **actual project conventions**, not a static template.

## Regression checklist

1. Test primary task and preserve related routes, forms, selection, filter, state persistence, localization and permission behavior.
2. Test relevant loading/empty/error/retry and fast repeated user actions.
3. Inspect actual desktop/mobile UI (or native target device) and changed interaction in real browser/device tools when available; see [live-browser.md](live-browser.md).
4. Fix composition/interaction issues, rerun affected checks and report any unavailable evidence.

Never call fixtures production, claim unseen screenshots were inspected, or conceal untested flows.
