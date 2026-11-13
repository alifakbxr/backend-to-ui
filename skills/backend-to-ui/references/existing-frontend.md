# Existing frontend — safe product improvement

**This skill is not only for backend-only repositories.** Use it on frontend-only projects, production web/mobile frontends, and full-stack applications with established interfaces. Do not treat the absence of a backend as a blocker for redesign, UX, accessibility or interaction work.

## Preserve design decisions across agents

Read the project's `UI_CONTRACT.json` before editing an existing frontend; see [design-contract.md](design-contract.md). If absent, first inspect real brand assets, tokens and UI screens; create a **provisional** contract using observed sources. Treat existing layout as evidence (not necessarily the desired final identity). The agent's own styling preferences cannot override user-approved brand decisions.

## Discover the existing implementation

Read the relevant parts of the project instead of guessing:
- **Framework and renderer:** package manifest, framework config, entry point, page/route structure, SSR or native boundaries, build scripts.
- **Design language:** existing palette, typography, CSS variables/tokens, component library, icons/illustrations, brand and image assets.
- **State and data:** stores, hooks/composables/services, existing fixtures, API clients, server data, persistence, permissions.
- **Interaction contract:** navigation, forms, keyboard/touch flows, loading and failure states, animations, focus, localization and responsive states.
- **Safety net:** tests, storybooks, UI screenshots, accessibility checks, typecheck/build, performance baselines.

Make a short **preservation map**: what may change vs what cannot change. Never delete an existing feature or backend integration just to simplify a redesign.

## Mandatory stack choice applies

If the user names a frontend framework, use it unless materially incompatible with the repository; explain the conflict. If they explicitly say "use the existing stack", detect it and proceed. If the user did **not** specify or authorize a stack, ask once before editing, even when Vue, React or plain HTML is detected. Read-only audits proceed without asking. See [stack-selection.md](stack-selection.md).

## Choose the least disruptive change

- Prefer existing design tokens, routing conventions, state/query libraries, component APIs and build setup. Compose or refactor existing components when useful; avoid duplicate global state.
- If a request is scoped to one feature or screen, do not redesign unrelated surfaces. Preserve keyboard paths, translations, themes and motion preferences.
- If the user specifically requests a comprehensive redesign, audit screen-by-screen, establish a consistent visual language, then migrate incrementally with working checkpoints.
- Preserve feature flags and role/permission logic; verify the same workflows after changes.
- Do not introduce fake APIs, data, role handling, toasts, animations or mock controls without labeling them as prototypes.
- No generic "dashboard-ification": choose task-first composition, test real content and criticize screenshots.

## Practical framework idioms

| Existing frontend | Preserve first | Avoid |
| --- | --- | --- |
| React / Preact / Next / Remix | component props, route boundaries, hooks, query owners, SSR/RSC semantics | gratuitous rerender, redundant fetch layers |
| Vue / Nuxt / Inertia | composables, stores, page props, transitions, component events | refetching page props, deep proxying huge arrays |
| Angular | services/DI, router, reactive forms, signals/observables | subscriptions without cleanup, competing state sources |
| Svelte / SvelteKit / Astro / Solid / Qwik | current render mode, actions/loaders, reactivity and navigation | forcing SPA or hydration everywhere |
| Django/Rails/WordPress/HTMX/templates | server templates, progressive enhancement, accessible forms | rebuilding as React without authorization |
| Plain HTML/CSS/JS | semantic markup, existing CSS structure, keyboard behavior | unnecessary bundler/framework |
| Flutter/SwiftUI/Jetpack Compose/React Native | lifecycle, navigation, native controls, accessible state | applying browser-only patterns to mobile |

The list is illustrative, **not an allowlist**. For an unfamiliar frontend, inspect its own framework docs and project conventions. Never force a favorite technology.

## Regression checklist

1. Capture initial screen state and identify top user task.
2. Implement the chosen layout/interaction in existing components.
3. Verify old and new routes, active tabs, forms, search/filter, sorting, pagination, animations, state restoration, themes and localization.
4. Test slow/failed data, rapid actions and long lists if the app uses them.
5. Capture desktop/mobile before/after screenshots; fix visual stop-ship defects.
6. Report actual tested behavior and outstanding risks. If browser/device testing is unavailable, say so, don't claim a pass.

## Cross-stack scope

The skill provides an engineering workflow, not working code for every framework. Agent ability depends on the project's available tools, tests and actual framework support. Maintain the existing application's architecture unless an explicit migration is requested.
