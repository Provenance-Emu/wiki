---
description: Auto-generated system and core reference from Provenance source code
---

# System Reference

{% hint style="info" %}
**Auto-generated** from [Provenance source code](https://github.com/Provenance-Emu/Provenance) on August 22, 2026. Do not edit manually — changes will be overwritten by the [sync workflow](https://github.com/Provenance-Emu/wiki/actions/workflows/sync-from-source.yml).
{% endhint %}

**Quick links:** [Systems](#systems) | [BIOS Requirements](#bios-requirements) | [File Extensions](#supported-file-extensions) | [Core Matrix](#core-to-system-matrix) | [Cheat Support](#cheat-support) | [Skin Identifiers](#skin-identifiers)

---

## Systems

Provenance supports **58 systems** (15 additional in development or disabled).

| Manufacturer | System | Short | Year | Bits | Screen | Portable | CD | Rumble | BIOS |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| Atari | Atari 2600 | 2600 | 1977 | 8 | CRT |  |  |  |  |
| Atari | Atari 5200 | 5200 | 1982 | 8 | CRT |  |  |  | ✅ Required |
| Atari | Atari 8bit Computer | 8Bit | 1982 | 8 | CRT |  |  |  | ✅ Required |
| Atari | Atari ST | ST | 1985 | 16 | CRT |  |  |  | ✅ Required |
| Atari | Atari 7800 | 7800 | 1986 | 8 | CRT |  |  |  |  |
| Atari | Atari Lynx | LYNX | 1989 | 8 | ColorLCD | Yes |  |  | ✅ Required |
| Atari | Atari Jaguar | Jaguar | 1993 | 32 | CRT |  |  |  | 🔶 Optional |
| Atari | Atari Jaguar CD | Jaguar CD | 1993 | 32 | CRT |  | Yes |  | 🔶 Optional |
| Bandai | WonderSwan | WS | 1999 | 16 | DotMatrix | Yes |  |  |  |
| Bandai | WonderSwan | WSC | 2000 | 16 | ColorLCD | Yes |  |  |  |
| CBS | CBS ColecoVision | ColecoVision | 1982 | 8 | CRT |  |  |  | ✅ Required |
| Capcom | CPS-1 | CPS1 | 0000 | 32 | CRT |  |  |  |  |
| Capcom | CPS-2 | CPS2 | 0000 | 32 | CRT |  |  |  |  |
| Capcom | CPS-3 | CPS3 | 0000 | 32 | CRT |  |  |  |  |
| Enterprise | Enterprise 128 | ep128 | 1985 | 8 | CRT |  |  |  |  |
| IBM | IBM PC DOS | DOS | 1980 | 32 | CRT |  |  |  |  |
| Libretro | RetroArch | RetroArch | 2010 | 64 | CRT | Yes | Yes |  |  |
| MAME | MAME | Arcade | 1997 | 32 | MonoLCD |  |  |  | 🔶 Optional |
| Magnavox | Magnavox Odyssey2 | Odyssey2 | 1978 | 8 | CRT |  |  |  | ✅ Required |
| Mattel | Mattel Intellivision | Intellivision | 1979 | 8 | CRT |  |  |  | ✅ Required |
| Microsoft | MSX | MSX | 1983 | 16 | CRT |  |  |  | ✅ Required |
| Microsoft | MSX2 | MSX2 | 1983 | 16 | CRT |  |  |  | ✅ Required |
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
| Nintendo | GameCube | GC | 2001 | 128 | CRT |  |  | Yes | 🔶 Optional |
| Nintendo | Game Boy Advance | GBA | 2001 | 32 | ColorLCD | Yes |  |  | 🔶 Optional |
| Nintendo | Pokémon mini | Pm | 2001 | 8 | DotMatrix | Yes |  |  | 🔶 Optional |
| Nintendo | DS | DS | 2004 | 32 | ColorLCD | Yes |  |  | 🔶 Optional |
| Nintendo | 3DS | 3DS | 2011 | 32 | ColorLCD | Yes |  |  |  |
| Panasonic | 3DO | 3DO | 1993 | 32 | CRT |  |  |  | ✅ Required |
| SNK | Neo Geo | NeoGeo | 1990 | 24 | MonoLCD |  |  |  | ✅ Required |
| SNK | Neo Geo CD | NeoGeoCD | 1994 | 24 | CRT |  | Yes |  | ✅ Required |
| SNK | Neo Geo Pocket | NGP | 1998 | 8 | MonoLCD | Yes |  |  |  |
| SNK | Neo Geo Pocket Color | NeoGeoPocketColor | 1999 | 16 | ColorLCD | Yes |  |  |  |
| Sega | SG-1000 | SG-1000 | 1983 | 8 | CRT |  |  |  |  |
| Sega | Master System | SMS | 1985 | 8 | CRT |  |  |  |  |
| Sega | Genesis | SG | 1988 | 16 | CRT |  |  |  |  |
| Sega | Game Gear | Game Gear | 1990 | 8 | ColorLCD | Yes |  |  |  |
| Sega | Sega CD | SCD | 1991 | 16 | CRT |  | Yes |  | ✅ Required |
| Sega | 32X | 32X | 1994 | 32 | CRT |  |  |  |  |
| Sega | Saturn | Saturn | 1995 | 32 | CRT |  | Yes |  | ✅ Required |
| Sega | Dreamcast | DC | 1999 | 32 | CRT |  |  |  | 🔶 Optional |
| Smith Engineering | Smith Engineering Vectrex | Vectrex | 1982 | 8 | CRT |  |  |  |  |
| Sony | PlayStation | PSX | 1994 | 32 | CRT |  | Yes | Yes | ✅ Required |
| Sony | PlayStation Portable | PSP | 2004 | 32 | ColorLCD | Yes | Yes | Yes |  |
| Various | Game Music | GME | 1980 | 0 | CRT |  |  |  |  |
| Watara | Supervision | Supervision | 1992 | 8 | DotMatrix | Yes |  |  |  |
| ZX | ZX Spectrum | Z80 | 1980 | 16 | CRT |  |  |  |  |

<details>
<summary><strong>Systems in Development / Disabled</strong></summary>

| Manufacturer | System | Year | Status |
|:---|:---|:---|:---|
| Apple | Apple II | 1977 | App Store disabled |
| Sammy | Atomiswave | 2003 | In development |
| Philips | CD-i | 2010 | App Store disabled |
| Commodore International | Commodore 64 | 1982 | In development |
| Id Software | Doom | 1993 | In development |
| Apple | Macintosh | 1984 | App Store disabled |
| Sega | NAOMI | 1998 | In development |
| Sega | NAOMI 2 | 2000 | In development |
| Palm | PalmOS | 2010 | App Store disabled |
| Sony | PlayStation 2 | 2000 | In development |
| Id Software | Quake | 1996 | App Store disabled |
| Id Software | Quake II | 1996 | App Store disabled |
| Nesbox | TIC-80 | 2017 | In development |
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
| Atari ST | `tos.img` | TOS 1.02 US Boot Image | `c1c57ce48e8ee4135885cee9e63a68a2` | 192 KB | ✅ Required |
|  | `tos100.img` | TOS 1.00 US Boot Image | `1a586c64dc73b7a11f07781ef3acc82b` | 128 KB | 🔶 Optional |
|  | `tos100de.img` | TOS 1.00 DE Boot Image | `fc3aa501f1f7605c06cbf2f99a3c9b6a` | 128 KB | 🔶 Optional |
|  | `tos102uk.img` | TOS 1.02 UK Boot Image | `3b5c6f14bdebb38e9a19db96bddb83ab` | 192 KB | 🔶 Optional |
|  | `tos104.img` | TOS 1.04 US Boot Image | `036c5ae4f885cbf58baea72fdb4b42f8` | 192 KB | 🔶 Optional |
|  | `tos104de.img` | TOS 1.04 DE Boot Image | `9526ef63b9cb6d7304376ac93e055d4d` | 192 KB | 🔶 Optional |
|  | `tos104uk.img` | TOS 1.04 UK Boot Image | `2b7f2ee22e4e7cd5f37d3c97bfcd3f18` | 192 KB | 🔶 Optional |
|  | `tos106.img` | TOS 1.06 ST Boot Image | `a2cf56fdada3c93d61306e44e994a80c` | 192 KB | 🔶 Optional |
|  | `tos162.img` | TOS 1.62 STE Boot Image | `c1374d3e6fd8f875cf23e2e2dada8a4b` | 256 KB | 🔶 Optional |
|  | `tos206.img` | TOS 2.06 STE Boot Image | `0b1f9ac65c1cc9a9b5e99b7f3d225a10` | 256 KB | 🔶 Optional |
|  | `emutos1m.img` | EmuTOS 1024k (open-source free alternative) |  | 1.0 MB | 🔶 Optional |
|  | `tos100us.rom` | TOS 1.00 US Boot ROM | `1a586c64dc73b7a11f07781ef3acc82b` | 128 KB | 🔶 Optional |
|  | `tos102us.rom` | TOS 1.02 US Boot ROM | `c1c57ce48e8ee4135885cee9e63a68a2` | 192 KB | 🔶 Optional |
|  | `tos104us.rom` | TOS 1.04 US Boot ROM | `036c5ae4f885cbf58baea72fdb4b42f8` | 192 KB | 🔶 Optional |
|  | `tos104se.rom` | TOS 1.04 SE Boot ROM |  | 192 KB | 🔶 Optional |
|  | `tos106us.rom` | TOS 1.06 US Boot ROM | `a2cf56fdada3c93d61306e44e994a80c` | 192 KB | 🔶 Optional |
|  | `tos205us.rom` | TOS 2.05 US Boot ROM |  | 256 KB | 🔶 Optional |
|  | `tos206uk.rom` | TOS 2.06 UK Boot ROM |  | 256 KB | 🔶 Optional |
|  | `tos206us.rom` | TOS 2.06 US Boot ROM | `0b1f9ac65c1cc9a9b5e99b7f3d225a10` | 256 KB | 🔶 Optional |
| Atari Lynx | `lynxboot.img` | Lynx boot ROM | `fcd403db69f54290b51035d82f835e7b` | 512 B | ✅ Required |
| Atari Jaguar | `jagboot.rom` | Jaguar BIOS | `bcfe348c565d9dedb173822ee6850dea` | 128 KB | 🔶 Optional |
| Atari Jaguar CD | `jagboot.rom` | Jaguar BIOS | `bcfe348c565d9dedb173822ee6850dea` | 128 KB | 🔶 Optional |
|  | `[BIOS] Atari Jaguar CD (World).j64` | Jaguar CD BIOS | `77cd95c7ad06a39f4c59995094aa10f9` | 256 KB | 🔶 Optional |
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
| MSX | `MSX.ROM` | MSX BIOS | `364a1a579fe5cb8dba54519bcfcdac0d` | 32 KB | ✅ Required |
|  | `DISK.ROM` | DiskROM/BDOS | `80dcd1ad1a4cf65d64b7ba10504e8190` | 16 KB | 🔶 Optional |
|  | `FMPAC.ROM` | FMPAC BIOS | `6f69cc8b5ed761b03afd78000dfb0e19` | 64 KB | 🔶 Optional |
|  | `MSXDOS2.ROM` | MSX-DOS 2 | `6418d091cd6907bbcf940324339e43bb` | 64 KB | 🔶 Optional |
|  | `PAINTER.ROM` | Yamaha Painter | `403cdea1cbd2bb24fae506941f8f655e` | 64 KB | 🔶 Optional |
|  | `KANJI.ROM` | Kanji Font | `febe8782b466d7c3b16de6d104826b34` | 128 KB | 🔶 Optional |
| MSX2 | `MSX2.ROM` | MSX2 BIOS  | `ec3a01c91f24fbddcbcab0ad301bc9ef` | 32 KB | ✅ Required |
|  | `MSX2EXT.ROM` | MSX2 ExtROM | `2183c2aff17cf4297bdb496de78c2e8a` | 16 KB | ✅ Required |
|  | `MSX2P.ROM` | MSX2+ BIOS | `847cc025ffae665487940ff2639540e5` | 32 KB | ✅ Required |
|  | `MSX2PEXT.ROM` | MSX2+ ExtROM | `7c8243c71d8f143b2531f01afa6a05dc` | 16 KB | ✅ Required |
|  | `DISK.ROM` | DiskROM/BDOS | `80dcd1ad1a4cf65d64b7ba10504e8190` | 16 KB | 🔶 Optional |
|  | `FMPAC.ROM` | FMPAC BIOS | `6f69cc8b5ed761b03afd78000dfb0e19` | 64 KB | 🔶 Optional |
|  | `MSXDOS2.ROM` | MSX-DOS 2 | `6418d091cd6907bbcf940324339e43bb` | 64 KB | 🔶 Optional |
|  | `PAINTER.ROM` | Yamaha Painter | `403cdea1cbd2bb24fae506941f8f655e` | 64 KB | 🔶 Optional |
|  | `KANJI.ROM` | Kanji Font | `febe8782b466d7c3b16de6d104826b34` | 128 KB | 🔶 Optional |
| TurboGrafx-CD | `syscard3.pce` | TurboGrafx-CD/PC Engine CD BIOS | `ff1a674273fe3540ccef576376407d1d` | 256 KB | ✅ Required |
| PCFX | `pcfx.rom` | PC-FX BIOS | `08e36edbea28a017f79f8d4f7ff9b6d7` | 1.0 MB | ✅ Required |
| Famicom Disk System | `disksys.rom` | Disk System BIOS | `ca30b50f880eb660a320674ed365ef7a` | 8 KB | ✅ Required |
| GameCube | `gc-dvd-20020823.bin` | DVD 20020823 | `c03f6bbaf644eb9b3ee261dbe199eb42` | 128 KB | 🔶 Optional |
|  | `gc-dvd-20020402.bin` | DVD 20020402 | `413154dd0e2c824c9b18b807fd03ec4e` | 128 KB | 🔶 Optional |
|  | `gc-dvd-20010831.bin` | DVD 20010831 | `b953eb1a8fc9922b3f7051c1cdc451f1` | 128 KB | 🔶 Optional |
|  | `gc-dvd-20010608.bin` | DVD 20010608 | `561532ad496f644897952d2cef5bb431` | 128 KB | 🔶 Optional |
|  | `gc-ntsc-12.bin` | NTSC 12 IPL.bin | `b17148254a5799684c7d783206504926` | 2.0 MB | 🔶 Optional |
|  | `gc-ntsc-11.bin` | NTSC 11 IPL.bin | `019e39822a9ca3029124f74dd4d55ac4` | 2.0 MB | 🔶 Optional |
|  | `gc-ntsc-10.bin` | NTSC 10 IPL.bin | `fc924a7c879b661abc37cec4f018fdf3` | 2.0 MB | 🔶 Optional |
|  | `gc-pal-10.bin` | PAL 10 IPL.bin | `0cdda509e2da83c85bfe423dd87346cc` | 2.0 MB | 🔶 Optional |
|  | `gc-pal-11.bin` | PAL 11 IPL.bin | `339848a0b7c2124cf155276c1e79cbd0` | 2.0 MB | 🔶 Optional |
|  | `gc-pal-12.bin` | PAL 12 IPL.bin | `db92574caab77a7ec99d4605fd6f2450` | 2.0 MB | 🔶 Optional |
| Game Boy Advance | `GBA.BIOS` | Game Boy Advance BIOS | `a860e8c0b6d573d191e4ec7db1b1e4f6` | 16 KB | 🔶 Optional |
| Pokémon mini | `bios.min` | Pokémon mini BIOS | `1e4fb124a3a886865acb574f388c803d` | 4 KB | 🔶 Optional |
| DS | `firmware.bin` | NDS Firmware - Optional | `145eaef5bd3037cbc247c213bb3da1b3` | 256 KB | 🔶 Optional |
|  | `bios7.bin` | ARM7 BIOS - Optional | `df692a80a5b1bc90728bc3dfc76cd948` | 16 KB | 🔶 Optional |
|  | `bios9.bin` | ARM9 BIOS - Optional | `a392174eb3e572fed6447e956bde4b25` | 4 KB | 🔶 Optional |
| 3DO | `panafz1.bin` | Panasonic FZ-1 BIOS | `f47264dd47fe30f73ab3c010015c155b` | 1.0 MB | 🔶 Optional |
|  | `panafz10.bin` | Panasonic FZ-10 BIOS | `51f2f43ae2f3508a14d9f56597e2d3ce` | 1.0 MB | ✅ Required |
|  | `panafz10-norsa.bin` | Panasonic FZ-10 BIOS (encryption check disabled) | `1477bda80dc33731a65468c1f5bcbee9` | 1.0 MB | 🔶 Optional |
|  | `panafz10e-anvil.bin` | Panasonic FZ-10E ANVIL BIOS | `a48e6746bd7edec0f40cff078f0bb19f` | 1.0 MB | 🔶 Optional |
|  | `panafz10e-anvil-norsa.bin` | Panasonic FZ-10E ANVIL BIOS (encryption check disabled) | `cf11bbb5a16d7af9875cca9de9a15e09` | 1.0 MB | 🔶 Optional |
|  | `goldstar.bin` | Goldstar GDO-101M BIOS | `8639fd5e549bd6238cfee79e3e749114` | 1.0 MB | 🔶 Optional |
|  | `sanyotry.bin` | Sanyo Try IMP-21J BIOS | `35fa1a1ebaaeea286dc5cd15487c13ea` | 1.0 MB | 🔶 Optional |
|  | `3do_arcade_saot.bin` | 3DO Arcade — Shootout at Old Tucson BIOS | `8970fc987ab89a7f64da9f8a8c4333ff` | 512 KB | 🔶 Optional |
|  | `panafz1-kanji.bin` | Panasonic FZ-1 Kanji font ROM | `b8dc97f778a6245c58e064b0312e8281` | 912 KB | 🔶 Optional |
|  | `panafz10ja-anvil-kanji.bin` | Panasonic FZ-10JA ANVIL Kanji font ROM | `428577250f43edc902ea239c50d2240d` | 1.0 MB | 🔶 Optional |
|  | `panafz1j.bin` | Panasonic FZ-1J BIOS | `a496cfdded3da562759be3561317b605` | 1.0 MB | 🔶 Optional |
|  | `panafz1j-norsa.bin` | Panasonic FZ-1J BIOS (encryption check disabled) | `f6c71de7470d16abe4f71b1444883dc8` | 1.0 MB | 🔶 Optional |
|  | `panafz1j-kanji.bin` | Panasonic FZ-1J Kanji font ROM | `c23fb5d5e6bb1c240d02cf968972be37` | 1.0 MB | 🔶 Optional |
|  | `rom2.rom` | Japanese character ROM (FreeDO / legacy filename) | `428577250f43edc902ea239c50d2240d` | 1.0 MB | 🔶 Optional |
| Neo Geo | `neogeo.zip` | NeoGeo BIOS (MAME 0.258 BIOS) | `00dad01abdbf8ea9e79ad2fe11bdb182` | 1.8 MB | 🔶 Optional |
|  | `aes.zip` | NeoGeo AES BIOS | `ad9585c72130c56f04ae26aae87c289d` | 830 KB | 🔶 Optional |
| Neo Geo CD | `neocdz.zip` | Neo Geo CD BIOS | `f39572af7584738b76f87a8e88cc5540` | 512 KB | ✅ Required |
|  | `neogeo.zip` | NeoGeo BIOS (MAME 0.258 BIOS, for CD titles) | `00dad01abdbf8ea9e79ad2fe11bdb182` | 1.8 MB | 🔶 Optional |
| Sega CD | `bios_CD_E.bin` | Mega-CD Model 1 (EU 921027) BIOS 1.00 | `e66fa1dc5820d254611fdcdba0662372` | 128 KB | ✅ Required |
|  | `bios_CD_U.bin` | Sega CD Model 1 (US 921011) BIOS 1.10 | `2efd74e3232ff260e371b99f84024f7f` | 128 KB | ✅ Required |
|  | `bios_CD_J.bin` | Mega-CD Model 1 (JP 911217) BIOS 1.00p | `bdeb4c47da613946d422d97d98b21cda` | 128 KB | ✅ Required |
| Saturn | `saturn_bios.bin` | Sega Saturn BIOS v1.00 (JAP/US) | `af5828fdff51384f99b3c4926be27762` | 512 KB | ✅ Required |
|  | `mpr-17933.bin` | Sega Saturn BIOS (EU) | `3240872c70984b6cbfda1586cab68dbe` | 512 KB | ✅ Required |
|  | `sega_101.bin` | Sega Saturn BIOS v1.01 (JAP) | `85ec9ca47d8f6807718151cbcca8b964` | 512 KB | ✅ Required |
| Dreamcast | `dc_bios.bin` | Dreamcast BIOS | `e10c53c2f8b90bab96ead2d368858623` | 2.0 MB | 🔶 Optional |
|  | `dc_flash.bin` | Dreamcast Flash USA | `0a93f7940c455905bea6e392dfde92a4` | 128 KB | 🔶 Optional |
|  | `dc_flashE.bin` | Dreamcast Flash Europe | `23df18aa53c8b30784cd9a84e061d008` | 128 KB | 🔶 Optional |
|  | `dc_flashJ.bin` | Dreamcast Flash Japan | `69c036adfca4ebea0b0c6fa4acfc8538` | 128 KB | 🔶 Optional |
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
| Atari ST | `.dim`, `.ipf`, `.mas`, `.msa`, `.st`, `.stx`, `.zip` |
| Atari 7800 | `.a78`, `.bin`, `.cdf`, `.zip` |
| Atari Lynx | `.lnx`, `.o`, `.zip` |
| Atari Jaguar | `.abs`, `.bin`, `.cof`, `.j64`, `.jag`, `.prg`, `.rom`, `.zip` |
| Atari Jaguar CD | `.cdi`, `.cue` |
| WonderSwan | `.ws` |
| WonderSwan | `.wsc` |
| CBS ColecoVision | `.col`, `.cv`, `.rom` |
| CPS-1 | `.zip` |
| CPS-2 | `.zip` |
| CPS-3 | `.zip` |
| Enterprise 128 | `.128`, `.bas`, `.cdt`, `.dsk`, `.dtf`, `.img`, `.tap`, `.trn` |
| IBM PC DOS | `.bat`, `.cfg`, `.com`, `.conf`, `.cue`, `.dosz`, `.exe`, `.ima`, `.img`, `.ins`, `.iso`, `.jrc`, `.m3u`, `.m3u8`, `.tc`, `.vhd`, `.zip` |
| RetroArch | `.cfg`, `.opt` |
| MAME | `.7z`, `.chd`, `.cmd`, `.zip` |
| Magnavox Odyssey2 | `.od2`, `.ody` |
| Mattel Intellivision | `.bin`, `.int`, `.rom` |
| MSX | `.cas`, `.dsk`, `.m3u`, `.msx`, `.mx1`, `.mx2`, `.rom`, `.tsx`, `.wav` |
| MSX2 | `.cas`, `.dsk`, `.m3u`, `.msx`, `.mx1`, `.mx2`, `.rom`, `.tsx`, `.wav` |
| PC98 | `.2hd`, `.88d`, `.98d`, `.cmd`, `.d88`, `.d98`, `.dup`, `.fdd`, `.fdi`, `.hdd`, `.hdi`, `.hdm`, `.hdn`, `.lzh`, `.nhd`, `.rar`, `.tfd`, `.thd`, `.xdf`, `.zip` |
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
| GameCube | `.ciso`, `.dol`, `.elf`, `.gcm`, `.gcz`, `.iso`, `.rvz`, `.tgc`, `.wad`, `.wbfs`, `.zip` |
| Game Boy Advance | `.agb`, `.bin`, `.gba`, `.zip` |
| Pokémon mini | `.min` |
| DS | `.ids`, `.nds`, `.zip` |
| 3DS | `.3ds`, `.3dsx`, `.app`, `.axf`, `.cci`, `.cia`, `.cxi`, `.elf`, `.zip` |
| 3DO | `.chd`, `.cue`, `.iso`, `.m3u`, `.zip` |
| Neo Geo | `.cmd`, `.neo`, `.ng`, `.zip` |
| Neo Geo CD | `.chd`, `.cue`, `.iso`, `.m3u` |
| Neo Geo Pocket | `.ngp`, `.zip` |
| Neo Geo Pocket Color | `.ngc`, `.ngpc`, `.npc`, `.zip` |
| SG-1000 | `.sg` |
| Master System | `.sms` |
| Genesis | `.68k`, `.bin`, `.bms`, `.chd`, `.gen`, `.gg`, `.m3u`, `.md`, `.mdx`, `.sgd`, `.smd`, `.sms`, `.zip` |
| Game Gear | `.gg`, `.zip` |
| Sega CD | `.chd`, `.cue`, `.iso`, `.zip` |
| 32X | `.32x` |
| Saturn | `.ccd`, `.chd`, `.cue`, `.iso`, `.m3u`, `.mds`, `.toc`, `.zip` |
| Dreamcast | `.7z`, `.cdi`, `.chd`, `.cue`, `.elf`, `.gdi`, `.iso`, `.zip` |
| Smith Engineering Vectrex | `.vec` |
| PlayStation | `.ccd`, `.chd`, `.cue`, `.m3u`, `.pbp`, `.toc`, `.zip` |
| PlayStation Portable | `.7z`, `.cso`, `.cue`, `.elf`, `.iso`, `.pbp`, `.zip` |
| Game Music | `.ay`, `.gbs`, `.gym`, `.hes`, `.kss`, `.nsf`, `.nsfe`, `.sap`, `.spc`, `.vgm`, `.vgz` |
| Supervision | `.bin`, `.sv` |
| ZX Spectrum | `.tzx`, `.z80` |

---

## Core-to-System Matrix

Shows which emulator cores are available for each system.

| System | Available Cores | Versions |
|:---|:---|:---|
| Atari 2600 | [Atari 2600 (RetroArch)](https://docs.libretro.com/library/stella/), [Stella](https://stella-emu.github.io), [Stella (Current) (RetroArch)](https://stella-emu.github.io), [Stella 2023 (RetroArch)](https://stella-emu.github.io) | 6.6, 3.4.1, Nightly, Nightly |
| Atari 5200 | [Atari 5200 (RetroArch)](https://docs.libretro.com/library/atari800/), [Atari 800](https://atari800.github.io) | 3.1.0, 3.1.0 |
| Atari 8bit Computer | [Atari 400/800/600XL/800XL/130XE (RetroArch)](https://docs.libretro.com/library/atari800/), [Atari 800](https://atari800.github.io) | 3.1.0, 3.1.0 |
| Atari ST | [Atari ST/STE/TT/Falcon (RetroArch)](https://docs.libretro.com/library/hatari/) | 1.8 |
| Atari 7800 | [Atari 7800 (RetroArch)](https://docs.libretro.com/library/prosystem/), [ProSystem](https://gstanton.github.io/ProSystem1_3/) | 1.3e, 1.3 |
| Atari Lynx | [Atari Lynx (RetroArch)](https://docs.libretro.com/library/beetle_lynx/), [Handy (Atari Lynx) (RetroArch)](https://github.com/libretro/libretro-handy), [Mednafen](https://mednafen.github.io) | 1.24.0, Nightly, 1.32.1 |
| Atari Jaguar | [Atari Jaguar (Virtual Jaguar) (RetroArch)](https://docs.libretro.com/library/virtual_jaguar/) | 2.1.0 |
| Atari Jaguar CD | [Atari Jaguar (Virtual Jaguar) (RetroArch)](https://docs.libretro.com/library/virtual_jaguar/) | 2.1.0 |
| WonderSwan | [Beetle WonderSwan (RetroArch)](https://github.com/libretro/beetle-wswan-libretro), [Mednafen](https://mednafen.github.io) | Nightly, 1.32.1 |
| WonderSwan | [Beetle WonderSwan (RetroArch)](https://github.com/libretro/beetle-wswan-libretro), [Mednafen](https://mednafen.github.io) | Nightly, 1.32.1 |
| CBS ColecoVision | [Gearcoleco](https://github.com/drhelius/Gearcoleco), [Gearcoleco (RetroArch)](https://github.com/drhelius/Gearcoleco), [MSX/SVI/ColecoVision/SG-1000 (blueMSX) (RetroArch)](https://github.com/libretro/blueMSX) | 1.0.1, Nightly, Nightly |
| CPS-1 | [FBAlpha CPS1 (RetroArch)](https://github.com/libretro/fbalpha) | Nightly |
| CPS-2 | [FBAlpha CPS2 (RetroArch)](https://github.com/libretro/fbalpha) | Nightly |
| CPS-3 | [FBAlpha CPS3 (RetroArch)](https://github.com/libretro/fbalpha) | Nightly |
| Enterprise 128 | [EP128Emu](http://ep128emu.sourceforge.net/about.html) | 2.0.11 |
| IBM PC DOS | [DosBox-Pure (RetroArch)](https://github.com/schellingb/dosbox-pure) | 0.9.2 |
| RetroArch | [2048 (RetroArch)](https://github.com/libretro/2048), [Atari 400/800/600XL/800XL/130XE (RetroArch)](https://docs.libretro.com/library/atari800/), [Commodore - C128 (RetroArch)](https://github.com/libretro/vice), [Commodore - C64 (RetroArch)](https://github.com/libretro/vice), [Commodore - C64 (x64sc) (RetroArch)](https://github.com/libretro/vice), [Commodore - PET (RetroArch)](https://github.com/libretro/vice), [Commodore - Plus/4 (RetroArch)](https://github.com/libretro/vice), [Commodore - VIC-20 (RetroArch)](https://github.com/libretro/vice), [DosBox-Pure (RetroArch)](https://github.com/schellingb/dosbox-pure), [MAME (Current) (RetroArch)](https://docs.libretro.com/development/cores/core-specific/mame/), [MSX/SVI/ColecoVision/SG-1000 (blueMSX) (RetroArch)](https://github.com/libretro/blueMSX), [MelonDS DS (RetroArch)](https://docs.libretro.com/library/melonds_ds/), [Mr.Boom (RetroArch)](https://docs.libretro.com/library/mrboom/), [NooDS (RetroArch)](https://github.com/Hydr8gon/NooDS), [Opera (RetroArch)](https://github.com/libretro/opera-libretro), [PUAE (Amiga) (RetroArch)](https://github.com/libretro/libretro-uae), [PUAE 2021 (Amiga) (RetroArch)](https://github.com/libretro/libretro-uae), [PalmOS (Mu) (RetroArch)](https://docs.libretro.com/library/mu/), [Philips - P2000T (RetroArch)](https://github.com/libretro/m2000), [Rick Dangerous (RetroArch)](https://github.com/libretro/xrick), [Sharp X1 (RetroArch)](https://github.com/libretro/x1), [Sinclair - ZX Spectrum (RetroArch)](https://github.com/libretro/fuse) | Nightly, 3.1.0, Nightly, Nightly, Nightly, Nightly, Nightly, Nightly, 0.9.2, v0.258, Nightly, git, Nightly, git, 1.0.0, Nightly, Nightly, Nightly, Nightly, Nightly, Nightly, Nightly |
| MAME | [FBNeo (RetroArch)](https://github.com/libretro/FBNeo), [MAME (Current) (RetroArch)](https://docs.libretro.com/development/cores/core-specific/mame/), [MAME 2000 (RetroArch)](https://github.com/libretro/mame2000-libretro), [MAME 2003 (RetroArch)](https://github.com/libretro/mame2003-libretro), [MAME 2003 Plus (RetroArch)](https://github.com/libretro/mame2003-plus-libretro), [MAME 2010 (RetroArch)](https://github.com/libretro/mame2010-libretro) | v1.0.0.02, v0.258, v0.139, v0.139, v0.139, v0.139 |
| Magnavox Odyssey2 | [O2EM (Odyssey 2) (RetroArch)](https://github.com/libretro/libretro-o2em) | Nightly |
| Mattel Intellivision | [FreeINTV (RetroArch)](https://github.com/libretro/FreeIntv), [FreeIntv](https://github.com/libretro/FreeIntv) | Nightly, 2018.1.5 |
| MSX | [MSX/SVI/ColecoVision/SG-1000 (blueMSX) (RetroArch)](https://github.com/libretro/blueMSX), [fMSX (RetroArch)](https://github.com/libretro/fmsx-libretro) | Nightly, Nightly |
| MSX2 | [MSX/SVI/ColecoVision/SG-1000 (blueMSX) (RetroArch)](https://github.com/libretro/blueMSX), [fMSX (RetroArch)](https://github.com/libretro/fmsx-libretro) | Nightly, Nightly |
| PC98 | [NP2Kai (PC-98) (RetroArch)](https://github.com/AZO234/NP2kai) | rev.22-145 |
| TurboGrafx-16 | [Beetle PC Engine (RetroArch)](https://github.com/libretro/beetle-pce-libretro), [Beetle PC Engine Fast (RetroArch)](https://github.com/libretro/beetle-pce-fast-libretro), [Beetle Supergrafx (PC Engine) (RetroArch)](https://github.com/libretro/beetle-supergrafx-libretro), [Mednafen](https://mednafen.github.io) | Nightly, Nightly, v1.29.0, 1.32.1 |
| TurboGrafx-CD | [Beetle PC Engine (RetroArch)](https://github.com/libretro/beetle-pce-libretro), [Beetle PC Engine Fast (RetroArch)](https://github.com/libretro/beetle-pce-fast-libretro), [Beetle Supergrafx (PC Engine) (RetroArch)](https://github.com/libretro/beetle-supergrafx-libretro), [Mednafen](https://mednafen.github.io) | Nightly, Nightly, v1.29.0, 1.32.1 |
| SuperGrafx | [Beetle PC Engine (RetroArch)](https://github.com/libretro/beetle-pce-libretro), [Beetle Supergrafx (PC Engine) (RetroArch)](https://github.com/libretro/beetle-supergrafx-libretro), [Mednafen](https://mednafen.github.io) | Nightly, v1.29.0, 1.32.1 |
| PCFX | [Beetle PC-FX (RetroArch)](https://github.com/libretro/beetle-pcfx-libretro), [Mednafen](https://mednafen.github.io) | Nightly, 1.32.1 |
| Nintendo | [FCEUX](http://sourceforge.net/projects/fceultra/), [FCEUmm (RetroArch)](https://github.com/libretro/fceumm), [Mednafen](https://mednafen.github.io), [Nestopia (RetroArch)](https://github.com/libretro/nestopia), [QuickNES (RetroArch)](https://github.com/libretro/QuickNES_Core) | 2.6.2, nightly, 1.32.1, v1.51.1, Nightly |
| Famicom Disk System | [FCEUX](http://sourceforge.net/projects/fceultra/), [FCEUmm (RetroArch)](https://github.com/libretro/fceumm), [Mednafen](https://mednafen.github.io), [Nestopia (RetroArch)](https://github.com/libretro/nestopia) | 2.6.2, nightly, 1.32.1, v1.51.1 |
| Game Boy | [Gambatte](https://github.com/sinamas/gambatte), [Gambatte (RetroArch)](https://github.com/libretro/gambatte-libretro), [Mednafen](https://mednafen.github.io), [SameBoy (RetroArch)](https://github.com/libretro/SameBoy), [TGBDual](https://github.com/libretro/tgbdual-libretro), [VBA-M (RetroArch)](https://docs.libretro.com/library/vba_m/), [mGBA (RetroArch)](https://github.com/libretro/mgba) | 0.5.0, Nightly, 1.32.1, v0.14.7, v0.8.3, nightly, v0.10-dev |
| Super Nintendo | [BSNES (RetroArch)](https://docs.libretro.com/library/bsnes/), [BSNES HD (RetroArch)](https://docs.libretro.com/library/bsnes/), [BSNES Mercury (Accuracy) (RetroArch)](https://docs.libretro.com/library/bsnes/), [BSNES Mercury (Balanced) (RetroArch)](https://docs.libretro.com/library/bsnes/), [BSNES Mercury (Performance) (RetroArch)](https://github.com/libretro/bsnes-mercury), [Beetle SNES (RetroArch)](https://github.com/libretro/beetle-bsnes-libretro), [Mednafen](https://mednafen.github.io), [Snes9x](http://www.snes9x.com), [Snes9x (RetroArch)](https://docs.libretro.com/library/snes9x/), [Snes9x 2002 (RetroArch)](https://github.com/libretro/snes9x2002), [Snes9x 2005 (RetroArch)](https://github.com/libretro/snes9x2005), [Snes9x 2005 Plus (RetroArch)](https://github.com/libretro/snes9x2005), [Snes9x 2010 (RetroArch)](https://github.com/libretro/snes9x2010), [Snesticle](https://github.com/iaddis/SNESticle) | nightly, nightly, nightly, nightly, nightly, Nightly, 1.32.1, 1.60, 1.61, Nightly, Nightly, Nightly, Nightly, 1.0 |
| Virtual Boy | [Beetle VB (RetroArch)](https://github.com/libretro/beetle-vb-libretro), [Mednafen](https://mednafen.github.io) | v0.9.36.1, 1.32.1 |
| Nintendo 64 | [Mupen64Plus](https://github.com/mupen64plus), [Mupen64Plus-Next](https://github.com/libretro/mupen64plus-libretro-nx), [Mupen64Plus-Next (RetroArch)](https://github.com/libretro/mupen64plus-libretro-nx) | 2.5, 2.4, 2024.10.29 |
| Game Boy Color | [Gambatte](https://github.com/sinamas/gambatte), [Gambatte (RetroArch)](https://github.com/libretro/gambatte-libretro), [Mednafen](https://mednafen.github.io), [SameBoy (RetroArch)](https://github.com/libretro/SameBoy), [TGBDual](https://github.com/libretro/tgbdual-libretro), [VBA-M (RetroArch)](https://docs.libretro.com/library/vba_m/), [mGBA (RetroArch)](https://github.com/libretro/mgba) | 0.5.0, Nightly, 1.32.1, v0.14.7, v0.8.3, nightly, v0.10-dev |
| GameCube | [Dolphin](https://github.com/Provenance-Emu/dolphin-ios-jitless/tree/brand175/master%2Bpatches) | 11 |
| Game Boy Advance | [Beetle GBA (RetroArch)](https://github.com/libretro/beetle-gba-libretro), [Mednafen](https://mednafen.github.io), [VBA Next (RetroArch)](https://github.com/libretro/vba-next), [VBA-M (RetroArch)](https://docs.libretro.com/library/vba_m/), [VisualBoyAdvance](https://sourceforge.net/projects/vba/), [gpSP (RetroArch)](https://github.com/libretro/gpsp), [mGBA](https://mgba.io/), [mGBA (RetroArch)](https://github.com/libretro/mgba) | v0.9.36, 1.32.1, Nightly, nightly, 1.8.0, Nightly, 0.10.3, v0.10-dev |
| Pokémon mini | [PokeMini](http://sourceforge.net/projects/pokemini/), [PokeMini (RetroArch)](https://docs.libretro.com/library/pokemini/) | v0.60, Nightly |
| DS | [DeSmuME (RetroArch)](https://docs.libretro.com/library/desmume/), [MelonDS (RetroArch)](https://melonds.kuribo64.net), [MelonDS DS (RetroArch)](https://docs.libretro.com/library/melonds_ds/), [NooDS (RetroArch)](https://github.com/Hydr8gon/NooDS) | git, 0.9.4, git, git |
| 3DS | [Azahar (Experimental)](https://azahar-emu.org), [EmuThreeds](https://github.com/emuPlace/emuThreeDS) | git, 1.0.6 |
| 3DO | [Opera](https://github.com/libretro/opera-libretro), [Opera (RetroArch)](https://github.com/libretro/opera-libretro) | 1.0.0, 1.0.0 |
| Neo Geo | [FBNeo (RetroArch)](https://github.com/libretro/FBNeo), [Geolith (RetroArch)](https://github.com/libretro/geolith-libretro), [MAME (Current) (RetroArch)](https://docs.libretro.com/development/cores/core-specific/mame/) | v1.0.0.02, 2015.02.16, v0.258 |
| Neo Geo CD | [NeoCD (RetroArch)](https://github.com/libretro/neocd_libretro) | Nightly |
| Neo Geo Pocket | [Beetle Neopop (RetroArch)](https://docs.libretro.com/library/beetle_neopop/), [Mednafen](https://mednafen.github.io), [RACE (RetroArch)](https://docs.libretro.com/library/race/) | v0.9.36.1, 1.32.1, v2.16 |
| Neo Geo Pocket Color | [Beetle Neopop (RetroArch)](https://docs.libretro.com/library/beetle_neopop/), [Mednafen](https://mednafen.github.io), [RACE (RetroArch)](https://docs.libretro.com/library/race/) | v0.9.36.1, 1.32.1, v2.16 |
| SG-1000 | [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX (RetroArch)](https://github.com/libretro/Genesis-Plus-GX), [Genesis Plus GX (Wide) (RetroArch)](https://github.com/libretro/Genesis-Plus-GX-Wide), [MSX/SVI/ColecoVision/SG-1000 (blueMSX) (RetroArch)](https://github.com/libretro/blueMSX) | v1.7.4, 1.7.4, nightly, Nightly |
| Master System | [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX (RetroArch)](https://github.com/libretro/Genesis-Plus-GX), [Genesis Plus GX (Wide) (RetroArch)](https://github.com/libretro/Genesis-Plus-GX-Wide), [SMS Plus GX (RetroArch)](https://github.com/libretro/smsplus-gx) | v1.7.4, 1.7.4, nightly, Nightly |
| Genesis | [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX (RetroArch)](https://github.com/libretro/Genesis-Plus-GX), [Genesis Plus GX (Wide) (RetroArch)](https://github.com/libretro/Genesis-Plus-GX-Wide) | v1.7.4, 1.7.4, nightly |
| Game Gear | [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX (RetroArch)](https://github.com/libretro/Genesis-Plus-GX), [Genesis Plus GX (Wide) (RetroArch)](https://github.com/libretro/Genesis-Plus-GX-Wide), [SMS Plus GX (RetroArch)](https://github.com/libretro/smsplus-gx) | v1.7.4, 1.7.4, nightly, Nightly |
| Sega CD | [Genesis Plus GX](https://github.com/ekeeke/Genesis-Plus-GX), [Genesis Plus GX (RetroArch)](https://github.com/libretro/Genesis-Plus-GX), [Genesis Plus GX (Wide) (RetroArch)](https://github.com/libretro/Genesis-Plus-GX-Wide) | v1.7.4, 1.7.4, nightly |
| 32X | [PicoDrive](https://github.com/notaz/picodrive) | 2.03 |
| Saturn | [Beetle Saturn (RetroArch)](https://github.com/libretro/beetle-saturn-libretro), [Mednafen](https://mednafen.github.io), [Yabause](https://yabause.org), [Yabause (Saturn) (RetroArch)](https://github.com/libretro/yabause) | v0.9.45.1, 1.32.1, v0.9.15, v0.9.15 |
| Dreamcast | [Flycast](https://github.com/flyinghead/flycast), [Flycast JIT-less (Provenance Beta)](https://github.com/flyinghead/flycast), [Reicast](https://github.com/reicast/reicast-emulator) | 5.0, 2.0, 18.04 |
| Smith Engineering Vectrex | [VecX (RetroArch)](https://docs.libretro.com/library/vecx/) | Nightly |
| PlayStation | [Beetle PSX (HW Renderer) (RetroArch)](https://github.com/libretro/beetle-psx-libretro), [Beetle PSX (SW Renderer) (RetroArch)](https://github.com/libretro/beetle-psx-libretro), [BeetlePSX](https://github.com/libretro/beetle-psx-libretro), [DuckStation](https://github.com/stenzek/duckstation/), [Mednafen](https://mednafen.github.io), [PCSX (Rearmed)](https://github.com/notaz/pcsx_rearmed), [PCSX ReARMed (RetroArch)](https://docs.libretro.com/library/pcsx_rearmed/) | 0.9.44.1, 0.9.44.1, 0, 2023.01.11, 1.32.1, r23l, r21 |
| PlayStation Portable | [PPSSPP](https://github.com/hrydgard/ppsspp.git), [PPSSPP](https://github.com/hrydgard/ppsspp.git), [PPSSPP (RetroArch)](https://docs.libretro.com/library/ppsspp/) | v1.13.2-2467, v1.13.2-2467, Git |
| Game Music | [GME](https://github.com/libretro/libretro-gme), [Game Music Emu (RetroArch)](https://docs.libretro.com/library/game_music_emu/) | v0.6.1, v0.6.3 |
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
| Atari ST | `com.provenance.atarist` | — | — |
| Atari 7800 | `com.provenance.7800` | — | — |
| Atari Lynx | `com.provenance.lynx` | — | — |
| Atari Jaguar | `com.provenance.jaguar` | — | — |
| Atari Jaguar CD | `com.provenance.jaguarcd` | — | — |
| WonderSwan | `com.provenance.ws` | — | — |
| WonderSwan | `com.provenance.wsc` | — | — |
| CBS ColecoVision | `com.provenance.colecovision` | — | — |
| CPS-1 | `com.provenance.cps1` | — | — |
| CPS-2 | `com.provenance.cps2` | — | — |
| CPS-3 | `com.provenance.cps3` | — | — |
| Enterprise 128 | `com.provenance.ep128` | — | — |
| IBM PC DOS | `com.provenance.dos` | — | — |
| RetroArch | `com.provenance.retroarch` | — | — |
| MAME | `com.provenance.mame` | — | — |
| Magnavox Odyssey2 | `com.provenance.odyssey2` | — | — |
| Mattel Intellivision | `com.provenance.intellivision` | — | — |
| MSX | `com.provenance.msx` | — | — |
| MSX2 | `com.provenance.msx2` | — | — |
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
| GameCube | `com.provenance.gamecube` | — | — |
| Game Boy Advance | `com.provenance.gba` | `com.rileytestut.delta.game.gba` | [DeltaStyles](https://deltastyles.com/?search=gba) |
| Pokémon mini | `com.provenance.pokemonmini` | — | — |
| DS | `com.provenance.ds` | — | — |
| 3DS | `com.provenance.3ds` | — | [DeltaStyles](https://deltastyles.com/?search=3ds) |
| 3DO | `com.provenance.3DO` | — | — |
| Neo Geo | `com.provenance.neogeo` | — | — |
| Neo Geo CD | `com.provenance.neogeocd` | — | — |
| Neo Geo Pocket | `com.provenance.ngp` | — | — |
| Neo Geo Pocket Color | `com.provenance.ngpc` | — | — |
| SG-1000 | `com.provenance.sg1000` | — | — |
| Master System | `com.provenance.mastersystem` | `com.rileytestut.delta.game.ms` | [DeltaStyles](https://deltastyles.com/?search=master+system) |
| Genesis | `com.provenance.genesis` | `com.rileytestut.delta.game.genesis` | [DeltaStyles](https://deltastyles.com/?search=genesis) |
| Game Gear | `com.provenance.gamegear` | `com.rileytestut.delta.game.gg` | [DeltaStyles](https://deltastyles.com/?search=game+gear) |
| Sega CD | `com.provenance.segacd` | — | [DeltaStyles](https://deltastyles.com/?search=sega+cd) |
| 32X | `com.provenance.32X` | — | — |
| Saturn | `com.provenance.saturn` | — | [DeltaStyles](https://deltastyles.com/?search=saturn) |
| Dreamcast | `com.provenance.dreamcast` | — | [DeltaStyles](https://deltastyles.com/?search=dreamcast) |
| Smith Engineering Vectrex | `com.provenance.vectrex` | — | — |
| PlayStation | `com.provenance.psx` | `com.rileytestut.delta.game.psx` | [DeltaStyles](https://deltastyles.com/?search=playstation) |
| PlayStation Portable | `com.provenance.psp` | — | [DeltaStyles](https://deltastyles.com/?search=psp) |
| Game Music | `com.provenance.music` | — | — |
| Supervision | `com.provenance.supervision` | — | — |
| ZX Spectrum | `com.provenance.zxspectrum` | — | — |

---

{% hint style="info" %}
For the interactive community database, see [eduo.info/pvl](https://eduo.info/pvl/). Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
