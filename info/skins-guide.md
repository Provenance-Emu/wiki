---
description: Customize on-screen controls with skins for every system
---

# Skins Guide

**Skins** are custom controller overlays that let you personalize the look and feel of Provenance's on-screen controls. Choose from hundreds of community-created designs, from classic console aesthetics to modern minimalist layouts.

## What Are Skins?

Skins change the visual appearance of your on-screen controller buttons and d-pad while you play. Each skin is designed for a specific system (e.g., NES, Game Boy, PlayStation) and can completely transform your gaming experience.

**Examples of popular skin styles:**
- 🎨 **Console-accurate** - Recreates the original hardware's button layout and colors
- 🌈 **Custom colors** - Transparent, neon, retro themes
- 📱 **Minimalist** - Simple, clean buttons that don't obstruct gameplay
- 🎮 **Game-themed** - Styled after specific games (Pokémon, Mario, Sonic)
- 👻 **Invisible** - For Backbone/Kishi users who want physical controls only

## ✨ What's New (Version 3.2.0+)

**Skins are now 100% FREE for all users!** No Provenance Plus subscription required.

**Key improvements:**
- ⚡ Dramatically faster rendering and loading
- 🔄 Fixed rotation issues (smooth orientation changes)
- 💾 Optimized memory usage
- 🎮 Full support for all RetroArch cores
- 📱 Works on iPhone, iPad, and Apple TV

## Supported Systems

Skins work with **all systems except**:
- ❌ Nintendo 3DS (coming soon)
- ❌ Nintendo DS (coming soon)

**Fully supported systems include:**
- ✅ NES, SNES, N64
- ✅ Game Boy, GBC, GBA
- ✅ Genesis, Sega CD, Dreamcast
- ✅ PlayStation, PSP
- ✅ Atari, Neo Geo, TurboGrafx-16
- ✅ And 30+ more!

---

## How to Get Skins

### Download from DeltaStyles.com

