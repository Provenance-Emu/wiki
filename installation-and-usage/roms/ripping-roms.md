---
description: How to legally dump ROMs, disc images, and save data from your own physical game collection for use in Provenance.
---

# Ripping ROMs

{% hint style="warning" %}
Only dump games you own. Downloading ROMs you do not own physical copies of may be illegal in your jurisdiction. This guide is for preservation of your own collection.
{% endhint %}

This guide covers four methods for getting game data off physical media:

1. **Cart Readers** — hardware adapters for cartridge-based systems
2. **Disc Ripping** — optical disc dumping with a PC optical drive or console homebrew
3. **Network / Softmod Ripping** — console homebrew that dumps over a network or to USB
4. **Save Data Dumping** — transferring real save files to Provenance

---

## 1. Cart Readers

Cartridge readers connect to your PC via USB and allow you to dump ROM data and save files directly.

### GB / GBC / GBA

| Device | Notes |
|---|---|
| **GB Operator** (Epilogue) | macOS/Windows app, plug-and-play, dumps ROM + save |
| **GBxCart RW** (insideGadgets) | Open-source, cross-platform, supports GB/GBC/GBA |
| **Joey Jr** (BennVenn) | Budget option, GB/GBC/GBA, USB |

Output: `.gb`, `.gbc`, `.gba` (ROM); `.sav` (save)

### NES / SNES / Genesis / N64 / and more

| Device | Notes |
|---|---|
| **Retrode 2** | Supports SNES, Genesis natively; adapters for NES, N64, GB, GBA, and more |
| **INLretro** | Supports a wide range of cartridge pinouts; open-source software |
| **Krikzz Dumper** | Focused on Genesis/Mega Drive and SNES |

Output: `.nes`, `.sfc`, `.md`, `.z64`, etc. depending on system

### GBA (PC-only alternative)

**EZ-Flash Omega** or similar flash carts can be used to copy a real cart to the flash cart's SD card on-device, though a dedicated cart reader is more reliable.

---

## 2. Disc Ripping

### PlayStation 1 & 2 (PC optical drive)

Most PS1/PS2 discs can be ripped with a standard PC DVD drive:

1. Insert disc into your PC's optical drive.
2. Use **ImgBurn** (Windows) or **cdrdao** (macOS/Linux) to create a full disc image.
3. For PS1, output a **`.bin` + `.cue`** pair (multi-track) rather than a single `.iso`.
4. For PS2, a single `.iso` is acceptable.

Output: `.bin`/`.cue` (PS1), `.iso` (PS2)

{% hint style="info" %}
PS1 games with multiple tracks (audio CDs) require `.bin`/`.cue`. A single-file `.iso` will be missing the audio tracks.
{% endhint %}

### Dreamcast (GD-ROM)

GD-ROMs use a proprietary high-density format that standard PC drives cannot read fully. Options:

