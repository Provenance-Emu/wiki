---
description: How to legally dump ROMs and disc images from your own physical game collection.
---

# Ripping ROMs

This guide covers how to create digital backups (ROMs and disc images) from physical game media you own. Ripping your own games is the legal way to obtain ROMs.

{% hint style="warning" %}
Only rip games you physically own. Downloading ROMs you do not own a physical copy of is not covered by this guide and may violate copyright law.
{% endhint %}

---

## Disc Ripping

Disc-based games require reading the raw data from optical media. The method depends on the disc format used by each system.

### Equipment Overview

| Method | Works For | What You Need |
|---|---|---|
| Standard CD-ROM drive | PS1, Sega CD, Saturn, 3DO, TG-CD, PC-FX, Neo Geo CD | Any modern optical drive |
| DVD-ROM drive | PS2 | DVD-capable drive |
| Specialized GD-ROM drive | Dreamcast | Yamaha CRW2200 or Plextor PX-W4012 (rare) |
| Network dump | PS2, Dreamcast, Wii, Xbox, PSP | Softmodded console + network |

---

### Standard CD Games (PS1, Sega CD, Saturn, 3DO, TG-CD, PC-FX, Neo Geo CD)

Standard CD-based games use 74-minute 700 MB optical discs readable by any modern CD-ROM drive. Use a raw ripping tool rather than a standard audio/data ripper to capture all subchannel data, which is required for copy-protection on PS1 and sector accuracy on other systems.

{% tabs %}
{% tab title="macOS" %}
**Tool:** cdrdao (command-line, via Homebrew)

1. Install Homebrew if you don't have it: [brew.sh](https://brew.sh)
2. Install cdrdao:
   ```bash
   brew install cdrdao
   ```
3. Insert the disc and find the device name:
   ```bash
   cdrdao scanbus
   ```
   Note the device identifier (e.g., `IODVDServices/2`).
4. Rip the disc to a `.toc` + `.bin` file:
   ```bash
   cdrdao read-cd --read-raw --paranoia-mode 3 --device IODVDServices/2 --datafile "game.bin" game.toc
   ```
5. Convert the `.toc` to a `.cue` file:
   ```bash
   toc2cue game.toc game.cue
   ```
   (toc2cue is included with cdrdao)

**Output:** `game.bin` + `game.cue`
{% endtab %}

{% tab title="Windows" %}
**Tool:** ImgBurn (free GUI)

