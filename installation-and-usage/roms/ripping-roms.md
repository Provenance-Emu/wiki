---
description: How to legally dump your own cartridges and discs for use in Provenance
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

### Choosing a Dumper

Different hardware covers different systems. Below is a quick-reference table of popular, accessible dumpers.

| Dumper | Supported Systems | Price Range | Notes |
|--------|------------------|-------------|-------|
| **GB Operator** (Epilogue) | Game Boy, GBC, GBA | ~$50 | macOS/Windows/Linux, also backs up saves |
| **GBxCart RW** (insideGadgets) | Game Boy, GBC, GBA | ~$30–$45 | Open-source firmware, flash cart support |
| **Retrode 2** | SNES, Genesis/Mega Drive, N64\*, Game Gear, SMS | ~$80+ (used) | USB plug-and-play, adapters available |
| **INLretro Dumper** | NES, SNES, N64, Game Boy, Genesis, and more | ~$60–$90 | Widest system support, open-source |
| **64drive** | Nintendo 64 | ~$100+ | Also a flash cart; dumping via PC software |
| **Krikzz Dumper** | Various | Varies | From the maker of Everdrive flash carts |

\*N64 support on Retrode 2 requires the optional N64 adapter.

{% hint style="info" %}
**Recommendation for beginners:** The **GB Operator** is the easiest option for Game Boy/GBC/GBA — plug in, launch the app, click Dump. For multi-system coverage, the **INLretro Dumper** offers the broadest support.
{% endhint %}

---

### Game Boy / Game Boy Color / Game Boy Advance

<details>
<summary><strong>Using the GB Operator (Epilogue) — Easiest Method</strong></summary>

The GB Operator is a USB device that reads GB, GBC, and GBA cartridges directly on macOS, Windows, and Linux.

