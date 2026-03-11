---
description: What save state version mismatches are, why they happen, and how to protect your progress
---

# Save State Version Mismatches

Save states are powerful for convenience, but they are **not safe long-term backups**. When an emulator core is updated, the internal save state format can change — and states created with an older version may not load correctly with a newer one.

{% hint style="danger" %}
**Do not rely on save states as long-term backups.** Use the game's own in-game battery save system for any progress you cannot afford to lose.
{% endhint %}

---

## What Is a Version Mismatch?

Every save state records the core version that created it. When you try to load a save state, Provenance compares:

- **Saved version** — The core version that created the state
- **Current version** — The core version installed now

If they differ, Provenance shows a **version mismatch warning** before loading.

---

## Why Does This Happen?

Emulator cores are actively developed. Updates can:

- Change how save state data is serialized or compressed
- Add or remove internal state fields
- Fix bugs that alter CPU or memory layout
- Upgrade to a new upstream core release with a different save format

Save states are snapshots of raw emulator internals — they are **not** a standardized or portable format. Even a small core update can make old states incompatible.

---

## Battery Saves Are Better for Long-Term Storage

For progress you need to keep across app updates, use the **game's own save system** instead of save states:

- Go to an in-game save point and save normally (e.g., a save room in Metroid, a Pokemon Center, a Final Fantasy save point)
- Battery saves (`.sav`, `.srm`, memory cards, etc.) use the game's own format — they are stable across emulator updates
- Battery saves can also be transferred between emulators

Save states are best used for **short-term convenience** — quick-saving before a boss fight, pausing mid-cutscene, or experimenting. Do not treat them as a permanent archive.

---

## The Version Mismatch Warning

When Provenance detects a version mismatch, it will show an alert before loading the state. You have two options:

| Option | What it does |
|--------|-------------|
| **Cancel** | Does not load the state. Your game stays as-is. |
| **Load Anyway** | Attempts to load the state despite the version difference. |

### "Load Anyway" — Risks

Loading a mismatched save state is **best effort**. Provenance will try to boot the state, but results may include:

- **Successful load** — The core may handle the difference gracefully (especially for minor version bumps)
- **Visual or audio glitches** — Corrupted graphics, wrong sounds, missing sprites
- **Game logic errors** — Progress flags, inventory, or position may be wrong
- **Crash or hard failure** — The core rejects the state and the game does not start
- **Emulator instability** — In some cases, resetting after a failed load may leave the emulator in a bad state requiring a force-quit

There is no way to predict in advance whether a mismatched state will load cleanly. The warning exists so you can make an informed choice.

---

## Before and After a Core Update

**Before updating Provenance:**

1. Create an in-game battery save at a stable point (save menu, save point, etc.)
2. If you have critical save states, export them as a backup — see [Restoring Files](miscellaneous/restoring-files.md)

**After updating Provenance:**

1. Load the game from a battery save or start fresh
2. Create a new save state with the updated core
3. Old save states may no longer load reliably — the new ones replace them as your working snapshots

---

## Frequently Asked Questions

<details><summary><strong>Will all my save states break after every update?</strong></summary>

Not necessarily. Minor core updates may not change the save state format at all, and existing states will continue to work. The version mismatch warning only appears when the recorded version differs from the current one. The risk depends on how significant the core change was.

</details>

<details><summary><strong>Can I convert an old save state to the new format?</strong></summary>

No. Save state formats are internal to each core and there is no general conversion tool. Your best option is to load the old state (accepting the risk), immediately create an in-game battery save, then create a fresh save state with the new core.

</details>

<details><summary><strong>I loaded a mismatched state and now the game is glitched. What do I do?</strong></summary>

Return to the game library and relaunch the game without loading the state. If you have a battery save, use the in-game load option to restore your progress cleanly. If not, the game will start from the beginning or the last battery save point.

</details>

<details><summary><strong>Does iCloud sync protect me from this?</strong></summary>

iCloud sync (Provenance Plus) backs up your save states and battery saves across devices, but it does not protect against version mismatches caused by a core update. Sync preserves your files — it does not change the fact that an old save state may be incompatible with a new core version. Battery saves synced via iCloud remain fully usable.

</details>

---

## See Also

- [Game Saves](saves.md) — Overview of battery saves and save states
- [Quick Continue](quick-continue.md) — Using save states to resume games on launch
- [Restoring Files](miscellaneous/restoring-files.md) — How to back up and restore save files
- [Provenance Plus](provenance-plus.md) — iCloud sync for saves across devices

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
