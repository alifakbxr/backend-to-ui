# product-ui

**Build the interface your product actually needs.**

**Repository:** `product-ui` · **Agent skill:** `backend-to-ui`

An open, stack-neutral [Agent Skill](https://agentskills.io/specification) to **build, redesign, audit or improve an existing frontend**, or turn a real backend into a useful interface. It understands the product, respects the current framework, maps real data and interactions, and asks for visual/functional QA—not another interchangeable AI dashboard.

No UI kit, new framework, runtime service or automatic migration is imposed.

## Install

Requires Node.js and a [supported coding agent](https://skills.sh/docs). In your project:

```bash
npx skills add alifakbxr/product-ui --skill backend-to-ui
```

Global (select the agents you use):

```bash
npx skills add alifakbxr/product-ui --skill backend-to-ui -g
```

Check discovery without installing:

```bash
npx skills add alifakbxr/product-ui --list
```

The skill is designed for Claude Code, Gemini CLI, Antigravity and Codex, as well as other compatible Agent Skills hosts. Actual tool availability varies by agent. GitHub is the distribution source; listing/ranking on skills.sh depends on its indexing and is not guaranteed immediately.

## Use it

### Improve an existing frontend

> Use backend-to-ui. Keep the existing frontend stack. Audit these screens, fix the UX and visual hierarchy, preserve working routes/data/state, and test desktop/mobile.

### Build a frontend from backend code

> Use backend-to-ui with Vue 3 + Inertia. Inspect this backend and implement the real user workflows. Keep data and rendering fast. Verify behavior and appearance.

### Audit without editing code

> Use backend-to-ui to audit the current UI, interactions, accessibility and performance. Report prioritized fixes without changing files.

**Important: tech stack selection.** For implementation/redesign, if you neither name a frontend stack nor explicitly authorize reuse of the existing one, the agent **must ask first**. Finding React, Vue or static HTML in the repo alone is not authorization. It must **never silently default to native HTML**. A read-only audit does not require that question. See [stack selection policy](skills/backend-to-ui/references/stack-selection.md).

## Consistent design across coding agents

`backend-to-ui` v1.4 uses a **project-scoped `UI_CONTRACT.json`** to record existing brand and component decisions, the user’s primary task, the chosen composition, what must remain working, and the source of each decision. The next agent reads the same contract instead of imposing its own look. New decisions remain **provisional** until supported or approved.

The skill ships an [example contract](skills/backend-to-ui/assets/UI_CONTRACT.example.json) and [contract policy](skills/backend-to-ui/references/design-contract.md), plus a standard-library validator:

```bash
python3 skills/backend-to-ui/scripts/check_contract.py --contract /path/to/project/UI_CONTRACT.json --project-root /path/to/project
```

The validator checks **structure and provenance**, not aesthetic excellence. Real visual QA still requires screenshots and working interactions. Compare two actual agent runs with `python3 evals/compare_agents.py agent-a.json agent-b.json`, holding the project commit, contract SHA and prompt fingerprint constant. Existing projects preserve their stack and design system unless a change is explicitly approved.

## Antigravity and Gemini CLI: install and verify

Install separately into each host’s documented global directory:

```bash
npx skills add alifakbxr/product-ui --skill backend-to-ui --agent antigravity -g
npx skills add alifakbxr/product-ui --skill backend-to-ui --agent gemini-cli -g
```

```bash
python3 skills/backend-to-ui/scripts/doctor.py --host all
python3 skills/backend-to-ui/scripts/doctor.py --host antigravity --strict
python3 skills/backend-to-ui/scripts/doctor.py --host gemini-cli --strict --json
```

`doctor.py` checks **on-disk discovery candidates and stale duplicates only**; it cannot confirm actual activation. Verify `/backend-to-ui` in Antigravity and `/skills list` / `/skills reload` in Gemini CLI. Read the [host troubleshooting guide](skills/backend-to-ui/references/host-compatibility.md) for exact paths and precedence.

## What it does

| Understand | Build or improve | Verify |
| --- | --- | --- |
| Actual users, workflows and product mode | Distinctive, product-specific layouts | Real routes, states and interactions |
| Existing frontend, components and design tokens | Incremental fixes in the current framework | Desktop/mobile screenshot review |
| Backend routes, auth, fields when present | No invented API operations or metrics | Error, loading, permission and recovery |
| Data ownership, navigation and performance | Scoped fetching, pagination, cancellation where needed | Performance evidence when tools are available |

**Works with existing frontends even if no backend is present.** React, Vue, Angular, Svelte, Next/Nuxt, server templates, WordPress, HTMX, native HTML, Flutter, SwiftUI and other stacks are supported as project-specific engineering workflows—not as a blanket claim that every combination has been benchmarked.

The workflow is **inspect → understand → map → compare two design compositions → implement → test → inspect actual screenshots → fix**. One-shot means one request can trigger the complete process *after* a frontend-stack choice is resolved.

## Project structure

```text
skills/backend-to-ui/
  SKILL.md                   # Entry point used by coding agents
  references/
    existing-frontend.md     # Modernize without rewriting working apps
    stack-selection.md       # Required stack-choice gate
    design.md                # Product-led art direction
    visual-review.md         # Stop-ship screenshot checks
    data.md                  # Real API/props/data contracts
    performance.md           # Request/rendering efficiency
    stacks.md                # Framework-specific patterns
    cases.md                 # Decision examples, not templates
    verify.md                # Functional/release checks
    design-contract.md       # Cross-agent design authority
    host-compatibility.md    # Host discovery and activation
  assets/UI_CONTRACT.example.json
  scripts/check_contract.py
  scripts/doctor.py
evals/                       # Behavioral scenarios + evidence scorer
tests/                       # Repository and evaluator tests
```

## Validate and contribute

```bash
python3 tests/validate.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

These checks validate repository integrity, design-contract schema rules, filesystem host discovery, and evaluation rules—not actual UI quality or agent activation across coding agents. Real acceptance requires representative source repositories, browser/device screenshots, interaction checks and measured network/render traces. Missing evidence is **inconclusive**, not a pass. See [evaluation protocol](evals/README.md) and [visual gates](skills/backend-to-ui/references/visual-review.md).

To contribute, open an issue or PR with a clear reproduction and evidence. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Releases must update [CHANGELOG.md](CHANGELOG.md), run the commands above, record real evaluation limitations, and tag the merged `main` commit.

## Publishing and distribution

The repository is `alifakbxr/product-ui`, but the skill name stays `backend-to-ui`. Install it using the command above. Listing on [skills.sh](https://skills.sh) happens through its discovery/indexing workflow, not a ZIP upload; publishing on GitHub alone does not guarantee immediate visibility.

## Credits and license

Independent approach informed by [Anthropic Frontend Design](https://skills.sh/anthropics/skills/frontend-design), [Impeccable](https://skills.sh/pbakaus/impeccable/impeccable), [Vercel Web Design Guidelines](https://skills.sh/vercel-labs/agent-skills/web-design-guidelines), [UI/UX Pro Max](https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max), and [VoltAgent awesome-design-md](https://github.com/VoltAgent/awesome-design-md). References are not installed dependencies or endorsements.

MIT · See [LICENSE](LICENSE).
