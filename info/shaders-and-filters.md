---
description: Visual filters and shader effects for retro games — CRT, LCD, VHS, Game Boy, and more
---

# Screen Filters & Shaders

Provenance includes built-in Metal screen filters that let you enhance or authentically reproduce the look of retro games. From CRT scanlines to LCD grids to VHS tape effects, these filters transform how games are displayed.

---

## Overview

Provenance supports multiple types of visual filters:

| Type | Technology | Availability |
|------|-----------|-------------|
| **Built-in filters** | Custom Metal shaders | All cores |
| **RetroArch shaders** | Core-specific shader support | RetroArch-based cores |
| **PPSSPP filters** | Built-in to PPSSPP core | PSP games |
| **Auto mode** | Automatic filter selection by screen type | All cores |

{% hint style="info" %}
**Coming soon:** Slang shader support (ported from RetroArch) is in active development, bringing hundreds of additional shader presets with a custom SwiftUI parameter preview and editing UI. Shaders are pre-converted to Metal for maximum performance.
{% endhint %}

---

## How to Apply Filters

### Global Filter Setting

Apply a filter to **all games**:

1. Open Provenance → **Settings**
2. Scroll to **Video / Display**
3. Select **Screen Filter**
4. Choose a filter from the list
5. The filter applies to all games immediately

### Per-Game Filter

Apply a filter to a **specific game only**:

1. **Long-press** a game in your library
2. Select **Game Settings**
3. Under **Video**, select **Screen Filter**
4. Choose a filter — this overrides the global setting for this game only

### Auto Mode

Provenance can **automatically select** the appropriate filter based on the emulated system's screen type:

| Screen Type | Auto Filter | Example Systems |
|-------------|------------|-----------------|
| **CRT** | Simple CRT or Complex CRT | NES, SNES, Genesis, PS1, N64 |
| **Color/Mono LCD** | LCD | GBA, Game Gear, Lynx, PSP |
| **Dot Matrix** | Game Boy | Game Boy, GBC |
| **Modern/Unknown** | None | — |

---

## Available Filters

### CRT Filters

Recreate the look of playing on a classic CRT television:

| Filter | Description | Configurable Parameters |
|--------|-------------|------------------------|
| **Simple CRT** | Lightweight CRT simulation — great balance of look and performance | Curvature, vignette, brightness, zoom |
| **Complex CRT** | Full-featured CRT with bloom, shadow mask, and TV line density | Bloom, scanlines, shadow mask, warp/curvature, gamma, TV line density |
| **Mega Tron** | CRT with mask intensity, scanline thinness, and Trinitron curve | Mask intensity, scanline thinness, scan blur, curvature, corner rounding |
| **ulTron** | CRT with hard scan/pixel effects and shadow mask | Hard scan, hard pixel, warp, shadow mask (dark/light), bright boost, bloom |

**Best for:** Console games (NES, SNES, Genesis, PS1, N64) — these were designed for CRT displays and look most authentic with CRT filters.

### LCD Filter

Simulate handheld LCD screens:

| Filter | Description | Configurable Parameters |
|--------|-------------|------------------------|
| **LCD** | Pixel grid simulation with ghosting and scanline effects | Grid density, grid brightness, contrast, saturation, ghosting, scanline depth, bloom |

**Best for:** Handheld games (GBA, Game Gear, Lynx, PSP) — recreates the original handheld LCD experience.

### Specialty Filters

| Filter | Description | Configurable Parameters |
|--------|-------------|------------------------|
| **Game Boy** | Dot-matrix LCD with classic 4-color green palette | Ghosting, contrast, scanline depth. Palette auto-adjusts based on screen type (dot matrix vs monochromatic LCD) |
| **VHS** | Animated VHS tape effect with noise and tracking artifacts | Noise, scanline jitter, color bleed, tracking noise, tape wobble, ghosting, vignette |

**Game Boy** is great for authentic DMG Game Boy aesthetics. **VHS** adds a fun retro TV recording look — the effect is animated with time-based noise and wobble.

---

## RetroArch Core Shaders

Games running on **RetroArch-based cores** can access additional shader options through the RetroArch settings interface:

1. Launch a game using a RetroArch core
2. Open the **pause menu**
3. Navigate to **RetroArch Settings** → **Shaders**
4. Browse and apply shader presets

RetroArch shaders offer more advanced effects including:
- Multi-pass shader chains
- Color correction and palette adjustments
- Phosphor glow effects
- Composite video simulation
- Integer scaling

---

## Performance Impact

| Filter | Performance Impact | Notes |
|--------|-------------------|-------|
| None (Nearest Neighbor) | None | Default, no processing |
| Simple CRT | Low | Lightweight — good for older devices |
| LCD | Low | Grid overlay + ghosting |
| Game Boy | Low | Palette swap + dot matrix |
| Complex CRT | Low-Medium | Bloom + shadow mask + multiple effects |
| Mega Tron / ulTron | Low-Medium | Multiple CRT effects |
| VHS | Medium | Animated — time-based noise and wobble |
| RetroArch multi-pass | Medium-High | Depends on shader complexity |

{% hint style="info" %}
All built-in Metal filters are highly optimized and have minimal performance impact on modern devices. RetroArch multi-pass shaders may reduce performance on older devices.
{% endhint %}

---

## Tips

- **Match the filter to the system** — CRT for console games, LCD for handhelds, Game Boy for DMG games, or use Auto mode
- **Try before committing** — Change filters mid-game from the pause menu to compare
- **Auto mode is smart** — It picks CRT, LCD, or Game Boy filter based on the system's original screen type
- **Disable on slower devices** — If you're getting frame drops on older hardware, use Simple CRT or disable filters
- **Per-game is powerful** — Set Complex CRT for your SNES games but Game Boy filter for GB, without changing anything globally
- **VHS for fun** — The animated VHS effect is great for screenshots and streams

---

## Troubleshooting

<details>
<summary><strong>Filters not appearing in settings</strong></summary>

Make sure you're on the latest version of Provenance. Filter options are in Settings → Video / Display. If using a RetroArch core, additional shaders are in the RetroArch settings interface (accessible from the pause menu).

</details>

<details>
<summary><strong>Game runs slowly with filters enabled</strong></summary>

Try simpler filters (Simple CRT, LCD) or disable filters entirely. The VHS filter and RetroArch multi-pass shaders are the most demanding. Built-in Metal filters have minimal overhead on iPhone 11+ and Apple TV 4K.

</details>

<details>
<summary><strong>Filter looks different in portrait vs landscape</strong></summary>

Some filters (like CRT scanlines) are orientation-dependent. The filter adjusts to the screen orientation automatically — horizontal scanlines in landscape, which matches real CRT behavior.

</details>

---

## See Also

- [In-Game Menu](in-game-menu.md) — Change filters mid-game from the pause menu
- [Performance Optimization](performance-optimization.md) — Filter impact on performance
- [Skins Guide](skins-guide.md) — Customize on-screen controls

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
