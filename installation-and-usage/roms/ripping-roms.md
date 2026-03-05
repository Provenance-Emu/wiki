---
description: How to legally dump ROMs, disc images, and save data from your own physical media
---

# Ripping ROMs

{% hint style="danger" %}
Dumping ROMs from media you own is legal in many jurisdictions. Downloading ROMs for games you do not own is not covered by this guide. Always check the laws in your region.
{% endhint %}

This guide covers methods to dump game data directly from physical cartridges, discs, and memory cards you own. Methods are organized by hardware approach.

---

## Cart Ripping

Cartridge-based games can be dumped using dedicated USB cart readers connected to a PC.

### Game Boy / GBA

* **GB Operator** (Epilogue) — plug-and-play USB reader; companion software handles dumping and save backup. Output: `.gb`, `.gbc`, `.gba`
* **GBxCart RW** (insideGadgets) — open-source reader/writer for GB, GBC, GBA; supports save read/write. Output: `.gb`, `.gbc`, `.gba`
* **Joey Jr** (BennVenn) — budget-friendly GBA reader. Output: `.gba`

### SNES / NES / Genesis

* **Retrode 2** — USB adapter supporting SNES and Genesis cartridges natively; NES, N64, and other adapters available separately. Output: `.sfc`, `.smc`, `.gen`, `.bin`
* **INLretro** — programmer/dumper board supporting many systems including NES, SNES, Genesis, and more. Output varies by system.

### Nintendo DS

* **NDS Backup Tool** via flashcart — run on original DS hardware to dump to microSD.
* **dumpTool** — open-source NDS dumping homebrew. Output: `.nds`

---

## Disc Ripping

Optical discs require either a standard PC optical drive (for some formats) or console-side homebrew.

### PS1 / PS2

* Any standard PC CD/DVD drive + **ImgBurn** or **CloneCD** — rip directly to `.bin`/`.cue` or `.iso`

### GameCube / Wii — CleanRip

1. Install the **Homebrew Channel** on your Wii
2. Download **CleanRip** and place it on an SD card
3. Launch CleanRip via HBC
4. Select output destination (SD or USB)
5. Insert disc and follow on-screen prompts
6. Output: `.iso` (GameCube), `.iso` (Wii)

See [GameCube & Wii Guide](../../info/system-guides/gamecube-wii.md) for folder structure requirements.

### Dreamcast — GD-ROM Dumping

Dreamcast GD-ROM discs require a two-step process:

