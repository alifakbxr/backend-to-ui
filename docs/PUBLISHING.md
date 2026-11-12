# Publish backend-to-ui to GitHub and skills.sh

There is no ZIP upload form for the public skills.sh leaderboard. The public skill is hosted in a Git repository; the skills CLI discovers it and skills.sh indexes installs from anonymous CLI telemetry. A valid public repository is installable immediately, but appearance/ranking on skills.sh is not instant or guaranteed. [Official FAQ](https://skills.sh/docs/faq).

## 1. Prepare

From this repository:

```bash
python3 tests/validate.py
```

Review `SKILL.md`, references, media, `SECURITY.md` and the license. Do not commit API keys, private response fixtures, or user data. The intro video is a **conceptual illustration**, not a live API integration demo.

## 2. Publish on GitHub

Recommended repository: `backend-to-ui`, visibility **Public**.

Using the GitHub website:

1. Create an empty public repository called `backend-to-ui` (do not auto-create a README/LICENSE if importing this folder).
2. Extract the ZIP and open a terminal in the `backend-to-ui` root.
3. Replace `alifakbxr` below if your GitHub username or organization differs.

```bash
git init
git add .
git commit -m "chore: publish backend-to-ui agent skill"
git branch -M main
git remote add origin https://github.com/alifakbxr/backend-to-ui.git
git push -u origin main
```

Alternatively, after `git init` and the first commit, use `gh repo create backend-to-ui --public --source=. --remote=origin --push` if GitHub CLI is authenticated. Do not run both remote-creation approaches.

Verify that this URL opens publicly: `https://github.com/alifakbxr/backend-to-ui/blob/main/skills/backend-to-ui/SKILL.md`.

## 3. Verify skill discovery

Once the public repo exists, run:

```bash
npx skills add alifakbxr/backend-to-ui --list
npx skills add alifakbxr/backend-to-ui --skill backend-to-ui
```

Only claim CLI compatibility once these commands resolve successfully. Share the same install command in project docs, posts or releases. The skill may eventually appear at `https://skills.sh/alifakbxr/backend-to-ui/backend-to-ui` after installation telemetry is indexed, but do not link it as an active listing until it exists.

**Do not manipulate leaderboard numbers.** Installs are tracked through CLI telemetry and users may opt out. There is no required PR to `vercel-labs/skills` to submit a new skill.

## 4. Show the video inline on GitHub

The README already displays a *clickable cover* that links to the committed `media/intro.mp4` file; this works without external hosting.

If you want a native **inline player**:

1. Open the GitHub repository and edit `README.md` in the web editor.
2. Drag `media/intro.mp4` into the editor. GitHub uploads it as a video attachment and inserts a **real** `https://github.com/user-attachments/assets/...` URL.
3. Place that newly generated URL on its **own paragraph**, separated by blank lines. Do not invent or copy a fake asset ID.
4. Commit and check the rendered README while signed in and signed out.

Use the GitHub-hosted attachment URL by itself, not a raw MP4 URL inside a generic `<video>` tag. Browser CSP behavior can make some HTML video embeds fail. Keep the existing cover as a fallback. Reference: [GitHub file attachment docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files).

## 5. Release hygiene

- Tag versions (e.g. `v1.0.0`) and update `CHANGELOG.md` when changing behavior.
- Run validation in CI before merging.
- Review security reports privately and avoid publishing secrets in tests, media or docs.
- Use normal GitHub issues/PRs for community feedback; maintain backward-compatible skill names.
- Re-test CLI discovery after changing the folder name or frontmatter.
