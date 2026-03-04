---
description: Complete guide to using Provenance on Apple TV and tvOS
---

# Provenance on Apple TV

Provenance is the premier multi-system emulator for Apple TV, bringing classic gaming to the big screen with support for **38+ game systems** from Atari to PlayStation. This guide covers everything you need to know to get the best experience on tvOS.

## Why Provenance on Apple TV?

✨ **Unique Features:**
- 🎮 **Native tvOS app** - Built specifically for big-screen gaming
- 🎯 **Full controller support** - PlayStation, Xbox, MFi, and Siri Remote
- ☁️ **iCloud sync** - Seamlessly continue games across iPhone, iPad, and Apple TV
- 📱 **TopShelf integration** - Quick access to recently played games
- 🏆 **Premium performance** - All Apple TV models run classic systems at full speed

**Supported on:** Apple TV HD (4th gen), Apple TV 4K (all generations)

---

## Getting Started

### Installation

**From the App Store (Recommended):**
1. Open the **App Store** on your Apple TV
2. Search for **"Provenance"**
3. Download and install (100% free)
4. Optional: Upgrade to **Provenance Plus** for iCloud sync ($3.99/month, $39.99/year, or $99.99 lifetime)

**Alternative:** [Sideload from Xcode](../installation-and-usage/installing-provenance/sideloading.md) (requires Mac + Apple Developer account)

### First Launch

