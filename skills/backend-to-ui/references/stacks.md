# Adapt to the stack; don't replace it

The correct frontend is the least disruptive implementation that meets the task.

| Existing architecture | Preferred approach | Common trap |
|---|---|---|
| Laravel + Inertia + Vue/React | Reuse page props, server filters, pagination, FormRequest/policies, existing components; use partial reload only when beneficial | Redundant Axios requests for props already delivered |
| Django/Rails/Phoenix/server templates | Server-rendered forms, querysets/preload, turbo/HTMX where already present, progressive enhancement | Replatforming to SPA without a reason |
| Next/Nuxt/SvelteKit/Remix | Existing loaders/server components, cache semantics, route conventions, streaming as appropriate | Fetching the same data twice on server + client |
| Vue/React/Angular/Svelte SPA | Installed query/cache libraries, precise state ownership, abort/race protection | Global reactive arrays and entire-list rendering |
| Spring/ASP.NET/Go/Rust backends | Match existing transport and generated client/types; decide SSR or SPA based on repo constraints | Inventing JSON envelopes or auth rules |
| Flutter/SwiftUI/Jetpack Compose | Native asynchronous data layer, paginated lists, lifecycle and cancellation, native navigation and accessibility | Assuming browser/CSS primitives apply |
| GraphQL/gRPC/realtime | Generated types, cursor connections, streaming and cancellation semantics | N+1 or unbounded realtime update loops |

Do not install large dependencies, rewrite auth, change the domain schema, or split out a new frontend service without a concrete documented reason. Respect whatever renderer, router, form library and testing stack is already working.
