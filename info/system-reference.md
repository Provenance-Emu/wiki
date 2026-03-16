---
description: Auto-generated system and core reference from Provenance source code
---

# System Reference

{% hint style="info" %}
**Auto-generated** from [Provenance source code](https://github.com/Provenance-Emu/Provenance) on March 16, 2026. Do not edit manually — changes will be overwritten by the [sync workflow](https://github.com/Provenance-Emu/wiki/actions/workflows/sync-from-source.yml).
{% endhint %}

**Quick links:** [Systems](#systems) | [BIOS Requirements](#bios-requirements) | [File Extensions](#supported-file-extensions) | [Core Matrix](#core-to-system-matrix) | [Cheat Support](#cheat-support) | [Skin Identifiers](#skin-identifiers)

---

## Systems

Provenance supports **47 systems** (21 additional in development or disabled).

| Manufacturer | System | Short | Year | Bits | Screen | Portable | CD | Rumble | BIOS |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Atari | Atari 2600 | 2600 | 1977 | 8 | CRT |  |  |  |  |
| Atari | Atari 5200 | 5200 | 1982 | 8 | CRT |  |  |  | ✅ Required |
| Atari | Atari 8bit Computer | 8Bit | 1982 | 8 | CRT |  |  |  | ✅ Required |
| Atari | Atari 7800 | 7800 | 1986 | 8 | CRT |  |  |  |  |
| Atari | Atari Lynx | LYNX | 1989 | 8 | ColorLCD | Yes |  |  | ✅ Required |
| Atari | Atari Jaguar | Jaguar | 1993 | 32 | CRT |  |  |  | 🔶 Optional |
| Bandai | WonderSwan | WS | 1999 | 16 | DotMatrix | Yes |  |  |  |
| Bandai | WonderSwan | WSC | 2000 | 16 | ColorLCD | Yes |  |  |  |
| CBS | CBS ColecoVision | ColecoVision | 1982 | 8 | CRT |  |  |  | ✅ Required |
| Capcom | CPS-1 | CPS1 | 0000 | 32 | CRT |  |  |  |  |
| Capcom | CPS-2 | CPS2 | 0000 | 32 | CRT |  |  |  |  |
| Capcom | CPS-3 | CPS3 | 0000 | 32 | CRT |  |  |  |  |
| Enterprise | Enterprise 128 | ep128 | 1985 | 8 | CRT |  |  |  |  |
| Libretro | RetroArch | RetroArch | 2010 | 64 | CRT | Yes | Yes |  |  |
| MAME | MAME | Arcade | 1997 | 32 | MonoLCD |  |  |  | 🔶 Optional |
| Magnavox | Magnavox Odyssey2 | Odyssey2 | 1978 | 8 | CRT |  |  |  | ✅ Required |
| Mattel | Mattel Intellivision | Intellivision | 1979 | 8 | CRT |  |  |  | ✅ Required |
| NEC | PC98 | PC98 | 1982 | 16 | CRT |  | Yes |  |  |
| NEC | TurboGrafx-16 | TG16 | 1987 | 16 | CRT |  |  |  |  |
| NEC | TurboGrafx-CD | TG16CD | 1988 | 16 | CRT |  | Yes |  | ✅ Required |
| NEC | SuperGrafx | SGRFX | 1989 | 16 | CRT |  |  |  |  |
| NEC | PCFX | PCFX | 1994 | 32 | CRT |  | Yes |  | ✅ Required |
| Nintendo | Nintendo | NES | 1983 | 8 | CRT |  |  |  |  |
| Nintendo | Famicom Disk System | FDS | 1986 | 8 | CRT |  |  |  | ✅ Required |
| Nintendo | Game Boy | GB | 1989 | 8 | DotMatrix | Yes |  |  |  |
| Nintendo | Super Nintendo | SNES | 1990 | 16 | CRT |  |  |  |  |
| Nintendo | Virtual Boy | Virtual Boy | 1995 | 32 | MonoLCD | Yes |  |  |  |
| Nintendo | Nintendo 64 | N64 | 1996 | 64 | CRT |  |  | Yes |  |
| Nintendo | Game Boy Color | GBC | 1998 | 8 | ColorLCD | Yes |  |  |  |
| Nintendo | Game Boy Advance | GBA | 2001 | 32 | ColorLCD | Yes |  |  | 🔶 Optional |
| Nintendo | Pokémon mini | Pm | 2001 | 8 | DotMatrix | Yes |  |  | 🔶 Optional |
| Panasonic | 3DO | 3DO | 1993 | 32 | CRT |  |  |  | ✅ Required |
| SNK | Neo Geo | NeoGeo | 1990 | 24 | MonoLCD |  |  |  | ✅ Required |
| SNK | Neo Geo Pocket | NGP | 1998 | 8 | MonoLCD | Yes |  |  |  |
| SNK | Neo Geo Pocket Color | NeoGeoPocketColor | 1999 | 16 | ColorLCD | Yes |  |  |  |
| Sega | SG-1000 | SG-1000 | 1983 | 8 | CRT |  |  |  |  |
| Sega | Master System | SMS | 1985 | 8 | CRT |  |  |  |  |
| Sega | Genesis | SG | 1988 | 16 | CRT |  |  |  |  |
| Sega | Game Gear | Game Gear | 1990 | 8 | ColorLCD | Yes |  |  |  |
| Sega | Sega CD | SCD | 1991 | 16 | CRT |  | Yes |  | ✅ Required |
| Sega | 32X | 32X | 1994 | 32 | CRT |  |  |  |  |
| Sega | Saturn | Saturn | 1995 | 32 | CRT |  | Yes |  | ✅ Required |
| Smith Engineering | Smith Engineering Vectrex | Vectrex | 1982 | 8 | CRT |  |  |  |  |
| Sony | PlayStation | PSX | 1994 | 32 | CRT |  | Yes | Yes | ✅ Required |
| Various | Game Music | GME | 1980 | 0 | CRT |  |  |  |  |
| Watara | Supervision | Supervision | 1992 | 8 | DotMatrix | Yes |  |  |  |
| ZX | ZX Spectrum | Z80 | 1980 | 16 | CRT |  |  |  |  |

<details>
<summary><strong>Systems in Development / Disabled</strong></summary>

| Manufacturer | System | Year | Status |
|:---|:---|:---|:---|
| Nintendo | 3DS | 2011 | In development |
| Apple | Apple II | 1977 | App Store disabled |
| Atari | Atari Jaguar CD | 1993 | In development |
| Atari | Atari ST | 1985 | In development |
| Philips | CD-i | 2010 | App Store disabled |
| Commodore International | Commodore 64 | 1982 | In development |
| Nintendo | DS | 2004 | In development |
| Id Software | Doom | 1993 | In development |
| Sega | Dreamcast | 1999 | In development |
| Nintendo | GameCube | 2001 | In development |
| IBM | IBM PC DOS | 1980 | In development |
| Microsoft | MSX | 1983 | In development |
| Microsoft | MSX2 | 1983 | In development |
| Apple | Macintosh | 1984 | App Store disabled |
| Palm | PalmOS | 2010 | App Store disabled |
| Sony | PlayStation 2 | 2000 | In development |
| Sony | PlayStation Portable | 2004 | In development |
| Id Software | Quake | 1996 | App Store disabled |
| Id Software | Quake II | 1996 | App Store disabled |
| Nintendo | Wii | 2006 | App Store disabled |
| Id Software | Wolfenstein 3D | 1992 | App Store disabled |

</details>

---

## BIOS Requirements

{% hint style="warning" %}
**DO NOT** ask us where to obtain BIOS files. Distributing BIOS files violates copyright law.
{% endhint %}

| System | File | Description | MD5 | Size | Status |
|:---|:---|:---|:---|:---|:---|
| Atari 5200 | `5200.rom` | Atari 5200 BIOS | `281f20ea4320404ec820fb7ec0693b38` | 2 KB | ✅ Required |
| Atari 8bit Computer | `ATARIBAS.ROM` | BIOS for the BASIC interpreter | `0bac0c6a50104045d902df4503a4c30b` | 8 KB | ✅ Required |
|  | `ATARIXL.ROM` | BIOS for Atari XL/XE OS | `06daac977823773a3eea3422fd26a703` | 16 KB | ✅ Required |
|  | `ATARIOSA.ROM` | BIOS for Atari 400/800 PAL | `eb1f32f5d9f382db1bbfb8d7f9cb343a` | 10 KB | ✅ Required |
|  | `ATARIOSB.ROM` | BIOS for Atari 400/800 NTSC | `a3e8d617c95d08031fe1b20d541434b2` | 10 KB | ✅ Required |
| Atari Lynx | `lynxboot.img` | Lynx boot ROM | `fcd403db69f54290b51035d82f835e7b` | 512 B | ✅ Required |
| Atari Jaguar | `jagboot.rom` | Jaguar BIOS | `bcfe348c565d9dedb173822ee6850dea` | 128 KB | 🔶 Optional |
| CBS ColecoVision | `coleco.rom` | ColecoVision BIOS | `2c66f5911e5b42b8ebe113403548eee7` | 8 KB | ✅ Required |
| MAME | `neogeo.zip` | NeoGeo BIOS (MAME 0.258 BIOS) | `00dad01abdbf8ea9e79ad2fe11bdb182` | 1.8 MB | 🔶 Optional |
| Magnavox Odyssey2 | `o2rom.bin` | Odyssey2 BIOS - G7000 model BIOS | `562d5ebf9e030a40d6fabfc2f33139fd` | 1 KB | ✅ Required |
|  | `c52.bin` | Videopac+ French BIOS - G7000 model | `f1071cdb0b6b10dde94d3bc8a6146387` | 1 KB | 🔶 Optional |
|  | `g7400.bin` | Videopac+ European BIOS - G7400 model | `c500ff71236068e0dc0d0603d265ae76` | 1 KB | 🔶 Optional |
|  | `jopac.bin` | Videopac+ French BIOS - G7400 model | `279008e4a0db2dc5f1c048853b033828` | 1 KB | 🔶 Optional |
| Mattel Intellivision | `exec.bin` | Executive ROM | `62e761035cb657903761800f4437b8af` | 8 KB | ✅ Required |
|  | `grom.bin` | Graphics ROM | `0cd5946c6473e42e8e4c2137785e427f` | 2 KB | ✅ Required |
|  | `ecs.bin` | Entertainment Computer System (ECS) ROM | `2e72a9a2b897d330a35c8b07a6146c52` | 24 KB | 🔶 Optional |
|  | `ivoice.bin` | Intellivoice RESROM | `d5530f74681ec6e0f282dab42e6b1c5f` | 2 KB | 🔶 Optional |
| TurboGrafx-CD | `syscard3.pce` | TurboGrafx-CD/PC Engine CD BIOS | `ff1a674273fe3540ccef576376407d1d` | 256 KB | ✅ Required |
| PCFX | `pcfx.rom` | PC-FX BIOS | `08e36edbea28a017f79f8d4f7ff9b6d7` | 1.0 MB | ✅ Required |
| Famicom Disk System | `disksys.rom` | Disk System BIOS | `ca30b50f880eb660a320674ed365ef7a` | 8 KB | ✅ Required |
| Game Boy Advance | `GBA.BIOS` | Game Boy Advance BIOS | `a860e8c0b6d573d191e4ec7db1b1e4f6` | 16 KB | 🔶 Optional |
| Pokémon mini | `bios.min` | Pokémon mini BIOS | `1e4fb124a3a886865acb574f388c803d` | 4 KB | 🔶 Optional |
| 3DO | `panafz10.bin` | 3DO BIOS | `51f2f43ae2f3508a14d9f56597e2d3ce` | 1.0 MB | ✅ Required |
|  | `panafz10-patched.bin` | 3DO Patches BIOS | `1477bda80dc33731a65468c1f5bcbee9` | 1.0 MB | 🔶 Optional |
|  | `rom2.rom` | Japanese Character ROM | `428577250f43edc902ea239c50d2240d` | 1.0 MB | 🔶 Optional |
| Neo Geo | `neogeo.zip` | NeoGeo BIOS (MAME 0.258 BIOS) | `00dad01abdbf8ea9e79ad2fe11bdb182` | 1.8 MB | 🔶 Optional |
|  | `aes.zip` | NeoGeo AES BIOS | `ad9585c72130c56f04ae26aae87c289d` | 830 KB | 🔶 Optional |
| Sega CD | `bios_CD_E.bin` | Mega-CD Model 1 (EU 921027) BIOS 1.00 | `e66fa1dc5820d254611fdcdba0662372` | 128 KB | ✅ Required |
|  | `bios_CD_U.bin` | Sega CD Model 1 (US 921011) BIOS 1.10 | `2efd74e3232ff260e371b99f84024f7f` | 128 KB | ✅ Required |
|  | `bios_CD_J.bin` | Mega-CD Model 1 (JP 911217) BIOS 1.00p | `bdeb4c47da613946d422d97d98b21cda` | 128 KB | ✅ Required |
| Saturn | `saturn_bios.bin` | Sega Saturn BIOS v1.00 (JAP/US) | `af5828fdff51384f99b3c4926be27762` | 512 KB | ✅ Required |
|  | `mpr-17933.bin` | Sega Saturn BIOS (EU) | `3240872c70984b6cbfda1586cab68dbe` | 512 KB | ✅ Required |
|  | `sega_101.bin` | Sega Saturn BIOS v1.01 (JAP) | `85ec9ca47d8f6807718151cbcca8b964` | 512 KB | ✅ Required |
| PlayStation | `scph5500.bin` | PlayStation (JP) SCPH-5500 BIOS | `8dd7d5296a650fac7319bce665a6a53c` | 512 KB | ✅ Required |
|  | `scph5501.bin` | PlayStation (NA) SCPH-5501 BIOS | `490f666e1afb15b7362b406ed1cea246` | 512 KB | ✅ Required |
|  | `scph5502.bin` | PlayStation (EU) SCPH-5502 BIOS | `32736f17079d0b2b7024407c39bd3050` | 512 KB | ✅ Required |

---

## Supported File Extensions

| System | Extensions |
|:---|:---|
| Atari 2600 | `.a26`, `.bin`, `.zip` |
| Atari 5200 | `.a52`, `.atr`, `.atx`, `.bin`, `.cas`, `.cdm`, `.xex`, `.xfd`, `.zip` |
| Atari 8bit Computer | `.a52`, `.atr`, `.atx`, `.bas`, `.bin`, `.cas`, `.cdm`, `.xex`, `.xfd`, `.zip` |
| Atari 7800 | `.a78`, `.bin`, `.cdf`, `.zip` |
| Atari Lynx | `.lnx`, `.o`, `.zip` |
| Atari Jaguar | `.abs`, `.bin`, `.cof`, `.j64`, `.jag`, `.prg`, `.rom`, `.zip` |
| WonderSwan | `.ws` |
| WonderSwan | `.wsc` |
| CBS ColecoVision | `.col`, `.cv`, `.rom` |
| CPS-1 | `.zip` |
| CPS-2 | `.zip` |
| CPS-3 | `.zip` |
| Enterprise 128 | `.128`, `.bas`, `.cdt`, `.dsk`, `.dtf`, `.img`, `.tap`, `.trn` |
| RetroArch | `.CFG`, `.cfg`, `.opt` |
| MAME | `.cmd`, `.zip` |
| Magnavox Odyssey2 | `.od2`, `.ody` |
| Mattel Intellivision | `.bin`, `.int`, `.rom` |
| PC98 | `.2HD`, `.2hd`, `.88D`, `.88d`, `.98D`, `.98d`, `.CMD`, `.D88`, `.D98`, `.FDD`, `.FDI`, `.HDD`, `.HDI`, `.HDM`, `.LZH`, `.NHD`, `.RAR`, `.ZIP`, `.cmd`, `.d88`, `.d98`, `.dup`, `.fdd`, `.fdi`, `.hdd`, `.hdi`, `.hdm`, `.hdn`, `.lzh`, `.nhd`, `.rar`, `.tfd`, `.thd`, `.xdf`, `.zip` |
| TurboGrafx-16 | `.pce`, `.zip` |
| TurboGrafx-CD | `.ccd`, `.chd`, `.cue`, `.m3u`, `.toc`, `.zip` |
| SuperGrafx | `.sgx`, `.zip` |
| PCFX | `.ccd`, `.chd`, `.cue`, `.zip` |
| Nintendo | `.nes`, `.unf`, `.unif`, `.zip` |
| Famicom Disk System | `.fds` |
| Game Boy | `.gb`, `.zip` |
| Super Nintendo | `.fig`, `.sfc`, `.smc`, `.snes`, `.zip` |
| Virtual Boy | `.bin`, `.vb`, `.vboy`, `.zip` |
| Nintendo 64 | `.n64`, `.z64`, `.zip` |
| Game Boy Color | `.gbc`, `.sgb`, `.zip` |
| Game Boy Advance | `.agb`, `.bin`, `.gba`, `.zip` |
| Pokémon mini | `.min` |
| 3DO | `.chd`, `.cue`, `.iso`, `.m3u`, `.zip` |
| Neo Geo | `.cmd`, `.neo`, `.ng`, `.zip` |
| Neo Geo Pocket | `.ngp`, `.zip` |
| Neo Geo Pocket Color | `.ngc`, `.ngpc`, `.npc`, `.zip` |
| SG-1000 | `.sg` |
| Master System | `.sms` |
| Genesis | `.68k`, `.bin`, `.bms`, `.chd`, `.gen`, `.gg`, `.m3u`, `.md`, `.mdx`, `.sgd`, `.smd`, `.sms`, `.zip` |
| Game Gear | `.gg`, `.zip` |
| Sega CD | `.chd`, `.cue`, `.iso`, `.zip` |
| 32X | `.32X`, `.32x` |
| Saturn | `.ccd`, `.chd`, `.cue`, `.iso`, `.m3u`, `.mds`, `.toc`, `.zip` |
| Smith Engineering Vectrex | `.vec` |
| PlayStation | `.ccd`, `.chd`, `.cue`, `.m3u`, `.pbp`, `.toc`, `.zip` |
| Game Music | `.ay`, `.gbs`, `.gym`, `.hes`, `.kss`, `.nsf`, `.nsfe`, `.sap`, `.spc`, `.vgm`, `.vgz` |
| Supervision | `.bin`, `.sv` |
| ZX Spectrum | `.tzx`, `.z80` |

---

## Core-to-System Matrix

Shows which emulator cores are available for each system.

| System | Available Cores | Versions |
|:---|:---|:---|
| Atari 2600 | [Atari 2600 (RetroArch)](https://docs.libretro.com/library/stella/), [Stella](https://stella-emu.github.io) | 6.6, 3.4.1 |
| Atari 5200 | [Atari 5200 (RetroArch)](https://docs.libretro.com/library/atari800/), [Atari 800](https://atari800.github.io) | 3.1.0, 3.1.0 |
| Atari 8bit Computer | [Atari 400/800/600XL/800XL/130XE (RetroArch)](https://docs.libretro.com/library/atari800/) | 3.1.0 |
| Atari 7800 | [Atari 7800 (RetroArch)](https://docs.libretro.com/library/prosystem/), [ProSystem](https://gstanton.github.io/ProSystem1_3/) | 1.3e, 1.3 |
| Atari Lynx | [Atari Lynx (RetroArch)](https://docs.libretro.com/library/beetle_lynx/), [Mednafen](https://mednafen.github.io) | 1.24.0, 1.32.1 |
| Atari Jaguar | [Atari Jaguar (Virtual Jaguar) (RetroArch)](https://docs.libretro.com/library/virtual_jaguar/) | 2.1.0 |
| WonderSwan | [Mednafen](https://mednafen.github.io) | 1.32.1 |
| WonderSwan | [Mednafen](https://mednafen.github.io) | 1.32.1 |
| CBS ColecoVision | FBNeo, [Final Burn Neo](https://neo-source.com), [Gearcoleco](https://github.com/drhelius/Gearcoleco), [MSX/SVI/ColecoVision/SG-1000 (blueMSX) (RetroArch)](https://github.com/libretro/blueMSX) | 1.0.0.2, 1.0.1, Nightly |
| CPS-1 | [FBAlpha CPS1 (RetroArch)](https://github.com/libretro/fbalpha) | Nightly |
| CPS-2 | [FBAlpha CPS2 (RetroArch)](https://github.com/libretro/fbalpha) | Nightly |
| CPS-3 | [FBAlpha CPS3 (RetroArch)](https://github.com/libretro/fbalpha) | Nightly |
| Enterprise 128 | [EP128Emu](http://ep128emu.sourceforge.net/about.html) | 2.0.11 |
| RetroArch | [2048 (RetroArch)](https://github.com/libretro/2048), [Amstrad - CPC/GX40000 (RetroArch)](https://github.com/libretro/caprice32), [Atari 400/800/600XL/800XL/130XE (RetroArch)](https://docs.libretro.com/library/atari800/), [Commodore - C128 (RetroArch)](https://github.com/libretro/vice), [Commodore - C64 (RetroArch)](https://github.com/libretro/vice), [Commodore - PET (RetroArch)](https://github.com/libretro/vice), [Commodore - VIC-20 (RetroArch)](https://github.com/libretro/vice), [DosBox-Pure (RetroArch)](https://github.com/schellingb/dosbox-pure), [MAME (Current) (RetroArch)](https://docs.libretro.com/development/cores/core-specific/mame/), [MSX/SVI/ColecoVision/SG-1000 (blueMSX) (RetroArch)](https://github.com/libretro/blueMSX), [MelonDS DS (RetroArch)](https://docs.libretro.com/library/melonds_ds/), [NooDS (RetroArch)](https://github.com/Hydr8gon/NooDS), [Opera (RetroArch)](https://github.com/libretro/opera-libretro), [PalmOS (Mu) (RetroArch)](https://docs.libretro.com/library/mu/), [Philips - P2000T (RetroArch)](https://github.com/libretro/m2000), [Rick Dangerous (RetroArch)](https://github.com/libretro/xrick), [Sharp X1 (RetroArch)](https://github.com/libretro/x1), [Sinclair - ZX Spectrum (RetroArch)](https://github.com/libretro/fuse), [TI-83 (Numero) (RetroArch)](https://github.com/libretro/numero), [Thomson - MO/TO (RetroArch)](https://github.com/libretro/theodore) | Nightly, Nightly, 3.1.0, Nightly, Nightly, Nightly, Nightly, 0.9.2, v0.258, Nightly, git, git, 1.0.0, Nightly, Nightly, Nightly, Nightly, Nightly, Nightly, Nightly |
| MAME | [FBNeo (RetroArch)](https://github.com/libretro/FBNeo), [MAME (Current) (RetroArch)](https://docs.libretro.com/development/cores/core-specific/mame/), [MAME 2000 (RetroArch)](https://github.com/libretro/mame2000-libretro), [MAME 2003 (RetroArch)](https://github.com/libretro/mame2003-libretro), [MAME 2003 Plus (RetroArch)](https://github.com/libretro/mame2003-libretro), [MAME 2010 (RetroArch)](https://github.com/libretro/mame2010-libretro) | v1.0.0.02, v0.258, v0.139, v0.139, v0.139, v0.139 |
| Magnavox Odyssey2 | — | — |
| Mattel Intellivision | [FreeIntv](https://github.com/libretro/FreeIntv) | 2018.1.5 |
| PC98 | [NP2Kai (PC-98) (RetroArch)](https://github.com/AZO234/NP2kai) | rev.22-145 |
| TurboGrafx-16 | [Beetle Supergrafx (PC Engine) (RetroArch)](https://github.com/libretro/beetle-supergrafx-libretro), [Mednafen](https://mednafen.github.io) | v1.29.0, 1.32.1 |
| TurboGrafx-CD | [Beetle Supergrafx (PC Engine) (RetroArch)](https://github.com/libretro/beetle-supergrafx-libretro), [Mednafen](https://mednafen.github.io) | v1.29.0, 1.32.1 |
| SuperGrafx | [Beetle Supergrafx (PC Engine) (RetroArch)](https://github.com/libretro/beetle-supergrafx-libretro), [Mednafen](https://mednafen.github.io) | v1.29.0, 1.32.1 |
| PCFX | [Mednafen](https://mednafen.github.io) | 1.32.1 |
| Nintendo | [FCEUX](http://sourceforge.net/projects/fceultra/), [FCEUmm (RetroArch)](https://github.com/libretro/fceumm), [Final Burn Neo](https://neo-source.com), [Mednafen](https://mednafen.github.io), [Nestopia (RetroArch)](https://github.com/libretro/nestopia) | 2.6.2, nightly, 1.0.0.2, 1.32.1, v1.51.1 |
| Famicom Disk System | [FCEUX](http://sourceforge.net/projects/fceultra/), [FCEUmm (RetroArch)](https://github.com/libretro/fceumm), [Mednafen](https://mednafen.github.io), [Nestopia (RetroArch)](https://github.com/libretro/nestopia) | 2.6.2, nightly, 1.32.1, v1.51.1 |
| Game Boy | [Gambatte](https://github.com/sinamas/gambatte), [Mednafen](https://mednafen.github.io), [SameBoy (RetroArch)](https://github.com/libretro/SameBoy), [TGBDual](https://github.com/libretro/tgbdual-libretro), [VBA-M (RetroArch)](https://docs.libretro.com/library/vba_m/), [mGBA (RetroArch)](https://github.com/libretro/mgba) | 0.5.0, 1.32.1, v0.14.7, 0.8.3, nightly, v0.10-dev |
| Super Nintendo | [BSNES (RetroArch)](https://docs.libretro.com/library/bsnes/), [BSNES HD (RetroArch)](https://docs.libretro.com/library/bsnes/), [BSNES Mercury (Accuracy) (RetroArch)](https://docs.libretro.com/library/bsnes/), [BSNES Mercury (Balanced) (RetroArch)](https://docs.libretro.com/library/bsnes/), [Mednafen](https://mednafen.github.io), [Snes9x](http://www.snes9x.com), [Snes9x (RetroArch)](https://docs.libretro.com/library/snes9x/), [Snesticle](https://github.com/iaddis/SNESticle) | nightly, nightly, nightly, nightly, 1.32.1, 1.60, 1.61, 1.0 |
| Virtual Boy | [Beetle VB (RetroArch)](https://github.com/libretro/beetle-vb-libretro), [Mednafen](https://mednafen.github.io) | v0.9.36.1, 1.32.1 |
| Nintendo 64 | [Mupen64Plus](https://github.com/mupen64plus), [Mupen64Plus-Next](https://github.com/libretro/mupen64plus-libretro-nx), [Mupen64Plus-Next (RetroArch)](https://github.com/libretro/mupen64plus-libretro-nx) | 2.5, 0, 2024.10.29 |
| Game Boy Color | [Gambatte](https://github.com/sinamas/gambatte), [Mednafen](https://mednafen.github.io), [SameBoy (RetroArch)](https://github.com/libretro/SameBoy), [TGBDual](https://github.com/libretro/tgbdual-libretro), [VBA-M (RetroArch)](https://docs.libretro.com/library/vba_m/), [mGBA (RetroArch)](https://github.com/libretro/mgba) | 0.5.0, 1.32.1, v0.14.7, 0.8.3, nightly, v0.10-dev |
| Game Boy Advance | [Beetle GBA (RetroArch)](https://github.com/libretro/beetle-gba-libretro), [Mednafen](https://mednafen.github.io), [VBA-M (RetroArch)](https://docs.libretro.com/library/vba_m/), [VisualBoyAdvance](https://sourceforge.net/projects/vba/), [mGBA](https://mgba.io/), [mGBA (RetroArch)](https://github.com/libretro/mgba) | v0.9.36, 1.32.1, nightly, 1.8.0, 0.10.3, v0.10-dev |
| Pokémon mini | [PokeMini](http://sourceforge.net/projects/pokemini/), [PokeMini (RetroArch)](https://docs.libretro.com/library/pokemini/) | 0.6, Nightly |
| 3DO | [Opera](https://github.com/libretro/opera-libretro), [Opera (RetroArch)](https://github.com/libretro/opera-libretro) | 0, 1.0.0 |
| Neo Geo | FBNeo, [FBNeo (RetroArch)](https://github.com/libretro/FBNeo), [Final Burn Neo](https://neo-source.com), [Geolith (RetroArch)](https://github.com/libretro/geolith-libretro), [MAME (Current) (RetroArch)](https://docs.libretro.com/development/cores/core-specific/mame/) | v1.0.0.02, 1.0.0.2, 2015.02.16, v0.258 |
| Neo Geo Pocket | [Beetle Neopop (RetroArch)](https://docs.libretro.com/library/beetle_neopop/), [Mednafen](https://mednafen.github.io), [RACE (RetroArch)](https://docs.libretro.com/library/race/) | v0.9.36.1, 1.32.1, v2.16 |
| Neo Geo Pocket Color | [Beetle Neopop (RetroArch)](https://docs.libretro.com/library/beetle_neopop/), [Mednafen](https://mednafen.github.io), [RACE (RetroArch)](https://docs.libretro.com/library/race/) | v0.9.36.1, 1.32.1, v2.16 |
| SG-1000 | [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX (RetroArch)](https://github.com/libretro/Genesis-Plus-GX), [Genesis Plus GX (Wide) (RetroArch)](https://github.com/libretro/Genesis-Plus-GX-Wide), [MSX/SVI/ColecoVision/SG-1000 (blueMSX) (RetroArch)](https://github.com/libretro/blueMSX) | 1.7.4 12.13.2020, 1.7.4 12.13.2020, 1.7.4, nightly, Nightly |
| Master System | [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX (RetroArch)](https://github.com/libretro/Genesis-Plus-GX), [Genesis Plus GX (Wide) (RetroArch)](https://github.com/libretro/Genesis-Plus-GX-Wide) | 1.7.4 12.13.2020, 1.7.4 12.13.2020, 1.7.4, nightly |
| Genesis | [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX (RetroArch)](https://github.com/libretro/Genesis-Plus-GX), [Genesis Plus GX (Wide) (RetroArch)](https://github.com/libretro/Genesis-Plus-GX-Wide) | 1.7.4 12.13.2020, 1.7.4 12.13.2020, 1.7.4, nightly |
| Game Gear | [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX (RetroArch)](https://github.com/libretro/Genesis-Plus-GX), [Genesis Plus GX (Wide) (RetroArch)](https://github.com/libretro/Genesis-Plus-GX-Wide) | 1.7.4 12.13.2020, 1.7.4 12.13.2020, 1.7.4, nightly |
| Sega CD | [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX (RetroArch)](https://github.com/libretro/Genesis-Plus-GX), [Genesis Plus GX (Wide) (RetroArch)](https://github.com/libretro/Genesis-Plus-GX-Wide) | 1.7.4 12.13.2020, 1.7.4 12.13.2020, 1.7.4, nightly |
| 32X | [PicoDrive](https://github.com/notaz/picodrive) | 1.93 |
| Saturn | [Beetle Saturn (RetroArch)](https://github.com/libretro/beetle-saturn-libretro), [Mednafen](https://mednafen.github.io), [Yabause](https://yabause.org), [Yabause (Saturn) (RetroArch)](https://github.com/libretro/yabause) | v0.9.45.1, 1.32.1, 0, v0.9.15 |
| Smith Engineering Vectrex | [VecX (RetroArch)](https://docs.libretro.com/library/vecx/) | Nightly |
| PlayStation | [Beetle PSX (HW Renderer) (RetroArch)](https://github.com/libretro/beetle-psx-libretro), [Beetle PSX (SW Renderer) (RetroArch)](https://github.com/libretro/beetle-psx-libretro), [BeetlePSX](https://github.com/libretro/beetle-psx-libretro), [DuckStation](https://github.com/stenzek/duckstation/), [Mednafen](https://mednafen.github.io), [PCSX (Rearmed)](https://github.com/notaz/pcsx_rearmed), [PCSX ReARMed (RetroArch)](https://docs.libretro.com/library/pcsx_rearmed/) | 0.9.44.1, 0.9.44.1, 0, 2023.01.11, 1.32.1, 1, r21 |
| Game Music | [GME](https://github.com/libretro/libretro-gme), [Game Music Emu (RetroArch)](https://docs.libretro.com/library/game_music_emu/) | 635b1e9, v0.6.3 |
| Supervision | [Potator](https://github.com/alekmaul/potator), [Potator (RetroArch)](https://github.com/libretro/potator) | 1.1, v20200223 |
| ZX Spectrum | [EP128Emu](http://ep128emu.sourceforge.net/about.html), [Fuse](http://fuse-emulator.sourceforge.net), [Sinclair - ZX Spectrum (RetroArch)](https://github.com/libretro/fuse) | 2.0.11, 0, Nightly |

---

## Cheat Support

Cores declaring cheat support in their `Core.plist` metadata:

| Core | Systems | Cheat Formats |
|:---|:---|:---|
| DuckStation | PSX | Game Shark |
| FCEUX | FDS, NES | Game Genie |
| Gambatte | GB, GBC | Game Genie, Game Shark |
| Genesis Plus GX | Game Gear, SG, SMS, SCD, SG-1000 | Game Genie, Pro Action Replay |
| Mupen64Plus | N64 | Game Shark |
| Mupen64Plus-Next | N64 | Game Shark |
| PicoDrive | 32X | Game Genie, Pro Action Replay |
| VisualBoyAdvance | GBA | GameShark, Code Breaker, Action Replay v3, Action Replay v1/v2 |
| mGBA | GBA | Game Shark, Code Breaker, Pro Action Replay |

{% hint style="info" %}
Additional cores support cheats through code-level protocol conformance not declared in Core.plist. See [Cheats Guide](cheats.md) for the complete list including Stella, Dolphin, PPSSPP, Azahar, and Play!.
{% endhint %}

---

## Skin Identifiers

Use these identifiers when creating `.deltaskin` files. Browse column links directly to system-filtered skins on DeltaStyles.

| System | Provenance ID | Delta Skin ID | Browse Skins |
|:---|:---|:---|:---|
| Atari 2600 | `com.provenance.2600` | — | — |
| Atari 5200 | `com.provenance.5200` | — | — |
| Atari 8bit Computer | `com.provenance.atari8bit` | — | — |
| Atari 7800 | `com.provenance.7800` | — | — |
| Atari Lynx | `com.provenance.lynx` | — | — |
| Atari Jaguar | `com.provenance.jaguar` | — | — |
| WonderSwan | `com.provenance.ws` | — | — |
| WonderSwan | `com.provenance.wsc` | — | — |
| CBS ColecoVision | `com.provenance.colecovision` | — | — |
| CPS-1 | `com.provenance.cps1` | — | — |
| CPS-2 | `com.provenance.cps2` | — | — |
| CPS-3 | `com.provenance.cps3` | — | — |
| Enterprise 128 | `com.provenance.ep128` | — | — |
| RetroArch | `com.provenance.retroarch` | — | — |
| MAME | `com.provenance.mame` | — | — |
| Magnavox Odyssey2 | `com.provenance.odyssey2` | — | — |
| Mattel Intellivision | `com.provenance.intellivision` | — | — |
| PC98 | `com.provenance.pc98` | — | — |
| TurboGrafx-16 | `com.provenance.pce` | — | — |
| TurboGrafx-CD | `com.provenance.pcecd` | — | — |
| SuperGrafx | `com.provenance.sgfx` | — | — |
| PCFX | `com.provenance.pcfx` | — | — |
| Nintendo | `com.provenance.nes` | `com.rileytestut.delta.game.nes` | [DeltaStyles](https://deltastyles.com/?search=nes) |
| Famicom Disk System | `com.provenance.fds` | — | — |
| Game Boy | `com.provenance.gb` | `com.rileytestut.delta.game.gbc` | [DeltaStyles](https://deltastyles.com/?search=gameboy) |
| Super Nintendo | `com.provenance.snes` | `com.rileytestut.delta.game.snes` | [DeltaStyles](https://deltastyles.com/?search=snes) |
| Virtual Boy | `com.provenance.vb` | — | — |
| Nintendo 64 | `com.provenance.n64` | `com.rileytestut.delta.game.n64` | [DeltaStyles](https://deltastyles.com/?search=n64) |
| Game Boy Color | `com.provenance.gbc` | `com.rileytestut.delta.game.gbc` | [DeltaStyles](https://deltastyles.com/?search=gameboy+color) |
| Game Boy Advance | `com.provenance.gba` | `com.rileytestut.delta.game.gba` | [DeltaStyles](https://deltastyles.com/?search=gba) |
| Pokémon mini | `com.provenance.pokemonmini` | — | — |
| 3DO | `com.provenance.3DO` | — | — |
| Neo Geo | `com.provenance.neogeo` | — | — |
| Neo Geo Pocket | `com.provenance.ngp` | — | — |
| Neo Geo Pocket Color | `com.provenance.ngpc` | — | — |
| SG-1000 | `com.provenance.sg1000` | — | — |
| Master System | `com.provenance.mastersystem` | `com.rileytestut.delta.game.ms` | [DeltaStyles](https://deltastyles.com/?search=master+system) |
| Genesis | `com.provenance.genesis` | `com.rileytestut.delta.game.genesis` | [DeltaStyles](https://deltastyles.com/?search=genesis) |
| Game Gear | `com.provenance.gamegear` | `com.rileytestut.delta.game.gg` | [DeltaStyles](https://deltastyles.com/?search=game+gear) |
| Sega CD | `com.provenance.segacd` | — | [DeltaStyles](https://deltastyles.com/?search=sega+cd) |
| 32X | `com.provenance.32X` | — | — |
| Saturn | `com.provenance.saturn` | — | [DeltaStyles](https://deltastyles.com/?search=saturn) |
| Smith Engineering Vectrex | `com.provenance.vectrex` | — | — |
| PlayStation | `com.provenance.psx` | `com.rileytestut.delta.game.psx` | [DeltaStyles](https://deltastyles.com/?search=playstation) |
| Game Music | `com.provenance.music` | — | — |
| Supervision | `com.provenance.supervision` | — | — |
| ZX Spectrum | `com.provenance.zxspectrum` | — | — |

---

{% hint style="info" %}
For the interactive community database, see [eduo.info/pvl](https://eduo.info/pvl/). Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
