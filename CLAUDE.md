# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is the **documentation wiki** for [Provenance](https://github.com/Provenance-Emu/Provenance), a multi-system emulator for iOS, iPadOS, macOS, and tvOS. The repo contains only Markdown files — there is no application code, build system, or test suite here.

**Note:** Provenance does NOT support visionOS or AirPlay.

## Structure

- **SUMMARY.md** — GitBook-style table of contents; defines the sidebar navigation. Update this when adding or renaming pages.
- **README.md** — Wiki landing page (home) with Quick Navigation links to all major pages.
- **faqs.md** — Main FAQ (App Store-focused). Advanced install questions go in `installation-and-usage/installing-provenance/faqs-advanced.md`.
- **installation-and-usage/** — Installation guides (App Store, sideloading, building from source), BIOS requirements, ROM importing/formatting/customization.
- **info/** — Feature guides (cheats, shaders, multiplayer, skins, saves, fast forward, RetroAchievements, etc.), system compatibility, controllers, performance, tvOS/iPad guides, system-specific guides (N64, 3DS, GameCube/Wii).
- **help/** — Troubleshooting, contributing guide, UDID registration.

## Writing Conventions

### Frontmatter & Structure
- All content pages use YAML frontmatter with a `description` field. Preserve existing frontmatter when editing.
- Internal links use relative paths (e.g., `[FAQ](faqs.md)`, `[Importing ROMs](installation-and-usage/roms/importing-roms.md)`).
- All content pages should end with a Discord help hint: `{% hint style="info" %}\nNeed help? Ask on [Discord](https://discord.gg/provenance).\n{% endhint %}`
- Feature pages should include a `## See Also` section with cross-links to related pages.

### GitBook Syntax
- **Tabs:** `{% tabs %}{% tab title="Name" %}Content{% endtab %}{% endtabs %}` — Use for parallel methods (import methods, platform differences, tool choices).
- **Expandables:** `<details><summary><strong>Title</strong></summary>\n\nContent\n\n</details>` — Use for FAQ Q&A pairs and troubleshooting items. Requires blank line after `<summary>` for markdown rendering.
- **Hints:** `{% hint style="info|warning|danger|success" %}Content{% endhint %}` — Use `success` for positive confirmations (e.g., "100% free!"), `danger` for destructive actions or strong warnings, `warning` for cautions, `info` for general notes.

### Content Guidelines
- The wiki emphasizes **App Store installation** as the primary/recommended path. Sideloading and building from source are documented under "Advanced."
- Provenance Plus is the optional subscription tier ($3.99/month, $39.99/year, $99.99 lifetime) — adds iCloud sync, TestFlight beta access, priority support. Apple TV gets free CloudKit sync because tvOS can silently delete app data.
- **Skins DO sync** with Provenance Plus (this was previously documented incorrectly).
- iPad IS supported with unique skin features (CRT TV bezel skins on DeltaStyles.com).

### Technical Accuracy
When documenting features, verify against the Provenance source code when possible:
- **Cheats:** Supported by 12+ native cores (Stella, Gambatte, SNES9x, Mednafen, VBA-M, mGBA, Mupen64Plus-NX, DuckStation, PPSSPP, Dolphin, Azahar/Citra, Play!) AND all RetroArch cores. Not just RetroArch.
- **Filters:** 7 built-in Metal filters: Simple CRT, Complex CRT, Mega Tron, ulTron, LCD, Game Boy, VHS. Plus Auto mode that selects by system screen type. Defined in `MetalFilterRenderer.swift` and `FilterOption.swift`.
- **Emulator cores:** Virtual Boy uses Mednafen (not Stella). DS uses DeSmuME/melonDS. 3DS uses emuThreeDS (Citra/Azahar). GameCube/Wii uses Dolphin with native folder structures.
- **System-specific guides** exist only for systems with extra configuration: N64 (texture packs, Mupen config), 3DS (emuThreeDS folders, encrypted ROMs), GameCube/Wii (Dolphin folders, motion controls).
- **Community resource:** [eduo.info/pvl](https://eduo.info/pvl/) is a community-built searchable database parsed from Provenance's source code — linked from supported-systems.md, bios-requirements.md, and formatting-roms.md.

### Common Pitfalls
- Don't use `../info/` paths from files already inside `info/` — use relative paths from current directory.
- Don't reference v1.4 or v1.5 — these are outdated version references. Use current terminology.
- Don't add features Provenance doesn't have (visionOS, AirPlay, animated skins, rewind).
- The `supported-systems.md` table has known typos that recur from upstream — watch for: Magnaxov→Magnavox, Intellivison→Intellivision, Vexctrex→Vectrex.

## Commit Style

Commits use short, descriptive messages — typically imperative or noun-phrase style:
- `Add comprehensive Skins Guide (3,100+ words) - W008 complete`
- `FAQ modernization (W012) - App Store focus + Advanced FAQ separation`
- `Fix: Skins DO sync with Provenance Plus`

Work item tags like `W003`, `W008`, `W012` are sometimes appended.

## Contribution Workflow

The main Provenance project uses a **fork-and-PR workflow** (not branch-based). PRs should squash changes into a single commit. See `help/contribute.md` for details.

## GitHub Automation

### Claude Code Agent
This repo has a GitHub Actions workflow (`.github/workflows/claude-code.yml`) that runs Claude Code autonomously:

- **Triggers:** `@claude` mentions in issue/PR comments, issues labeled `agent-work`, PR review comments mentioning `@claude`, and change-requested reviews on `[Agent]` PRs.
- **Agent PRs** are prefixed with `[Agent]` and target the `master` branch.
- **Issue template:** `.github/ISSUE_TEMPLATE/agent-task.md` — use this for well-scoped documentation tasks.
- **Label:** Add `agent-work` to an issue to trigger the agent automatically.
- **`/claude-fix`** in a PR comment triggers the agent to fix all pending review comments.

### CI Workflows
- **Link Checker** (`.github/workflows/link-checker.yml`) — Validates all internal markdown links on push to master and on PRs. Catches broken links before they go live.
- **Spell Checker** (`.github/workflows/spellcheck.yml`) — Runs cspell on all markdown files. Custom dictionary in `.cspell/custom-dictionary.txt` includes emulation-specific terms.
- **Sync from Source** (`.github/workflows/sync-from-source.yml`) — Scheduled workflow that reads Core.plist and Systems.plist files from the main Provenance repo and updates wiki pages with accurate system metadata, BIOS requirements, supported extensions, and feature matrices.