1. **GDEmu ODE method** — use a GDEmu or similar optical drive emulator device to dump via `GDmenu` or similar homebrew
2. **Broadband Adapter + httpd-ism method** — use a broadband adapter and the `httpd-ism` FTP homebrew to dump over network (see [Network / Softmod Ripping](#network--softmod-ripping) below)

Output: `.gdi` + track files, or `.chd`

### PSP UMD — PC Method

Standard PC optical drives cannot read UMD discs. Use the [PSP CFW method](#psp--custom-firmware) in the Network section below.

---

## Network / Softmod Ripping

{% hint style="warning" %}
These methods require modifying or exploiting your console's software. Refer to community guides for custom firmware installation. This guide only covers the ROM dumping step after homebrew is in place.
{% endhint %}

Some consoles can dump their own media using homebrew software and networking or USB storage — no specialized PC hardware needed.

### PS2 + FreeMcBoot + OPL

**Prerequisites:** PS2 with FreeMcBoot memory card, OPL installed, Ethernet connection and PC with SMB shared folder.

**Method A — ETH Disc Dump via OPL:**

1. Boot your PS2 with the FreeMcBoot memory card inserted
2. Launch **OPL** (Open PS2 Loader)
3. Go to **Settings → ETH Settings** and configure your network/SMB share
4. Navigate to **Apps** or use the disc dump option in OPL's menu
5. Insert the PS2 disc and select "ETH disc dump"
6. OPL streams the disc image directly to your PC's shared folder
7. Output: `.iso`

**Method B — USB via uLaunchELF:**

1. Boot FreeMcBoot and launch **uLaunchELF**
2. Navigate to `cdrom0:/` (the disc drive)
3. Copy the disc contents to `mass:/` (USB storage)
4. Transfer the USB drive to your PC
5. Output: `.iso`

### Dreamcast + Broadband Adapter

The Dreamcast broadband adapter combined with FTP homebrew allows network-based disc dumping. See the [Disc Ripping — Dreamcast GD-ROM section](#dreamcast--gd-rom-dumping) above for the full method, which also covers the network/FTP approach.

### Wii + Homebrew Channel

The Wii Homebrew Channel enables two disc-dumping methods:

* **CleanRip** — see the [Disc Ripping — GameCube / Wii section](#gamecube--wii--cleanrip) above for full instructions
* **USB Loader GX** — can dump Wii and GameCube discs directly to a USB drive:
  1. Launch USB Loader GX from the Homebrew Channel
  2. Insert disc
  3. Select the game and choose **Install** or **Dump**
  4. Wii discs output as `.wbfs`; GameCube discs output as `.iso`

See [GameCube & Wii Guide](../../info/system-guides/gamecube-wii.md) for Dolphin folder structure requirements.

### PSP + Custom Firmware

**Prerequisites:** PSP with custom firmware installed (6.61 PRO-C or LME recommended).

**Method A — Recovery Menu ISO Dump:**

1. Hold **R** while booting to enter the CFW Recovery Menu
2. Navigate to **Tools → Create ISO from UMD**
3. Insert the UMD disc and confirm
4. The ISO is written to your Memory Stick Duo (`ms0:/ISO/`)
5. Connect PSP to PC via USB; copy the `.iso` file
6. Output: `.iso`

**Method B — FTP over Wi-Fi:**

1. Enable the FTP server in your CFW (location varies; common in PRO/LME plugins or apps like **FTPhost**)
2. Connect from your PC using an FTP client (e.g., FileZilla) using the PSP's IP address shown on screen
3. Navigate to `disc0:/` to browse the mounted UMD
4. Download all files to your PC
5. Output: folder of disc contents; use **UMDGen** or **PSP ISO Tools** to repack as `.iso` if needed

{% hint style="info" %}
PSX-on-PSP games use the `.eboot.pbp` format. Provenance natively supports `.pbp` files for PlayStation, so you may be able to use them directly. If a `.pbp` file does not load correctly, convert it back to a standard disc image (`.iso` or `.bin/.cue`) using tools such as **PSP ISO Tools** on your computer.
{% endhint %}

### Original Xbox (Softmod)

Softmodded original Xbox consoles running a custom dashboard (Avalaunch, EvoX, UnleashX) expose an FTP server on the local network:

1. Note the IP address shown in the dashboard network settings
2. Connect from a PC FTP client
3. Browse to the game partition (typically `E:\Games\` or `F:\Games\`)
4. Copy game folders to your PC

{% hint style="info" %}
Original Xbox emulation is **not supported** in Provenance. This method is documented for collection archiving and preservation purposes only.
{% endhint %}

---

## Save Data Dumping

{% hint style="success" %}
Provenance uses standard save formats (`.sav`, `.mcr`, `.srm`, `.eep`) compatible with other emulators. Saves dumped from real hardware work directly. See [Game Saves](../../info/saves.md) for import instructions.
{% endhint %}

Transfer existing save data from physical memory cards and cartridges to Provenance.

### GB / GBC / GBA Saves

The same cart readers used for ROM dumping (GB Operator, GBxCart RW, Joey Jr) also read and write save data:

* All three readers dump the save RAM alongside or separately from the ROM
* Use the companion software to export the save file before transferring the ROM to Provenance
* Output: `.sav`

{% hint style="warning" %}
Back up your saves before transferring. Old cartridge batteries may fail during the read process. Some carts (especially GBA) have aging batteries — if the cart reader reports a blank save, the battery may have already died.
{% endhint %}

### PlayStation Memory Cards

**Method A — PS3 + Memory Card Adaptor:**

The official Sony Memory Card Adaptor (model CECHMCA) lets a PS3 read PS1/PS2 memory cards:

1. Insert the PS1/PS2 memory card into the adaptor and plug into a PS3
2. Copy saves using the PS3's **Saved Data Utility**
3. Transfer the save data to PC and use tools such as **PSXMemTool** or **MemcardRex** to extract individual saves and convert to `.mcr`

**Method B (Recommended) — FreeMcBoot + uLaunchELF:**

<details>
<summary><strong>Step-by-step: Dump PS1/PS2 memory card with FreeMcBoot</strong></summary>

1. Boot your PS2 with the FreeMcBoot memory card and launch **uLaunchELF**
2. Navigate to `mc0:/` for Memory Card 1 or `mc1:/` for Memory Card 2
3. Select all save folders you want to back up
4. Copy them to `mass:/` (USB drive) using the file manager
5. On your PC, use **MemcardRex** (Windows) or **mymc** (cross-platform) to open the memory card image or individual save folders
6. Export saves to `.mcr` format (Provenance compatible)

</details>

Output: `.mcr`

See [Game Saves](../../info/saves.md) for instructions on importing `.mcr` files into Provenance.

### GameCube Memory Cards

**GCMM (GameCube Memory Manager)** homebrew running on a Wii can back up GameCube memory cards to SD card:

1. Install **GCMM** via the Homebrew Channel on your Wii
2. Insert an SD card and launch GCMM from HBC
3. Insert your GameCube memory card into Slot A or Slot B
4. Select **Backup All** to export all saves
5. GCMM saves individual `.gci` files (one per game save) or a full memory card image to the SD card
6. Copy the SD card files to your PC, then import into Provenance

Output: `.gci` files or full memory card image

See [GameCube & Wii Guide](../../info/system-guides/gamecube-wii.md) for information on Dolphin's save and folder structure.

### N64 Controller Pak

N64 Controller Pak (memory pak) saves require a cart reader with a Controller Pak adapter:

* **Retrode 2 + N64 Adapter** — insert the Controller Pak into the Retrode's controller port; it appears as a readable file on your PC. Output: `.mpk`
* **INLretro + N64 Adapter** — similar approach using the INLretro programmer's N64 controller port adapter. Output: `.mpk`

---

## See Also

* [Formatting ROMs](formatting-roms.md) — converting between disc image formats (e.g., `.chd`, `.bin`/`.cue`, `.ecm`)
* [Importing ROMs](importing-roms.md) — getting ROMs into Provenance
* [Game Saves](../../info/saves.md) — managing and importing save data
* [GameCube & Wii Guide](../../info/system-guides/gamecube-wii.md) — Dolphin folder structure

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
