---
description: System-specific setup guides for systems that need extra configuration
---

# System-Specific Guides

Most systems in Provenance work out of the box — import a ROM and play. However, some systems have extra configuration options, additional file requirements, or unique features worth knowing about.

- [Nintendo 64](n64.md) — Custom texture packs, Mupen64Plus settings
- [Nintendo 3DS](3ds.md) — emuThreeDS native core, system files, performance tips
- [GameCube & Wii](gamecube-wii.md) — Dolphin native core, system folder, HD textures

---

## RetroArch Core Folder Structure

Many systems in Provenance use **RetroArch-based cores**. These cores support additional files and configuration through RetroArch's standard folder structure:

- **System files** — BIOS, firmware, and other required files
- **Cheats** — `.cht` cheat code files
- **Shader presets** — Custom visual filter configurations
- **Core overrides** — Per-core and per-game settings

Files placed in the RetroArch system directories are automatically available to the corresponding cores. Access these folders via the [Web Server](../miscellaneous/restoring-files.md) or Files app.

---

{% hint style="info" %}
Need help with a specific system? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
