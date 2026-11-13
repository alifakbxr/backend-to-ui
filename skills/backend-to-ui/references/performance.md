# Performance and data flow

## Decide the pipeline before components

Map the available pipeline: database → query → serializer → transport → client query/cache → view **when applicable**, or local state → derivation → view for frontend-only work. Find the bottleneck at its owner, instead of moving work blindly into the browser.

**Server:** index hot filters, avoid N+1 with explicit eager loads/batched resolvers, aggregate in SQL when sensible, select needed fields, set stable ordering, serve page/cursor windows, use HTTP caching where safe. Do not paginate an unordered relation or inflate massive nested JSON.

**Network:** deduplicate in-flight same-key reads, cap parallel fetches, avoid waterfalls and background request storms, follow API rate limits, gzip/brotli where available, classify retryable status. Use `AbortController`/equivalent for obsolete requests and an incrementing sequence/token when cancellation is insufficient. Never reuse a private cache entry across authentication scopes.

**Frontend-only:** profile heavy computed selectors, expensive effects/watchers, unnecessary third-party packages, event listener leaks, layout thrashing, long lists and animation jank even when there is no network request.

**Client:** choose one data owner per dataset; maintain normalized, minimal state. Use stable keys and memoization selectively. Derive simple computed view state, not duplicate sources of truth. Debounce text search when it triggers network I/O. Never deeply proxy thousands of records needlessly. Paginate or virtualize long lists, with accessible fallback and correct row identity. Avoid render-time sorting of full datasets, nonessential hydration and large bundles.

**Mutations:** lock/dedupe repeated submissions as appropriate, display pending/error, apply server authoritative result, invalidate precisely; optimistic state only with safe rollback. Do not call refetch for the entire application after one update unless required.

**Realtime:** batch UI updates, skip duplicate/out-of-order events, patch keyed entities, reconnect and resync, protect scroll/focus, suspend streams that are no longer visible if possible.

## What to measure

Measure baseline and after for representative workflows, using browser/device profiler if available:

- Requests per route/action, duplicate requests, failed requests, 95th percentile endpoint latency, payload KB.
- Time to first meaningful content, page responsiveness (INP where measurable), longest blocking task, JS bundle/hydration cost, DOM node count/long-list behavior.
- Slow network; fast typing with overlapping responses; 10x data; throttled CPU; flaky API; back/forward restoration; permission change.

Use targets only as starting hypotheses, never claim results without measurement. Example **targets**: avoid >500 visible DOM list rows without virtualization; keep normal interactions under ~200 ms where feasible; keep requested first-page JSON proportionate to what is displayed. Real thresholds depend on device and product.

## Quick acceptance tests

1. Trigger query A then B; ensure late A never replaces B.
2. Trigger identical reads simultaneously; verify only one in-flight request when dedupe is intended.
3. Verify page 2 doesn't load every prior page unless that is the deliberate UX.
4. Render 10k representative items; DOM stays bounded and scrolling remains responsive.
5. Force 401, 403, 422, 429 and 500; UI handles them without exposing sensitive data or losing user input unnecessarily.
6. Change tenant/user/session and confirm cached private data is not reused.
