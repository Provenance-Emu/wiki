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

## ✨ Key Features

**Skins are 100% FREE for all users!** No Provenance Plus subscription required.

**Highlights:**
- ⚡ Fast rendering and loading
- 🔄 Smooth orientation changes
- 💾 Optimized memory usage
- 🎮 Full support for all RetroArch cores
- 📱 Works on iPhone, iPad, and Apple TV
- 🎨 **Multi-theme variants** — multiple color schemes in one skin file
- 🌊 **Animated backgrounds** — frame sequences, APNG, or GIF
- ⌨️ **Keyboard overlays** — for C64, Atari, ZX Spectrum and other keyboard systems
- 📳 **Per-button haptics** — custom haptic intensity per button

## Supported Systems

Skins work with **all systems except**:
- ❌ Nintendo DS (not currently supported)

**Fully supported systems include:**
- ✅ NES, SNES, N64
- ✅ Game Boy, GBC, GBA
- ✅ Nintendo 3DS (iOS/iPadOS/macOS only — not supported on tvOS)
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

{% tabs %}
{% tab title="Safari Download" %}
1. **Visit DeltaStyles.com** on your iPhone/iPad
2. **Browse by system** (e.g., Game Boy Advance)
3. **Tap "Download"** on a skin you like
4. Safari will download the `.deltaskin` file
5. **Tap the downloaded file** in Safari's download manager
6. **Select "Open in Provenance"**
7. ✅ Skin is now imported!
{% endtab %}

{% tab title="AirDrop" %}
1. Download skins on your Mac/another device
2. **AirDrop the `.deltaskin` files** to your iPhone/iPad
3. **Tap the file** when it arrives
4. **Select "Open in Provenance"**
{% endtab %}

{% tab title="Files App" %}
1. Save `.deltaskin` files to iCloud Drive or local storage
2. Open **Files app**
3. Navigate to the skin file
4. **Tap and hold** → **Share** → **Provenance**
{% endtab %}

{% tab title="Import via Settings" %}
1. Open **Provenance**
2. Tap **Settings** (gear icon)
3. Scroll to **Controller Skins**
4. Tap a system (e.g., "Game Boy Advance")
5. Tap **"+"** to import from Files app
{% endtab %}
{% endtabs %}

---

## How to Apply Skins

{% tabs %}
{% tab title="Global Default (Per System)" %}
Apply a skin to **all games** for a specific system:

1. Open **Provenance**
2. Tap **Settings** → **Controller Skins**
3. **Select a system** (e.g., "Super Nintendo")
4. **Tap the skin** you want to use
5. **Select "Set as Default"**
6. ✅ This skin will now be used for all SNES games
{% endtab %}

{% tab title="Per-Game Skin" %}
Apply a unique skin to a **specific game only**:

1. **Long-press a game** in your library
2. Tap **"Game Settings"**
3. Scroll to **Controller Skin**
4. **Select a skin** from the list
5. ✅ This game will now use that skin (overrides global default)
{% endtab %}

{% tab title="Switch Mid-Game" %}
Change skins without exiting your game:

1. While playing, **open the pause menu** (pause button)
2. Tap **Settings**
3. Tap **Controller Skin**
4. **Select a new skin**
5. Resume playing with the new skin applied
{% endtab %}
{% endtabs %}

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

**Performance tip:** The skin browser features smooth, responsive scrolling even with large collections.

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
    ├── preview.png    # Thumbnail for skin browser
    └── bg001.png      # (Optional) Animated background frames
