# Live browser QA — verify the actual running product

Do not call an interface "tested", "responsive" or "ready" just because a build passed or a design screenshot looks good. Use a **real browser, WebView or native simulator when available**. Tools may be Playwright, browser DevTools/CDP, Chrome DevTools MCP, agent-browser, an approved browser plugin, or an agent's own browser/computer-use tool. Tool names vary. **Only invoke tools that exist in the current host**.

## Risk-first tool choice

1. Reuse the running app and existing browser/test framework first. Use its actual host/port, startup instructions and authentication approach.
2. Prefer existing Playwright/Cypress/browser tests over adding a dependency; use DevTools/CDP or browser-agent navigation for gaps.
3. If no browser tool is available, run available unit/integration/lint/typecheck and report **live browser QA: unverified**. Don't claim a tool ran or install a new browser automation package without checking project policy.
4. **Safety:** use local development/staging, test accounts and seeded non-sensitive data. Avoid production modifications or destructive requests. An isolated local server is preferable; stop servers you start, unless the user requests otherwise. Never expose debugging ports publicly.

## Minimum live checks for a changed user flow

- **Navigate** to the actual route and wait for usable content, not just a splash.
- **Interact** with the changed task: input, select, submit, navigate, undo/confirm where applicable. Verify resulting UI and persistence/network response when relevant.
- **Inspect DevTools evidence:** JavaScript errors, failed requests, runtime warnings. For a backend-driven change, verify the endpoint, status and payload/permission semantics from the actual network trace where authorized.
- **Exercise states relevant to the change:** loading, empty, validation error, unauthorized, retry and mutation feedback. Don't test irrelevant states just to inflate a checklist.
- **Render** the actual page at desktop and mobile widths; an intermediate viewport for layout changes when practical. Inspect full viewport, content clipping, overflow, focus/keyboard and touch targets. For changes affecting keyboard/touch, actually exercise the behavior—not only inspect CSS.
- **Correct + retest** any serious product-fit, visual composition, accessibility or functional failure. Avoid repeated screenshot captures without an intervening correction.

## Tool-mode notes

- **DevTools/CDP:** console/runtime errors, network request status and performance timeline. Use a *local* debugging endpoint; bind to 127.0.0.1.
- **Playwright/Cypress:** reproducible navigation, assertions, input, screenshots, viewport/device emulation and regression suites.
- **Agent browser / browser plugin:** inspect and click within available permissions; record what was visibly observed. Do not assume API network capture or persistent automation if unavailable.
- **Native apps:** use platform simulator/UI test tools instead of pretending browser viewport screenshots prove native behavior.

## Evidence contract

A compact report is enough:

\`\`\`text
route + environment: /orders | local staging
tool: Playwright Chromium | test account | actual run
actions: search → select → confirm → persisted state (pass)
runtime: 0 uncaught errors; relevant requests verified
screenshots: desktop-1440.png; mobile-390.png
unverified: production SSO; physical iOS device
\`\`\`

If a result is simulated/fixture data, label it. Passing smoke tests does not imply a full security audit, accessibility conformance or production readiness. Do not publish credentials, cookies or sensitive network bodies.
