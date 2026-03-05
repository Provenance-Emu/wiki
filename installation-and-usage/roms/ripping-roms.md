---
description: How to legally dump ROMs, disc images, and save data from physical media you own.
---

# Ripping ROMs from Physical Media

{% hint style="danger" %}
**Legal notice.** Dumping games you own for personal use is generally considered fair use. Sharing dumps online, downloading dumps you don't own, or distributing copyrighted files violates copyright law. This guide covers only backing up physical media you own. Provenance and its contributors take no responsibility for illegal use.
{% endhint %}

**Quick links:** [Cartridge Dumping](#cartridge-dumping) | [Disc Ripping](#disc-ripping) | [Network / Softmod Ripping](#network-softmod-ripping) | [Save Data Dumping](#save-data-dumping) | [Format Conversion](#format-conversion)

---

## Cartridge Dumping

Cartridge-based systems (NES, SNES, Game Boy, GBA, N64, Sega, etc.) require a physical cartridge reader to dump ROMs.

### Recommended Hardware

{% tabs %}
{% tab title="GB / GBC / GBA" %}
**[GB Operator](https://www.epilogue.co/product/gb-operator)** (Epilogue) — USB device for Game Boy, Game Boy Color, and Game Boy Advance cartridges.

- Software: Epilogue desktop app (Mac, Windows, Linux)
- Dumps ROM and save data
- Also supports flashing flash carts

**[GBxCart RW](https://www.gbxcart.com/)** (insideGadgets) — Open-source USB cartridge reader/writer.

- Compatible with GB, GBC, GBA, and many flash carts
- Software: **FlashGBX** (cross-platform, open-source)
- Dumps ROM, RAM/save data, and RTC data
{% endtab %}

{% tab title="Multi-System" %}
**[Retrode 2](https://www.retrode.com/)** — USB cartridge reader for SNES and Sega Genesis/Mega Drive.

- Adapter modules available for N64, Game Boy, Game Gear, Master System
- Appears as a USB mass storage device — no special software needed
- Dumps ROM files directly

**[INLretro Dumper](https://www.infiniteneslives.com/inlretro.php)** (Infinite NES Lives) — Supports a wide range of cartridge formats including NES, SNES, N64, Game Boy, Sega, and more.

- Open-source software
- Requires more technical setup than Retrode
{% endtab %}

{% tab title="NES / Famicom" %}
**[INLretro Dumper](https://www.infiniteneslives.com/inlretro.php)** — NES/Famicom focused with broad support.

**[Kazzo / USBSNES](https://github.com/snes9xgit/snes9x)** — Various open-source NES dumpers exist for different mappers.

Many NES dumper projects are community-built — search the NesDev forums for the latest recommendations for specific mappers.
{% endtab %}
{% endtabs %}

### Dumping Process (General)

1. Install the reader's software on your Mac or PC.
2. Insert your cartridge into the reader.
3. Connect the reader to your computer via USB.
4. Follow the software's dump/backup procedure.
5. The output will be a ROM file (e.g., `.gb`, `.gba`, `.sfc`, `.n64`).
6. [Import the ROM](importing-roms.md) into Provenance.

{% hint style="info" %}
Some cartridges use battery-backed SRAM for saves. Dump your save data **before** the battery dies — see [Save Data Dumping](#save-data-dumping) below.
{% endhint %}

### OSCR (Open Source Cartridge Reader)

The **[OSCR](https://github.com/sanni/cartreader)** (formerly Cart Reader by sanni) is an Arduino-based open-source cartridge reader that supports dozens of systems — NES, SNES, N64, Game Boy, Sega Genesis, Sega Master System, Game Gear, WonderSwan, and more.

- Requires assembly and some soldering
- Extensive community support on the GitHub repository
- One of the most comprehensive multi-system options available

---

## Disc Ripping

CD, DVD, and other optical disc-based games can be dumped using optical drives or dedicated hardware.

### CD-Based Systems (PS1, Saturn, Sega CD, TurboGrafx-CD, PC-FX)

{% tabs %}
{% tab title="macOS" %}
**cdrdao** — Command-line tool that creates `.bin` + `.toc` disc images with subchannel data.

```bash
# Install via Homebrew
brew install cdrdao

# Dump a disc (replace /dev/disk2 with your drive)
cdrdao read-cd --read-raw --datafile game.bin --device /dev/disk2 --driver generic-mmc-raw game.toc
```

**ddrescue** — For scratched or damaged discs, `ddrescue` retries bad sectors:

```bash
brew install ddrescue
ddrescue -d -r3 /dev/disk2 game.iso game.log
```

After dumping, convert `.toc` to `.cue` using `toc2cue` (included with cdrdao):

```bash
toc2cue game.toc game.cue
```
{% endtab %}

{% tab title="Windows" %}
**[ImgBurn](https://www.imgburn.com/)** — Free disc imaging tool.

1. Insert disc → Select **Read** mode.
2. Choose output format: `.bin` + `.cue`.
3. Enable subchannel data reading for PS1 games (required for copy-protected titles).

**[IsoBuster](https://www.isobuster.com/)** — Advanced disc recovery and imaging tool (paid, with free tier).

- Handles damaged discs
- Supports many disc formats
{% endtab %}

{% tab title="Linux" %}
**cdrdao** — Available in most package managers:

```bash
sudo apt install cdrdao
cdrdao read-cd --read-raw --datafile game.bin --device /dev/sr0 --driver generic-mmc-raw game.toc
toc2cue game.toc game.cue
```

**ddrescue** — For damaged discs:

```bash
sudo apt install gddrescue
ddrescue -d -r3 /dev/sr0 game.iso game.log
```
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
PS1 games require subchannel data for accurate dumps. Always use raw mode (`--read-raw`) with cdrdao or enable subchannel reading in ImgBurn.
{% endhint %}

### DVD-Based Systems (PS2, GameCube, Wii)

{% tabs %}
{% tab title="GameCube / Wii" %}
**CleanRip** (Wii homebrew) — The recommended method for GameCube and Wii disc dumping.

1. Install the [Homebrew Channel](https://wii.guide/) on your Wii.
2. Download **CleanRip** and place it in `sd:/apps/CleanRip/`.
3. Launch CleanRip from the Homebrew Channel.
4. Select your source (Disc Drive), output device (SD/USB), and dump format.
5. CleanRip produces `.iso` files (or split files for games over 4 GB).

For Provenance's Dolphin core, see the [GameCube & Wii Guide](../../info/system-guides/gamecube-wii.md) for the correct folder structure.
{% endtab %}

{% tab title="PS2" %}
**[FreeMcBoot](https://www.ps2-home.com/forum/page/freemc-boot-fmcb-1-966)** + **uLaunchELF** — Softmod method for PS2.

1. Install FreeMcBoot on a memory card.
2. Use **uLaunchELF** to access the DVD drive.
3. Use **dvd2usb** or similar ELF homebrew to dump discs to USB.

Alternatively, use a PC DVD drive with **ImgBurn** (Windows) or **ddrescue** (macOS/Linux) — PS2 discs are standard DVDs.
{% endtab %}
{% endtabs %}

### PSP (UMD)

PSP UMD discs cannot be read by standard PC drives. Use the PSP itself:

1. Enable USB mode on your PSP (Settings → USB Connection).
2. Use **[PPSSPP](https://www.ppsspp.org/)** or custom firmware to dump UMDs.
3. With custom firmware (CFW) installed, use **UMDGen** or the built-in ISO dumper in CFW.

Alternatively, enable **USB ISO** mode in CFW settings to dump directly over USB to your computer.

### Dreamcast (GD-ROM)

GD-ROM discs are a proprietary format that standard drives cannot read. Options:

- **[GDEMU](https://gdemu.wordpress.com/)** or **[USB-GDROM](http://www.dreamcast-talk.com/)** — ODE (Optical Drive Emulator) hardware that can dump GD-ROMs.
- **Dreamshell** — Homebrew environment for Dreamcast that supports disc dumping to SD card via an SD adapter.
- Many Dreamcast games are available as **CDI** or **GDI** dumps — check [Formatting ROMs](formatting-roms.md) for compatible formats.

---

## Network / Softmod Ripping

Several consoles can dump games over a network or via homebrew software without additional hardware.

### Nintendo 3DS

{% tabs %}
{% tab title="GodMode9" %}
**[GodMode9](https://github.com/d0k3/GodMode9)** — Full-access file system browser for 3DS with custom firmware.

1. Install custom firmware ([Luma3DS](https://github.com/LumaTeam/Luma3DS)) following [3ds.hacks.guide](https://3ds.hacks.guide/).
2. Boot into GodMode9 (hold START while powering on).
3. Navigate to `[C:] GAMECART` for cartridges or `[A:] SYSNAND SD` for installed titles.
4. Select the game → NCSD image options → Dump to `.cia` or `.3ds`.

For Provenance's emuThreeDS core, see the [3DS Guide](../../info/system-guides/3ds.md) for decrypted ROM requirements.
{% endtab %}
{% endtabs %}

### Nintendo DS

NDS cartridges can be dumped using:

- **[GoodDS](https://gbatemp.net/)** or **DSOrganize** on a DS with homebrew.
- A **3DS with GodMode9** — insert DS cartridge and dump via `[C:] GAMECART`.
- **Flashcart-based dumpers** available from the GBAtemp community.

### PS1 / PS2 (via FreeMcBoot)

With **FreeMcBoot** installed on a PS2 memory card:

1. Boot with FreeMcBoot memory card inserted.
2. Launch **uLaunchELF**.
3. Use `mass:` (USB) as output destination with disc dumping homebrew.

### SNES Classic / NES Classic (hakchi)

Games installed on SNES/NES Classic can be extracted using **[hakchi2 CE](https://github.com/TeamShinkansen/hakchi2)** on Windows.

---

## Save Data Dumping

Back up your save files from physical media before batteries die or hardware fails.

### Game Boy / GBA Saves

Most GB/GBC/GBA cartridges store saves in battery-backed SRAM.

- **GB Operator** — Dumps save data alongside ROM. Use the "Backup Save" function.
- **GBxCart RW + FlashGBX** — Reads and writes save RAM. Supports `.sav` format compatible with Provenance.

{% hint style="warning" %}
GB/GBC cartridge batteries typically last 15–20 years. If your cartridge is from the 1990s or early 2000s, dump your saves soon.
{% endhint %}

### PS1 Memory Cards

- **[MemcardRex](https://github.com/ShendoXT/memcardrex)** — Windows app for reading PS1 memory cards via a USB memory card reader.
- **[GCMM](https://github.com/suloku/gcmm)** (GameCube Memory Card Manager) — Wii homebrew for backing up GameCube memory cards to SD.
- **[MCMM Mod](https://gbatemp.net/)** — Wii/GC homebrew alternatives exist for various memory card formats.

Raw memory card dumps are `.mcr` files. Individual save files can be exported as `.mcs` or `.srm` format. See [Game Saves](../../info/saves.md) for importing save files into Provenance.

### PS2 Saves

- **[Open PS2 Loader (OPL)](https://github.com/ps2homebrew/Open-PS2-Loader)** — Includes memory card backup utilities.
- **uLaunchELF** — Allows copying save files from PS2 memory card to USB storage.
- Save files can be imported/exported using **MyMC** on PC.

### N64 Saves (Controller Pak)

N64 Controller Pak (memory card) saves can be backed up using:

- **[64drive](https://64drive.retroactive.be/)** or **[EverDrive-64](https://krikzz.com/)** — Flashcarts with Controller Pak backup support.
- **N64 save dumpers** — Various community tools on GBAtemp.

SRAM/EEPROM/FlashRAM saves stored on cartridges can be dumped with the INLretro or OSCR hardware mentioned above.

---

## Format Conversion

After dumping, you may need to convert files to formats Provenance supports.

### CHD (Compressed Hunks of Data)

CHD is highly recommended for disc-based games — it reduces file sizes by 40–70% while maintaining perfect accuracy.

```bash
# Install chdman (part of MAME tools)
# macOS:
brew install mame

# Convert BIN/CUE to CHD
chdman createcd -i game.cue -o game.chd

# Convert ISO to CHD
chdman createcd -i game.iso -o game.chd

# Verify CHD integrity
chdman verify -i game.chd
```

See [Advanced ROM Management](advanced-management.md) for batch CHD conversion workflows.

### Converting Other Image Formats

Some tools produce formats Provenance doesn't directly support:

| Source Format | Tool | Output Format |
|---|---|---|
| `.nrg` (Nero) | `nrg2iso` | `.iso` |
| `.mdf` + `.mds` (Alcohol) | `mdf2iso` | `.iso` |
| `.img` + `.ccd` | ImgBurn (re-burn or convert) | `.bin` + `.cue` |
| `.ecm` | `unecm` | `.bin` |
| `.cdi` (Dreamcast) | `cdirip` | `.bin` + `.cue` |

```bash
# macOS — install conversion tools
brew install ecm-tools

# Convert ECM-compressed file
unecm game.bin.ecm
```

### Multi-Disc Games and M3U Playlists

For games with multiple discs, create an `.m3u` playlist file so Provenance can handle disc swapping:

```
# game.m3u
game_disc1.chd
game_disc2.chd
game_disc3.chd
```

See [Formatting ROMs](formatting-roms.md) for complete M3U instructions and supported formats per system.

### Supported Formats Reference

After conversion, check [Formatting ROMs](formatting-roms.md) to confirm your output format is supported by Provenance for your target system.

---

## See Also

- [Importing ROMs](importing-roms.md) — Get your dumped ROMs into Provenance
- [Formatting ROMs](formatting-roms.md) — Supported formats, multi-file ROMs, archiving
- [Advanced ROM Management](advanced-management.md) — CHD conversion, library organization
- [BIOS Requirements](../bios-requirements.md) — Required BIOS files for disc-based systems
- [Game Saves](../../info/saves.md) — Importing dumped save files
- [GameCube & Wii Guide](../../info/system-guides/gamecube-wii.md) — Dolphin memory card structure
- [3DS Guide](../../info/system-guides/3ds.md) — Decrypted ROM notes

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
