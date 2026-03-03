---
description: Solutions for common issues with Provenance on iOS, iPadOS, macOS, tvOS, and visionOS
---

# Troubleshooting

{% hint style="warning" %}
**Provenance-Emu is a small team of volunteers.** Before reaching out, check this guide and the [FAQ](../faqs.md) — your answer is probably here.
{% endhint %}

**Quick links:** [Crashes](#app-crashes) | [Performance](#performance-issues) | [ROMs & Import](#rom-and-import-issues) | [Controllers](#controller-issues) | [iCloud Sync](#icloud-sync-issues) | [Saves](#save-issues) | [Skins](#skin-issues) | [Installation](#installation-issues) | [Advanced Debugging](#advanced-debugging)

---

## App Crashes

### Crashes on Launch

**App Store users:**
1. Ensure your device is on **iOS 16.0+** (Settings → General → About)
2. Restart your device (full power off → wait 10 seconds → power on)
3. Delete and reinstall Provenance from the App Store
4. If it persists, report on [GitHub Issues](https://github.com/Provenance-Emu/Provenance/issues)

**Sideloaders:** If the app worked before but crashes after ~7 days, your provisioning profile has expired. Free Apple Developer accounts expire every 7 days — re-sign with AltStore or Sideloadly. Your saves and ROMs are safe. See [Advanced Installation FAQ](../installation-and-usage/installing-provenance/faqs-advanced.md) for details.

### Crashes When Importing ROMs

- **Archives containing folders will crash the app.** Archive only loose files — do not include folder structure inside a .zip.
- **Filenames with extra periods** (e.g., `Game.v1.2.rom`) can cause crashes. Rename to remove extra dots before the extension.
- **CD-based / multi-file ROMs** should be uploaded one at a time. If importing breaks, delete the game from the app and from the file system (ROMs and Imports folders), then re-upload.

### Crashes on Library Screen

This may indicate a **corrupted database**. Symptoms:
- Games appear duplicated
- Metadata or artwork missing
- Consistent crashes when browsing library

**Fix:** See [Corrupted Database](#corrupted-database) under Advanced Debugging.

### General Crash Steps

1. **Force quit and restart** — Double-tap Home → Swipe up on Provenance → Relaunch
2. **Update to latest version** — App Store → Provenance → Update
3. **Restart device** — Full power cycle
4. **Reinstall** — Delete app → Reinstall from App Store (saves in iCloud are preserved with Provenance Plus)

---

## Performance Issues

### Game is Slow or Stuttering

Try these fixes in order:

1. **Close background apps** — Double-tap Home, swipe up on all other apps
2. **Disable visual filters** — Settings → Turn off Smoothing and CRT Filter
3. **Lower internal resolution** — Settings → Resolution Multiplier → 1x or 2x
4. **Enable frameskip** — Settings → Frameskip → Auto
5. **Try an alternate core** — If available, some cores perform better for certain games
6. **Restart device** — Power off for 10 seconds, then power on

**Check your build:** If the app is named "Prov Debug" on the Home Screen or Settings shows "DEBUG", you built the debug version by mistake. Debug builds have extra logging and no compiler optimizations — they're significantly slower. Rebuild using the `Provenance-Release` (iOS) or `ProvenanceTV-Release` (tvOS) scheme.

### Specific Game is Slow, Others Are Fine

- Some games are inherently demanding (e.g., GoldenEye 007, Conker's Bad Fur Day on N64)
- Try a different ROM dump — bad/corrupted ROMs can hurt performance
- Check online compatibility lists for the emulator core
- Update Provenance — cores improve with each release

### Audio Crackling or Popping

This means the CPU can't keep up with the audio buffer.

1. Enable frameskip (Settings → Frameskip → Auto)
2. Close apps playing background audio
3. Switch from Bluetooth to wired headphones/speakers (Bluetooth audio adds latency)
4. Disable in-game audio settings if available

### Device Performance Guide

| Device | What Runs Well | May Struggle |
|--------|---------------|-------------|
| **iPhone 8 / SE 2nd-3rd gen** | NES, SNES, GB, GBA, Genesis, PS1 | N64 (some titles), GameCube |
| **iPhone 11-13** | All above + N64, PSP | GameCube, Dreamcast (demanding titles) |
| **iPhone 14+ / M1 iPad** | All systems | — |
| **Apple TV HD** | 16-bit and earlier, PS1 | N64 (minor slowdown) |
| **Apple TV 4K** | All systems | — |
| **Mac (Apple Silicon)** | All systems | — |

**Full guide:** [Performance Optimization](../info/performance-optimization.md)

---

## ROM and Import Issues

### ROMs Won't Import

1. **Check file format** — See [Formatting ROMs](../installation-and-usage/roms/formatting-roms.md) for supported formats per system
2. **Don't include folders in archives** — Zip only the ROM files, not a folder containing them
3. **Check for extra dots in filenames** — Files like `Game.v1.2.rom` can cause issues; rename to `Game v1-2.rom`
4. **Verify the ROM isn't corrupted** — Re-download if the file hash doesn't match known good dumps
5. **Restart Provenance** — Force quit and relaunch after importing

### Games Missing from Library After Import

- **Wrong file format** — Loose `.bin` files from CD-based games may be detected as Sega Genesis ROMs. Use `.cue + .bin` pairs or `.chd` format instead.
- **Missing BIOS** — Some systems won't show games without BIOS files. See [BIOS Requirements](../installation-and-usage/bios-requirements.md).
- **ROM in Conflicts folder** — If auto-detection fails, the ROM may be in the Conflicts folder. Check via the web server or Files app and move it to the correct system folder.
- **Re-import** — Delete the game from the library, then re-add the ROM.

### Multi-Disc Games Not Working

Multi-disc games (e.g., Final Fantasy VII on PS1) require an M3U playlist file:

1. Create a text file named `GameName.m3u`
2. List each disc on its own line:
   ```
   GameName (Disc 1).chd
   GameName (Disc 2).chd
   GameName (Disc 3).chd
   ```
3. Import the `.m3u` file along with all disc files

**Full guide:** [Advanced ROM Management](../installation-and-usage/roms/advanced-management.md#multi-disc-games-advanced)

### Region Pack ROMs (Multiple Versions in One Archive)

If importing an archive creates multiple identical-looking games, the archive likely contains multiple region versions. Extract the archive, keep only the region you want, re-archive, and re-import.

### Black Screen After Launching Game

1. **Missing BIOS** — PlayStation, Sega CD, Saturn, and Dreamcast require BIOS files. Check [BIOS Requirements](../installation-and-usage/bios-requirements.md).
2. **Corrupted ROM** — Try a different dump of the same game.
3. **Wrong core** — If multiple cores are available, try switching to an alternate core.
4. **Report it** — If the issue persists, report on [GitHub Issues](https://github.com/Provenance-Emu/Provenance/issues) with the game name and system.

---

## Controller Issues

### Controller Won't Pair

**PlayStation / Xbox controllers:**
1. Put controller in pairing mode:
   - **PS4/PS5:** Hold **Share + PS button** until light flashes rapidly
   - **Xbox:** Hold **Pairing button** (top edge) until Xbox logo flashes
2. On device: **Settings → Bluetooth** → Select controller
3. If it doesn't appear, power cycle the controller and try again

**MFi controllers:** Usually pair automatically when turned on near the device. If not, check Settings → Bluetooth.

### Controller Keeps Disconnecting

1. **Check battery** — Low battery is the #1 cause of disconnects
2. **Reduce Bluetooth interference** — Move WiFi routers, microwave ovens, and other Bluetooth devices away
3. **Apple TV: Use Ethernet** — Wired internet frees up the WiFi/Bluetooth antenna, improving stability
4. **Forget and re-pair** — Settings → Bluetooth → Tap (i) on controller → Forget This Device → Re-pair

### Buttons Not Responding or Wrong Mapping

1. **Update controller firmware** — Connect to PS5/Xbox console to update, or use the manufacturer's app (8BitDo Firmware Updater, etc.)
2. **Check MFi profile limitations** — MFi controllers lack Select/Start; Provenance maps L2 = Select, R2 = Start for systems that need them
3. **iCade controllers** — These use keyboard hacks and have limitations. Only one iCade controller can be used at a time. Cannot use iCade and MFi simultaneously.
4. **Restart the game** — Close and relaunch the current game

**Full guide:** [Controllers & Controls](../info/controllers-and-controls/controllers/README.md) | [Controller Recommendations](../info/controllers-and-controls/controllers/controller-reviews.md)

---

## iCloud Sync Issues

### Sync Not Working

**Requirements:**
- Active **Provenance Plus** subscription (Apple TV gets free CloudKit sync)
- Available iCloud storage
- Active internet connection on all devices
- Same Apple ID signed in on all devices

**Fixes:**
1. Toggle sync off and back on — Settings → iCloud Sync → OFF → wait 10 seconds → ON
2. Force quit Provenance and relaunch
3. Check iCloud storage — Settings → [Your Name] → iCloud (may be full)
4. Wait 10-15 minutes — Large libraries take time to sync initially

### Sync is Stuck or Slow

1. Force quit Provenance
2. Disable iCloud Sync in Provenance settings
3. Re-enable iCloud Sync
4. Restart device
5. Wait 10-15 minutes for the queue to process

### "Not Enough iCloud Storage"

1. Check usage: Settings → [Your Name] → iCloud → Manage Storage
2. Delete old device backups you no longer need
3. Upgrade iCloud plan ($0.99/month for 50 GB)
4. Disable sync for less-played systems to reduce usage

### Sync Conflicts Between Devices

- Only enable iCloud sync on **one version** of Provenance (don't sync both App Store and sideloaded versions)
- If using multiple devices, let one device finish syncing before starting the other
- If saves conflict, the most recent save wins

**Full guide:** [iCloud Sync Troubleshooting](../installation-and-usage/roms/advanced-management.md#troubleshooting-icloud-issues)

---

## Save Issues

### Battery Save Not Loading

- Filename must match exactly: `[ROM-Filename].sav`
- The save must be from the same region/version of the ROM — saves are not compatible across different ROM versions
- Try re-importing the save file

### Save States Not Working After Update

{% hint style="warning" %}
**Save state compatibility between app updates is NOT guaranteed.** Core updates can change how save states are stored, making old states incompatible.
{% endhint %}

**Best practices:**
- Before updating Provenance, launch important games and create **in-game saves** (battery saves) — these are more portable than save states
- Save states are tied to the specific emulator core version — switching cores means old states won't load
- Battery saves (`.sav` / `.srm`) are the safest long-term save format

### Save States from Other Emulators

Save states from RetroArch or other emulators generally won't work unless they use the **exact same core version**. Battery saves (`.srm`, `.sav`) are much more compatible across emulators.

**Full guide:** [Game Saves](../info/saves.md)

---

## Skin Issues

### Skin Not Showing in Browser

1. Check file extension — must be `.deltaskin`, not `.zip`
2. Verify system compatibility — not all skins support all systems (DS not supported; 3DS not supported on tvOS)
3. Force quit Provenance and reopen
4. Re-import the skin

### Skin Looks Corrupted or Glitchy

1. Re-download the skin (may have been corrupted during download)
2. Check device compatibility (some skins are iPhone-only or iPad-only)
3. Update Provenance to the latest version
4. Report to the skin creator via DeltaStyles or GitHub

### Buttons Don't Respond with Custom Skin

1. Check that the skin's `info.json` has correct button mappings
2. Toggle "Touch Controls" off and back on in Settings
3. Try a different skin to isolate if it's skin-specific
4. Restart the game

### Performance Slowdown with Skins

Complex skins with detailed graphics can add overhead. Try a simpler skin, close background apps, and disable CRT/Smoothing filters.

**Full guide:** [Skins Guide](../info/skins-guide.md)

---

## Installation Issues

### App Store

| Problem | Solution |
|---------|----------|
| "Not available in your region" | Use different Apple ID from supported region, or sideload instead |
| "Not enough storage" | Provenance needs ~2.5 GB + space for games. Free up 10+ GB recommended |
| Installation stuck | Force-close App Store → Restart device → Try again. Check [Apple System Status](https://www.apple.com/support/systemstatus/) |
| Crashes immediately on launch | Ensure iOS 16.0+ → Restart device → Delete and reinstall |

### Sideloading

| Problem | Solution |
|---------|----------|
| "Untrusted Developer" | Settings → General → VPN & Device Management → Trust your profile |
| App expires after 7 days | Free accounts expire weekly. Re-sign with AltStore/Sideloadly or upgrade to paid $99/year account |
| "App is already installed" | Delete existing version first, or use a different bundle ID |
| Cannot authenticate (2FA) | Create an App-Specific Password at appleid.apple.com → Security |
| Max App ID limit reached | Too many bundle IDs this week. Reuse an existing one, or use a different Apple ID |
| Duplicate app installed | Use the **same** bundle ID as original build to update in place |

### Building from Source

| Problem | Solution |
|---------|----------|
| `xcrun: error: unable to find utility "xcodebuild"` | Xcode → Preferences → Locations → Select Command Line Tools |
| Cycle in dependencies error | Clean Build Folder (Shift+Cmd+K) and delete DerivedData: `rm -rf ~/Library/Developer/Xcode/DerivedData` |
| Stuttering/slow after build | You built debug. Use `Provenance-Release` or `ProvenanceTV-Release` scheme |
| Missing submodules / Mupen error | Don't download .zip from GitHub. Clone with `git clone --recursive` |
| `Linking... Failed` | Clean Build Folder (Shift+Cmd+K) and rebuild |
| Signing certificate issues | Xcode → Preferences → Accounts → Manage Certificates → Delete old → Create new |

**Full guides:** [Building from Source](../installation-and-usage/installing-provenance/building-from-source.md) | [Sideloading](../installation-and-usage/installing-provenance/sideloading.md) | [Advanced FAQ](../installation-and-usage/installing-provenance/faqs-advanced.md)

---

## Large Library Issues

### Library Loading is Slow

1. Delete ROMs you no longer play
2. Optimize artwork — compress cover images under 500 KB
3. Clear cache: Settings → Advanced → Clear Cache
4. Restart device
5. Temporarily disable iCloud sync while loading

### Corrupted Database

**Symptoms:** Duplicated games, missing metadata, crashes on library screen.

**Fix (last resort — rebuilds your library index):**
1. Force quit Provenance
2. Open Files app → On My Device → Provenance
3. Delete the `Provenance.realm` file
4. Restart Provenance — the library will rebuild automatically (may take 10-30 minutes for large collections)

{% hint style="warning" %}
This does NOT delete your ROMs or saves — only the library index. Your games will be re-scanned and re-imported.
{% endhint %}

---

## Advanced Debugging

If you're comfortable with developer tools, you can dig deeper into issues:

### Viewing Crash Logs (iPhone/iPad)

1. Go to **Settings → Privacy & Security → Analytics & Improvements → Analytics Data**
2. Search for `Provenance` log files and tap to view
3. Use the share button to send logs to the [Discord](https://discord.gg/provenance) #help channel

### Live Logging with NSLogger (Preferred)

Provenance uses [CocoaLumberjack](https://github.com/CocoaLumberjack/CocoaLumberjack) for logging. You can view logs in real time using [NSLogger](https://github.com/fpillet/NSLogger/):

1. Download [NSLogger.app](https://github.com/fpillet/NSLogger/releases) on your Mac
2. Open NSLogger
3. Ensure your device and Mac are on the same network
4. Open Provenance on your device
5. The NSLogger window will populate automatically

**Tips:**
- Filter with the search bar (upper right)
- Filter by severity: Cmd+0 through Cmd+4 (0 = Error, 1 = Warning, 2 = Info, 3 = Debug, 4 = Verbose)
- Toggle the **f** button on the bottom toolbar to see source file and line numbers

### Crash Reports via Xcode

1. Open Xcode
2. **Window → Devices and Simulators**
3. Select your device (connect via USB if not available over WiFi)
4. Click **View Device Logs** (may take a minute to download)

### Live Logging via Xcode

1. Build and run Provenance from Xcode
2. If the console isn't visible: **View → Debug Area → Show Debug Area**
3. Provenance debug output will appear as you use the app

{% hint style="info" %}
The app must be started from within Xcode for live logging to work.
{% endhint %}

---

## Still Need Help?

1. **Search [GitHub Issues](https://github.com/Provenance-Emu/Provenance/issues)** — Your problem may already be reported
2. **Join [Discord](https://discord.gg/provenance)** — Live community support in the #help channel
3. **Report a bug** — Open a [new GitHub Issue](https://github.com/Provenance-Emu/Provenance/issues/new) with:
   - Device model and OS version
   - Provenance version (Settings → About)
   - Steps to reproduce the issue
   - Crash logs if available (see [Advanced Debugging](#advanced-debugging))
