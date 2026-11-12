# Contributing

Contributions are welcome when they make the skill more accurate, portable, safer, or easier to use. Keep the skill focused on *existing backend → context-aware working frontend*, not a general catalog of frontend trends.

## Before a pull request

1. Open an issue for changes that significantly alter the skill's goals, structure or safety behavior.
2. Keep `SKILL.md` concise and move specialized guidance to `references/`.
3. Make rules framework-neutral unless the reference specifically addresses a named stack.
4. Add a concrete failure mode and verification approach for new performance advice.
5. Avoid unverifiable claims such as “works on every project” or “guarantees 90+ Lighthouse”.
6. Run `python3 tests/validate.py` and mention what you tested.

## Pull requests

Describe the problem, affected scenarios, changes, tests performed and tradeoffs. Prefer small focused PRs. Do not copy brand designs, private code, copyrighted visual assets or sensitive production payloads into examples. If updating the demo media, verify the license and playback and keep Git history size in mind.

The license is MIT; contributed content is submitted under the repository's license. For security-sensitive issues, see [SECURITY.md](SECURITY.md) rather than opening a public issue.
