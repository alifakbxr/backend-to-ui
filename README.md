# product-ui

**Build the interface your product actually needs.**

![product-ui — introduction](media/intro.gif)

[Watch the 30 FPS introduction with audio](media/intro.mp4) · [View the cover](media/cover.png)

*17 seconds · 1280 × 720 H.264/AAC video · 800 × 450 / 15 FPS looping GIF.*

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
evals/                       # Behavioral scenarios + evidence scorer
tests/                       # Repository and evaluator tests
media/intro.gif              # Smooth 15 FPS introduction (README)
media/intro.mp4              # 30 FPS H.264/AAC video with original audio
media/cover.png              # Poster frame
scripts/render_intro.py      # Reproducible source animation
```

## Validate and contribute

```bash
python3 tests/validate.py
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

These checks validate repository integrity and evaluation rules—not UI quality across coding agents. Real acceptance requires representative source repositories, browser/device screenshots, interaction checks and measured network/render traces. Missing evidence is **inconclusive**, not a pass. See [evaluation protocol](evals/README.md) and [visual gates](skills/backend-to-ui/references/visual-review.md).

To contribute, open an issue or PR with a clear reproduction and evidence. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Releases must update [CHANGELOG.md](CHANGELOG.md), run the commands above, record real evaluation limitations, and tag the merged `main` commit.

## Publishing and distribution

The repository is `alifakbxr/product-ui`, but the skill name stays `backend-to-ui`. Install it using the command above. Listing on [skills.sh](https://skills.sh) happens through its discovery/indexing workflow, not a ZIP upload; publishing on GitHub alone does not guarantee immediate visibility.

The video and GIF are newly designed and encoded from the **same deterministic source animation**. The previous 6 FPS GIF was replaced with a 15 FPS loop and the video plays at 30 FPS with original, understated sound design. The before/after workspace is an **illustrative motion concept**, not a claim of live backend integration.

To regenerate locally, install Python Pillow and ffmpeg, then run:

```bash
python3 scripts/render_intro.py --out media
ffmpeg -hide_banner -loglevel error -y -i media/intro.mp4 \
  -filter_complex "fps=15,scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=96:stats_mode=diff[p];[s1][p]paletteuse=dither=bayer:bayer_scale=4:diff_mode=rectangle" \
  -loop 0 media/intro.gif
```

Build dependencies are **only** for the promotional assets; the Agent Skill itself does not require Pillow or ffmpeg.

## Credits and license

Independent approach informed by [Anthropic Frontend Design](https://skills.sh/anthropics/skills/frontend-design), [Impeccable](https://skills.sh/pbakaus/impeccable/impeccable), [Vercel Web Design Guidelines](https://skills.sh/vercel-labs/agent-skills/web-design-guidelines), [UI/UX Pro Max](https://skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max), and [VoltAgent awesome-design-md](https://github.com/VoltAgent/awesome-design-md). References are not installed dependencies or endorsements.

MIT · See [LICENSE](LICENSE).