```

### `info.json` Structure

```json
{
  "name": "My Custom Skin",
  "identifier": "com.yourname.myskin",
  "gameTypeIdentifier": "public.aoshuang.game.gba",
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

Common system identifiers for `info.json` — use the Provenance/ManicEmu identifiers (`public.aoshuang.game.*`) for broadest compatibility:

| System | Identifier |
|--------|------------|
| NES | `public.aoshuang.game.nes` |
| SNES | `public.aoshuang.game.snes` |
| Nintendo 64 | `public.aoshuang.game.n64` |
| Nintendo DS | `public.aoshuang.game.ds` |
| Game Boy | `public.aoshuang.game.gb` |
| Game Boy Color | `public.aoshuang.game.gbc` |
| Game Boy Advance | `public.aoshuang.game.gba` |
| PlayStation | `public.aoshuang.game.ps1` |
| PSP | `public.aoshuang.game.psp` |
| Sega Genesis / MD | `public.aoshuang.game.md` |
| Sega CD | `public.aoshuang.game.mcd` |
| Sega 32X | `public.aoshuang.game.32x` |
| Game Gear | `public.aoshuang.game.gg` |
| Dreamcast | `public.aoshuang.game.dc` |
| PC Engine / TG-16 | `public.aoshuang.game.pce` |
| Atari 2600 | `public.aoshuang.game.2600` |
| Atari 7800 | `public.aoshuang.game.7800` |
| Neo Geo | `public.aoshuang.game.neogeo` |
| Commodore 64 | `public.aoshuang.game.c64` |

Delta-compatible skins (`com.rileytestut.delta.game.*`) also work in Provenance.

**For a complete list**, check the [Provenance skin catalog](https://provenance-emu.com/skins/) source code.

---

## Advanced ManicSkin Features

Provenance supports advanced skin capabilities that go beyond static button layouts. These features are configured in `info.json` and give skin creators powerful new options.

{% hint style="info" %}
These features require the latest version of Provenance. Check [App Store](../installation-and-usage/installing-provenance/app-store.md) or [advanced installs](../installation-and-usage/installing-provenance/advanced.md) for the most current builds.
{% endhint %}

### Multi-Theme Variants

A single skin file can contain multiple visual themes (e.g., light mode / dark mode / game-specific palettes). Users select themes via a segmented control in the skin picker.

```json
{
  "name": "Lux GBA",
  "themes": [
    { "identifier": "dark",  "displayName": "Dark Mode" },
    { "identifier": "light", "displayName": "Light Mode" },
    { "identifier": "purple", "displayName": "Purple Haze" }
  ]
}
```

Each theme identifier corresponds to asset variants bundled inside the `.deltaskin` ZIP. The skin validator will catch missing theme assets before import.

### Animated Backgrounds

Skins can include animated backgrounds behind the game screen using frame sequences, APNG, or GIF files.

{% tabs %}
{% tab title="Frame Sequence" %}
```json
"backgroundAnimation": {
  "type": "frames",
  "frames": ["bg001.png", "bg002.png", "bg003.png", "bg004.png"],
  "fps": 12,
  "loops": 0
}
```
`loops: 0` means loop infinitely. Include the frame images inside your `.deltaskin` ZIP.
{% endtab %}

{% tab title="APNG / GIF" %}
```json
"backgroundAnimation": {
  "type": "apng",
  "source": "background.png"
}
```
Or for GIF:
```json
"backgroundAnimation": {
  "type": "gif",
  "source": "background.gif"
}
```
{% endtab %}
{% endtabs %}

**Supported `blendMode` values:** `normal`, `multiply`, `screen`, `overlay` (optional field, defaults to `normal`).

### Keyboard Overlay

For systems with keyboard input (Commodore 64, Atari 8-bit, ZX Spectrum, etc.), skins can include an on-screen keyboard overlay.

```json
"keyboardOverlay": {
  "layout": "full",
  "position": "bottom",
  "opacity": 0.85,
  "autoShow": true
}
```

**Layout variants:**

| `layout` | Description |
|----------|-------------|
| `full` | Standard QWERTY keyboard |
| `compact` | Condensed layout for smaller screens |
| `functionRow` | Function keys only (F1–F12) |
| `c64` | Commodore 64 key layout |
| `zxSpectrum` | ZX Spectrum key layout |
| `amstradCPC` | Amstrad CPC key layout |
| `atariST` | Atari ST key layout |

- `position`: `"top"` or `"bottom"` — where the keyboard appears on screen
- `autoShow`: `true` to show keyboard automatically when a text input is focused

### Per-Button Haptics

Individual buttons can have custom haptic feedback intensity, letting skin creators match haptic feel to button importance or game genre.

Add `hapticStrength` to any button mapping:

```json
"mappings": {
  "a": { "x": 280, "y": 380, "width": 60, "height": 60, "hapticStrength": "heavy" },
  "b": { "x": 340, "y": 320, "width": 60, "height": 60, "hapticStrength": "medium" },
  "start": { "x": 180, "y": 450, "width": 44, "height": 44, "hapticStrength": "light" }
}
```

**Haptic strength values:** `none`, `light`, `medium`, `heavy`, `rigid`, `soft`

### Skin Validator

Provenance automatically validates `.deltaskin` files on import:

- **Errors** (block import): missing `info.json`, invalid `gameTypeIdentifier`, referenced image files not found in ZIP, malformed JSON
- **Warnings** (shown after import): missing optional fields, deprecated field names, oversized assets

The validator helps skin creators catch issues before distributing their work.

---

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

**External skin creation guides:**
- **[Manic EMU Homemade Skin Guide](https://manicemu.site/Homemade-Skin-Guide-EN/)** — Extremely detailed guide covering press animations, custom function buttons, and advanced skin features (uses the same `.deltaskin` format)
- **[DeltaCore Skins Spec](https://github.com/rileytestut/DeltaCore/wiki/Skins)** — Official technical specification for the `.deltaskin` format (JSON schema, coordinate systems, image requirements)

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

<details>
<summary><strong>Skin Not Showing in Browser</strong></summary>

**Problem:** Imported skin doesn't appear in the skin list

**Solutions:**
1. ✅ **Check file extension** - Must be `.deltaskin` (not `.zip`)
2. ✅ **Verify system** - Skin must match a supported system (DS not yet supported; 3DS not supported on tvOS)
3. ✅ **Restart Provenance** - Force quit app and reopen
4. ✅ **Re-import** - Delete and re-download the skin

</details>

<details>
<summary><strong>Skin Looks Corrupted or Glitchy</strong></summary>

**Problem:** Buttons are misaligned, missing, or stretched

**Solutions:**
1. ✅ **Re-download skin** - File may have been corrupted during download
2. ✅ **Check device compatibility** - Some skins are iPhone-only or iPad-only
3. ✅ **Update Provenance** - Ensure you're on the latest version from the App Store
4. ✅ **Report to skin creator** - Leave feedback on DeltaStyles or GitHub

</details>

<details>
<summary><strong>Buttons Don't Respond</strong></summary>

**Problem:** Tapping skin buttons doesn't register input

**Solutions:**
1. ✅ **Check `info.json` mappings** - Button coordinates may be wrong
2. ✅ **Disable "Touch Controls"** - Settings → ensure touch controls are enabled
3. ✅ **Try a different skin** - Test if the issue is skin-specific
4. ✅ **Restart game** - Close and relaunch the game

</details>

<details>
<summary><strong>Performance Slowdown with Skins</strong></summary>

**Problem:** Game lags or stutters after applying a skin

**Solutions:**
1. ✅ **Use simpler skins** - Complex, high-resolution graphics add overhead
2. ✅ **Update to the latest version** - Contains skin performance improvements
3. ✅ **Close background apps** - Free up memory
4. ✅ **Disable visual filters** - Turn off CRT/Smoothing in settings

</details>

---

## Storage & File Management

### Where Are Skins Stored?

Skins are stored on your device in Provenance's app container.

**iCloud sync:** On Apple TV (tvOS), iCloud/CloudKit sync is included for free. On iPhone, iPad, and Mac, **Provenance Plus** is required for iCloud sync of skins, your game library, save states, BIOS files, and custom artwork. [Learn more about Provenance Plus →](../faqs.md#what-is-provenance-plus)

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

<details>
<summary><strong>Do skins work on Apple TV?</strong></summary>

Yes, for most systems! Skins render on Apple TV when using touch-based systems (though most users prefer physical controllers). Note: Nintendo 3DS skins are not supported on tvOS.

</details>

<details>
<summary><strong>Can I use the same skin on multiple systems?</strong></summary>

No — each skin is designed for a specific system's button layout (SNES skins won't work for GBA).

</details>

<details>
<summary><strong>Are animated skins supported?</strong></summary>

Yes! Animated backgrounds are supported via the `backgroundAnimation` field in `info.json`. Skin creators can use frame sequences (PNG), APNG, or GIF files. See [Animated Backgrounds](#animated-backgrounds) above.

</details>

<details>
<summary><strong>Do skins affect game performance?</strong></summary>

Minimal impact thanks to optimized rendering in current versions.

</details>

<details>
<summary><strong>Can I disable skins entirely?</strong></summary>

Yes — select the default "Standard" skin for any system to use Provenance's built-in controls.

</details>

<details>
<summary><strong>Where can I request a specific skin design?</strong></summary>

Check the [Provenance Discord](https://discord.gg/provenance) or r/EmulationOniOS — community designers often take requests!

</details>

---

## Next Steps

- 🎨 **[Browse skins at DeltaStyles →](https://deltastyles.com)**
- 🎮 **[Controllers & Controls Guide](controllers-and-controls/)** - Optimize your control setup
- 📱 **[Performance Optimization](performance-optimization.md)** - Get the best gameplay experience
- ⚙️ **[Troubleshooting Guide](../help/troubleshooting.md)** - Fix common issues

---

**Have an amazing skin to share?** Submit it to the [Skin Catalog](skin-catalog-contributing.md) so it appears in the built-in Skin Browser for everyone — or join the [Provenance community on Discord](https://discord.gg/provenance) and show off your creations!

*Update to the latest version from the App Store for the best skins experience.*