1. Download and install [ImgBurn](https://www.imgburn.com).
2. Insert the disc.
3. Select **Mode → Read** (reads disc to image file).
4. Set **Destination** to your desired output folder and filename.
5. For PlayStation 1 games, click the settings icon and enable:
   - **Read Sub-Channel Data from Disc** → Yes
   - **Sub-Channel Data Type** → Combined Q & R-W Data
6. Click the Read button (disc → folder icon).

**Output:** `.bin` + `.cue`

{% hint style="info" %}
ImgBurn automatically names tracks and generates a valid `.cue` file for multi-track discs (common on PS1 games with audio tracks).
{% endhint %}
{% endtab %}

{% tab title="Linux" %}
**Tool:** cdrdao (same commands as macOS)

1. Install cdrdao via your package manager:
   ```bash
   # Debian/Ubuntu
   sudo apt install cdrdao

   # Fedora
   sudo dnf install cdrdao

   # Arch
   sudo pacman -S cdrdao
   ```
2. Insert the disc and find the device:
   ```bash
   cdrdao scanbus
   ```
   Alternatively, your drive is likely `/dev/sr0`.
3. Rip the disc:
   ```bash
   cdrdao read-cd --read-raw --paranoia-mode 3 --device /dev/sr0 --datafile "game.bin" game.toc
   toc2cue game.toc game.cue
   ```

**For damaged or scratched discs**, use `ddrescue` for better error recovery:
```bash
sudo apt install gddrescue
ddrescue -d -r3 /dev/sr0 game.bin game.log
```

`ddrescue` produces a single raw binary image. For multi-track discs (e.g., PS1 games with audio tracks), you will need to create a `.cue` file manually or use cdrdao instead, as `ddrescue` alone does not generate subchannel/cue data.

**Output:** `game.bin` (raw image; use cdrdao for proper `.bin` + `.cue` with subchannel data)
{% endtab %}
{% endtabs %}

**Output format:** `.bin + .cue` (multi-file ROM). See [Formatting ROMs — Multi-file ROMs](formatting-roms.md#multi-file-roms) for how to package these for import into Provenance.

{% hint style="info" %}
**Verify your rip with Redump:** After ripping, calculate the MD5 hash of your `.bin` file(s) and search [redump.org](http://redump.org) to confirm your dump matches a known-good release. This ensures your rip is complete and accurate.

**Mac/Linux:** `md5 game.bin` or `md5sum game.bin`
**Windows:** `certutil -hashfile game.bin MD5`
{% endhint %}

{% hint style="warning" %}
**TurboGrafx-CD / PC Engine CD:** These systems require the System Card BIOS file to run CD games. See [BIOS Requirements](../bios-requirements.md) for the required files.
{% endhint %}

**Saturn multi-disc games:** Saturn games with multiple discs should use an `.m3u` playlist file. See [Formatting ROMs — Multi-disc Games](formatting-roms.md#multi-disc-games) for instructions.

**Sega CD regional BIOS:** Sega CD requires one of three regional BIOS files depending on your game's region (USA, Europe, Japan). All three regional BIOS files are available — see [BIOS Requirements](../bios-requirements.md) for details.

---

### PlayStation 2

PS2 games are typically pressed on DVD discs (mostly single-layer DVD-5, with some dual-layer DVD-9), and a smaller number were released on CD-ROM. Most modern PC DVD drives can read these discs, though macOS optical drives are often unreliable with dual-layer (DVD-9) media.

**Method A: DVD drive on PC (Recommended)**

{% tabs %}
{% tab title="Windows" %}
Use **ImgBurn** (same as CD games above):

1. Insert PS2 disc.
2. Mode → **Read**.
3. Output format: ISO image (`.iso`).
4. Click Read.

Most single-layer PS2 games (DVD-5) rip reliably. Some dual-layer games (DVD-9) may require a higher-quality drive.
{% endtab %}

{% tab title="Linux" %}
Use `ddrescue` for reliable DVD ripping:

```bash
sudo ddrescue -d -r3 /dev/sr0 game.iso game.log
```

The `-d` flag enables direct disc access (bypasses OS cache) and `-r3` retries unreadable sectors three times.
{% endtab %}

{% tab title="macOS" %}
macOS optical drives are generally unreliable for dual-layer PS2 discs. Use a Windows or Linux machine, or use Method B (network dump) instead.

For single-layer PS2 games, you can try:
```bash
dd if=/dev/disk2 of=game.iso bs=2048
```
Replace `disk2` with the correct disk identifier from `diskutil list`.
{% endtab %}
{% endtabs %}

**Method B: Network dump via OPL/FreeMcBoot** — Requires a softmodded PS2 running Open PS2 Loader (OPL) with network access. This allows dumping games over your local network without a PC DVD drive.

**Output:** `.iso`

---

### Dreamcast GD-ROM

{% hint style="danger" %}
GD-ROM (Gigabyte Disc) is a proprietary Sega format. Standard PC CD/DVD drives can only read the low-density area (~1 GB) of a GD-ROM — they **cannot** read the high-density area where the actual game data is stored. A standard drive will produce an incomplete, unplayable dump.
{% endhint %}

**Method A: Specialized GD-ROM drive (rare)**

Only a handful of drives can read the full GD-ROM:
- **Yamaha CRW2200** (most commonly cited)
- **Plextor PX-W4012**

These drives are rare and typically cost $100–$300+ on the used market. If you have one, use compatible GD-ROM ripping software or scripts (as documented by the Dreamcast preservation community) to extract all tracks. This method is not practical for most users.

**Method B: Network dump via httpd-ism (Recommended)**

<details><summary><strong>Dumping via httpd-ism (Broadband Adapter method)</strong></summary>

This method requires a Dreamcast with a Broadband Adapter (BBA) or LAN Adapter and uses a bootable disc to serve game data over the network.

**Requirements:**
- Dreamcast console with Broadband Adapter or LAN Adapter
- `httpd-ism` boot disc (a self-booting CDI image)
- A PC on the same local network
- A web browser on the PC

**Steps:**
1. Boot the `httpd-ism` disc on your Dreamcast. If you have homebrew access (e.g., via SD card adapter or other legitimate homebrew boot method), boot it from there.
2. When prompted, insert the GD-ROM game you want to dump.
3. The Dreamcast's IP address will appear on screen.
4. On your PC, open a browser and navigate to `http://[dreamcast-ip]/` (e.g., `http://192.168.1.100/`).
5. The disc's track listing will appear. Download each track file listed.
6. You will get a set of `.iso` / `.raw` / `.wav` track files plus a `.gdi` descriptor file.

**Note:** Transfer speed is slow (~1 MB/s over a 10Mbps LAN Adapter, faster with BBA). A full game dump can take 30–90 minutes.

</details>

<details><summary><strong>Alternative: Dreamshell SD card method</strong></summary>

**DreamShell** is a homebrew OS for Dreamcast that supports dumping GD-ROMs to an SD card via a BIOS mod chip or IDE adapter (Dreamcast Terra Drive / GDEMU users).

1. Boot DreamShell from an SD card or modified BIOS.
2. Navigate to **Dump GD** in the DreamShell file manager.
3. Select output destination (SD card or USB).
4. Begin dump — DreamShell reads the GD-ROM directly via the Dreamcast's internal drive mechanism, bypassing the standard CD-ROM area limitation.

This method requires hardware modification (IDE adapter or GDEMU) and is more involved but produces reliable dumps.

</details>

**Output format:** `.gdi` (GD-ROM Image) with associated track files.

After dumping, convert to `.chd` for a single compressed file:

```bash
chdman createcd -i game.gdi -o game.chd
```

See [Advanced ROM Management — CHD Format](advanced-management.md#chd-format-recommended) for more on chdman.

---

### GameCube & Wii

GameCube and Wii discs use a proprietary format that standard PC drives cannot read. The recommended method is CleanRip, a homebrew application that reads discs using the console's own drive.

<details><summary><strong>CleanRip (Wii homebrew — Recommended)</strong></summary>

**Requirements:**
- Wii console with the Homebrew Channel installed
- SD card or USB drive (4 GB+ free space; 8 GB SD recommended for Wii games)
- CleanRip app ([download from wiibrew.org](https://wiibrew.org/wiki/CleanRip))

**Setup:**
1. Download CleanRip and extract the `apps` folder to the root of your SD card.
2. Insert the SD card into your Wii and launch the **Homebrew Channel**.
3. Launch **CleanRip** from the Homebrew Channel app list.

**Dumping:**
1. Choose your output destination: **SD card** or **USB drive**.
2. When prompted, confirm whether to use Redump.org Disc IDs (recommended — enables hash verification).
3. Insert the GameCube or Wii disc when prompted.
4. CleanRip will begin reading the disc. Do not interrupt — **GameCube games take ~10 minutes**, **Wii games take 20–40 minutes**.
5. When complete, the `.iso` file will be on your SD card or USB drive.
6. Transfer the file to your computer.

**Note:** Wii game ISOs vary in size — many titles are single-layer and smaller, while some dual-layer games can be up to 8.5 GB. Ensure your SD card is formatted as FAT32 with 32 KB cluster size, or use a USB drive formatted as FAT32 or NTFS.

</details>

<details><summary><strong>PC drive alternative (less reliable)</strong></summary>

Some specific PC drives can read GameCube/Wii discs, but compatibility is limited and results are inconsistent:

**Drives known to work:**
- LG GH22NS30 (with specific firmware)
- LG GH24NS95 (with RipIt4Me or Friidump)
- ASUS DRW-24B1ST (some firmware versions)

**Tools:**
- **Rawdump 2.1** — Windows GUI for dumping GameCube/Wii ISOs
- **Friidump** — Command-line alternative

**Limitations:**
- Not all drives work; the same model may produce errors depending on firmware
- Wii dual-layer games are often unreliable via PC drive
- CleanRip via Wii is significantly more reliable and is the recommended path

</details>

**Output:** `.iso` for both GameCube and Wii games.

After ripping, see [GameCube & Wii System Guide](../../info/system-guides/gamecube-wii.md) for the required folder structure when importing into Provenance.

---

### PSP UMD

PSP UMD discs use a proprietary format that cannot be read by any PC drive. Dumping requires Custom Firmware (CFW) running on the PSP itself.

<details><summary><strong>Dumping PSP UMDs via Custom Firmware (CFW)</strong></summary>

**Requirements:**
- PSP console with Custom Firmware installed (e.g., PRO, ME, or Infinity CFW for PSP 1000/2000/3000; HEN for PSP Go)
- Memory Stick Pro Duo or microSD with adapter (sufficient space for game — most UMDs are 100 MB–1.8 GB)

**Steps:**
1. Boot your PSP with CFW enabled.
2. Navigate to **Game → Memory Stick** and locate the **ISO Tool** or **UMD Dumper** homebrew, or use the built-in UMD dumping feature in your CFW.
3. Insert the UMD you want to dump.
4. Select **Dump UMD** (or equivalent). The game will be saved as an `.iso` file on your Memory Stick.
5. Transfer the `.iso` to your computer via USB.

**Output:** `.iso`

</details>

---

### Other Disc Systems

These systems use standard CD media and follow the same process as the [Standard CD Games](#standard-cd-games-ps1-sega-cd-saturn-3do-tg-cd-pc-fx-neo-geo-cd) section above.

| System | Same As | Additional Notes |
|---|---|---|
| **3DO** | Standard CD | No BIOS required for disc ripping; BIOS needed for emulation |
| **Neo Geo CD** | Standard CD | No additional BIOS required |
| **PC Engine CD / TurboGrafx-CD** | Standard CD | System Card BIOS required — see [BIOS Requirements](../bios-requirements.md) |
| **PC-FX** | Standard CD | BIOS required — see [BIOS Requirements](../bios-requirements.md) |
| **Sega CD / Mega CD** | Standard CD | Requires one of three regional BIOS files (USA, Europe, Japan) — see [BIOS Requirements](../bios-requirements.md) |

---

{% hint style="info" %}
After ripping, convert disc images to CHD format for smaller files and single-file convenience. See [Advanced ROM Management](advanced-management.md#chd-format-recommended) for chdman commands.
{% endhint %}

## See Also

- [Formatting ROMs](formatting-roms.md) — Supported file formats, multi-file ROMs, multi-disc `.m3u` playlists
- [BIOS Requirements](../bios-requirements.md) — Required BIOS files for CD-based systems
- [Advanced ROM Management](advanced-management.md) — CHD conversion, batch processing, large library management
- [GameCube & Wii System Guide](../../info/system-guides/gamecube-wii.md) — Folder structure for GameCube/Wii games
- [Importing ROMs](importing-roms.md) — How to import your ripped games into Provenance

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