**What you need:**
- GB Operator device
- [Epilogue app](https://www.epilogue.co/operator) (free download)
- A USB-C or USB-A port on your computer

**Steps:**
1. Download and install the Epilogue app from epilogue.co
2. Insert your cartridge into the GB Operator slot
3. Connect the GB Operator to your computer via USB
4. Open the Epilogue app — your cartridge details appear automatically
5. Click **Dump ROM** and choose a save location
6. Wait for the dump to complete (usually under a minute)
7. The resulting `.gb`, `.gbc`, or `.gba` file is ready to import into Provenance

**Save backup:** The Epilogue app can also dump your in-game save data. Use **Dump Save** to back it up before dumping — useful for preserving Pokémon saves.

</details>

<details>
<summary><strong>Using GBxCart RW (insideGadgets) — Budget Option</strong></summary>

The GBxCart RW is an open-source USB flasher/dumper for GB, GBC, and GBA.

**What you need:**
- GBxCart RW device
- [FlashGBX software](https://github.com/lesserkuma/FlashGBX) (free, cross-platform)

**Steps:**
1. Install FlashGBX on your computer
2. Insert your cartridge into the GBxCart RW
3. Connect via USB to your computer
4. Open FlashGBX — the cartridge is detected automatically
5. Select **Read ROM** and choose an output folder
6. Click **Start** and wait for the dump to complete
7. Import the `.gb`, `.gbc`, or `.gba` file into Provenance

</details>

---

### NES / Famicom

<details>
<summary><strong>Using the INLretro Dumper</strong></summary>

The INLretro Dumper supports NES, Famicom, and many other cartridge types through swappable adapters.

**What you need:**
- INLretro Dumper with NES adapter
- [INLretro software](https://www.infiniteneslives.com/inlretro.php) (Windows; runs under Wine on macOS/Linux)

**Steps:**
1. Attach the NES cartridge adapter to the INLretro board
2. Insert your NES cartridge
3. Connect the device to your computer via USB
4. Open the INLretro software
5. Select **NES** as the system and choose the appropriate mapper (auto-detect works for most common games)
6. Click **Dump ROM** and select an output location
7. The resulting `.nes` file is ready for Provenance

{% hint style="info" %}
The INLretro software includes a mapper database. If auto-detect fails, look up the mapper for your specific game on [NESdev Wiki](https://www.nesdev.org/).
{% endhint %}

</details>

---

### SNES / Super Famicom

<details>
<summary><strong>Using the Retrode 2</strong></summary>

The Retrode 2 mounts SNES (and Genesis) cartridges as a USB mass storage device — no software install required on modern operating systems.

**What you need:**
- Retrode 2

**Steps:**
1. Insert your SNES cartridge into the top slot of the Retrode 2
2. Connect the Retrode 2 to your computer via USB
3. Your computer mounts the Retrode as a drive
4. Open the drive — you will see a `.smc` or `.sfc` file representing your ROM
5. Copy this file to your computer
6. Import into Provenance

</details>

<details>
<summary><strong>Using the INLretro Dumper</strong></summary>

1. Attach the SNES adapter to the INLretro board
2. Insert your SNES cartridge
3. Open the INLretro software
4. Select **SNES** as the system
5. Click **Dump ROM** and wait for completion
6. Import the `.smc` or `.sfc` file into Provenance

</details>

---

### Sega Genesis / Mega Drive

<details>
<summary><strong>Using the Retrode 2</strong></summary>

Genesis cartridges are supported natively in the Retrode 2's bottom slot.

**Steps:**
1. Insert your Genesis cartridge into the large bottom slot
2. Connect the Retrode 2 to your computer via USB
3. Open the mounted drive on your computer
4. Copy the `.md` or `.bin` ROM file to your computer
5. Rename the extension to `.md` if needed for Provenance compatibility
6. Import into Provenance

</details>

---

### Nintendo 64

<details>
<summary><strong>Using the INLretro Dumper with N64 Adapter</strong></summary>

N64 cartridges use a 64-pin edge connector and require a dedicated adapter.

**What you need:**
- INLretro Dumper with N64 adapter
- INLretro software

**Steps:**
1. Attach the N64 adapter to the INLretro board
2. Insert your N64 cartridge
3. Open the INLretro software and select **N64**
4. Click **Dump ROM** — N64 dumps are larger (8–64 MB) and take several minutes
5. The output file is a `.z64` (big-endian) ROM, which is the preferred format for Provenance
6. Import into Provenance

{% hint style="warning" %}
N64 ROMs come in three byte-order formats: `.z64` (big-endian), `.v64` (byte-swapped), and `.n64` (little-endian). Provenance supports `.z64` and `.n64`; `.z64` is the standard. If your dumper produces `.v64`, convert it to `.z64` or `.n64` with [Tool64](https://github.com/jkbenaim/tool64) or similar utilities before importing into Provenance.
{% endhint %}

</details>

<details>
<summary><strong>Using the Retrode 2 with N64 Adapter</strong></summary>

The optional N64 plug-in adapter for Retrode 2 allows cartridge dumping via USB mass storage, similar to SNES.

**Steps:**
1. Attach the N64 adapter plug-in to the Retrode 2
2. Insert your N64 cartridge
3. Connect to your computer — the Retrode mounts as a drive
4. Copy the ROM file from the drive
5. Import into Provenance

</details>

---

### Game Boy Advance (Additional Detail)

GBA ROMs dump as `.gba` files. If you have save data on the cartridge you want to preserve:

| Action | GB Operator | GBxCart RW |
|--------|-------------|------------|
| Dump ROM | Yes | Yes |
| Dump save | Yes | Yes |
| Write save back | Yes | Yes |
| Flash ROM back | No | Yes |

To use an existing GBA save with Provenance, dump the `.sav` file and place it in the same directory as your `.gba` file with the same base filename before importing.

---

### Other Cartridge Systems

| System | Recommended Dumper | Notes |
|--------|--------------------|-------|
| **Game Gear** | Retrode 2 + SMS/GG adapter | Shares hardware with SMS |
| **Sega Master System** | Retrode 2 + SMS/GG adapter | |
| **Atari 2600 / 7800** | INLretro Dumper | Atari adapters available |
| **TurboGrafx-16 / PC Engine** | INLretro Dumper + HuCard adapter | |
| **Neo Geo Pocket** | Specialized dumpers (limited availability) | Community-built options exist |
| **WonderSwan** | Specialized community dumpers | Rare hardware |

---

## Disc Ripping

CD and DVD-based systems require different methods. In most cases, you rip directly from the disc using a computer's optical drive or via the game console itself.

{% hint style="info" %}
See [Formatting ROMs](formatting-roms.md) for the correct file formats to use with Provenance after ripping.
{% endhint %}

**Quick overview by system:**

| System | Method | Output Format |
|--------|--------|---------------|
| PlayStation (PS1) | PC optical drive + ImgBurn | `.bin` + `.cue` or `.chd` |
| PlayStation 2 | PC optical drive + ImgBurn | `.iso` or `.chd` |
| PSP | PC optical drive or console dump | `.iso` or `.cso` |
| GameCube | Wii console + CleanRip, or PC + Dolphin | `.iso` |
| Wii | Wii console + CleanRip | `.iso` or `.wbfs` |
| Dreamcast | GD-ROM Loader on console, or specialized drive | `.gdi` or `.chd` |
| Sega CD | PC optical drive + ImgBurn | `.bin` + `.cue` or `.chd` |

### PlayStation 1 / PlayStation 2 / Sega CD / Saturn

<details>
<summary><strong>Using ImgBurn (Windows) — Recommended</strong></summary>

**ImgBurn** is a free Windows disc imaging tool that produces `.bin`+`.cue` files compatible with Provenance.

**What you need:**
- A computer with a DVD/CD optical drive
- [ImgBurn](https://www.imgburn.com/) (free, Windows)

**Steps:**
1. Insert your game disc into your optical drive
2. Open ImgBurn and select **Create image file from disc**
3. Set the destination folder and filename
4. Click the **Read** button — ImgBurn reads the disc and creates the image
5. For PS1/Sega CD: ImgBurn produces a `.bin` + `.cue` pair — keep both files together
6. For PS2: ImgBurn produces an `.iso` file
7. Import into Provenance (or convert to `.chd` — see [Format Conversion](#format-conversion))

</details>

<details>
<summary><strong>Using cdrdao (macOS / Linux)</strong></summary>

**cdrdao** is a command-line tool for ripping CD-based games. It produces accurate `.bin`+`.cue` pairs.

**Install:** `brew install cdrdao` (macOS) or `sudo apt install cdrdao` (Linux)

**Steps:**
1. Insert your game disc
2. Find your drive device: `cdrdao scanbus`
3. Rip the disc: `cdrdao read-cd --read-raw --datafile game.bin --device /dev/cdrom game.cue`
4. The output `.bin` + `.cue` pair is ready to import into Provenance

</details>

<details>
<summary><strong>Using ddrescue for damaged discs (macOS / Linux)</strong></summary>

**ddrescue** is useful when a disc has scratches and a standard rip fails. It retries bad sectors and logs progress.

**Install:** `brew install ddrescue` (macOS) or `sudo apt install gddrescue` (Linux)

**Steps:**
1. Insert the disc
2. Run: `ddrescue -d -r3 /dev/cdrom game.iso game.log`
3. ddrescue will retry damaged sectors up to 3 times
4. The resulting `.iso` can be imported into Provenance (PS2) or converted to `.chd`

</details>

### GameCube / Wii

<details>
<summary><strong>Using CleanRip on a Wii</strong></summary>

**CleanRip** is a homebrew tool for the Wii that dumps GameCube and Wii discs directly to an SD card or USB drive.

**What you need:**
- A Wii with the Homebrew Channel installed
- [CleanRip](https://github.com/emukidid/cleanrip) installed via the Homebrew Channel
- SD card or USB drive (FAT32 formatted, 8 GB+ for Wii discs)

**Steps:**
1. Insert the game disc and launch CleanRip from the Homebrew Channel
2. Select your output device (SD card or USB)
3. Choose **Yes** to use a database for verification
4. Select the disc type (GameCube or Wii) and region
5. CleanRip dumps the disc — GameCube takes ~20 minutes; Wii discs can take 60+ minutes
6. Transfer the `.iso` from your SD/USB to your computer and import into Provenance

See the [GameCube & Wii Guide](../../info/system-guides/gamecube-wii.md) for Dolphin folder structure.

</details>

### Dreamcast

<details>
<summary><strong>Using GD-ROM Loader on a Dreamcast</strong></summary>

Dreamcast games use GD-ROM discs, which require a Dreamcast console running a GD-ROM emulator/loader or a specialized PC GD-ROM drive to dump.

**GD-ROM Loader method (via Dreamcast):**
1. Use a Dreamcast running Dreamshell or similar homebrew
2. Insert the GD-ROM game disc
3. Dump the disc to an SD card as a `.gdi` image
4. Transfer to computer and import (or convert to `.chd`)

**Output format:** `.gdi` (three-file set: `.gdi` + `.raw`/`.iso` tracks) — recommended to convert to `.chd` to keep as a single file.

</details>

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
| `.mdf + .mds` (Alcohol) | `.iso` | IsoBuster / mdf2iso | Win / All | mdf2iso outputs `.iso`; IsoBuster can also convert to `.bin + .cue` |
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
for f in */*.gdi; do chdman createcd -i "$f" -o "${f%.gdi}.chd"; done
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
