---
description: Get the best performance from Provenance across all systems and devices
---

# Performance Optimization Guide

Provenance is highly optimized for Apple devices, but performance can vary based on your device, the emulated system, and your settings. This guide helps you get smooth, full-speed emulation across all 38+ supported systems.

## Quick Performance Checklist

✅ **5-Minute Performance Boost:**

1. **Close background apps** - Double-tap Home, swipe up to close
2. **Disable visual effects** - Settings → Turn off Smoothing and CRT filters
3. **Use recommended cores** - See [per-system recommendations](#by-system) below
4. **Enable Low Power Mode** - For longer gaming sessions (slight performance trade-off)
5. **Update to latest version** - Performance improvements in every release

**Still slow?** Continue reading for system-specific optimizations.

---

## Understanding Performance

### What Affects Performance?

**Device Age (Most Important):**
- 📱 **iPhone 7 or newer** - Full speed for all systems up to PlayStation/N64
- 📱 **iPhone 6 or older** - Good for 8-bit and 16-bit systems, struggles with 3D
- 📱 **iPad Air 2 or newer** - Excellent for all supported systems
- 📺 **Apple TV 4K** - Best performance, especially for demanding systems like Dreamcast

**Emulated System Complexity:**
- 🟢 **Easy:** NES, Game Boy, SNES, Genesis (full speed on any device)
- 🟡 **Moderate:** GBA, PlayStation, N64 (requires iPhone 6s or newer)
- 🔴 **Demanding:** Dreamcast, PSP (requires iPhone 11 or newer / Apple TV 4K)

**App Settings:**
- ⚙️ **Visual filters** (Smoothing, CRT) add processing overhead
- ⚙️ **Save states** can cause brief frame drops when created
- ⚙️ **Audio sync** affects timing accuracy vs performance

---

## Device-Specific Recommendations

### iPhone

**Modern (iPhone 11 and newer):**
- ✅ All systems run at full speed
- ✅ Enable all visual enhancements without performance loss
- ✅ Dreamcast, PSP playable

**Mid-Range (iPhone 7-10):**
- ✅ All systems up to PlayStation/N64 at full speed
- ⚠️ Disable visual filters for demanding games
- ⚠️ Dreamcast/PSP may be slow

**Older (iPhone 6 and earlier):**
- ✅ 8-bit and 16-bit systems (NES, SNES, GB, GBA, Genesis)
- ⚠️ PlayStation and N64 require frameskip
- ❌ Dreamcast/PSP not recommended

### iPad

**Modern (iPad Air 3 / Pro 2018 and newer):**
- ✅ All systems at maximum performance
- ✅ Best screen size for retro gaming
- ✅ No compromises needed

**Mid-Range (iPad Air 2, iPad Mini 4, iPad 2017-2019):**
- ✅ All systems up to PlayStation/N64
- ⚠️ Some Dreamcast games may need frameskip

**Older (iPad 2, iPad Mini 1-3):**
- ✅ 8-bit and 16-bit systems only
- ❌ 3D systems (PlayStation, N64) too slow

### Apple TV

See the dedicated **[Apple TV / tvOS Guide](tvos-guide.md#performance-tips)** for detailed performance optimization on tvOS.

**Summary:**
- **Apple TV 4K (2nd/3rd gen):** Perfect performance, all systems
- **Apple TV 4K (1st gen):** Full speed up to N64/PlayStation
- **Apple TV HD:** Good for 16-bit and earlier systems

---

## Performance by System

### 8-Bit Systems (Full Speed Everywhere)

**Systems:** NES, Game Boy, Game Boy Color, Sega Master System, Game Gear, Atari 2600, Atari 7800, Atari Lynx

**Performance:** ✅ Full speed on all devices, including iPhone 5s and older

**Tips:**
- No optimization needed
- All visual filters work without slowdown
- Perfect for older devices and battery life

---

### 16-Bit Systems (Full Speed on iPhone 6+)

**Systems:** SNES, Genesis/Mega Drive, Sega CD, TurboGrafx-16, Neo Geo Pocket, WonderSwan

**Performance:** ✅ Full speed on iPhone 6 and newer

**Tips:**
- **SNES:** Some special chip games (Star Fox, Yoshi's Island) may be slow on older devices
- **Genesis:** Multiple cores available - use "Genesis Plus GX" for best compatibility
- **Sega CD:** Requires BIOS + CHD format for multi-disc games

**Optimization:**
- Disable CRT filter on iPhone 6/6s for consistent 60fps
- Use save states instead of in-game saves (faster loading)

---

### Portable Systems

#### Game Boy Advance

**Performance:** ✅ Full speed on iPhone 6s and newer

**Tips:**
- **Core:** Use "mGBA" core (most accurate, good performance)
- **Alternative:** "VBA-M" core for older devices (slightly faster)
- **Battery:** GBA games drain battery faster than GB/GBC (3D effects)

**Optimization:**
- Disable "Solar Sensor" if not using Boktai games (saves CPU)

#### Nintendo DS

**Performance:** ⚠️ Requires iPhone 8 or newer for full speed

**Tips:**
- **3D games** (Mario 64 DS, Mario Kart DS) need iPhone 11+ for smooth play
- **2D games** (Pokémon, Advance Wars) run well on iPhone 8-10
- **Screen layout:** Vertical layout recommended (one screen above the other)

**Optimization:**
- Lower internal resolution in settings (3x → 2x)
- Disable "High-Res 3D" for 3D games

#### PSP

**Performance:** 🔴 Requires iPhone 11 or newer

**Tips:**
- **Most demanding system** in Provenance
- Works best on iPhone 12 Pro or newer with active cooling
- Apple TV 4K recommended for best experience

**Optimization:**
- Set frameskip to "Auto" or "1" if needed
- Lower internal resolution to 2x (still looks great)
- Disable texture filtering if slow
- Close all background apps

---

### 3D Systems

#### Nintendo 64

**Performance:** 🟡 Full speed on iPhone 7 and newer

**Tips:**
- **Multiple cores available:** "Mupen64Plus" (recommended) and "ParaLLEl"
- **ParaLLEl core:** Better accuracy, requires iPhone 11+ for full speed
- **Mupen64Plus:** Faster, works on older devices

**Game-Specific:**
- ✅ **Works great:** Super Mario 64, Ocarina of Time, Mario Kart 64
- ⚠️ **Needs newer device:** Perfect Dark, Conker's Bad Fur Day, Donkey Kong 64
- ❌ **Problematic:** GoldenEye 007 (slowdown even on newest devices)

**Optimization:**
- Use "Rice" video plugin for older devices (faster but less accurate)
- Disable "widescreen hack" for performance
- Lower resolution multiplier: 2x → 1x (native N64 resolution)

#### PlayStation

**Performance:** ✅ Full speed on iPhone 7 and newer

**Tips:**
- **Best core:** "PCSX-ReARMed" (excellent compatibility + speed)
- **CHD support:** Multi-disc games work great in CHD format (faster loading)
- **Memory cards:** Provenance auto-creates, no setup needed

**Game-Specific:**
- ✅ **Perfect:** Final Fantasy VII-IX, Crash Bandicoot, Spyro, Metal Gear Solid
- ⚠️ **May need frameskip:** Ridge Racer Type 4, Gran Turismo 2

**Optimization:**
- Use CHD format instead of BIN/CUE (20-40% smaller, faster)
- Enable "Enhanced Resolution" on iPhone 11+ (sharper graphics, minimal performance hit)

#### Dreamcast

**Performance:** 🔴 Requires iPhone 11 or newer

**Tips:**
- Use **Reicast core**
- Apple TV 4K recommended for best experience
- Not all games are compatible (core still in development)

**Game-Specific:**
- ✅ **Works well:** Sonic Adventure, Crazy Taxi, Soulcalibur
- ⚠️ **Slow/buggy:** Shenmue, Jet Set Radio
- ❌ **Incompatible:** Some titles don't boot

**Optimization:**
- Disable "Widescreen" mode (adds overhead)
- Lower internal resolution if needed
- Use "Frameskip: Auto" for demanding games

---

## Advanced Optimization

### Battery Life vs Performance

**Best Battery Life:**
1. ✅ Enable **Low Power Mode** (Settings → Battery)
2. ✅ Lower screen brightness (biggest battery drain)
3. ✅ Play 8-bit/16-bit systems (NES, SNES, GB, Genesis)
4. ✅ Use wired headphones (Bluetooth drains faster)
5. ✅ Disable background app refresh for Provenance

**Battery Impact by System:**
- 🟢 **Low drain:** NES, GB, GBC, SNES, Genesis (~4-6 hours)
- 🟡 **Moderate:** GBA, PlayStation (~3-4 hours)
- 🔴 **High drain:** N64, Dreamcast, PSP (~2-3 hours)

### Visual Quality vs Performance

**Maximum Quality (iPhone 11+ recommended):**
- ✅ Smoothing filter ON
- ✅ CRT filter ON
- ✅ Enhanced resolution (PlayStation, N64)
- ✅ Shader effects (specific cores)

**Balanced (iPhone 7-10):**
- ⚙️ Smoothing: OFF
- ⚙️ CRT filter: OFF
- ⚙️ Enhanced resolution: ON (PlayStation only)

**Maximum Performance (iPhone 6 and older):**
- ❌ All filters OFF
- ❌ Native resolution only
- ❌ Frameskip: Auto

### Recommended Cores by System

When multiple cores are available, these are the best performance/compatibility balance:

| System | Recommended Core | Alternative | Notes |
|--------|------------------|-------------|-------|
| **Genesis** | Genesis Plus GX | PicoDrive | Plus GX = better accuracy |
| **SNES** | Snes9x | bsnes | Snes9x = faster |
| **GBA** | mGBA | VBA-M | mGBA = best accuracy |
| **N64** | Mupen64Plus | ParaLLEl | ParaLLEl needs iPhone 11+ |
| **PlayStation** | PCSX-ReARMed | Beetle PSX | ReARMed = faster |

---

## Troubleshooting Performance Issues

### Game is Slow or Stuttering

**Symptoms:** Framerate drops, audio crackling, sluggish controls

**Solutions (try in order):**

1. ✅ **Close background apps**
   - Double-tap Home button
   - Swipe up on all apps except Provenance

2. ✅ **Disable visual filters**
   - Provenance Settings → Smoothing: OFF
   - Provenance Settings → CRT Filter: OFF

3. ✅ **Check core selection**
   - In-game menu → Core Info
   - Try alternative core if available

4. ✅ **Lower internal resolution**
   - Settings → Video → Resolution Multiplier: 1x or 2x

5. ✅ **Enable frameskip**
   - Settings → Frameskip: Auto

6. ✅ **Restart device**
   - Power off → Wait 10 seconds → Power on

### Specific Game is Slow, Others Are Fine

**Cause:** Game-specific compatibility or CPU-intensive content

**Solutions:**
1. Check online compatibility lists for that core
2. Try alternative ROM dump (bad ROM = poor performance)
3. Some games are just demanding (GoldenEye 007, Conker, etc.)
4. Update to latest Provenance version (cores improve over time)

### Audio Crackling or Popping

**Cause:** CPU can't keep up with audio buffer

**Solutions:**
1. Enable frameskip (lets audio stay smooth)
2. Close background audio apps (Music, Spotify)
3. Disable Bluetooth audio (use wired headphones)
4. Lower in-game audio settings if available

### Performance Got Worse After Update

**Cause:** New settings default, cache issue, or regression

**Solutions:**
1. Check if new visual settings were enabled automatically
2. Delete and reinstall Provenance (backup saves first!)
3. Report regression on [GitHub Issues](https://github.com/Provenance-Emu/Provenance/issues)

---

## Performance Testing Results

### Real-World Benchmarks

Tested on **iPhone 12** with default settings:

| System | Test Game | FPS | Performance |
|--------|-----------|-----|-------------|
| NES | Super Mario Bros. 3 | 60/60 | ✅ Perfect |
| SNES | Super Metroid | 60/60 | ✅ Perfect |
| GBA | Metroid Fusion | 60/60 | ✅ Perfect |
| Genesis | Sonic 3 & Knuckles | 60/60 | ✅ Perfect |
| PlayStation | Final Fantasy VII | 60/60 | ✅ Perfect |
| N64 | Ocarina of Time | 60/60 | ✅ Perfect |
| N64 | GoldenEye 007 | 25-45/60 | ⚠️ Slow |
| Dreamcast | Sonic Adventure | 55-60/60 | ✅ Great |
| PSP | Crisis Core | 30-50/60 | ⚠️ Playable |

*Note: Results vary by device. iPhone 11 and newer recommended for 3D systems.*

---

## Tips from the Community

**From Discord/Reddit/App Store reviews:**

1. 💡 **"Airplane mode improves battery life by 30%"** - Disables background sync
2. 💡 **"CHD format loads 2-3x faster than BIN/CUE"** - Especially for multi-disc PlayStation games
3. 💡 **"Close Music app before playing"** - Prevents audio interference
4. 💡 **"Delete old save states"** - Too many save states can slow library loading
5. 💡 **"Use iPad for PSP games"** - Bigger screen + better cooling = smoother performance

---

## Next Steps

- ⚙️ **[Troubleshooting Guide](../help/troubleshooting.md)** - Fix common issues
- 🎮 **[Supported Systems](supported-systems.md)** - Full system compatibility list
- 📺 **[Apple TV Performance](tvos-guide.md#performance-tips)** - tvOS-specific optimization
- 📖 **[ROM Formatting](../installation-and-usage/roms/formatting-roms.md)** - Convert ROMs to optimal formats

---

**Still having performance issues?** Ask in the [Provenance Discord](https://discord.gg/provenance) or check the [FAQ](../faqs.md).
