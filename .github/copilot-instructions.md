# Provenance Wiki — Copilot Instructions

## Project Overview

This is the documentation wiki for **Provenance**, a multi-system emulator for iOS, iPadOS, macOS, tvOS, and visionOS. The wiki is a collection of Markdown files organized with GitBook-style navigation.

## Repository Structure

- **SUMMARY.md** — Table of contents / sidebar navigation. Must be updated when pages are added or renamed.
- **README.md** — Landing page (home).
- **faqs.md** — Main FAQ (App Store-focused). Advanced install questions in `installation-and-usage/installing-provenance/faqs-advanced.md`.
- **installation-and-usage/** — Install guides, BIOS requirements, ROM importing/formatting.
- **info/** — System compatibility, controllers, saves, skins, performance, tvOS guide.
- **help/** — Troubleshooting, contributing, UDID registration.

## Content Conventions

- **App Store first**: The App Store is the recommended installation method. Sideloading and building from source are "Advanced" alternatives.
- **Provenance Plus**: Optional subscription ($3.99/month, $39.99/year, or $99.99 lifetime). Apple TV gets free CloudKit sync; other platforms require Plus.
- **Internal links**: Always use relative paths (e.g., `[FAQ](faqs.md)`).
- **Frontmatter**: Some pages have YAML frontmatter with a `description` field. Preserve it when editing.
- **Supported systems**: Currently 38+ systems. Verify count against `info/supported-systems.md`.

## PR Review Criteria

When reviewing documentation PRs, check for:

1. **Accuracy** — Facts match the current state of the Provenance app
2. **Links** — All internal links use relative paths and point to existing pages
3. **SUMMARY.md** — Updated if pages were added or renamed
4. **Formatting** — Consistent Markdown style, no broken tables or lists
5. **Frontmatter** — Preserved on pages that had it
6. **Messaging** — App Store-first positioning maintained
7. **No orphaned pages** — Every new page is linked from SUMMARY.md

## Agent PRs

PRs with `[Agent]` prefix are created by the Claude Code automation. Review them for content accuracy and wiki convention compliance. These PRs target the `master` branch.
