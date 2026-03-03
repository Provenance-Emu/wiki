---
description: Use cheat codes with Game Genie, Action Replay, and other formats
---

# Cheats

Provenance supports cheat codes for many systems through its RetroArch-based emulator cores. Apply Game Genie, Action Replay, GameShark, and other cheat formats to your games.

{% hint style="info" %}
Cheat support is available in **RetroArch-based cores**. An improved cheat UI is in development for a future update.
{% endhint %}

---

## How to Use Cheats

### Enabling Cheats

1. Launch a game
2. Open the **pause menu**
3. Navigate to **RetroArch Settings** (available for RetroArch-based cores)
4. Go to **Cheats**
5. Load or enter cheat codes
6. Toggle cheats **ON** and resume gameplay

### Cheat Code Formats

| Format | Systems | Example |
|--------|---------|---------|
| **Game Genie** | NES, SNES, Genesis, Game Boy | `SXIOPO` (NES) |
| **Action Replay / GameShark** | GBA, N64, PlayStation, DS | `0100A2C5` (GBA) |
| **Pro Action Replay** | SNES, Genesis | `7E0DBE:09` (SNES) |
| **Raw / Memory Address** | Most systems | `address:value` format |

### Loading Cheat Files

RetroArch cores can load `.cht` cheat files:

1. Place `.cht` files in the appropriate RetroArch cheats directory
2. In the RetroArch Cheats menu, select **Load Cheat File**
3. Browse and select your cheat file
4. Enable individual cheats from the list

{% hint style="warning" %}
Cheats modify game memory in real-time. Some cheats may cause crashes or save corruption. **Save your game before enabling cheats** as a precaution.
{% endhint %}

---

## Supported Systems

Cheat support depends on the emulator core. **RetroArch-based cores** generally support cheats:

| System | Cheat Support | Common Formats |
|--------|--------------|----------------|
| NES / Famicom | Yes | Game Genie, Raw |
| SNES / Super Famicom | Yes | Game Genie, Pro Action Replay, Raw |
| Game Boy / GBC | Yes | Game Genie, GameShark |
| Game Boy Advance | Yes | Action Replay, GameShark, Code Breaker |
| Nintendo 64 | Yes | GameShark |
| Nintendo DS | Yes | Action Replay |
| Genesis / Mega Drive | Yes | Game Genie, Pro Action Replay |
| PlayStation | Yes | GameShark |
| PSP | Core-dependent | CWCheat |

{% hint style="info" %}
**Non-RetroArch cores** (native cores) may have limited or no cheat support. If cheats aren't available for a game, try switching to a RetroArch-based core for that system.
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
- **Core matters** — If cheats don't work with one core, try a different RetroArch core for that system

---

## Troubleshooting

<details>
<summary><strong>Cheats option not available in pause menu</strong></summary>

The Cheats menu appears in the RetroArch settings interface. Make sure you're using a **RetroArch-based core** — native cores may not expose the cheats interface. You can change the core for a game by long-pressing it → Game Settings → Core.

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
