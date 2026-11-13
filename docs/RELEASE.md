# Release checklist

This project is a source-only Agent Skill, not a compiled frontend package. A green README validator or passing GitHub Actions does **not** guarantee production-ready generated applications.

## Before tagging

1. Review `skills/backend-to-ui/SKILL.md`, mandatory [stack-selection policy](../skills/backend-to-ui/references/stack-selection.md), data/performance/design/visual references and security guidance.
2. Run `python3 tests/validate.py` and `python3 -m unittest discover -s tests -p 'test_*.py' -v`.
3. Test discovery with `npx skills add alifakbxr/backend-to-ui --list`. This validates CLI discovery; it is not proof of listing/indexing on skills.sh.
4. Run real agent evaluations from [evals/README.md](../evals/README.md). Record exact agent/model/skill SHA, questions, changed files, screenshots, accessibility checks and network/render traces. **Explicitly disclose scenarios you have not executed.**
5. Confirm one-shot obeys stack selection: no frontend stack → one question, zero implementation files; chosen stack or authorized existing stack → continue.
6. Check important permissions, private cache boundaries, loading/error behavior, slow network and a meaningful long-list stress case.
7. Update README, changelog and skill metadata version consistently; preserve known limitations.
8. Use a human review to merge a PR. Create a signed or annotated version tag/release only **after** the intended changes reach `main`. Do not tag a PR branch as production release.

## Versioning

- `metadata.version` in `SKILL.md` is the human-readable skill version.
- `CHANGELOG.md` records unreleased and released changes. A changelog entry alone is **not** a GitHub Release.
- Git tags `vMAJOR.MINOR.PATCH` and optional GitHub Releases should reference actual commits on `main`.
- For evaluation reproducibility, always capture a commit SHA; relying only on the current `main` loses historical context.

## Review boundaries

Do not merge if an agent silently chooses native HTML when the stack is unspecified, a read-only audit edits files, a visual stop-ship defect remains unacknowledged, or performance claims lack measured evidence.

The instructions and tests are stack-agnostic. They are not a substitute for release QA in an actual Laravel, Django, React, Vue, native, or other target application.
