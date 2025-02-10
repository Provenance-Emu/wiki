---
description: Certain emulator cores require specific BIOS files in order to play.
---

# BIOS Requirements

✅ [**Systems**](bios-requirements.md#systems) requiring/utilizing BIOS ℹ️ [**Specifications**](bios-requirements.md#specifications) per System 🛃 [**Importing**](bios-requirements.md#importing) BIOS files

{% hint style="warning" %}
**DO NOT** ask us where to obtain BIOS files. Distributing BIOS files violates copyright law.
{% endhint %}

## Systems

**BIOS**: ✅ = Required 🔶 = Optional

| Manufacturer | System                                              | BIOS |
| ------------ | --------------------------------------------------- | ---- |
| Atari        | 2600                                                |      |
|              | 5200                                                | ✅    |
|              | 7800                                                |      |
|              | Lynx                                                | ✅    |
|              | Jaguar                                              |      |
|              | ST                                                  | ✅    |
| Bandai       | WonderSwan                                          |      |
|              | WonderSwan Color                                    |      |
| CBS          | ColecoVision                                        | ✅    |
| NEC          | PC Engine / TurboGrafx-16                           |      |
|              | PC Engine Super CD-ROM² System / TurboGrafx-CD      | ✅    |
|              | PC Engine SuperGrafx                                |      |
|              | PC-FX                                               | ✅    |
| Nintendo     | Famicom / Nintendo Entertainment System             |      |
|              | Famicom Disk System                                 | ✅    |
|              | Game Boy                                            |      |
|              | Super Famicom / Super Nintendo Entertainment System |      |
|              | Game Boy Color                                      |      |
|              | Virtual Boy                                         |      |
|              | Nintendo 64                                         |      |
|              | Game Boy Advance                                    | 🔶   |
|              | Pokemon mini                                        |      |
| Palm         | PalmOS                                              | ✅    |
| Philips      | CD-i                                                | ✅    |
| Sega         | SG-1000                                             |      |
|              | Master System                                       |      |
|              | Mega Drive / Genesis                                |      |
|              | Game Gear                                           |      |
|              | Mega-CD / CD                                        | ✅×3  |
|              | 32X                                                 |      |
|              | Saturn                                              | ✅×3  |
| SNK          | Neo Geo Pocket                                      |      |
|              | Neo Geo Pocket Color                                |      |
| Sony         | PlayStation                                         | ✅×3  |

## Specifications

{% hint style="info" %}
Filenames are arbitrary as long as the MD5s match. Provenance will rename files on import.
{% endhint %}

### Atari 5200

| Filename   | MD5 Hash                         |
| ---------- | -------------------------------- |
| `5200.rom` | 281f20ea4320404ec820fb7ec0693b38 |

### Atari Lynx

| Filename       | MD5 Hash                         |
| -------------- | -------------------------------- |
| `lynxboot.img` | fcd403db69f54290b51035d82f835e7b |

### CBS ColecoVision

| Filename           | MD5 Hash                         |
| ------------------ | -------------------------------- |
| `colecovision.rom` | 2c66f5911e5b42b8ebe113403548eee7 |

### Nintendo Famicom Disk System

| Filename      | MD5 Hash                         |
| ------------- | -------------------------------- |
| `disksys.rom` | ca30b50f880eb660a320674ed365ef7a |

### Nintendo Game Boy Advance

| Filename   | MD5 Hash                         |
| ---------- | -------------------------------- |
| `gba.bios` | a860e8c0b6d573d191e4ec7db1b1e4f6 |

{% hint style="info" %}
Game Boy Advance BIOS is optional.
{% endhint %}

### NEC PC Engine Super CD-ROM² System / TurboGrafx-CD

| Filename       | MD5 Hash                         |
| -------------- | -------------------------------- |
| `syscard3.pce` | ff1a674273fe3540ccef576376407d1d |

### NEC PC-FX

| Filename   | MD5 Hash                         |
| ---------- | -------------------------------- |
| `pcfx.rom` | 08e36edbea28a017f79f8d4f7ff9b6d7 |

### Palm PalmOS

| Filename               | BIOS Name / Version                    | MD5 Hash                         |
| ---------------------- | -------------------------------------- | -------------------------------- |
| `palmos41-en-m515.rom` | Palm OS 4.1                            |                                  |
| `palmos40-en-m500.rom` | Palm OS 4.0                            |                                  |
| `palmos52-en-t3.rom`   | Palm OS 5.2                            |                                  |
| `palmos60-en-t3.rom`   | Palm OS 6.0                            |                                  |
| `bootloader-dbvz.rom`  | UART Bootloader                        |                                  |

{% hint style="info" %}
Only `palmos41-en-m515.rom` is required
{% endhint %}

### Philips CD-i

<table><thead><tr><th>Filename</th><th>MD5 Hash</th><th>Notes</th><th data-type="checkbox">Required</th></tr></thead><tbody><tr><td>cdimono1.zip</td><td>c59f92647701428bc453976740eb75cf</td><td>Must manually put in RetroArch/system/same_cdi/bios/</td><td>true</td></tr><tr><td>cdimono2.zip</td><td></td><td></td><td>false</td></tr><tr><td>cdibios.zip</td><td></td><td></td><td>false</td></tr></tbody></table>

{% hint style="warning" %}
Must manually put in \`RetroArch/system/same\_cdi/bios/\`
{% endhint %}

### Sega Mega-CD / CD

| Filename        | BIOS Name / Version                    | Region | MD5 Hash                         |
| --------------- | -------------------------------------- | ------ | -------------------------------- |
| `bios_CD_U.bin` | Sega CD Model 1 (US 921011) BIOS 1.10  | US     | 2efd74e3232ff260e371b99f84024f7f |
| `bios_CD_E.bin` | Mega-CD Model 1 (EU 921027) BIOS 1.00  | EU     | e66fa1dc5820d254611fdcdba0662372 |
| `bios_CD_J.bin` | Mega-CD Model 1 (JP 911217) BIOS 1.00p | JP     | bdeb4c47da613946d422d97d98b21cda |

{% hint style="success" %}
All 3 BIOS are required.
{% endhint %}

### Sega Saturn

| Filename          | BIOS Name / Version     | Region | MD5 Hash                         |
| ----------------- | ----------------------- | ------ | -------------------------------- |
| `saturn_bios.bin` | Sega Saturn BIOS v1.00  | JP/US  | af5828fdff51384f99b3c4926be27762 |
| `mpr-17933.bin`   | Sega Saturn BIOS v1.01a | EU     | 3240872c70984b6cbfda1586cab68dbe |
| `sega_101.bin`    | Sega Saturn BIOS v1.01  | JP     | 85ec9ca47d8f6807718151cbcca8b964 |

{% hint style="success" %}
All 3 BIOS are required. Filenames online may vary. If the MD5s match, Provenance will correctly rename for you on import.
{% endhint %}

### Sony PlayStation

| Filename       | BIOS Name / Version | Region | MD5 Hash                           |
| -------------- | ------------------- | ------ | ---------------------------------- |
| `scph5500.bin` | SCPH-5500 / v3.0J   | JP     | `8dd7d5296a650fac7319bce665a6a53c` |
| `scph5501.bin` | SCPH-5501 / v3.0A   | USA    | `490f666e1afb15b7362b406ed1cea246` |
| `scph5502.bin` | SCPH-5502 / v3.0E   | EU     | `32736f17079d0b2b7024407c39bd3050` |

{% hint style="success" %}
All 3 BIOS are required.
{% endhint %}

## Importing

BIOS files are imported exactly the same as ROMs: [Importing ROMs](roms/importing-roms.md). When you have the correct BIOS successfully imported they will shown in Settings → Cores or they show as missing/red/required, otherwise you have the wrong files. You need the exact ROMs files matching the MD5 hashes above.

### MD5

Though not required, you can verify the MD5 hashes of your files to be certain. To obtain the MD5 hash of your BIOS files, you can use `md5 [path to file, or drag and drop file here]` in Terminal. Check that it matches the MD5 hash of the file listed above.

Alternatively, BIOS files can be force [uploaded](roms/importing-roms.md#uploading) manually into `/BIOS/com.provenance.[system]` via WebUI or WebDav (iOS, tvOS) or the Apple Files app (iOS only).

{% hint style="info" %}
🗯 If you are still stuck ask for [help](https://discord.gg/NhzgrXh) on our Discord.
{% endhint %}