1. **Grant permissions** - Allow file access when prompted
2. **Pair a controller** (recommended) - See [Controller Setup](#controller-setup) below
3. **Add BIOS files** - Some systems require BIOS (see [BIOS Requirements](../installation-and-usage/bios-requirements.md))
4. **Import ROMs** - See [Importing ROMs](#importing-roms) below

---

## Controller Setup

### Supported Controllers

Provenance supports nearly every modern game controller on Apple TV:

**Recommended Controllers:**
- 🎮 **PlayStation 4/5 DualShock/DualSense** - Best overall compatibility
- 🎮 **Xbox One/Series X|S Controller** - Excellent button mapping
- 🍎 **MFi (Made for iOS) Controllers** - Native Apple support
- 📱 **Siri Remote** (tvOS 17+) - Basic control for simple games

**Not Recommended:**
- ⚠️ Siri Remote on older tvOS - Limited buttons, awkward for most games

### Pairing Your Controller

**PlayStation or Xbox Controller:**
1. Put controller in pairing mode:
   - **PS4/PS5:** Hold **Share + PS** button until light flashes
   - **Xbox:** Hold **Pairing** button until Xbox logo flashes
2. On Apple TV: **Settings** → **Remotes and Devices** → **Bluetooth**
3. Select your controller from the list
4. ✅ Controller is now paired!

**MFi Controller:**
- Usually pairs automatically when turned on near Apple TV
- If not: Settings → Remotes and Devices → Bluetooth → Select controller

### Controller Tips

- 🔋 **Battery:** Most controllers last 8-12 hours per charge
- 🔄 **Multi-device:** Controllers can pair with multiple devices (hold pairing button to switch)
- 📶 **Range:** Bluetooth range ~30 feet / 10 meters (line of sight)
- ⚡ **Latency:** Wired Ethernet connection improves Bluetooth performance (see [Performance Tips](#performance-tips))

---

## Importing ROMs

### Method 1: iCloud Sync (Provenance Plus)

If you have Provenance Plus and multiple Apple devices:

1. **On iPhone/iPad:**
   - Import ROMs using [any standard method](../installation-and-usage/roms/importing-roms.md)
   - Enable iCloud sync in Provenance settings
2. **On Apple TV:**
   - Open Provenance
   - Your library will automatically sync via iCloud
   - ✅ All saves and game states sync across devices!

### Method 2: Direct Transfer

**Via AirDrop (easiest):**
1. On Mac/iPhone: Select ROM files
2. AirDrop to your Apple TV
3. Open files in Provenance

**Via File Sharing (Finder):**
1. Connect Apple TV to Mac via USB-C
2. Open **Finder** → Select Apple TV
3. **Files** tab → Drag ROMs to **Provenance**
4. ROMs appear in library on next app launch

**Via Xcode (for developers):**
1. Connect Apple TV to Mac
2. In Xcode: **Window** → **Devices and Simulators**
3. Select Apple TV → **Installed Apps** → **Provenance**
4. Drag ROMs into the file container

### Method 3: Cloud Services

- Import from **Dropbox, Google Drive, OneDrive** via Files app
- Select ROM → **Share** → **Provenance**

---

## Best Systems for Big-Screen Gaming

### Highly Recommended (Perfect on TV)

These systems were designed for TVs and translate perfectly to Apple TV:

- 🎮 **Nintendo 64** (1996-2002) - *Super Mario 64, GoldenEye 007, The Legend of Zelda: Ocarina of Time*
- 🎮 **PlayStation** (1994-2006) - *Final Fantasy VII, Crash Bandicoot, Metal Gear Solid*
- 🎮 **Sega Dreamcast** (1998-2001) - *Sonic Adventure, Shenmue, Crazy Taxi*
- 🎮 **SNES** (1990-2003) - *Super Metroid, Chrono Trigger, Super Mario World*
- 🎮 **Sega Genesis** (1988-1997) - *Sonic the Hedgehog, Streets of Rage 2, Phantasy Star IV*

### Also Great

- 🕹️ **Arcade** (MAME, FinalBurn Neo) - *Street Fighter II, Pac-Man, Metal Slug*
- 🎮 **NES** - *Super Mario Bros. 3, The Legend of Zelda, Metroid*
- 🎮 **Game Boy Advance** - Better on TV than you'd expect! (*Metroid Fusion, Pokémon Emerald*)

### Less Ideal for TV

- 📱 **Game Boy / Game Boy Color** - Tiny screen designed for handhelds, hard to see on TV
- 📱 **DS / 3DS** - Dual-screen layouts don't translate well to single TV screen

---

## Performance Tips

### Optimize for Big-Screen Gaming

**Reduce Input Latency:**
1. 🌐 **Use Ethernet instead of WiFi** - Dramatically improves Bluetooth controller performance
2. 📺 **Enable "Game Mode" on your TV** - Reduces display lag (check TV settings)
3. 🎨 **Turn off Dolby Vision** - Adds processing delay (Settings → Video and Audio)
4. 🔌 **Disconnect unused Bluetooth devices** - Reduces interference
5. 📡 **Position Apple TV in open space** - Avoid thick walls, metal objects near device

**Graphics & Performance:**
- ⚙️ **Disable "Smoothing" and "CRT filters"** - Slight performance gain (Provenance Settings)
- 🎞️ **Use native resolution** - Don't force 4K upscaling on non-4K TVs

**System-Specific:**
- **N64 on older Apple TV HD:** Some games may need frameskip enabled
- **PlayStation:** Runs full speed on all Apple TV models
- **Dreamcast:** Requires Apple TV 4K for best performance

### Expected Performance

| Apple TV Model | Recommended Systems | Performance Notes |
|---------------|---------------------|-------------------|
| **Apple TV 4K (2nd/3rd gen)** | All systems up to PlayStation/N64/Dreamcast | Full speed, no compromises |
| **Apple TV 4K (1st gen)** | All systems up to PlayStation/N64 | Dreamcast playable, some slowdown |
| **Apple TV HD (4th gen)** | All systems up to PlayStation | N64 mostly full speed with minor slowdown |

---

## Provenance Plus on Apple TV

**iCloud Library & Save Sync:**
- 🎮 Start a game on iPhone during your commute
- 🏠 Continue exactly where you left off on Apple TV at home
- 💾 All save states, game saves, and settings sync automatically
- 📚 Your entire ROM library syncs across devices

**Other Plus Features:**
- 🔔 Early access to new cores and features
- 🛠️ Priority support
- 📬 TestFlight beta access

**Cost:** $3.99/month or $39.99/year (App Store free trial available for subscriptions), or $99.99 lifetime

---

## TopShelf Integration

Provenance integrates with tvOS TopShelf for quick access to your games:

**What is TopShelf?**
- The top row of your Apple TV home screen
- Shows your most recently played games
- Launch games directly without opening Provenance first

**How to Use:**
1. Move Provenance to the **top row** of your Apple TV home screen
2. Swipe to Provenance (don't open it)
3. See your recently played games in the expanded TopShelf view
4. Select a game to launch directly into gameplay

---

## Troubleshooting

### Controller Not Pairing

**Problem:** Controller won't connect or keeps disconnecting

**Solutions:**
1. ✅ **Forget and re-pair:**
   - Settings → Remotes and Devices → Bluetooth → Select controller → Forget Device
   - Re-pair from scratch
2. ✅ **Check battery:** Low battery causes connection issues
3. ✅ **Reduce interference:** Move WiFi routers, microwave ovens away from Apple TV
4. ✅ **Update firmware:** PS5/Xbox controllers may need firmware updates (connect to console first)
5. ✅ **Use Ethernet:** Wired connection improves Bluetooth stability

### Games Running Slow or Stuttering

**Problem:** Lag, framerate drops, audio stuttering

**Solutions:**
1. ✅ **Check build type:** App should say "Provenance" not "Prov Debug" (debug builds are slow)
2. ✅ **Disable visual effects:** Turn off Smoothing, CRT filters in settings
3. ✅ **Enable Game Mode on TV:** Check your TV's picture settings
4. ✅ **Close other apps:** Double-tap TV button, swipe up to close unused apps
5. ✅ **Restart Apple TV:** Hold Home button → Sleep, then wake Apple TV

### iCloud Sync Not Working

**Problem:** Games or saves not syncing between devices

**Solutions:**
1. ✅ **Verify Provenance Plus:** Active subscription required for sync
2. ✅ **Check iCloud storage:** Settings → Accounts → iCloud → Manage Storage (need available space)
3. ✅ **Enable iCloud in Provenance:** App Settings → iCloud Sync → ON (on all devices)
4. ✅ **Check network:** iCloud sync requires active internet connection
5. ✅ **Force sync:** Close and reopen Provenance to trigger manual sync

### ROM Not Showing in Library

**Problem:** Imported ROM doesn't appear

**Solutions:**
1. ✅ **Check file format:** See [supported formats](../installation-and-usage/roms/formatting-roms.md)
2. ✅ **Verify ROM hash:** Corrupted downloads won't import (re-download)
3. ✅ **Check BIOS:** Some systems require BIOS files (see [BIOS Requirements](../installation-and-usage/bios-requirements.md))
4. ✅ **Re-import:** Delete and re-add the ROM
5. ✅ **Restart app:** Force quit Provenance and relaunch

### Black Screen After Launching Game

**Problem:** Game starts but shows only black screen (audio may work)

**Solutions:**
1. ✅ **BIOS missing:** PlayStation, Sega CD, Saturn, Dreamcast require BIOS files
2. ✅ **Try different ROM:** File may be corrupted
3. ✅ **Update cores:** Settings → Core Management → Check for updates
4. ✅ **Report bug:** If persistent, report on [GitHub Issues](https://github.com/Provenance-Emu/Provenance/issues)

---

## Advanced: Dark Mode

Provenance respects tvOS system-wide Dark Mode:

**Enable Dark Mode:**
1. Apple TV **Settings** → **General** → **Appearance**
2. Select **Dark ✓**
3. Provenance UI will update automatically

---

## Tips for the Best Experience

### For Multiplayer

- 🎮 **Pair multiple controllers** - Up to 4 players (system-dependent)
- 👥 **Use same controller types** - Mixing controllers can cause mapping issues
- 🔋 **Check all batteries** - Nothing worse than dying mid-game!
- 📖 **Full guide:** [Multiplayer](multiplayer.md)

### For Save States

- 💾 **Use incremental saves** - Create multiple save states per game
- ☁️ **iCloud backup** - Enable iCloud sync to never lose progress
- 🎯 **Quick save before bosses** - Save state right before difficult sections

### For Streaming/Recording

- 📺 **Use AirPlay** - Stream your Apple TV to Mac for recording
- 🎥 **Built-in screen recording** - Requires Xcode + connected Mac
- 🎬 **Capture cards** - HDMI capture cards work great with Apple TV 4K

---

## See Also

- [BIOS Requirements](../installation-and-usage/bios-requirements.md) — Required system files
- [Importing ROMs](../installation-and-usage/roms/importing-roms.md) — Add games to your library
- [Controllers & Controls](controllers-and-controls/) — Full controller compatibility list
- [Multiplayer](multiplayer.md) — Local and online play guide
- [Performance Optimization](performance-optimization.md) — System-specific optimization
- [Provenance Plus](provenance-plus.md) — iCloud sync details
- [Troubleshooting](../help/troubleshooting.md) — Common issues and solutions

---

**Enjoy retro gaming on the big screen! 🎮📺**

*For support, visit the [Provenance Discord](https://discord.gg/provenance) or check the [FAQ](../faqs.md).*
