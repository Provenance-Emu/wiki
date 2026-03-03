---
description: Visual filters and shader effects for retro games — CRT, LCD, smoothing, and more
---

# Screen Filters & Shaders

Provenance includes built-in screen filters and shader support that let you enhance or authentically reproduce the look of retro games. From CRT scanlines to LCD grid effects, these filters transform how games are displayed.

---

## Overview

Provenance supports multiple types of visual filters:

| Type | Technology | Availability |
|------|-----------|-------------|
| **Built-in filters** | Custom Metal shaders | All cores |
| **LCD filters** | Custom Metal shaders | All cores |
| **RetroArch shaders** | Core-specific shader support | RetroArch-based cores |
| **PPSSPP filters** | Built-in to PPSSPP core | PSP games |

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

---

## Available Filters

### CRT Filters

Recreate the look of playing on a classic CRT television:

| Filter | Description |
|--------|-------------|
| **CRT Scanlines** | Horizontal dark lines simulating a CRT display |
| **CRT Curved** | Scanlines with barrel distortion (curved screen effect) |
| **CRT Shadow Mask** | Simulates the RGB phosphor pattern of CRT screens |

**Best for:** Console games (NES, SNES, Genesis, PS1) — these were designed for CRT displays and often look most authentic with CRT filters.

### LCD Filters

Simulate handheld LCD screens:

| Filter | Description |
|--------|-------------|
| **LCD Grid** | Visible pixel grid simulating a Game Boy or GBA screen |
| **LCD Ghosting** | Subtle motion blur mimicking slow LCD response times |

**Best for:** Handheld games (Game Boy, GBC, GBA, Game Gear, Lynx) — recreates the original handheld experience.

### Smoothing Filters

Reduce pixelation for a cleaner look:

| Filter | Description |
|--------|-------------|
| **Bilinear** | Basic smoothing that blurs pixels together |
| **Nearest Neighbor** | Sharp pixels with no smoothing (default) |

**Best for:** Players who prefer a clean, modern look — or those who want pixel-perfect sharpness.

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

| Filter Type | Performance Impact | Notes |
|------------|-------------------|-------|
| Nearest Neighbor | None | Default, no processing |
| Bilinear | Minimal | Standard GPU operation |
| CRT Scanlines | Low | Simple overlay effect |
| CRT Shadow Mask | Low-Medium | Per-pixel color processing |
| LCD Grid | Low | Grid overlay |
| RetroArch multi-pass | Medium-High | Depends on shader complexity |

{% hint style="info" %}
Built-in Metal filters are highly optimized and have minimal performance impact on modern devices. RetroArch multi-pass shaders may reduce performance on older devices.
{% endhint %}

---

## Tips

- **Match the filter to the system** — CRT for console games, LCD for handhelds, no filter for modern-style pixel art
- **Try before committing** — Change filters mid-game from the pause menu to compare
- **Disable on slower devices** — If you're getting frame drops on older hardware, switch to Nearest Neighbor
- **Per-game is powerful** — Set CRT for your SNES games but LCD for Game Boy, without changing anything globally

---

## Troubleshooting

<details>
<summary><strong>Filters not appearing in settings</strong></summary>

Make sure you're on the latest version of Provenance. Filter options are in Settings → Video / Display. If using a RetroArch core, additional shaders are in the RetroArch settings interface (accessible from the pause menu).

</details>

<details>
<summary><strong>Game runs slowly with filters enabled</strong></summary>

Complex shaders (especially RetroArch multi-pass) can impact performance on older devices. Try simpler filters (Bilinear, basic CRT Scanlines) or disable filters entirely. Built-in Metal filters have minimal overhead.

</details>

<details>
<summary><strong>Filter looks different in portrait vs landscape</strong></summary>

Some filters (like CRT scanlines) are orientation-dependent. The filter adjusts to the screen orientation automatically — horizontal scanlines in landscape, which matches real CRT behavior.

</details>

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
