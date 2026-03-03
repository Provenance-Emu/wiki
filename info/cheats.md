---
description: Use cheat codes with Game Genie, Action Replay, GameShark, and other formats
---

# Cheats

Provenance supports cheat codes across many systems — both through native emulator cores and RetroArch-based cores. Apply Game Genie, Action Replay, GameShark, and other cheat formats to your games.

{% hint style="info" %}
Provenance has a **native cheat UI** for managing and applying cheats. An improved UI with search and input validation is in development for a future update.
{% endhint %}

---

## How to Use Cheats

### Enabling Cheats

1. Launch a game
2. Open the **pause menu**
3. Tap **Cheats**
4. Load or enter cheat codes
5. Toggle cheats **ON** and resume gameplay

For RetroArch-based cores, cheats are also accessible via **RetroArch Settings** → **Cheats** in the pause menu.

### Cheat Code Formats

| Format | Systems | Example |
|--------|---------|---------|
| **Game Genie** | NES, SNES, Genesis, Game Boy | `SXIOPO` (NES) |
| **Action Replay / GameShark** | GBA, N64, PlayStation, DS, PS2 | `0100A2C5` (GBA) |
| **Pro Action Replay** | SNES, Genesis, PS2 | `7E0DBE:09` (SNES) |
| **GameShark V3** | PS2 | Various |
| **Code Breaker** | GBA, PS2 | Various |
| **Gecko** | GameCube, Wii | Various |
| **Gateway** | 3DS | Various |
| **CWCheat** | PSP | Various |
| **Raw / Memory Address** | Most systems | `address:value` format |

### Loading Cheat Files

Cores support `.cht` cheat files:

1. Place `.cht` files in the appropriate cheats directory
2. In the cheats menu, select **Load Cheat File**
3. Browse and select your cheat file
4. Enable individual cheats from the list

{% hint style="warning" %}
Cheats modify game memory in real-time. Some cheats may cause crashes or save corruption. **Save your game before enabling cheats** as a precaution.
{% endhint %}

---

## Supported Cores & Systems

Cheat support is available in both **native cores** and **RetroArch-based cores**.

### Native Cores

| Core | System(s) | Cheat Formats |
|------|-----------|---------------|
| **Stella** | Atari 2600 | Enabled |
| **Gambatte** | Game Boy / GBC | Game Genie, GameShark |
| **SNES9x** | SNES | Game Genie, Pro Action Replay, Gold Finger, Raw |
| **Mednafen** | GB, SNES, PlayStation | Game Genie, GameShark, Pro Action Replay |
| **VBA-M** | GBA | Action Replay, GameShark |
| **mGBA** | GBA | GameShark, Code Breaker, Pro Action Replay |
| **Mupen64Plus-NX** | N64 | Supported |
| **DuckStation** | PlayStation | GameShark |
| **PPSSPP** | PSP | CWCheat |
| **Dolphin** | GameCube / Wii | Action Replay, Gecko |
| **Azahar (Citra)** | 3DS | Gateway |
| **Play!** | PS2 | Code Breaker, GameShark V3, Pro Action Replay |

### RetroArch Cores

All **RetroArch-based cores** support cheats through the standard libretro cheat interface. This covers 80+ sub-cores including NES, SNES, Genesis, PlayStation, N64, Dreamcast, arcade systems (MAME, FinalBurn Neo), and more.

{% hint style="info" %}
If cheats aren't working with one core, try switching to an alternative core for that system. Some cores support more cheat formats than others.
{% endhint %}

---

## Finding Cheat Codes

Popular sources for cheat codes and `.cht` files:

- **[GameHacking.org](https://gamehacking.org/)** — Large database organized by system and game
- **[RetroArch Cheats Database](https://github.com/libretro/libretro-database/tree/master/cht)** — Official `.cht` files for RetroArch cores
- **Game-specific wikis** — Search for "[game name] cheat codes [system]"

---

## Tips

- **Save before cheating** — Create a save state before enabling cheats so you can revert if something breaks
- **Disable before saving** — Some cheats should be turned off before creating in-game saves to avoid corrupted save data
- **One at a time** — Enable cheats one at a time to identify which ones work and which cause issues
- **Core matters** — If cheats don't work with one core, try a different core for that system

---

## Troubleshooting

<details>
<summary><strong>Cheats option not available in pause menu</strong></summary>

Not all cores support cheats. Check the [supported cores table](#native-cores) above. If your current core doesn't support cheats, try switching to a different core — long-press the game → Game Settings → Core.

</details>

<details>
<summary><strong>Cheat code doesn't work</strong></summary>

- Verify the code matches your ROM's **region** (US/EU/JP codes are different)
- Check that the code format matches what the core expects
- Some codes only work with specific ROM versions (v1.0, v1.1, etc.)
- Try a different cheat source — codes from some databases may be inaccurate

</details>

<details>
<summary><strong>Game crashes after enabling cheats</strong></summary>

Some cheat codes are unstable or incompatible with certain core versions. Disable all cheats, reload from a clean save state, and try enabling them one at a time to identify the problematic code.

</details>

---

{% hint style="info" %}
Need help with cheats? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
