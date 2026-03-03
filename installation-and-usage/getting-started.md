---
description: Go from zero to playing your first game in under 10 minutes
---

# Getting Started

New to Provenance? This walkthrough takes you from installation to playing your first game, step by step.

---

## Step 1: Install Provenance

{% tabs %}
{% tab title="iPhone / iPad" %}
1. Open the **App Store**
2. Search for **"Provenance"** or tap: [Provenance on App Store](https://apps.apple.com/us/app/provenance-app/id1596862805)
3. Tap **Get** (it's free — ~2.5 GB download)
4. Once installed, tap **Open**
{% endtab %}

{% tab title="Apple TV" %}
1. On your Apple TV, open the **App Store**
2. Search for **"Provenance"**
3. Select **Get** (it's free)
4. Once installed, open Provenance from the Home Screen

**Tip:** You'll need a Bluetooth controller — the Siri Remote can navigate menus but not play games. See [Apple TV Guide](../info/tvos-guide.md).
{% endtab %}

{% tab title="Mac (Apple Silicon)" %}
1. Open the **App Store** on your Mac
2. Search for **"Provenance"**
3. Click **Get** (it's free)
4. Launch from Applications or Launchpad

**Requires:** macOS 13.0+ on Apple Silicon (M1 or later).
{% endtab %}
{% endtabs %}

{% hint style="success" %}
That's it for installation. No developer account, no sideloading, no Xcode required.
{% endhint %}

**Want to sideload or build from source instead?** See [Alternative Installation Methods](installing-provenance/advanced.md).

---

## Step 2: Get Your Game Files Ready

Provenance plays ROMs — digital copies of game cartridges and discs. You'll need:

1. **ROM files** for the games you want to play
2. **BIOS files** (only for certain systems — see below)

### Which systems need BIOS files?

Most systems work without any BIOS. These popular systems **do NOT need BIOS** — just drop in ROMs and play:

- NES, SNES, N64, Game Boy, GBC, GBA, Genesis, Game Gear, Neo Geo Pocket, Atari 2600/7800

These systems **require BIOS files** before games will run:

- PlayStation (3 BIOS files)
- Sega CD (3 BIOS files)
- Sega Saturn (3 BIOS files)
- TurboGrafx-CD, Atari Lynx, Atari 5200, ColecoVision

**Full list with filenames and MD5 hashes:** [BIOS Requirements](bios-requirements.md)

{% hint style="warning" %}
Import BIOS files **before** importing ROMs for that system. Provenance auto-detects them by MD5 hash — filenames don't matter.
{% endhint %}

### Supported ROM formats

| Format | Type | Best for |
|--------|------|----------|
| `.zip` | Compressed single ROM | Most cartridge games |
| `.7z` | Compressed single ROM | Most cartridge games |
| `.chd` | Compressed disc image | CD-based games (PS1, Sega CD, etc.) |
| `.cue` + `.bin` | Disc image pair | CD-based games (keep both files together) |
| `.iso` | Disc image | PSP, some CD systems |

**Full formatting guide:** [Formatting ROMs](roms/formatting-roms.md)

---

## Step 3: Import Your First Game

Pick the method that works best for you:

{% tabs %}
{% tab title="AirDrop (Fastest)" %}
**Mac to iPhone/iPad — the quickest way to get started.**

1. On your Mac, find your ROM file (e.g., `SuperMarioWorld.zip`)
2. Right-click → **Share** → **AirDrop**
3. Select your iPhone/iPad
4. On your device, tap **Provenance** when prompted
5. The game appears in your library automatically
{% endtab %}

{% tab title="Files App" %}
**Works with iCloud Drive, Dropbox, Google Drive, or local storage.**

1. Save your ROM to the **Files** app (iCloud Drive, local, or any cloud provider)
2. Open **Files**, find your ROM
3. Tap and hold → **Share** → **Copy to Provenance**
4. The game appears in your library
{% endtab %}

{% tab title="Web Browser" %}
**Import from built-in web server (great for bulk transfers).**

1. Open Provenance and tap the **+** button (or Settings → Import/Export)
2. Note the IP address shown (e.g., `http://192.168.1.42`)
3. On your computer, open that URL in a browser
4. Click **Imports**, then drag and drop ROM files
5. Games appear in your library when the upload finishes

**WebDAV option:** Connect to `http://[device-ip]:81` from Finder (Mac) or any WebDAV client.
{% endtab %}

{% tab title="Safari Download" %}
**Download directly on your device.**

1. Open Safari on your iPhone/iPad
2. Download a ROM file from your source
3. Tap the downloaded file in Safari's download bar
4. Choose **Open in Provenance**
{% endtab %}
{% endtabs %}

{% hint style="info" %}
**Importing BIOS files** works the same way — just AirDrop, copy, or upload them. Provenance auto-detects BIOS files by their contents and puts them in the right place.
{% endhint %}

**Detailed guide:** [Importing ROMs](roms/importing-roms.md)

---

## Step 4: Play!

1. Your imported game appears in the **Library** with cover art (auto-matched)
2. **Tap the game** to launch it
3. Use **on-screen controls** or a connected **Bluetooth controller**
4. To pause, tap the **Menu** button (top of screen) for save states, settings, and quit options

### Essential controls while playing

| Action | On-screen | Controller |
|--------|-----------|------------|
| Pause / Menu | Tap pause button | Press Menu / Options |
| Save state | Pause → Save State | — |
| Load state | Pause → Load State | — |
| Fast forward | Pause → Fast Forward | — |
| Quit to library | Pause → Quit | — |

---

## Step 5: Make It Yours

Now that you're playing, here are ways to improve the experience:

### Connect a controller

Physical controllers make a huge difference. Any MFi or Bluetooth controller works:

- **Best overall:** PlayStation DualSense, Xbox Wireless Controller
- **Best for iPhone:** Razer Kishi V2, Backbone One (clip-on style)
- **Budget-friendly:** 8BitDo SN30 Pro

**Full guide:** [Controllers & Controls](../info/controllers-and-controls/README.md)

### Customize your on-screen controls

Don't like the default buttons? **Skins** are free custom controller overlays:

1. Visit [DeltaStyles.com](https://deltastyles.com) on your device
2. Download a skin for your system (`.deltaskin` file)
3. Tap the file → **Open in Provenance**
4. Apply in Settings → Controller Skins

**Full guide:** [Skins Guide](../info/skins-guide.md)

### Sync across devices (optional)

**Provenance Plus** ($3.99/month, $39.99/year, or $99.99 lifetime) syncs your library, saves, and settings across iPhone, iPad, Mac, and Apple TV via iCloud.

**Apple TV users:** iCloud sync is included free!

---

## Quick Reference

| Task | Where |
|------|-------|
| Import games | **+** button in Library, or AirDrop / Files |
| Change controls | Settings → Controller Skins |
| Connect controller | Pair via Bluetooth (Settings → Bluetooth) |
| Save/load state | Pause menu during gameplay |
| Check BIOS status | Settings → Cores → [System name] |
| Get help | [Troubleshooting](../help/troubleshooting.md) or [Discord](https://discord.gg/provenance) |

---

## Troubleshooting First-Time Setup

<details>
<summary><strong>Game doesn't appear after importing</strong></summary>

1. Check the file format — must be a [supported ROM format](roms/formatting-roms.md)
2. Pull down to refresh the library
3. Force quit Provenance and reopen
4. If importing via web server, wait for the upload to fully complete before navigating away

</details>

<details>
<summary><strong>"Missing BIOS" or game shows black screen</strong></summary>

The system requires BIOS files. Check [BIOS Requirements](bios-requirements.md) for the exact files needed, then import them the same way you imported ROMs. Verify in Settings → Cores that the BIOS shows as detected (green).

</details>

<details>
<summary><strong>Game runs slowly</strong></summary>

- Close other apps running in the background
- Try a different emulator core (long-press game → Game Settings → Core)
- Some systems (N64, PSP, Dreamcast, 3DS) need newer hardware — see [Performance Optimization](../info/performance-optimization.md)

</details>

<details>
<summary><strong>No sound</strong></summary>

- Check your device isn't in Silent Mode (flip the side switch on iPhone)
- Make sure volume is up
- Check that no Bluetooth audio device is connected unexpectedly

</details>

<details>
<summary><strong>Controller not working</strong></summary>

- Ensure the controller is paired in Settings → Bluetooth
- Open a game, pause → check controller is assigned to Player 1
- See [Controllers Guide](../info/controllers-and-controls/README.md) for setup details

</details>

---

{% hint style="success" %}
**Need more help?** Check the [Troubleshooting Guide](../help/troubleshooting.md), browse the [FAQ](../faqs.md), or join the [Provenance Discord](https://discord.gg/provenance).
{% endhint %}
