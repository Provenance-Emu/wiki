---
description: Speed up gameplay for grinding, cutscenes, and text-heavy sections
---

# Fast Forward

Fast forward lets you speed up emulation — perfect for RPG grinding, slow dialogue, unskippable cutscenes, or just getting through menus quickly.

---

## How to Use

### Toggle from Pause Menu

1. Open the **pause menu** during gameplay (Menu button / `~` key)
2. Select **Fast Forward**
3. The game runs at increased speed
4. Open the pause menu again and toggle off to return to normal speed

### Controller Shortcut

You can assign a fast forward toggle to a physical controller button:

1. Go to Settings → **Controllers**
2. Set a **Fast Forward** shortcut button
3. Press the assigned button during gameplay to toggle fast forward on/off without opening the pause menu

---

## Speed

Fast forward speed varies by core and device performance:

| Factor | Impact |
|--------|--------|
| **Emulator core** | Each core has its own maximum fast forward speed |
| **Device hardware** | Newer devices can sustain higher speeds |
| **Game complexity** | Simple 2D games fast forward faster than 3D games |
| **Screen filters** | Disabling filters increases maximum speed |

**Typical speeds:**
- **Simple systems** (NES, Game Boy, GBA): 4-8x or higher
- **Medium systems** (SNES, Genesis, PS1): 2-4x
- **Complex systems** (N64, PSP, Dreamcast): 1.5-3x
- **Heavy systems** (3DS, GameCube): Limited speed increase

{% hint style="info" %}
Fast forward runs the emulator as fast as your device can handle — there's no configurable speed cap. The actual speed depends on how much headroom your device has beyond real-time emulation.
{% endhint %}

---

## Core Support

Most cores support fast forward:

| Core Type | Fast Forward | Notes |
|-----------|-------------|-------|
| **RetroArch cores** | Yes | Most systems |
| **PPSSPP** (PSP) | Yes | |
| **emuThreeDS** (3DS) | Limited | Performance-dependent |
| **Dolphin** (GameCube/Wii) | Limited | Performance-dependent |
| **Native cores** | Varies | Check per-core |

---

## Tips

- **RPG grinding** — Fast forward through random battles and level-up animations
- **Visual novels / text games** — Speed through already-read dialogue
- **Unskippable cutscenes** — Get past long intros and transitions
- **Save before fast forwarding** — Create a save state first in case you need to go back
- **Disable filters for max speed** — Turning off CRT/LCD filters frees up GPU for faster emulation

{% hint style="warning" %}
**RetroAchievements Hardcore Mode** disables fast forward. If you're achievement hunting in Hardcore, you'll need to play at normal speed. Switch to Softcore mode to use fast forward while still earning achievements.
{% endhint %}

---

## Rewind

Provenance does **not** currently support rewind (frame-by-frame backwards playback). Use **save states** as an alternative — save before difficult sections and reload if needed.

---

## See Also

- [In-Game Menu](in-game-menu.md) — All pause menu features
- [Performance Optimization](performance-optimization.md) — Get better performance for higher fast forward speeds
- [RetroAchievements](retroachievements.md) — Hardcore mode disables fast forward

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
