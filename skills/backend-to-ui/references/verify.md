# Verification (evidence over confidence)

## Function
- Main user goal works from real entry point to result; no inert controls or disconnected form.
- Real values map to permitted backend fields; no fake metrics/actions.
- Forms show validation and pending, double-submit protection, success, errors, conflict state.
- Loading, empty, permission denial, offline/timeout and retry are deliberate.
- Back/forward, deep link, search/filter/pagination, long data, keyboard and mobile work.

## Performance
- Capture network and render baseline before optimizing where practical.
- Check large records, duplicate/in-flight requests, late A vs newer B search, request failures, cache isolation and list DOM growth.
- Run available build/test/typecheck and browser tests; log what was actually measured.
- If browser tools not available, state that visual QA remains unverified. Never claim a score or Lighthouse pass without evidence.

## Visual critique
- Would a genuine user of *this* product recognize the purpose from the first screen?
- Is the main next step obvious? Does the UI reveal enough context to make a decision?
- Does visual hierarchy serve the task? Is it original to its category rather than generic AI output?
- Test at phone and desktop widths; inspect actual screenshots and fix meaningful issues.

## Closing report

Mention: user flow built; endpoints/contracts used; data-performance decisions; tests and observed metrics; significant visual correction; outstanding verification limits. No need to generate five ceremony documents for a small repository; keep documentation proportional.
