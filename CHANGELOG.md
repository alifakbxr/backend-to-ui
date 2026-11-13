# Changelog

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) in a lightweight form and intends to use [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Media
- Replaced the previous 6 FPS / 640 × 360 GIF with a new 15 FPS / 800 × 450 / 17-second looping introduction.
- Created an original 30 FPS / 1280 × 720 H.264 video with understated original AAC audio.
- Added a reproducible Pillow+ffmpeg motion source and a cover frame.
- Updated README with inline GIF and downloadable video; the video shows an illustrative existing-frontend upgrade, not a real API-backed demo.

### Repository
- Renamed distribution repository to `product-ui` while keeping the Agent Skill name `backend-to-ui`.
- Replaced the committed MP4 introduction with an optimized inline README GIF.
- Consolidated installation, publishing, release and design reference documentation into the root README and existing skill references; removed `docs/`.

### Skill
- Added explicit support for improving frontend-only and established frontend projects in any framework.
- Requires preservation of working components, routing, styling conventions and state before redesign.
- Extended behavioral scenarios for React, Angular, Svelte, WordPress and frontend-only read-only audits.
- Retained the mandatory stack-choice gate and performance/visual stop-ship rules.



### Added
- Mandatory frontend-stack choice gate: ask when unspecified; no silent native HTML fallback.
- Portable behavioral evaluation scenarios, evidence format and offline evaluation runner.
- Performance/visual acceptance scenarios with honest reporting of unexecuted agent runs.
- Release checklist and version-consistent documentation.

### Changed
- Clarified that one-shot begins after frontend stack choice is resolved.
- Extended CI with evaluator unit tests and scenario coverage checks.


## [1.1.0] - 2026-11-12

### Changed
- Added product-mode selection and two-composition decision before frontend implementation.
- Upgraded screenshot-based visual QA to explicit stop-ship gates and a required correction/re-capture loop where tools permit.
- Strengthened the one-shot workflow against generic dashboard shells, undersized core interactions and cosmetic-only redesigns.
- Added contextual case studies for games, operations, catalogues, records, editors and landing pages.
- Added design reference credits and updated public README, workflow and troubleshooting guidance.
- Preserved backend truth, accessibility, performance requirements and stack neutrality.


### Documentation
- Added public README with clickable demo cover.
- Documented GitHub publication, skills.sh discovery, inline video attachment process and agent installations.
- Added workflow, contribution and security documentation.
- Added automated repository validation in CI.

## [1.0.0] - 2026-11-12

- Initial `backend-to-ui` instruction-only Agent Skill.
- Backend contract discovery, context-first design, efficient data pipeline and verification guides.
- Introductory motion concept and cover asset.
