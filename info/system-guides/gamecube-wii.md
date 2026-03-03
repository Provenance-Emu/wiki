---
description: GameCube & Wii setup — Dolphin native core, system folder, HD textures, and configuration
---

# GameCube & Wii Guide

Provenance supports GameCube and Wii emulation through **Dolphin**, a native core (not RetroArch-based). Dolphin brings excellent compatibility and advanced features like HD texture support, custom system configurations, and Wii NAND emulation.

---

## Basics

| Detail | GameCube | Wii |
|--------|----------|-----|
| **Core** | Dolphin (native) | Dolphin (native) |
| **BIOS required** | No (built-in HLE) | No (built-in HLE) |
| **ROM formats** | `.iso`, `.gcm`, `.gcz`, `.ciso` | `.iso`, `.wbfs`, `.gcz`, `.ciso` |
| **Max players** | 4 | 4 |
| **Controller** | Physical controller recommended | Physical controller recommended |

{% hint style="info" %}
A **physical controller** is strongly recommended for GameCube and Wii games. On-screen controls work but many games benefit from analog sticks and shoulder buttons.
{% endhint %}

---

## Dolphin Folder Structure

Dolphin uses its own native folder structure (not RetroArch's). Access via the Web Server or Files app:

```
Dolphin/
├── Config/           # Dolphin configuration files
├── GameSettings/     # Per-game INI overrides
├── GC/               # GameCube system data
│   ├── USA/          # Region-specific memory cards
│   ├── EUR/
│   └── JAP/
├── Wii/              # Wii NAND (virtual internal storage)
│   └── title/        # Installed Wii channels and saves
├── Load/
│   └── Textures/     # HD texture packs (per game ID)
├── Maps/             # Symbol maps for debugging
├── ResourcePacks/    # Custom resource packs
├── Shaders/          # Custom shader files
└── StateSaves/       # Dolphin save states
```

---

## HD Texture Packs

Dolphin supports custom HD textures for both GameCube and Wii games:

### Installing Texture Packs

1. Download a texture pack for your game
2. Start the Web Server (tap **+** or Settings → Import/Export)
3. Navigate to:
   ```
   Dolphin/Load/Textures/[GameID]/
   ```
4. Upload the texture files into the game-specific folder
5. Launch the game — textures load automatically

### Finding the Game ID

Each GameCube/Wii game has a unique 6-character ID (e.g., `GALE01` for Super Smash Bros. Melee). You can find it:
- In the game info within Provenance (long-press → Game Info)
- On [GameTDB](https://www.gametdb.com/) — search your game

### Finding Texture Packs

- **[Dolphin Forums - Custom Textures](https://forums.dolphin-emu.org/Forum-custom-texture-projects)** — Community texture pack projects
- **GitHub** — Search for "[game name] dolphin texture pack"

---

## Wii NAND

Some Wii games require or benefit from NAND data (virtual internal storage):

- **Wii System Menu** — Can be installed for accessing system settings
- **Save data** — Some games store saves in NAND rather than the virtual memory card
- **Wii Channels** — Can be installed for games that require them

The NAND is stored in the `Dolphin/Wii/` folder and is managed automatically by the core.

---

## GameCube Memory Cards

Dolphin emulates GameCube memory cards automatically:

- Virtual memory cards are stored in `Dolphin/GC/[Region]/`
- Each region (USA, EUR, JAP) has its own memory card
- Save data persists across play sessions

---

## Performance

GameCube and Wii are demanding to emulate:

| Device | GameCube | Wii |
|--------|----------|-----|
| **iPhone 15 Pro / Pro Max** | Good | Fair-Good |
| **iPad Pro (M-series)** | Good | Good |
| **iPhone 14 Pro / 13 Pro** | Fair | Fair |
| **Older devices** | Poor | Poor |

### Optimization Tips

1. **Use a modern device** — M-series or A16+ chips handle Dolphin best
2. **Close background apps** — GameCube/Wii emulation needs all available resources
3. **Skip EFB access** — Improves performance in some games (Dolphin settings)
4. **Lower internal resolution** — Reduces GPU load
5. **Disable V-Sync** if experiencing stuttering

---

## Wii Motion Controls

Wii games that require motion controls have limited support through device sensors:

- **Pointer** — Touch screen simulates the Wii Remote pointer
- **Accelerometer/Gyroscope** — Device sensors can simulate Wii Remote motion
- **Physical controller** — Map Wii Remote buttons to a standard controller

{% hint style="warning" %}
Games that rely heavily on Wii Remote motion (Wii Sports, Skyward Sword) may not play well. Games with Classic Controller support (Smash Bros. Brawl, Mario Kart Wii) work best with a standard controller.
{% endhint %}

---

## Known Quirks

<details>
<summary><strong>Some games have audio stuttering</strong></summary>

Dolphin is demanding on CPU. If audio stutters, try closing background apps, lowering resolution, or enabling audio stretching in Dolphin settings.

</details>

<details>
<summary><strong>Game crashes on boot</strong></summary>

Some games may need specific Dolphin settings. Check the [Dolphin Wiki](https://wiki.dolphin-emu.org/) for game-specific compatibility notes and recommended settings.

</details>

<details>
<summary><strong>Wii Remote games don't work with my controller</strong></summary>

Not all Wii games support Classic Controller input. Check if the game supports Classic Controller or GameCube controller — those map most naturally to standard Bluetooth controllers.

</details>

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
