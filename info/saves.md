---
description: Battery saves, save states, and syncing your game progress
---

# Game Saves

There are two ways to save progress in Provenance:

- **Battery Saves** — The game's native save system (in-game save). Portable and reliable across updates.
- **Save States** — Emulator snapshots that freeze the exact state of the game at any moment. Powerful but fragile across updates.

---

## Battery Saves

A **battery save** is created by the game itself when you use its built-in save feature (e.g., saving at a save point in an RPG, or choosing "Save" from a game's menu). These are the most reliable way to preserve progress.

### How to Save

Use the game's own save menu — this varies by game. For example:
- **Pokemon (Game Boy):** Start menu → Save
- **Legend of Zelda (SNES):** In-game save screen
- **Final Fantasy (PlayStation):** Save at a save point

The save file is stored at: `Battery States/[ROM-Filename]/[ROM-Filename].sav`

### Supported Formats

| System | Save Format(s) |
|--------|---------------|
| Game Boy / Game Boy Color | `.sav` |
| Game Boy Advance | `.sav` |
| SNES / Super Famicom | `.srm`, `.sav` |
| Nintendo 64 | `.eep`, `.sra`, `.fla`, `.mpk` |
| Nintendo DS | `.sav`, `.dsv` |
| Genesis / Mega Drive | `.srm`, `.sav` |
| PlayStation | `.mcr` (memory card) |
| Most other systems | `.sav` |

### Importing Saves from Other Emulators

Battery saves are portable — you can move them between emulators (unlike save states):

1. Start the Web Server in Provenance (tap **+** or Settings → Import/Export)
2. Navigate to `Battery States/[ROM-Filename]/`
3. Upload your save file into this folder
4. Rename it to `[ROM-Filename].sav` (must match the ROM filename exactly)
5. Stop the Web Server and load the game
6. Use the game's in-game **Load** option

{% hint style="warning" %}
If the game doesn't recognize the save, verify the filename matches exactly. Saves from a different ROM region or version may be incompatible.
{% endhint %}

### Converting PlayStation Memory Cards

If you have PlayStation memory card files from another emulator, convert them to `.mcr` format:

- **Windows:** [MemcardRex](https://github.com/ShendoXT/memcardrex)
- **Cross-platform:** [MemCard PRO](https://8bitmods.com/) or similar tools

---

## Save States

**Save states** are emulator-level snapshots that capture the exact state of the game — every pixel, every register, every byte of memory. They let you save anywhere, even mid-battle or during a cutscene.

{% hint style="danger" %}
**Save states are NOT guaranteed to survive app updates.** Emulator core changes can break compatibility. Always keep **battery saves** (in-game saves) for your important progress.
{% endhint %}

### Saving a State

1. While playing, tap the **pause/menu** button
2. Select **Save States**
3. Tap **+** to create a new save state
4. Or tap an existing state → **Overwrite** to replace it

**Auto-save:** Provenance can automatically create a save state when the app is backgrounded or when you return to the library. Enable this in Settings.

### Loading a State

1. While playing, tap the **pause/menu** button
2. Select **Save States**
3. Tap a save state → **Load**

When launching a game, Provenance may offer to resume from the most recent auto-save state.

### Deleting a State

1. Open **Save States** from the pause menu
2. Tap a state → **Delete**

{% hint style="warning" %}
Deleting a save state is permanent. Back up important states before deleting — see [Restoring Files](../info/miscellaneous/restoring-files.md).
{% endhint %}

---

## Syncing Saves Across Devices

{% tabs %}
{% tab title="Provenance Plus (iCloud)" %}
**Provenance Plus** subscribers get automatic iCloud sync of:
- Battery saves
- Save states
- ROM library
- Settings and preferences

Enable in Settings → **iCloud Sync**. Progress syncs automatically across iPhone, iPad, Mac, and Apple TV.

{% hint style="info" %}
**Apple TV users:** iCloud sync is included free — no Provenance Plus subscription required.
{% endhint %}
{% endtab %}

{% tab title="Manual Sync" %}
Without Provenance Plus, you can manually transfer saves:

1. **Export** saves via Web Server, Files app, or AirDrop
2. **Import** on the other device using the same method

Full guide: [Restoring Files](../info/miscellaneous/restoring-files.md)
{% endtab %}
{% endtabs %}

---

## Best Practices

1. **Use battery saves for important progress** — They survive app updates and core changes
2. **Use save states for convenience** — Quick-save before a hard boss fight, risky decision, etc.
3. **Don't rely solely on save states** — Create an in-game save periodically as a safety net
4. **Back up before updating** — Especially if you have save states you can't afford to lose
5. **Enable iCloud Sync** — If you have Provenance Plus, let it handle backups automatically

---

{% hint style="info" %}
Need help with save management? See [Restoring Files](../info/miscellaneous/restoring-files.md) for backup/restore instructions, or ask on [Discord](https://discord.gg/provenance).
{% endhint %}