- **Redump-compatible GD-ROM rip**: Use a compatible Plextor or Kreon drive with **DiscImageCreator** following the [Redump Dreamcast guide](http://wiki.redump.org/index.php?title=Dreamcast_Dumping_Guide). Output: GDI + track files.
- **Dreamcast Broadband Adapter method**: See [Network / Softmod Ripping](#3-network--softmod-ripping) below.

Output: `.gdi` + track bin files (preferred), or `.cdi`

### GameCube & Wii (CleanRip)

**CleanRip** is a Wii homebrew app that rips GameCube and Wii discs using the console's own drive — the most reliable method for these formats.

1. Install the **Homebrew Channel** on your Wii.
2. Download **CleanRip** and place it on an SD card.
3. Launch CleanRip from the Homebrew Channel.
4. Insert the disc and follow the on-screen prompts to dump to SD or USB.

Output: `.iso` (GameCube), `.iso` (Wii — can be converted to `.wbfs`)

See [GameCube & Wii guide](../../info/system-guides/gamecube-wii.md) for Dolphin folder structure in Provenance.

### PSP (UMD)

See [Network / Softmod Ripping — PSP](#psp--custom-firmware) below.

---

## 3. Network / Softmod Ripping

{% hint style="warning" %}
These methods require modifying or exploiting your console's software. Refer to community guides for custom firmware installation. This guide only covers the ROM dumping step after homebrew is in place.
{% endhint %}

Some consoles can dump their own media using homebrew software and networking or USB storage — no specialized PC hardware needed.

### PS2 + FreeMcBoot + OPL

**Prerequisites:** PS2 with FreeMcBoot memory card, Open PS2 Loader (OPL) installed, Ethernet adapter and SMB share on your PC, or USB storage.

**Method A — ETH disc dump via OPL:**

1. Boot your PS2 with the FreeMcBoot memory card inserted.
2. Launch **OPL** from the FreeMcBoot menu.
3. Go to **Settings → ETH Settings** and configure your PC's SMB share.
4. Insert the PS2 disc.
5. From the OPL main menu select **ETH disc dump** and follow the prompts.
6. The disc image is written directly to your PC's shared folder.

**Method B — USB via uLaunchELF:**

1. From FreeMcBoot, launch **uLaunchELF**.
2. Navigate to `cdfs:/` (the inserted disc).
3. Copy the contents to `mass:/` (USB storage).

Output: `.iso`

### Dreamcast + Broadband Adapter

For Dreamcast disc ripping using the console's own networking hardware, see the **Dreamcast (GD-ROM)** entry in [Disc Ripping](#2-disc-ripping) above for the recommended PC-based GD-ROM rip workflow. The Broadband Adapter can be used with tools like **dcload-ip** to transfer data over FTP once a GD-ROM rip is complete.

### Wii + Homebrew Channel

**CleanRip** (covered in [Disc Ripping](#2-disc-ripping) above) is the standard method for ripping Wii and GameCube discs.

**Alternatively — USB Loader GX:**

1. Install **USB Loader GX** via the Homebrew Channel.
2. Insert a USB hard drive.
3. Insert the disc and use USB Loader GX's built-in **Install** function to dump the disc to USB storage.

Output: `.wbfs` (Wii) or `.iso` (GameCube)

### PSP + Custom Firmware

**Prerequisites:** PSP with custom firmware — 6.61 PRO-C or LME recommended.

**Method A — Create ISO from UMD (Memory Stick):**

1. Power on your PSP with CFW loaded.
2. Access the **Recovery Menu** (hold `R` while booting, or via VSH menu).
3. Select **"Create ISO from UMD"** (location varies by CFW).
4. Wait for the dump to complete — the `.iso` is saved to `ms0:/ISO/`.
5. Connect PSP to PC via USB (Settings → USB Connection) and copy the file.

**Method B — FTP over Wi-Fi:**

1. Enable the built-in FTP server in your CFW's settings or install a homebrew FTP app (e.g., **FTPD**).
2. Connect from your PC using an FTP client (FileZilla, Cyberduck, etc.) to the IP shown on your PSP screen.
3. Navigate to `disc0:/` to access the UMD contents, or `ms0:/ISO/` if you already dumped with Method A.
4. Download the `.iso`.

Output: `.iso`

{% hint style="info" %}
PSX-on-PSP games (PSOne Classics) are in `.pbp` format. These require conversion or can be loaded directly — see [Formatting ROMs](formatting-roms.md) for details.
{% endhint %}

### Original Xbox (Softmod)

{% hint style="info" %}
Original Xbox emulation is **not supported** in Provenance. This section is included for collection archiving purposes only.
{% endhint %}

With a softmodded Xbox running a custom dashboard (Avalaunch, EvoX, UnleashX):

1. Configure FTP access in the dashboard settings.
2. Connect from your PC with an FTP client using the Xbox's local IP.
3. Browse the **E:/** or **F:/** game partitions.
4. Copy the game folder to your PC.

---

## 4. Save Data Dumping

Transfer existing save data from physical memory cards and cartridges into Provenance.

{% hint style="success" %}
Provenance uses standard save formats (`.sav`, `.mcr`, `.srm`, `.eep`) compatible with other emulators. Saves dumped from real hardware work directly. See [Game Saves](../../info/saves.md) for import instructions.
{% endhint %}

### GB / GBC / GBA Saves

The same cart readers listed in [Section 1 — Cart Readers](#1-cart-readers) (GB Operator, GBxCart RW, Joey Jr) all support dumping and restoring save data alongside ROMs.

- Insert the cartridge and use the device's companion software to **back up save data**.
- Output: `.sav`

{% hint style="warning" %}
Back up saves **before** transferring. Old cartridge batteries can fail at any time — a dead battery means your save is gone forever. Dump it now.
{% endhint %}

### PlayStation Memory Cards

**Method A — PS3 + Memory Card Adaptor (CECHMCA):**

1. Insert your PS1 memory card into the official Sony Memory Card Adaptor (model CECHMCA).
2. Plug the adaptor into a PS3 and copy saves to the PS3's internal storage.
3. On PC, use **MemcardRex** (Windows) or **mymc** to extract individual saves as `.mcr`.

**Method B (recommended) — FreeMcBoot + uLaunchELF:**

<details><summary><strong>Step-by-step: Copy PS1 saves to USB with uLaunchELF</strong></summary>

1. Boot your PS2 with the FreeMcBoot memory card inserted.
2. Launch **uLaunchELF** from the FreeMcBoot menu.
3. Press **Circle** (or the configured button) to open the file browser.
4. Navigate to **mc0:/** for Memory Card slot 1, or **mc1:/** for slot 2.
5. Select the save folder(s) you want to back up.
6. Press **R1** to open the copy menu and copy to **mass:/** (USB drive).
7. On your PC, open the copied files with **MemcardRex** (Windows) or **mymc** (cross-platform) to convert to `.mcr` format.

</details>

Output: `.mcr` (Provenance compatible)

See [Game Saves](../../info/saves.md) for how to import `.mcr` files into Provenance.

### GameCube Memory Cards

**GCMM (GameCube Memory Manager)** is a Wii homebrew app that backs up GameCube memory card contents to SD card.

1. Install the Homebrew Channel on your Wii.
2. Download **GCMM** and place it on your SD card.
3. Launch GCMM from the Homebrew Channel.
4. Insert your GameCube memory card into Slot A or Slot B.
5. Select **"Backup All"** — saves are written to your SD card.

Output: Individual `.gci` files or a full memory card image (`.raw`)

See [GameCube & Wii guide](../../info/system-guides/gamecube-wii.md) for how Provenance/Dolphin organizes GameCube save data.

### N64 Controller Pak

The N64 Controller Pak (memory pak) stores saves for games that don't use cartridge SRAM. Dump it with:

- **Retrode 2 + N64 adapter**: Insert the Controller Pak into the Retrode's controller port with the N64 adapter attached. It appears as a readable file on your PC.
- **INLretro + N64 adapter**: Similar approach — use the INLretro software to read the Controller Pak.

Output: `.mpk` files

---

## See Also

- [Formatting ROMs](formatting-roms.md) — file format conversion and naming
- [Importing ROMs](../importing-roms.md) — how to get files into Provenance
- [Game Saves](../../info/saves.md) — managing save files in Provenance
- [GameCube & Wii Guide](../../info/system-guides/gamecube-wii.md)
- [BIOS Requirements](../bios-requirements.md)

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
