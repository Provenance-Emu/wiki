---
description: How to legally dump ROMs, disc images, and save data from your own physical media for use with Provenance.
---

# Ripping & Dumping Physical Media

This guide covers how to create digital backups of game cartridges and discs you **legally own**, for use in Provenance. "Ripping" or "dumping" a ROM means copying the game data from physical media onto your computer or device.

{% hint style="danger" %}
**Legal Notice:** In some regions, creating ROM backups of games you legally own for your own personal use may be permitted, but laws and anti-circumvention rules vary by country and may change over time. Downloading or sharing ROMs for games you do not own, or distributing copyrighted game files, may infringe copyright or other rights. Always research and follow the laws in your jurisdiction before dumping, using, or distributing game files. This guide is for informational purposes and focuses on personal backups only.
{% endhint %}

## Quick Navigation

- [Cartridge Dumping](#cartridge-dumping) — Game Boy, GBA, NES, SNES, N64, Genesis, and more
- [Disc Ripping](#disc-ripping) — PlayStation, PS2, PSP, GameCube, Wii, Dreamcast
- [Network / Softmod Ripping](#network--softmod-ripping) — 3DS, NDS, PS2, SNES/NES Classic
- [Save Data Dumping](#save-data-dumping) — GB/GBA saves, PS1 memory cards, PS2, N64
- [Format Conversion](#format-conversion) — CHD, M3U playlists, format table

---

## Cartridge Dumping

Cartridge-based games require dedicated hardware — a "cart dumper" — to read the ROM data. Most dumpers connect to your computer via USB and come with software to save the game file.

### Hardware Overview

| Hardware | Systems Supported | Approx. Price | Open Source | URL |
|---|---|---|---|---|
| **GB Operator** (Epilogue) | GB, GBC, GBA | ~$50 | No | [epilogue.co](https://epilogue.co) |
| **GBxCart RW** (insideGadgets) | GB, GBC, GBA | ~$35 | Yes | [insidegadgets.com](https://insidegadgets.com) |
| **Joey Jr** (BennVenn) | GB, GBC, GBA | ~$45 | No | [bennvenn.myshopify.com](https://bennvenn.myshopify.com) |
| **Retrode 2** | SNES, Genesis, N64/GB/GBA (adapters) | ~$80 used | Yes | [retrode.org](https://retrode.org) |
| **INLretro Dumper-Programmer** | NES, SNES, N64, Genesis, GB, GBA+ | ~$80 | Yes | [inlretro.com](https://inlretro.com) |
| **Open Source Cart Reader (OSCR)** | 50+ systems (NES, SNES, N64, Genesis, GB, GBA, etc.) | ~$50 DIY | Yes | [github.com/sanni/cartreader](https://github.com/sanni/cartreader) |
| **GodMode9** (3DS CFW) | DS, 3DS | Free (software) | Yes | [github.com/d0k3/GodMode9](https://github.com/d0k3/GodMode9) |

---

### Game Boy / GBC / GBA

Three well-supported options exist for dumping Game Boy family cartridges. All produce standard `.gb`, `.gbc`, or `.gba` ROM files and `.sav` save files compatible with Provenance.

<details>
<summary><strong>GB Operator (Epilogue) — Recommended for beginners</strong></summary>

The GB Operator is the easiest plug-and-play solution. It connects via USB-C and uses Epilogue's desktop app (macOS/Windows/Linux).

**What you need:**
- GB Operator device
- Epilogue desktop app
- USB-C cable

**Steps:**

1. Download and install the Epilogue app.
2. Insert your Game Boy, GBC, or GBA cartridge into the GB Operator.
3. Connect the GB Operator to your computer via USB-C.
4. Open the Epilogue app — your cartridge should be detected automatically.
5. Click **Backup ROM** to dump the game ROM to your computer.
6. Optionally click **Backup Save** to dump any existing save data.

The app saves files to a folder of your choice. ROM files use standard extensions (`.gb`, `.gbc`, `.gba`) and save files use `.sav`.

{% hint style="success" %}
`.sav` files dumped from a cartridge are directly compatible with Provenance's save system. Copy them alongside your ROM file when importing.
{% endhint %}

</details>

<details>
<summary><strong>GBxCart RW (insideGadgets) — Open source option</strong></summary>

The GBxCart RW is an open-source, lower-cost alternative. It uses the **FlashGBX** software (community-developed, cross-platform).

**What you need:**
- GBxCart RW device
- FlashGBX app (available at [github.com/lesserkuma/FlashGBX](https://github.com/lesserkuma/FlashGBX))
- USB cable (included with device)

**Steps:**

1. Download FlashGBX from the GitHub releases page.
2. Insert your cartridge into the GBxCart RW and connect to your computer.
3. Open FlashGBX — the device should be auto-detected.
4. Select **Backup ROM** to dump the game.
5. Select **Backup Save Data** if you want to preserve the cartridge save.

FlashGBX also supports writing ROMs and saves back to cartridges (useful for restoring saves).

</details>

<details>
<summary><strong>Joey Jr (BennVenn) — Windows-focused</strong></summary>

The Joey Jr is a compact USB dumper from BennVenn. It uses BennVenn's own companion software.

**Steps:**

1. Download the BennVenn software from [bennvenn.myshopify.com](https://bennvenn.myshopify.com) (check the product page for the latest version).
2. Insert your cartridge and connect the Joey Jr via USB.
3. Open the companion app and select **Dump ROM**.
4. Save the resulting file to your computer.

{% hint style="warning" %}
The BennVenn companion software is **Windows-only**. macOS/Linux users should consider the GB Operator or GBxCart RW instead.
{% endhint %}

</details>

---

### NES / SNES / N64 / Genesis / SMS / Game Gear

Several hardware options support cartridge-based home consoles. The right choice depends on which systems you need and your budget.

<details>
<summary><strong>Retrode 2 — No software required</strong></summary>

The Retrode 2 appears as a **USB mass storage device** — your computer mounts it like a flash drive and the ROM is directly readable. No driver or app installation required.

**Supported natively (with included slots):**
- SNES / Super Famicom
- Sega Genesis / Mega Drive

**Supported with optional adapters:**
- N64, Game Boy (GB/GBC/GBA), Sega Master System, Game Gear, and more

**Steps:**

1. Insert the cartridge into the appropriate slot on the Retrode 2.
2. Connect the Retrode 2 to your computer via USB.
3. Your computer mounts a virtual drive — open it in Finder (macOS) or Explorer (Windows).
4. Copy the `.sfc`, `.md`, or other ROM file directly to your computer.

{% hint style="warning" %}
The Retrode 2 is **discontinued** but available used (eBay, forums). The N64 adapter has known compatibility issues with some cartridges — CIC/lockout chips may cause partial or failed dumps. Use INLretro or OSCR for more reliable N64 dumping.
{% endhint %}

</details>

<details>
<summary><strong>INLretro Dumper-Programmer — Active development, NES native support</strong></summary>

The INLretro is actively maintained and supports a wide range of cartridge formats including NES (with native mapper support), SNES, N64, Genesis, and many others.

**Steps:**

1. Download the INLretro client software from [inlretro.com](https://inlretro.com).
2. Connect the INLretro device via USB.
3. Insert your cartridge into the appropriate adapter/slot.
4. Open the client software and select your system.
5. Click **Dump** to read the ROM to your computer.

INLretro is especially recommended for NES — it handles many mappers and PCB variants natively.

</details>

<details>
<summary><strong>Open Source Cart Reader (OSCR) — Broadest system support</strong></summary>

The OSCR (by sanni) is a DIY Arduino-based cart reader that supports 50+ systems. It dumps directly to an SD card — no computer software required during the dump.

**What you need:**
- OSCR hardware (build from [GitHub](https://github.com/sanni/cartreader), or buy pre-assembled from community vendors)
- SD card (FAT32 formatted)
- Appropriate cart slot/adapter for your system

**Steps:**

1. Insert a FAT32-formatted SD card into the OSCR.
2. Insert the game cartridge into the correct slot.
3. Power on the OSCR and navigate the menu to select your system.
4. Select **Dump ROM** — the file is written directly to the SD card.
5. Transfer the SD card to your computer and copy the ROM file.

{% hint style="info" %}
The OSCR has the broadest system support of any cart reader. Community slot adapters are available for Neo Geo MVS/AES, WonderSwan, PC Engine HuCard, Atari 2600/5200/7800, and many more. Check the OSCR GitHub wiki for a full adapter list.
{% endhint %}

</details>

---

### Nintendo DS & 3DS

Dumping DS and 3DS cartridges requires a hacked 3DS running **GodMode9**, a powerful homebrew tool.

{% hint style="warning" %}
**Prerequisites:** Your 3DS must have custom firmware (CFW) installed before using GodMode9. Follow the complete CFW setup guide at [3ds.hacks.guide](https://3ds.hacks.guide) — this installs Luma3DS and enables homebrew. This process is outside the scope of this wiki.
{% endhint %}

<details>
<summary><strong>GodMode9 — Dumping DS & 3DS cartridges</strong></summary>

GodMode9 is a full-access file system browser for the 3DS. It can dump game cartridges to the SD card.

**What you need:**
- Nintendo 3DS with Luma3DS CFW installed
- GodMode9 installed (typically already included with a standard CFW setup via 3ds.hacks.guide)
- SD card with sufficient free space (3DS games can be up to 4 GB)

**Steps:**

1. Power off your 3DS.
2. Insert the game cartridge you want to dump.
3. Hold the **Start** button and power on the 3DS to boot into GodMode9.
4. Navigate to **`[C:] GAMECART`** using the D-pad.
5. Select the `.trim.3ds` or `.nds` file shown (this is your cartridge).
6. Press **A** to open the options menu, then select **`Copy to 0:/gm9/out`** (or your preferred output location on the SD card).
7. Wait for the dump to complete, then power off the 3DS.
8. Remove the SD card and transfer the dumped ROM file to your computer.

For **DS cartridges** inserted into a 3DS, the same process applies — GodMode9 will show the `.nds` file under `[C:] GAMECART`.

{% hint style="info" %}
3DS ROM dumps (`.3ds` files) may need to be decrypted before Provenance can use them. See the [Nintendo 3DS Guide](../../info/system-guides/3ds.md) for details on decrypted ROMs and compatible formats.
{% endhint %}

</details>

---

### Other Systems

<details>
<summary><strong>Other systems with OSCR adapter support</strong></summary>

The OSCR ([GitHub](https://github.com/sanni/cartreader)) supports adapters for many additional systems:

| System | Method | Notes |
|---|---|---|
| **Neo Geo MVS / AES** | OSCR with Neo Geo adapter | MVS (arcade) and AES (home) cartridges |
| **Atari 2600 / 5200 / 7800** | INLretro or OSCR with Atari adapter | Check INLretro system support page |
| **WonderSwan / WonderSwan Color** | OSCR with WonderSwan adapter | Community-built adapter |
| **PC Engine / TurboGrafx-16 HuCard** | OSCR with PCE adapter | HuCard only (not CD-ROM²) |
| **Sega Master System / Game Gear** | Retrode 2 adapter or OSCR | Both use similar cartridge pinouts |

For systems not listed here, search the OSCR GitHub issues and wiki — the community frequently adds new adapter designs.

</details>

---

## Disc Ripping

Use the table below to find the right method for your system, then follow the instructions in the relevant section.

### Equipment Overview

| Method | Works For | What You Need |
|---|---|---|
| Standard CD-ROM drive | PS1, Sega CD, Saturn, 3DO, TG-CD, PC-FX, Neo Geo CD | Any modern optical drive |
| DVD-ROM drive | PS2 | DVD-capable drive |
| Specialized GD-ROM drive | Dreamcast | Yamaha CRW2200 or Plextor PX-W4012 (rare) |
| Console-side dump (CleanRip) | GameCube, Wii | Wii with Homebrew Channel + SD card or USB drive |
| Network dump | PS2, Dreamcast, PSP | Softmodded console + network |

{% hint style="info" %}
**Xbox not supported:** Original Xbox backups are out of scope for this guide — Provenance does not support the original Xbox.
{% endhint %}

---

### Standard CD Games (PS1, Sega CD, Saturn, 3DO, TG-CD, PC-FX, Neo Geo CD)

Most CD-based games can be ripped with any standard optical drive. The output is a `.bin + .cue` pair — see [Formatting ROMs — Multi-file ROMs](formatting-roms.md#multi-file-roms) for how to package them for import.

{% tabs %}
{% tab title="macOS" %}
**Tool:** cdrdao (free, command-line)

1. Install [Homebrew](https://brew.sh) if you haven't already.
2. Install cdrdao:
   ```bash
   brew install cdrdao
   ```
3. Insert the disc and find the device path:
   ```bash
   drutil status
   ```
   Note the device (typically `/dev/disk2`).
4. Rip the disc as a raw image:
   ```bash
   cdrdao read-cd --read-raw --datafile "game.bin" --device /dev/disk2 --driver generic-mmc-raw game.toc
   ```
5. Convert the `.toc` file to `.cue`:
   ```bash
   toc2cue game.toc game.cue
   ```

You now have `game.bin` and `game.cue`. Archive both in a single `.zip` or `.7z` before importing.
{% endtab %}

{% tab title="Windows" %}
**Tool:** ImgBurn (free GUI)

1. Download and install [ImgBurn](https://www.imgburn.com).
2. Insert the disc.
3. Select **Mode → Read Disc**.
4. Set the **Destination** to a folder on your PC.
5. For PlayStation 1 discs, click the **Options** tab and set:
   - **Read Sub Channel Data from Disc:** Yes
   - **Type:** User Data + Sub-Channel Q
6. Click the **Read** button (disc-to-folder icon).

ImgBurn outputs a `.bin` and `.cue` file. Archive both before importing into Provenance.
{% endtab %}

{% tab title="Linux" %}
**Tool:** cdrdao (same commands as macOS)

1. Install cdrdao via your package manager:
   ```bash
   sudo apt install cdrdao      # Debian/Ubuntu
   sudo dnf install cdrdao      # Fedora
   ```
2. Find your disc device:
   ```bash
   lsblk
   ```
   It's usually `/dev/sr0`.
3. Rip the disc:
   ```bash
   cdrdao read-cd --read-raw --datafile game.bin --device /dev/sr0 --driver generic-mmc-raw game.toc
   toc2cue game.toc game.cue
   ```

For scratched or damaged **data-only** discs, `ddrescue` can attempt a more robust read. This produces a single-track `.bin`; for mixed-mode or audio CDs (PS1, Sega CD, Saturn), use `cdrdao` above instead:
```bash
sudo apt install gddrescue
ddrescue -d -r3 /dev/sr0 game.bin game.log
```
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Verify your rip with Redump:** Calculate the MD5 hash of your `.bin` file (`md5 game.bin` on macOS, `md5sum game.bin` on Linux, `certutil -hashfile game.bin MD5` on Windows) and search [redump.org](https://redump.org) to confirm it matches the known-good dump. A matching hash means your rip is accurate.
{% endhint %}

{% hint style="warning" %}
**TurboGrafx-CD / PC Engine CD:** These systems require a System Card BIOS file to run. See [BIOS Requirements](../bios-requirements.md) for the correct files.
{% endhint %}

**Saturn multi-disc games:** Saturn titles that span multiple discs need an `.m3u` playlist file. See [Formatting ROMs — Multi-disc Games](formatting-roms.md#multi-disc-games) for instructions.

**Sega CD:** All three regional BIOS files are required (USA, Europe, Japan) depending on the game's region. See [BIOS Requirements](../bios-requirements.md).

---

### PlayStation 2

PS2 discs are standard DVDs and can be ripped with a DVD-ROM drive. Dual-layer discs (larger games) may fail on macOS optical drives — a USB DVD drive or network dump is more reliable.

**Method A: DVD drive on PC**

{% tabs %}
{% tab title="Windows" %}
Use ImgBurn in **Mode → Read Disc**. Output format: **ISO**. No special subchannel settings needed.
{% endtab %}
{% tab title="Linux" %}
```bash
# Install (Debian/Ubuntu): sudo apt install gddrescue
# Then run:
ddrescue -d -r3 /dev/sr0 game.iso game.log
```
`ddrescue` handles read errors better than a simple `dd`, which is important for dual-layer discs.
{% endtab %}
{% endtabs %}

**Method B: Network dump (OPL/FreeMcBoot)**

If you have a softmodded PS2 running FreeMcBoot and Open PS2 Loader (OPL), you can dump discs over the network without a PC DVD drive. See the [Network / Softmod Ripping](#network--softmod-ripping) section below.

Output format for PS2: `.iso`

### Network Dump (PS2, Dreamcast, PSP)

A *network dump* means using a modified console to stream game data over your local network to a computer, instead of reading the disc directly with a PC drive.

Typical flow:

- Softmod or homebrew-enable your console (e.g. FreeMcBoot/OPL on PS2, homebrew loader on Dreamcast/PSP).
- Run a dumping utility on the console that exposes the disc or UMD over the network.
- Connect from your computer (often via a small helper app or web interface) and save the disc image to storage.
- Import the resulting ISO/CSO (or other supported format) into Provenance as you would any other ROM.

For consoles without a reliable PC-compatible drive (like Dreamcast GD-ROM or UMD-based systems), network dumping is often the most practical way to get a complete image of your own discs. See [Network / Softmod Ripping](#network--softmod-ripping) below for step-by-step instructions.

---

### Dreamcast GD-ROM

{% hint style="danger" %}
**GD-ROM is a proprietary format.** Standard PC optical drives can only read the low-density area (~1 GB) of a GD-ROM disc — the game data lives in the high-density area and is **inaccessible** to ordinary drives. You need a specialized drive or a network dump method.
{% endhint %}

**Method A: Specialized GD-ROM drive (rare)**

Two drives are known to work with GD-ROM ripping tools:
- **Yamaha CRW2200** — most common recommended drive
- **Plextor PX-W4012** — also works

These drives typically cost $100–$300+ and are hard to find. If you have one, use **GD-ROM Explorer** or other compatible GD-ROM ripping software with the appropriate PC tools.

**Method B: Network dump via httpd-ism (recommended)**

<details><summary><strong>httpd-ism network dump method</strong></summary>

This method uses an original Dreamcast equipped with the official Broadband Adapter and the **httpd-ism** boot disc to serve GD-ROM data over HTTP.

**Requirements:**
- Dreamcast console
- Dreamcast Broadband Adapter (HIT-0400)
- httpd-ism boot disc (burned CD-R)
- PC on the same local network

**Steps:**
1. Boot the httpd-ism disc on the Dreamcast.
2. Note the IP address displayed on screen.
3. On your PC, open a browser and navigate to `http://[dreamcast-ip]/` — you'll see a file listing of the GD-ROM tracks.
4. Download all track files (typically `track01.iso`, `track02.raw`, etc.) to a folder on your PC.
5. Download the accompanying `.gdi` descriptor file.

**Alternative:** **DreamShell** is a more modern alternative that also supports network dumping via SD card or network adapter. Consult the DreamShell documentation for setup details.

</details>

**Output format:** `.gdi` (a descriptor file referencing multiple track files)

After dumping, convert to a single `.chd` file for easier import:

```bash
chdman createcd -i game.gdi -o game.chd
```

See [Advanced ROM Management — CHD Format](advanced-management.md#chd-format-recommended) for more on `chdman`.

---

### GameCube & Wii

Nintendo optical discs use a proprietary format that standard PC drives cannot read directly. **CleanRip** is the recommended homebrew tool that runs on the Wii itself.

<details><summary><strong>CleanRip (recommended) — dump from the console</strong></summary>

**Requirements:**
- Wii console with the **Homebrew Channel** installed
- SD card or USB drive formatted as **FAT32** with 8+ GB free. FAT32 is required — the Wii cannot read exFAT or NTFS. CleanRip automatically splits Wii ISOs (~4.7 GB) into 4 GB chunks to work around FAT32's file size limit; the split files can be rejoined with a tool like **wit** (Wiimms ISO Tools) after transfer to your PC.
- CleanRip homebrew app

**Steps:**
1. Download CleanRip and copy it to your SD card: `SD:/apps/CleanRip/boot.dol`
2. Boot the Wii and launch the Homebrew Channel.
3. Launch **CleanRip**.
4. Select your dump destination (SD or USB).
5. When prompted, insert the GameCube or Wii disc.
6. Select the disc type and confirm settings (leave defaults unless you know otherwise).
7. CleanRip will dump the disc — allow 10–40 minutes depending on disc size.
8. Copy the resulting `.iso` file to your PC.

</details>

<details><summary><strong>PC drive alternative (less reliable)</strong></summary>

Specific LG and Asus drives with certain firmware can read Wii/GameCube discs using raw read commands.

**Known compatible drives (partial list):**
- LG GH22NS30 (with patched firmware)
- Asus DRW-24B1ST

**Tools:**
- **Friidump** — open-source, reads via raw SCSI commands
- **Rawdump** — Windows-only alternative

This method is less reliable than CleanRip, requires finding a compatible drive, and may fail on dual-layer Wii discs. CleanRip is strongly preferred.

</details>

Output format: `.iso` (for both GameCube and Wii)

For folder structures and further configuration, see the [GameCube & Wii system guide](../../info/system-guides/gamecube-wii.md).

---

### PSP UMD

UMD discs cannot be read by a standard PC drive. Dumping requires **Custom Firmware (CFW)** running on the PSP itself. See the [Network / Softmod Ripping](#network--softmod-ripping) section for details.

---

### Other Disc Systems

| System | Method | Notes |
|---|---|---|
| **3DO** | Standard CD drive | Same as PS1 section above. Output: `.bin + .cue` |
| **Neo Geo CD** | Standard CD drive | Same as PS1 section above. Output: `.bin + .cue` |
| **PC Engine CD / TurboGrafx-CD** | Standard CD drive | Same as PS1 section above. Requires System Card BIOS — see [BIOS Requirements](../bios-requirements.md) |
| **PC-FX** | Standard CD drive | Same as PS1 section above. Requires PC-FX BIOS — see [BIOS Requirements](../bios-requirements.md) |
| **Sega CD / Mega CD** | Standard CD drive | Same as PS1 section above. All 3 regional BIOS files required — see [BIOS Requirements](../bios-requirements.md) |

---

{% hint style="info" %}
After ripping, convert disc images to CHD format for smaller files and single-file convenience. See [Advanced ROM Management](advanced-management.md#chd-format-recommended) for chdman commands.
{% endhint %}

---

## Network / Softmod Ripping

Some systems can dump games directly from the console using custom firmware (CFW) or homebrew software — no dedicated hardware dumper required.

### Nintendo 3DS

<details>
<summary><strong>Using GodMode9 on a CFW 3DS (Luma3DS)</strong></summary>

3DS ROM dumping requires a 3DS running custom firmware. The most common CFW is **Luma3DS**, installed via the [3ds.hacks.guide](https://3ds.hacks.guide/) process.

**What you need:**
- A 3DS/2DS with Luma3DS CFW installed
- **GodMode9** (included with most CFW setups)

**Steps:**
1. Power on your 3DS and hold **Start** to boot into GodMode9
2. Navigate to `[C:] GAMECART` if you have a physical card inserted, or `[A:] SYSNAND SD` for installed titles
3. Select your game and choose **Copy to 0:/gm9/out**
4. The output is a `.3ds` file (encrypted) or use the **Decrypt** option for a decrypted `.cia`
5. Transfer the file to your computer via the SD card
6. Import into Provenance — see the [Nintendo 3DS Guide](../../info/system-guides/3ds.md) for compatible formats

</details>

### Nintendo DS

<details>
<summary><strong>Dumping DS cards via flashcard</strong></summary>

DS game cards require a flashcard (such as an R4) and a homebrew dumping tool on a DS or DSi.

{% hint style="warning" %}
DS card dumping via homebrew requires a homebrew-enabled DS/DSi. Refer to [dsi.cfw.guide](https://dsi.cfw.guide/) for setup guides.
{% endhint %}

**Steps:**
1. Enable homebrew on your DS/DSi using the guide above
2. Use a DS ROM dumping homebrew app (search GBAtemp for current tools)
3. Dump the card to your SD card as a `.nds` file
4. Transfer to your computer and import into Provenance

</details>

### PlayStation 2 (FreeMcBoot)

{% hint style="warning" %}
**PS2 support is in development** — PlayStation 2 emulation in Provenance is currently experimental and not fully available in stable releases. These instructions are provided for when PS2 support ships.
{% endhint %}

<details>
<summary><strong>Using FreeMcBoot + Open PS2 Loader (OPL)</strong></summary>

PS2 can dump disc images to a USB drive or network share using homebrew tools via a modded memory card.

**What you need:**
- PS2 console with **FreeMcBoot** memory card
- **Open PS2 Loader (OPL)** installed on the memory card
- USB drive (FAT32 formatted)

**Steps:**
1. Boot your PS2 with the FreeMcBoot memory card
2. Launch OPL from the FreeMcBoot menu
3. Insert your PS2 disc
4. Use OPL's **Install Game** feature to rip the disc to a USB drive or network share
5. The output is an `.iso` file
6. Transfer to your computer and import into Provenance (or convert to `.chd` — see [Format Conversion](#format-conversion))

</details>

### SNES / NES Classic (hakchi)

<details>
<summary><strong>Exporting ROMs from a Nintendo Classic Mini</strong></summary>

If you own a SNES Classic or NES Classic, you can export the pre-installed ROMs using **hakchi2 CE** or **hakchi** (a console mod tool).

**What you need:**
- SNES Classic or NES Classic console
- **hakchi2 CE** (Windows/macOS via Wine)
- USB cable (Micro-USB for NES Classic, USB-C for SNES Classic)

**Steps:**
1. Follow the hakchi2 CE setup guide to install custom firmware on your Classic console
2. Connect the console to your computer via USB
3. In hakchi2 CE, go to **Synchronize selected games** to view installed ROMs
4. Export the ROM files from the hakchi2 CE working directory (found in your Documents folder)
5. Import the exported ROMs into Provenance

{% hint style="info" %}
SNES Classic ROMs are standard `.sfc` files; NES Classic ROMs are standard `.nes` files — both work directly in Provenance.
{% endhint %}

</details>

---

## Save Data Dumping

Backing up save data lets you preserve progress from your original cartridges and memory cards.

### Game Boy / GBA Saves

| Tool | Method | Notes |
|------|--------|-------|
| **GB Operator** | Open Epilogue app → **Dump Save** | Easiest; saves as `.sav` |
| **GBxCart RW** | Open FlashGBX → **Read Save** | Open-source; supports all GB/GBC/GBA |

To use a dumped save in Provenance: place the `.sav` file in the same folder as your ROM with the same base filename (e.g., `Pokemon Red.gb` → `Pokemon Red.sav`).

### PS1 Memory Cards

<details>
<summary><strong>Using MemcardRex</strong></summary>

**MemcardRex** is a free tool for reading PS1 memory cards via a USB memory card reader.

**What you need:**
- PS1 memory card reader (e.g., a PS1-to-USB adapter)
- [MemcardRex](https://github.com/ShendoXT/memcardrex) (Windows/Linux via Wine)

**Steps:**
1. Connect your PS1 memory card reader to your computer
2. Open MemcardRex and select **Open Memory Card**
3. Choose your memory card reader device
4. MemcardRex reads the card and displays all save slots
5. Export individual saves as `.mcd` or the full card as a memory card image
6. Provenance can use these saves for PS1 games (place alongside the ROM)

</details>

### PlayStation 2 Saves

PS2 save data can be exported using **Open PS2 Loader (OPL)** or **uLaunchELF** on a FreeMcBoot-enabled console, then transferred via USB.

<details>
<summary><strong>Using uLaunchELF to copy saves</strong></summary>

1. Boot your PS2 with the FreeMcBoot memory card
2. Launch **uLaunchELF** from the FreeMcBoot menu
3. Navigate to `mc0:/` (Memory Card slot 1) or `mc1:/`
4. Find your save folder (named by game ID, e.g., `BASLUS-12345`)
5. Copy it to `mass:/` (USB drive) using the file manager
6. Transfer to your computer

</details>

### Nintendo 64 Saves

N64 saves are stored on the cartridge itself (SRAM or EEPROM) or on a Controller Pak (memory pak). Most cart dumpers also dump the save:

| Dumper | Save Method |
|--------|------------|
| INLretro | **Dump RAM** option dumps SRAM/EEPROM alongside the ROM |
| Retrode 2 | The mounted drive includes a `.srm` save file alongside the ROM |

Controller Pak saves require a dedicated tool — search GBAtemp for current N64 Controller Pak reader projects.

---

## Format Conversion

When you obtain disc images from your own physical media, they may not always be in a format that Provenance accepts directly. This section covers converting between common formats.

{% hint style="info" %}
**Already covered elsewhere:**
- CHD conversion (BIN/CUE → CHD): [Advanced ROM Management](advanced-management.md#chd-format-recommended)
- UnECM (.ecm file restoration): [Formatting ROMs](formatting-roms.md#unecm)
- Multi-file ROM archiving: [Formatting ROMs](formatting-roms.md#multi-file-roms)
{% endhint %}

### Quick Reference

| Source Format | Target Format | Tool | Platform | Notes |
|---|---|---|---|---|
| `.bin + .cue` | `.chd` | chdman | All | See [Advanced ROM Management](advanced-management.md#chd-format-recommended) |
| `.gdi` (Dreamcast) | `.chd` | chdman | All | `chdman createcd -i game.gdi -o game.chd` |
| `.iso` (CD / DVD) | `.chd` | chdman | All | CD: `chdman createcd -i game.iso -o game.chd` · DVD: `chdman createdvd -i game.iso -o game.chd` |
| `.nrg` (Nero) | `.iso` | nrg2iso | All | Free CLI tool |
| `.mdf + .mds` (Alcohol) | `.bin + .cue` (preferred) / `.iso` (data-only) | IsoBuster / mdf2iso | Win / All | Prefer BIN/CUE for mixed-mode or audio; use ISO only for pure data discs |
| `.cdi` (DiscJuggler) | `.gdi` | cdirip | All | Mainly for Dreamcast dumps |
| `.bin.ecm` | `.bin` | unecm | All | See [Formatting ROMs](formatting-roms.md#unecm) |
| `.pbp` (PSP game EBOOT) | — (no conversion) | — | All | PSP titles in `.pbp` can be used as-is |
| `.pbp` (PSX-on-PSP EBOOT) | `.bin + .cue` | PSX2PSP | Win | For PS1 games packaged as PSP EBOOTs |

### Format Reference Table

| System | Raw Dump Format | Recommended Provenance Format |
|--------|----------------|-------------------------------|
| PS1 | `.bin` + `.cue` | `.chd` |
| PS2 | `.iso` | `.chd` |
| PSP | `.iso` | `.iso` or `.cso` |
| GameCube | `.iso` | `.iso`, `.gcm`, `.gcz`, `.ciso` |
| Wii | `.iso` | `.iso` or `.wbfs` |
| Dreamcast | `.gdi` or `.cdi` | `.chd` |
| Sega CD | `.bin` + `.cue` | `.chd` |
| Saturn | `.bin` + `.cue` | `.chd` |

See [Formatting ROMs](formatting-roms.md) for the complete extension list for all systems.

---

### NRG → ISO (Nero Image Format)

Nero Burning ROM creates `.nrg` disc images that are not directly usable with Provenance. Use **nrg2iso** to convert them to standard ISO files.

**Install nrg2iso:**

{% tabs %}
{% tab title="macOS" %}
```bash
brew install nrg2iso
```
{% endtab %}
{% tab title="Linux" %}
```bash
sudo apt install nrg2iso
```
{% endtab %}
{% tab title="Windows" %}
Download from SourceForge: search "nrg2iso" and download the Windows binary.
{% endtab %}
{% endtabs %}

**Convert:**

```bash
nrg2iso game.nrg game.iso
```

After converting, you can import the `.iso` directly into Provenance, or convert it further to `.chd` for better compression (see [Advanced ROM Management](advanced-management.md#chd-format-recommended)).

---

### MDF/MDS → BIN/CUE (or ISO for data-only discs)

Alcohol 120% creates `.mdf` (image data) + `.mds` (metadata) pairs. For best compatibility, convert to `.bin + .cue` (then optionally to `.chd` for compression). Only convert to `.iso` if you are sure the disc is data-only (no CD audio tracks).

{% hint style="info" %}
Saturn and other mixed-mode CD dumps often come as `.mdf + .mds`. Keep both files in the same folder and, if you run into issues, convert the dump to a standard format like BIN/CUE or CHD.
{% endhint %}

**Option 1: IsoBuster (Windows, GUI)**

1. Open IsoBuster and load the `.mds` file
2. Right-click the disc icon → **Extract CD Image** → **Extract RAW**
3. Save as `.bin` — a `.cue` file is generated automatically

**Option 2: mdf2iso (Cross-platform CLI)**

```bash
mdf2iso game.mdf game.iso
```

mdf2iso converts the MDF/MDS pair to a standard `.iso` image. For CD-based games, use `createcd` to convert the ISO to CHD; for DVD-based games, use `createdvd`:

```bash
# Install chdman first (brew install rom-tools on macOS)

# CD-based ISO → CHD
chdman createcd -i game.iso -o game.chd

# DVD-based ISO → CHD
chdman createdvd -i game.iso -o game.chd
```

---

### CDI → GDI (DiscJuggler / Dreamcast)

DiscJuggler `.cdi` files are a proprietary Dreamcast disc format. Use **cdirip** to extract them into a GDI layout, which can then be converted to CHD.

**Install and run cdirip:**

```bash
# Download cdirip from its project page (cross-platform binary)
cdirip game.cdi
```

This outputs track files in GDI layout (a `.gdi` file plus `.raw`/`.bin` tracks). Then convert to CHD:

```bash
chdman createcd -i "game.gdi" -o "game.chd"
```

See [Advanced ROM Management](advanced-management.md#chd-format-recommended) for full chdman documentation.

---

### PBP (PSP EBOOT.PBP)

`.pbp` files come in two distinct types — handle them differently:

**PSP games (CFW backups)**

PSP games ripped from UMD typically produce `.iso` files. Provenance's PPSSPP core accepts both `.iso` and `.pbp` formats directly — no conversion needed.

**PSX-on-PSP titles**

Some PSP firmware allowed playing PS1 games packaged as `EBOOT.PBP`. These wrap a PS1 game inside a PSP container.

Recommended approach:

1. Import the `EBOOT.PBP` directly into Provenance **as a PlayStation game** (not as PSP/PPSSPP).

If a particular PSX-on-PSP `.pbp` does not work correctly when imported as a PlayStation title, you can extract the underlying PS1 disc image:

1. Use **PSX2PSP** (Windows) in reverse/extract mode
2. Point it at the `EBOOT.PBP`
3. Extract to `.bin + .cue`
4. Import the `.bin + .cue` (or convert to `.chd`) into Provenance as a PS1 game

{% hint style="warning" %}
Do not import PSX-on-PSP `.pbp` files as PSP games — the PPSSPP core will not run PS1 content correctly. Always treat them as PlayStation titles; only extract to `.bin + .cue` as a fallback if a specific `.pbp` has issues.
{% endhint %}

---

### GDI → CHD (Dreamcast)

GDI is the standard ripping format for Dreamcast discs. Convert to CHD for better compression and single-file convenience.

**Install chdman:**

{% tabs %}
{% tab title="macOS" %}
```bash
brew install rom-tools
```
{% endtab %}
{% tab title="Windows" %}
Download `chdman.exe` from the MAME project at mamedev.org.
{% endtab %}
{% endtabs %}

**Convert:**

```bash
chdman createcd -i "game.gdi" -o "game.chd"
```

For batch conversion of a folder of Dreamcast GDI dumps:

```bash
find . -type f -name '*.gdi' -print0 | while IFS= read -r -d '' f; do
  chdman createcd -i "$f" -o "${f%.gdi}.chd"
done
```

### Multi-Disc M3U Playlists

Games that span multiple discs (e.g., Final Fantasy VII) need an `.m3u` playlist file so Provenance can switch discs mid-game.

**Create an `.m3u` file** in the same folder as your disc images with one line per disc:

```
Final Fantasy VII (Disc 1).chd
Final Fantasy VII (Disc 2).chd
Final Fantasy VII (Disc 3).chd
```

Name the `.m3u` file after the game: `Final Fantasy VII.m3u`. Import the `.m3u` file into Provenance — it will appear as a single game entry.

See [Formatting ROMs](formatting-roms.md) for more details on multi-disc setup.

---

## After Dumping

Once you have your ROM files:

1. **Check the format** — Review [Formatting ROMs](formatting-roms.md) to confirm you have the correct file extension for your system
2. **Convert if needed** — CD-based games may need conversion to `.chd` for space savings (see [Advanced ROM Management](advanced-management.md))
3. **Import into Provenance** — See [Importing ROMs](importing-roms.md) for all import methods
4. **Check BIOS requirements** — Some systems need BIOS files — see [BIOS Requirements](../bios-requirements.md)

{% hint style="success" %}
Dumped ROMs from your own hardware are the highest quality source — no compression artifacts, correct region, and exact checksums. These will produce the best results in Provenance.
{% endhint %}

---

## Troubleshooting

<details>
<summary><strong>My dumper isn't recognized by my computer</strong></summary>

- Try a different USB cable (use a data cable, not a charge-only cable)
- Try a different USB port — avoid USB hubs for dumpers
- On macOS, check System Settings → Privacy & Security if the driver is blocked
- Install any required drivers from the manufacturer's site (some dumpers need CH340 or FTDI drivers)
- Restart your computer after installing drivers

</details>

<details>
<summary><strong>The ROM dump seems too small or is obviously wrong</strong></summary>

- The cartridge may have dirty contacts — clean with isopropyl alcohol (90%+) and a cotton swab, then retry
- Reseat the cartridge — remove and reinsert it firmly
- Some cartridges have battery-backed SRAM; the battery may be dead, but this shouldn't affect ROM dumping
- Verify the mapper setting if using the INLretro — an incorrect mapper produces garbled output

</details>

<details>
<summary><strong>The dumped ROM doesn't work in Provenance</strong></summary>

- Check that the file extension is correct for your system (see [Formatting ROMs](formatting-roms.md))
- Compare the file size against known-good values — a 4 MB SNES ROM should be exactly 4,194,304 bytes
- For CD-based games, ensure you have both the `.bin` and `.cue` files, or convert to `.chd`
- Try renaming the file to remove special characters — stick to alphanumeric names

</details>

<details>
<summary><strong>GB Operator / GBxCart shows "No cartridge detected"</strong></summary>

- Clean the cartridge contacts with isopropyl alcohol
- Ensure the cartridge is fully inserted and seated
- Try a different USB port or cable
- Some aftermarket or bootleg cartridges may not be recognized — official Nintendo cartridges should always work

</details>

---

## See Also

- [Importing ROMs](importing-roms.md) — How to get your dumped ROMs into Provenance
- [Formatting ROMs](formatting-roms.md) — Correct file formats for every system
- [BIOS Requirements](../bios-requirements.md) — BIOS files needed for certain systems
- [Advanced ROM Management](advanced-management.md) — CHD conversion, organizing large libraries
- [Game Saves](../../info/saves.md) — Managing save files and save states in Provenance
- [Nintendo 3DS Guide](../../info/system-guides/3ds.md) — 3DS-specific setup in Provenance
- [GameCube & Wii Guide](../../info/system-guides/gamecube-wii.md) — Dolphin folder structure for GameCube/Wii ROMs

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