[**DeltaStyles**](https://deltastyles.com) is the largest community repository for Provenance-compatible skins.

**What's available:**
- 🎨 Hundreds of free skins
- 🎮 Organized by system (NES, GBA, PlayStation, etc.)
- 🌈 Multiple color themes per system
- 👥 Community uploads and ratings

**File format:** `.deltaskin`

**Compatibility:** Provenance supports both **Delta skins** and **Manic skins** - they're the same format!

### Other Sources

- **PlayCase.gg** - Curated skin collection
- **Reddit** (r/EmulationOniOS) - Community-shared skins
- **Discord** - Provenance community often shares custom skins

---

## How to Import Skins

### Method 1: Direct Download (Safari)

1. **Visit DeltaStyles.com** on your iPhone/iPad
2. **Browse by system** (e.g., Game Boy Advance)
3. **Tap "Download"** on a skin you like
4. Safari will download the `.deltaskin` file
5. **Tap the downloaded file** in Safari's download manager
6. **Select "Open in Provenance"**
7. ✅ Skin is now imported!

### Method 2: AirDrop

1. Download skins on your Mac/another device
2. **AirDrop the `.deltaskin` files** to your iPhone/iPad
3. **Tap the file** when it arrives
4. **Select "Open in Provenance"**

### Method 3: Files App

1. Save `.deltaskin` files to iCloud Drive or local storage
2. Open **Files app**
3. Navigate to the skin file
4. **Tap and hold** → **Share** → **Provenance**

### Method 4: Import via Settings

1. Open **Provenance**
2. Tap **Settings** (gear icon)
3. Scroll to **Controller Skins**
4. Tap a system (e.g., "Game Boy Advance")
5. Tap **"+"** to import from Files app

---

## How to Apply Skins

### Set a Global Default (Per System)

Apply a skin to **all games** for a specific system:

1. Open **Provenance**
2. Tap **Settings** → **Controller Skins**
3. **Select a system** (e.g., "Super Nintendo")
4. **Tap the skin** you want to use
5. **Select "Set as Default"**
6. ✅ This skin will now be used for all SNES games

### Set a Skin for One Game

Apply a unique skin to a **specific game only**:

1. **Long-press a game** in your library
2. Tap **"Game Settings"**
3. Scroll to **Controller Skin**
4. **Select a skin** from the list
5. ✅ This game will now use that skin (overrides global default)

### Switch Skins Mid-Game

Change skins without exiting your game:

1. While playing, **open the pause menu** (pause button)
2. Tap **Settings**
3. Tap **Controller Skin**
4. **Select a new skin**
5. Resume playing with the new skin applied

---

## Skin Browser

Provenance includes a built-in **skin browser** for managing your collection:

**How to access:**
- Settings → Controller Skins → [System Name]

**Features:**
- 📸 **Preview thumbnails** - See what each skin looks like
- 🗑️ **Delete skins** - Swipe left to remove unwanted skins
- 🌟 **Mark favorites** - Star your most-used skins for quick access
- 📂 **Organize by system** - Automatic sorting by console

**Performance tip:** The skin browser in version 3.2.0+ is dramatically faster than previous versions. Scrolling through large collections is now smooth and responsive.

---

## Creating Custom Skins

### Can I Make My Own Skins?

**Yes!** Custom skin creation is supported, but it requires design tools and familiarity with the `.deltaskin` file format.

**What you need:**
- 🎨 **Image editor** (Photoshop, GIMP, Affinity Designer)
- 📐 **Understanding of JSON** (skin configuration file)
- 📱 **iOS device resolution knowledge** (different layouts for iPhone/iPad)

### File Structure

A `.deltaskin` file is actually a **ZIP archive** containing:

```
MySkin.deltaskin/
├── info.json          # Skin metadata (name, author, system)
├── portrait.png       # Portrait mode controller image
├── landscape.png      # Landscape mode controller image
├── edgeToEdge.png     # (Optional) Full-screen layout
└── assets/            # (Optional) Additional graphics
    └── preview.png    # Thumbnail for skin browser
```

### `info.json` Structure

```json
{
  "name": "My Custom Skin",
  "identifier": "com.yourname.myskin",
  "gameTypeIdentifier": "com.provenance.gba",
  "author": "Your Name",
  "version": "1.0",
  "orientation": "portrait",
  "mappings": {
    "a": { "x": 280, "y": 380, "width": 60, "height": 60 },
    "b": { "x": 340, "y": 320, "width": 60, "height": 60 },
    "dpad": { "x": 40, "y": 360, "width": 100, "height": 100 }
  }
}
```

**Key fields:**
- `gameTypeIdentifier` - System this skin is for (see [System Identifiers](#system-identifiers) below)
- `mappings` - Button positions (x, y coordinates + dimensions)
- `orientation` - "portrait", "landscape", or both

### System Identifiers

Common system identifiers for `info.json`:

| System | Identifier |
|--------|------------|
| NES | `com.provenance.nes` |
| SNES | `com.provenance.snes` |
| Game Boy | `com.provenance.gb` |
| Game Boy Color | `com.provenance.gbc` |
| Game Boy Advance | `com.provenance.gba` |
| Nintendo 64 | `com.provenance.n64` |
| Genesis | `com.provenance.genesis` |
| PlayStation | `com.provenance.psx` |
| PSP | `com.provenance.psp` |
| Dreamcast | `com.provenance.dreamcast` |

**For a complete list**, check the [Provenance GitHub wiki](https://github.com/Provenance-Emu/Provenance/wiki) or Delta's documentation.

### Tools for Skin Creation

**Recommended workflow:**
1. **Download an existing skin** as a template
2. **Unzip the `.deltaskin` file** (rename to `.zip` → extract)
3. **Edit PNG images** in your image editor
4. **Adjust `info.json` mappings** if needed
5. **Re-zip the folder** → rename to `.deltaskin`
6. **Import into Provenance** and test

**Advanced tools:**
- **Delta Skin Editor** (web-based tool) - Simplifies mapping button coordinates
- **Skin Template PSDs** - Pre-made Photoshop templates (search GitHub/Reddit)

---

## Tips & Best Practices

### For Best Performance

1. ✅ **Use optimized PNGs** - Compress images to reduce file size (tinypng.com)
2. ✅ **Avoid overly complex designs** - Simple graphics load faster
3. ✅ **Test on your device** - Preview how skins look at actual screen size
4. ✅ **Delete unused skins** - Keep your collection organized

### For Better Gameplay

1. 🎮 **Match button placement to your grip** - Different layouts feel better for different hand sizes
2. 🔆 **Consider transparency** - Semi-transparent buttons let you see more of the game
3. 📱 **Test both orientations** - Some games play better in portrait vs landscape
4. 👀 **Check button visibility** - Make sure buttons are easy to see against game graphics

### Popular Community Recommendations

**Best all-around skins (per DeltaStyles ratings):**
- **GBA:** "Atomic Purple" (classic transparent purple)
- **SNES:** "Classic Gray" (original SNES controller recreation)
- **PlayStation:** "DualShock" (authentic PS1 button layout)
- **Game Boy:** "DMG Original" (1989 gray brick aesthetic)

---

## Troubleshooting

### Skin Not Showing in Browser

**Problem:** Imported skin doesn't appear in the skin list

**Solutions:**
1. ✅ **Check file extension** - Must be `.deltaskin` (not `.zip`)
2. ✅ **Verify system** - Skin must match a supported system (3DS/DS not yet supported)
3. ✅ **Restart Provenance** - Force quit app and reopen
4. ✅ **Re-import** - Delete and re-download the skin

### Skin Looks Corrupted or Glitchy

**Problem:** Buttons are misaligned, missing, or stretched

**Solutions:**
1. ✅ **Re-download skin** - File may have been corrupted during download
2. ✅ **Check device compatibility** - Some skins are iPhone-only or iPad-only
3. ✅ **Update Provenance** - Older versions had skin rendering bugs (fixed in 3.2.0+)
4. ✅ **Report to skin creator** - Leave feedback on DeltaStyles or GitHub

### Buttons Don't Respond

**Problem:** Tapping skin buttons doesn't register input

**Solutions:**
1. ✅ **Check `info.json` mappings** - Button coordinates may be wrong
2. ✅ **Disable "Touch Controls"** - Settings → ensure touch controls are enabled
3. ✅ **Try a different skin** - Test if the issue is skin-specific
4. ✅ **Restart game** - Close and relaunch the game

### Performance Slowdown with Skins

**Problem:** Game lags or stutters after applying a skin

**Solutions:**
1. ✅ **Use simpler skins** - Complex, high-resolution graphics add overhead
2. ✅ **Update to 3.2.0+** - Massive skin performance improvements
3. ✅ **Close background apps** - Free up memory
4. ✅ **Disable visual filters** - Turn off CRT/Smoothing in settings

---

## Storage & File Management

### Where Are Skins Stored?

**Local storage only** - Skins are stored on your device in Provenance's app container.

**iCloud sync:** Skins do **not** currently sync via iCloud (ROMs and saves do, but not skins).

**File size:** Most skins are 500KB - 2MB each (negligible storage impact).

### How to Organize Many Skins

**Recommended workflow:**
1. **Delete unused skins** - Swipe left in skin browser
2. **Name skins clearly** - Use descriptive names when creating custom skins
3. **Keep backups** - Save favorite skins to iCloud Drive or Files app

### Sharing Skins

**How to share your custom skins:**
1. Export the `.deltaskin` file from Provenance
2. Upload to DeltaStyles.com (create free account)
3. Or share via AirDrop, Discord, Reddit

**Community etiquette:**
- 🙏 Credit original artists if you modify their work
- 📝 Include a preview screenshot when sharing
- 🔄 Share source files (PSD/Figma) for easier community remixing

---

## Frequently Asked Questions

**Q: Do skins work on Apple TV?**  
A: Yes! Skins render on Apple TV when using touch-based systems (though most users prefer physical controllers).

**Q: Can I use the same skin on multiple systems?**  
A: No - each skin is designed for a specific system's button layout (SNES skins won't work for GBA).

**Q: Are animated skins supported?**  
A: Not currently - only static PNG images.

**Q: Do skins affect game performance?**  
A: Minimal impact in version 3.2.0+ thanks to optimized rendering. Older versions had more overhead.

**Q: Can I disable skins entirely?**  
A: Yes - select the default "Standard" skin for any system to use Provenance's built-in controls.

**Q: Where can I request a specific skin design?**  
A: Check the [Provenance Discord](https://discord.gg/provenance) or r/EmulationOniOS - community designers often take requests!

---

## Next Steps

- 🎨 **[Browse skins at DeltaStyles →](https://deltastyles.com)**
- 🎮 **[Controllers & Controls Guide](controllers-and-controls/)** - Optimize your control setup
- 📱 **[Performance Optimization](performance-optimization.md)** - Get the best gameplay experience
- ⚙️ **[Troubleshooting Guide](../help/troubleshooting.md)** - Fix common issues

---

**Have an amazing skin to share?** Join the [Provenance community on Discord](https://discord.gg/provenance) and show off your creations! 🎨

*Skins feature available in Provenance 3.2.0 and later. Update to the latest version for best performance.*
