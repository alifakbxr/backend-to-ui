# Read backend data as a product contract

## Discovery order

1. Read package manifests and README, app/router entry points, schemas/migrations, API specs, example responses, tests, plus existing frontend before making assumptions.
2. Inventory routes/endpoints or handlers (including HTTP methods, params, schema, middleware/policy, errors, rate limits, sorting and pagination). In server-rendered systems, inspect view models/page props rather than assuming an HTTP JSON API.
3. Trace source → query → serialization → transport → client mapping → UI. Identify sensitive and tenant-scoped fields; do not expose internal objects or secrets to the client.
4. Identify top user tasks. Attach each screen element to contract evidence. Never surface fields simply because they exist in a model.

## Suggested mapping (keep in reasoning or create a small file)

| Human task | Backend operation | Relevant fields | Authorization | UI behavior | Failure |
|---|---|---|---|---|---|
| Find an order | GET /orders?q=... | id, customerName, status, total | orders.read | Search + paginated results | Offline, empty, 401, 403, 429 |
| Update order | PATCH /orders/:id | status, version | orders.update | Form, pending, confirmation | Validation, conflict, rollback |

This table is illustrative, **not** authorization to invent these endpoints in a real project.

## Protocol-specific checks

- **REST/OpenAPI:** response envelopes, offset/cursor, conditional requests, Retry-After, partial fields, idempotency, 401/403/404/409/422/429/5xx.
- **GraphQL:** fragments and nested depth, variables, cursor connections, partial `data` with `errors`, normalized cache, N+1 at resolver.
- **tRPC/RPC/gRPC:** generated types, status codes, unary vs streaming, deadline and cancellation, versioned schemas.
- **Server templates / Inertia / SSR:** page props and shared props, partial reload, validation bags, flash messages, server query params, progressive enhancement, revalidation.
- **WebSockets/SSE:** stream lifecycle, reconnect/backoff, event sequence, eventual consistency, auth expiry, dedupe, resync after gaps.

## State machine

Every asynchronous view must distinguish: idle → loading → success/empty or failure. Also consider refresh with previous content, partial response, offline, unauthorized, forbidden, not found, rate-limited, cancelled, stale, conflict and post-mutation reconciliation. Show a retry action only when retry is valid.

Never let the frontend infer authorization from hidden buttons alone. Server validates every mutation. Scope cached data by user/tenant/role/query, invalidate on permission change or logout. Avoid storing credentials in logs, fixtures or public files.
