---
description: Everything you can do from the pause menu while playing a game
---

# In-Game Menu

The **pause menu** is your control center during gameplay. Access save states, fast forward, cheats, screen filters, controller settings, and more — all without leaving your game.

---

## Opening the Pause Menu

| Method | How |
|--------|-----|
| **On-screen** | Tap the **Menu** / **Pause** button on the controller overlay |
| **Physical controller** | Press the **Menu** / **Options** button |
| **Keyboard** | Press `~` (tilde) |

---

## Menu Options

### Save States

Create, load, and manage save state snapshots:

- **Save State** — Freeze the game at this exact moment
- **Load State** — Resume from a previously saved snapshot
- **Auto Save** — Provenance automatically creates a save state when you leave a game or background the app
- **Overwrite / Delete** — Manage existing states (each shows a screenshot preview)

{% hint style="info" %}
Save states are tied to specific emulator cores. If you switch cores, old save states won't work. Use **in-game saves** (battery saves) for long-term progress. See [Game Saves](saves.md) for details.
{% endhint %}

### Fast Forward

Speed up gameplay — useful for grinding, slow cutscenes, or text-heavy RPGs:

- **Toggle Fast Forward** — Increases emulation speed (typically 2-4x, varies by core)
- Fast forward stays active until you toggle it off or exit the game

See [Fast Forward](fast-forward.md) for full details.

### Screen Filters

Change visual filters without leaving your game:

- Switch between CRT, LCD, smoothing, and other shader effects
- Preview how each filter looks in real-time
- Per-game filter settings override global defaults

See [Screen Filters & Shaders](shaders-and-filters.md) for all available filters.

### Cheats

Enable or disable cheat codes mid-game:

- Toggle individual cheats on/off
- Access the RetroArch cheats interface (RetroArch-based cores)
- Changes take effect immediately

See [Cheats](cheats.md) for setup instructions and code formats.

### Controller Settings

Adjust controller configuration during gameplay:

- **Player assignment** — Reassign controllers to different player slots
- **Controller skin** — Switch to a different on-screen skin
- View current controller mapping

### RetroArch Settings

For games running on **RetroArch-based cores**, access the full RetroArch settings interface:

- Advanced shader configuration
- Core-specific options (resolution scaling, audio settings)
- RetroAchievements settings
- Netplay / online multiplayer configuration
- Save/load RetroArch core overrides

{% hint style="info" %}
RetroArch settings are only available for RetroArch-based cores. Native cores (emuThreeDS, Dolphin) have their own configuration systems.
{% endhint %}

### Screenshot

Capture a screenshot of the current game frame.

### Reset

Restart the game from the beginning (simulates a console power cycle). Your save states and battery saves are preserved — this only resets the current play session.

### Quit to Library

Return to the game library. If auto-save is enabled, a save state is created automatically before quitting.

---

## Quick Actions

Some actions can also be triggered without opening the full pause menu:

| Action | Method |
|--------|--------|
| **Quick Save** | Configurable controller shortcut |
| **Quick Load** | Configurable controller shortcut |
| **Fast Forward Toggle** | Configurable controller shortcut |
| **Screenshot** | Configurable controller shortcut |

Check Settings → Controllers to configure quick action shortcuts for your physical controller.

---

## See Also

- [Fast Forward](fast-forward.md) — Speed up gameplay
- [Game Saves](saves.md) — Save states vs battery saves
- [Screen Filters & Shaders](shaders-and-filters.md) — Visual filter options
- [Cheats](cheats.md) — Cheat code support
- [Controllers & Controls](controllers-and-controls/README.md) — Controller setup

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
