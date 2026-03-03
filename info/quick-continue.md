---
description: The Quick Continue UI — pick your core, preview saves, and jump right back in
---

# Quick Continue

When you launch a game, Provenance's **Quick Continue** interface helps you get back into your game as fast as possible. It shows your save states with screenshot previews, lets you pick between emulator cores, and handles cloud sync automatically.

---

## How It Works

### Single Core Games

For games with only one compatible core:

1. **Tap a game** in your library
2. If you have save states, the **Quick Continue screen** appears showing:
   - Save state thumbnails with screenshots
   - Timestamps for each save
   - Cloud sync status indicators
3. **Tap a save state** to resume from that point
4. Or tap **New Game** to start fresh

### Multi-Core Games

For games compatible with multiple emulator cores (e.g., a SNES game can run on bsnes or Snes9x):

1. **Tap a game** in your library
2. The **Core Picker** appears listing each compatible core:
   - Core name and version
   - Number of save states for that game in each core
3. **Select a core**
4. The Quick Continue screen shows save states for the selected core
5. Choose a save state or start a new game

{% hint style="info" %}
Save states are **core-specific** — a save made with one core can only be loaded with the same core. Battery saves (in-game saves) work across cores.
{% endhint %}

---

## Save State Previews

Each save state in the Quick Continue screen shows:

| Element | Description |
|---------|-------------|
| **Screenshot** | A preview image captured at the moment the state was saved |
| **Timestamp** | When the save was created (date and time) |
| **Cloud icon** | Shows if the save needs to sync from iCloud (Plus subscribers) |
| **Core label** | Which emulator core the save was made with |

---

## Cloud Sync Integration

For **Provenance Plus** subscribers (and all Apple TV users), Quick Continue integrates with iCloud sync:

### Sync Status Indicators

| Icon | Meaning |
|------|---------|
| **Cloud with arrow** | Save state needs to download from iCloud |
| **Checkmark** | Save is available locally, ready to load |
| **Syncing** | Currently downloading or uploading |

### Auto-Sync on Launch

When you tap a game, Quick Continue automatically:

1. **Checks for missing saves** — Downloads any save states that exist in iCloud but not on this device
2. **Checks for missing BIOS** — If the system requires BIOS files and they're in iCloud, downloads them
3. **Checks for missing ROM** — If the ROM was deleted by the OS (common on tvOS), re-downloads it from iCloud

{% hint style="info" %}
**Why this matters on Apple TV:** tvOS can silently delete app data to reclaim storage space. Quick Continue's auto-sync ensures you never lose progress — your saves, BIOS files, and even ROMs are restored from iCloud on demand.
{% endhint %}

---

## Changing the Default Core

If you prefer a specific core for a system or game:

### Per-Game Core

1. **Long-press** a game in your library
2. Select **Game Settings**
3. Under **Emulator Core**, choose your preferred core
4. This game will always launch with the selected core

### Per-System Core

1. Open **Settings**
2. Go to **Cores** → select a system
3. Choose the default core for all games on that system
4. Individual per-game settings override this

### Resetting Core Settings

To reset per-game or per-system core overrides back to defaults:

1. Open **Settings** → **Cores**
2. Select the system or game
3. Choose **Reset to Default**

---

## Tips

- **Use Quick Continue for convenience** — Jump right back into your last session with one tap
- **Multiple cores = more options** — Try different cores for the same game to compare speed, accuracy, and features
- **Keep iCloud Sync enabled** — Ensures your saves are always available, even if your device clears storage
- **Battery saves transfer between cores** — If you want to switch cores, use in-game saves (not save states) as your transfer mechanism

---

## See Also

- [Game Saves](saves.md) — Battery saves vs save states
- [Provenance Plus](provenance-plus.md) — iCloud sync details
- [Performance Optimization](performance-optimization.md) — Choosing the right core for your device

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
