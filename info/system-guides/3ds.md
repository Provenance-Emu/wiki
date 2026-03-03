---
description: Nintendo 3DS setup — emuThreeDS core, system files, and performance tips
---

# Nintendo 3DS Guide

Provenance supports Nintendo 3DS emulation through **emuThreeDS**, a native core (not RetroArch-based). The 3DS is one of the most demanding systems to emulate and requires specific setup.

{% hint style="warning" %}
3DS emulation is **iOS, iPadOS, and macOS only** — it is not supported on tvOS (Apple TV).
{% endhint %}

---

## Basics

| Detail | Info |
|--------|------|
| **Core** | emuThreeDS (native) |
| **BIOS required** | No (but system files improve compatibility) |
| **ROM formats** | `.3ds`, `.cia`, `.cxi`, `.app`, `.elf` |
| **Platform support** | iPhone, iPad, Mac (not tvOS) |
| **Max players** | 1 (local) |

---

## System Files

emuThreeDS uses its own native folder structure (not RetroArch's). System files improve game compatibility and are required for some titles.

### NAND and System Data

The 3DS core maintains a virtual NAND (internal storage) that some games require. System archives and shared fonts are among the files that can be placed here for better compatibility.

Access the core's file structure via the Web Server or Files app:

```
emuThreeDS/
├── nand/          # Virtual NAND storage
├── sdmc/          # Virtual SD card
├── sysdata/       # System data files
└── config/        # Core configuration
```

### Encrypted vs Decrypted ROMs

- **Decrypted ROMs** (`.3ds` decrypted, `.cia`) work directly
- **Encrypted ROMs** may require AES keys placed in the `sysdata/` folder
- Decrypted ROMs are recommended for the best compatibility

---

## Performance

3DS emulation is **very demanding**. Recommended hardware:

| Device | Performance |
|--------|-------------|
| **iPhone 15 Pro / Pro Max** | Good — most games playable |
| **iPhone 14 Pro / 13 Pro** | Fair — simpler 3DS games playable |
| **iPad Pro (M-series)** | Good — best iPad experience |
| **iPad Air (M-series)** | Good |
| **Older devices** | Poor — expect slowdowns in most games |

### Optimization Tips

1. **Close all background apps** — 3DS needs maximum CPU/RAM
2. **Use Low Power Mode cautiously** — it can throttle performance
3. **Avoid Sleep Mode throttling** — keep the screen active during gameplay
4. **Simpler games first** — 2D titles (Kirby, Pokemon X/Y overworld) run better than 3D-heavy games (Monster Hunter, Zelda)
5. **Reduce resolution** if the core supports it — lower internal resolution improves frame rate

---

## Controls

The 3DS has unique inputs that map to on-screen controls:

| 3DS Input | Provenance Mapping |
|-----------|--------------------|
| Circle Pad | Left analog stick |
| D-Pad | D-Pad |
| A / B / X / Y | Face buttons |
| L / R | Shoulder buttons |
| Touch Screen | Tap the bottom screen area |
| Microphone | Device microphone (enable in Settings → Privacy → Microphone → Provenance) |
| Gyroscope | Device gyroscope (for games like Ocarina of Time 3D) |

{% hint style="info" %}
**Touch screen games** require tapping on the bottom screen area of the display. Some games rely heavily on touch input (e.g., Professor Layton, Zelda: Phantom Hourglass).
{% endhint %}

---

## Dual Screen Layout

The 3DS has two screens. Provenance handles the layout automatically:

- **Portrait mode** — Screens stacked vertically (top screen above, bottom/touch below)
- **Landscape mode** — Screens side-by-side or with focus on the primary screen

Custom skins can change the dual-screen layout — check [DeltaStyles](https://deltastyles.com) for 3DS-specific skins.

---

## Known Limitations

<details>
<summary><strong>Not all games are playable</strong></summary>

3DS emulation is still maturing. Some games may have graphical glitches, audio issues, or crash. Check community compatibility lists for your specific game. The emuThreeDS core is actively being improved.

</details>

<details>
<summary><strong>No tvOS support</strong></summary>

The 3DS core is not available on Apple TV due to performance and input requirements (touch screen). Use iPhone, iPad, or Mac instead.

</details>

<details>
<summary><strong>Online features not supported</strong></summary>

3DS online services (Nintendo Network) are not emulated. Single-player and local features only.

</details>

<details>
<summary><strong>Microphone not working</strong></summary>

Go to your device's Settings → Privacy & Security → Microphone → enable Provenance. Some 3DS games (like Nintendogs) require microphone input.

</details>

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
