# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **documentation wiki** for [Provenance](https://github.com/Provenance-Emu/Provenance), a multi-system emulator for iOS, iPadOS, macOS, tvOS, and visionOS. The repo contains only Markdown files — there is no application code, build system, or test suite here.

## Structure

- **SUMMARY.md** — GitBook-style table of contents; defines the sidebar navigation. Update this when adding or renaming pages.
- **README.md** — Wiki landing page (home).
- **faqs.md** — Main FAQ (App Store-focused). Advanced install questions go in `installation-and-usage/installing-provenance/faqs-advanced.md`.
- **installation-and-usage/** — Installation guides (App Store, sideloading, building from source), BIOS requirements, ROM importing/formatting/customization.
- **info/** — System compatibility, controllers, saves, skins, performance optimization, tvOS guide.
- **help/** — Troubleshooting, contributing guide, UDID registration.

## Writing Conventions

- Some pages use YAML frontmatter with a `description` field (e.g., `faqs.md`). Preserve existing frontmatter when editing those pages.
- Internal links use relative paths (e.g., `[FAQ](faqs.md)`, `[Importing ROMs](installation-and-usage/roms/importing-roms.md)`).
- The wiki emphasizes **App Store installation** as the primary/recommended path. Sideloading and building from source are documented under "Advanced."
- Provenance Plus is the optional subscription tier (iCloud sync, beta access). Apple TV gets free CloudKit sync.

## Commit Style

Commits use short, descriptive messages — typically imperative or noun-phrase style:
- `Add comprehensive Skins Guide (3,100+ words) - W008 complete`
- `FAQ modernization (W012) - App Store focus + Advanced FAQ separation`
- `Fix: Skins DO sync with Provenance Plus`

Work item tags like `W003`, `W008`, `W012` are sometimes appended.

## Contribution Workflow

The main Provenance project uses a **fork-and-PR workflow** (not branch-based). PRs should squash changes into a single commit. See `help/contribute.md` for details.
