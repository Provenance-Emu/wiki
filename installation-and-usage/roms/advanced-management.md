---
description: Advanced techniques for managing large ROM libraries
---

# Advanced ROM Management

This guide covers power-user workflows for managing 100+ games, multi-disc collections, custom metadata, backups, and optimization strategies for large libraries.

**For basic ROM importing**, see [Importing ROMs](importing-roms.md) | **For file formats**, see [Formatting ROMs](formatting-roms.md)

---

## Table of Contents

- [Managing Large Libraries](#managing-large-libraries)
- [Multi-Disc Games](#multi-disc-games-advanced)
- [Metadata & Artwork](#metadata--artwork-optimization)
- [iCloud Sync Strategies](#icloud-sync-for-large-collections)
- [Backup & Migration](#backup--migration)
- [ROM Hacks & Patches](#rom-hacks--patches)
- [Performance Optimization](#performance-optimization)

---

## Managing Large Libraries

### Organizational Strategies

**Recommended structure for 1000+ ROMs:**

```
ROMs/
├── NES/           (250 games)
├── SNES/          (300 games)
├── GBA/           (200 games)
├── PlayStation/   (150 games)
│   ├── Multi-Disc/     (Final Fantasy, Metal Gear Solid)
│   └── Single-Disc/    (Crash, Spyro)
└── N64/           (100 games)
```

**Benefits:**
- ⚡ Faster library loading (Provenance indexes by system)
- 🔍 Easier to find specific games
- ☁️ Better iCloud sync organization
- 📊 Clearer storage usage tracking

### Naming Conventions

**Use consistent naming for automatic metadata matching:**

✅ **Good:** `Final Fantasy VII (USA).chd`  
✅ **Good:** `Super Mario World (USA) (Rev 1).smc`  
❌ **Bad:** `ff7_disk1.bin`  
❌ **Bad:** `mario[!].sfc`

**Best practices:**
- Include region codes: `(USA)`, `(Europe)`, `(Japan)`
- Use No-Intro or Redump naming standards
- Avoid special characters: `[`, `]`, `!`, `+`
- Be consistent with revision markers: `(Rev 1)`, `(v1.1)`

**Why this matters:**
- 🎨 Automatic artwork matching via OpenVGDB
- 📝 Accurate metadata (publisher, release date, genre)
- 🌐 Better game database recognition
- 💾 Proper multi-disc grouping

### Filtering & Searching

**Use Provenance's search features:**

1. **Library Search** - Tap magnifying glass
   - Search by title, system, or genre
   - Filters: Favorites, Recently Played, System

2. **Custom Collections** (Favorites)
   - Long-press game → "Add to Favorites"
   - Quick access to frequently played games

3. **System-Specific Views**
   - Browse by console for focused game selection
   - Faster scrolling than mixed library view

**Pro tip:** Mark 10-20 favorite games for quick access - much faster than scrolling through 1000+ titles.

---

## Multi-Disc Games (Advanced)

### M3U Playlists

**What are M3U files?**  
Plain text files that group multi-disc games into a single library entry with disc-swapping support.

**Example: Final Fantasy VII**

Create `Final Fantasy VII (USA).m3u`:

```
Final Fantasy VII (USA) (Disc 1).chd
Final Fantasy VII (USA) (Disc 2).chd
Final Fantasy VII (USA) (Disc 3).chd
```

**How to create:**
1. Use a text editor (Notes, TextEdit, VS Code)
2. List each disc file (one per line)
3. Save as `.m3u` with the **same name** as disc 1
4. Import the M3U + all disc files into Provenance

**Supported systems:**
- ✅ PlayStation (most common use case)
- ✅ Sega CD
- ✅ Saturn
- ✅ PC Engine CD / TurboGrafx-CD
- ✅ PC-FX

### CHD Format (Recommended)

**What is CHD?**  
Compressed Hunks of Data - a lossless compression format that reduces disc images by 40-70%.

**Benefits:**
- 💾 **Massive space savings** (700MB BIN/CUE → 300MB CHD)
- ⚡ **Faster loading** (less data to read from storage)
- 📦 **Single file** (no more .cue + .bin + .sub mess)
- ✅ **Full compatibility** (PlayStation, Sega CD, Saturn, Dreamcast)

**Conversion:**

**Mac/Linux:**
```bash
# Install chdman (part of MAME tools)
brew install rom-tools

# Convert BIN/CUE to CHD
chdman createcd -i "game.cue" -o "game.chd"

# Batch convert all CUE files
for f in *.cue; do chdman createcd -i "$f" -o "${f%.cue}.chd"; done
```

**Windows:**
```powershell
# Download chdman.exe from MAME website
# Run in command prompt
chdman.exe createcd -i "game.cue" -o "game.chd"
```

**After conversion:**
1. Verify CHD loads in Provenance
2. Delete original BIN/CUE files
3. Update M3U playlists to reference `.chd` files

**Storage comparison (real examples):**

| Game | BIN/CUE | CHD | Savings |
|------|---------|-----|---------|
| Final Fantasy VII (3 discs) | 2.1 GB | 1.2 GB | 43% |
| Metal Gear Solid | 702 MB | 287 MB | 59% |
| Resident Evil 2 (2 discs) | 1.4 GB | 623 MB | 55% |

### Disc Swapping During Gameplay

**How to swap discs:**

1. **Open pause menu** (pause button)
2. **Tap "Change Disc"** (only appears for multi-disc games)
3. **Select the next disc** from the list
4. **Resume gameplay**

**When to swap:**
- Game prompts "Insert Disc 2"
- After major story progression (e.g., end of disc 1)
- For side content on bonus discs

**Pro tip:** Create save states **before** disc swap prompts - makes retrying easier if swap fails.

---

## Metadata & Artwork Optimization

### Automatic Metadata Matching

Provenance uses **OpenVGDB** to automatically fetch:
- 🎮 Game title (cleaned up)
- 🎨 Box art and screenshots
- 📅 Release date
- 🏢 Publisher/Developer
- 🎭 Genre

**To trigger re-matching:**
1. Long-press game in library
2. Tap "More Info"
3. Tap "Refresh Metadata"

**Improving match accuracy:**
- Use No-Intro or Redump naming standards
- Include region codes: `(USA)`, `(Japan)`
- Remove ROM hack tags: `[T+Eng]`, `[h1]`
- Verify ROM hash matches database (use `md5sum`)

### Custom Artwork

**Add your own box art/screenshots:**

1. Long-press game → **"Edit"**
2. Tap **"Artwork"** thumbnail
3. Choose source:
   - 📷 **Take Photo** - Capture physical box art
   - 🖼️ **Photo Library** - Use downloaded images
   - 📁 **Files** - Import from iCloud/Downloads
4. Crop and adjust
5. **Save**

**Recommended artwork specs:**
- **Format:** JPEG or PNG
- **Dimensions:** 512x512 minimum (1024x1024 ideal)
- **Aspect ratio:** Match original box art (varies by system)
- **File size:** Under 500KB for faster loading

**Where to find high-quality artwork:**
- [MobyGames](https://www.mobygames.com) - Comprehensive database
- [TheGamesDB](https://thegamesdb.net) - Community-curated
- [LaunchBox Database](https://gamesdb.launchbox-app.com) - High-res scans
- Physical box scans (your own collection)

### Metadata Editing

**Edit game information manually:**

1. Long-press game → **"Edit"**
2. Modify fields:
   - **Title** - Display name in library
   - **Publisher** - Company that released the game
   - **Developer** - Studio that created the game
   - **Release Date** - Original launch date
   - **Genre** - Category (RPG, Action, Platformer)
   - **Description** - Game summary

**Use cases:**
- 🎮 ROM hacks: `Super Mario World → Kaizo Mario World`
- 🌐 Fan translations: Add `(English Patched)` to title
- 🔧 Homebrew: Set proper developer credit
- 📝 Custom collections: Genre organization

---

## iCloud Sync for Large Collections

### Enable iCloud Sync (Provenance Plus)

**Requirements:**
- 📱 Provenance Plus subscription
- ☁️ Available iCloud storage (check Settings → [Your Name] → iCloud)
- 📶 WiFi connection (recommended for large libraries)

**Setup:**
1. Provenance → **Settings** → **iCloud Sync**
2. Toggle **ON**
3. Wait for initial upload (may take hours for 50+ GB)
4. Verify sync status: **Settings → iCloud Sync → Status**

### What Syncs?

✅ **Synced:**
- 🎮 ROM files
- 💾 Save states
- 🎯 Battery saves
- 🎨 Custom artwork
- 📝 Metadata edits
- 📁 BIOS files

❌ **Not synced:**
- 🎨 Skins (local only)
- ⚙️ App settings
- 🎮 Controller mappings

### Optimizing for Large Libraries

**Best practices:**

1. **Use CHD format** - 40-70% smaller files = faster sync
2. **Delete duplicates** - Remove (Europe) ROMs if you have (USA)
3. **Clean up old saves** - Delete unused save states
4. **Schedule uploads** - Enable sync overnight when on WiFi
5. **Monitor storage** - Check iCloud storage usage monthly

**Storage tiers:**
- 50 GB: $0.99/month - Fits ~200 games (CHD format)
- 200 GB: $2.99/month - Fits ~800 games
- 2 TB: $9.99/month - Fits entire collection + backups

**Sync speed expectations:**

| Library Size | Initial Upload | Incremental Sync |
|--------------|----------------|------------------|
| 10 GB (50 games) | 1-2 hours | 5-10 minutes |
| 50 GB (250 games) | 6-12 hours | 15-30 minutes |
| 200 GB (1000 games) | 24-48 hours | 30-60 minutes |

**Pro tip:** Import ROMs in batches of 20-30 games, let iCloud sync, then import next batch. Avoids overwhelming the sync queue.

### Troubleshooting iCloud Issues

**Sync stuck or slow:**
1. Force quit Provenance
2. Disable iCloud Sync
3. Re-enable iCloud Sync
4. Restart device
5. Wait 10-15 minutes for queue to process

**"Not enough iCloud storage":**
1. Check usage: Settings → [Your Name] → iCloud
2. Delete old device backups
3. Upgrade iCloud plan
4. Or disable iCloud sync for less-played systems

---

## Backup & Migration

### Backing Up Your Library

**Method 1: Mac/PC File Sharing (Best)**

1. Connect iOS device to Mac via USB
2. Open **Finder** → Select device
3. **Files** tab → **Provenance**
4. Drag **entire folder** to Mac desktop
5. Store backup on external drive or cloud storage

**Backup includes:**
- All ROMs
- Save states
- Battery saves
- BIOS files
- Custom artwork
- Metadata database

**Method 2: iCloud Drive (If Sync Enabled)**

Your data is already backed up to iCloud. To export:

1. Mac **Finder** → **iCloud Drive** → **Provenance**
2. Copy folder to external drive
3. Store as secondary backup

**Method 3: iTunes File Sharing (Legacy)**

On older Macs with iTunes:
1. iTunes → Device → **File Sharing**
2. Select **Provenance**
3. Save files to Mac

### Migrating to a New Device

**Transfer everything from old iPhone/iPad to new one:**

**Option A: iCloud Sync (Easiest)**
1. Old device: Enable iCloud Sync, wait for upload
2. New device: Install Provenance, log in with same Apple ID
3. Enable iCloud Sync → Wait for download
4. ✅ Done - library appears automatically

**Option B: Mac Backup/Restore**
1. Backup old device via Finder (see above)
2. Install Provenance on new device
3. Connect new device to Mac
4. Finder → New device → Files → Provenance
5. Drag backup folder into Provenance container
6. Restart Provenance on new device

**Option C: AirDrop (Small Libraries Only)**
1. Export ROMs from old device (Share → AirDrop)
2. On new device, accept files
3. Open in Provenance
4. Repeat for all games

---

## ROM Hacks & Patches

### Applying IPS/BPS Patches

**What are ROM patches?**  
Modification files that transform original ROMs into:
- 🌐 Fan translations (Japanese → English)
- 🎮 ROM hacks (Kaizo Mario, Pokémon randomizers)
- 🐛 Bug fixes (community patches)

**How to patch:**

**Mac/Linux:**
```bash
# Install Flips patcher
brew install flips

# Apply IPS patch
flips --apply "patch.ips" "original-rom.smc" "patched-rom.smc"

# Apply BPS patch (more reliable)
flips --apply "patch.bps" "original-rom.gba" "patched-rom.gba"
```

**Windows:**
- Download **Floating IPS (Flips)** or **Lunar IPS**
- Open patcher → Select original ROM → Select patch file → Apply
- Save output with descriptive name

**After patching:**
1. Import patched ROM into Provenance
2. Edit metadata to reflect patch name
3. Add custom artwork if desired

**Popular ROM hacks:**
- **Super Mario World** → Kaizo Mario World (extreme difficulty)
- **Pokémon FireRed** → Pokémon Unbound (new story)
- **Zelda: A Link to the Past** → Parallel Worlds (new dungeons)
- **Final Fantasy VI** → Brave New World (rebalanced)

---

## Performance Optimization

### Large Library Loading Speed

**If your library is slow to load:**

1. ✅ **Delete unused ROMs** - Remove games you never play
2. ✅ **Optimize artwork** - Compress images under 500KB
3. ✅ **Clear cache** - Settings → Advanced → Clear Cache
4. ✅ **Restart device** - Frees up memory
5. ✅ **Disable iCloud sync temporarily** - Re-enable after cleanup

### Database Maintenance

**Rebuild game database (if corrupted):**

⚠️ **Warning:** Only do this if library loading is broken

1. Force quit Provenance
2. Delete database file via Finder (Mac):
   - Connect device
   - Finder → Device → Files → Provenance
   - Delete `Provenance.realm` file
3. Restart Provenance
4. Library will rebuild (may take 10-30 minutes)

**Symptoms of corrupted database:**
- Games appear duplicated
- Metadata missing
- Artwork not loading
- Crashes on library screen

### Storage Management

**Find biggest files:**

1. Settings → General → iPhone Storage → Provenance
2. See total usage breakdown
3. Identify largest ROMs

**Systems ranked by typical storage:**

| System | Avg per Game | 100 Games |
|--------|--------------|-----------|
| NES | 200 KB | 20 MB |
| SNES | 2 MB | 200 MB |
| GBA | 8 MB | 800 MB |
| N64 | 12 MB | 1.2 GB |
| PlayStation (CHD) | 300 MB | 30 GB |
| Dreamcast (CHD) | 600 MB | 60 GB |
| PSP (ISO) | 1.2 GB | 120 GB |

**Space-saving tips:**
- 💾 Convert to CHD (PlayStation, Dreamcast, Saturn)
- 🗑️ Delete (Europe) duplicates if you have (USA)
- 📦 Use 7z compression for cartridge ROMs
- 🎮 Keep only games you actively play

---

## Quick Reference

### Essential Tools

**Mac:**
- **Flips** - ROM patcher (IPS/BPS)
- **chdman** - CHD converter
- **The Unarchiver** - Extract 7z, RAR

**Windows:**
- **Floating IPS** - ROM patcher
- **CHDman** - CHD converter
- **7-Zip** - Archive extraction

**Cross-platform:**
- **EmulationStation** - Test ROMs before importing
- **RomCenter** - ROM collection manager
- **ClrMAME Pro** - ROM verification

### File Format Cheat Sheet

| Format | System | Use Case |
|--------|--------|----------|
| `.chd` | PS1, Dreamcast, Saturn | **Best** - Compressed disc images |
| `.m3u` | PS1, Sega CD | **Required** - Multi-disc grouping |
| `.7z` | Cartridge ROMs | Compression (extract before import) |
| `.cue + .bin` | PS1, Sega CD | Legacy - Convert to CHD |
| `.iso` | PlayStation, PSP | Uncompressed - Convert to CHD |

### Common Issues & Solutions

| Problem | Solution |
|---------|----------|
| Multi-disc game shows 3 entries | Create M3U playlist |
| ROMs won't import | Check [Formatting ROMs](formatting-roms.md) |
| Metadata incorrect | Use proper naming convention |
| Library slow to load | Delete unused games, optimize artwork |
| iCloud sync stuck | Disable/re-enable sync |
| Duplicate games | Delete extras, rebuild database |

---

## Next Steps

- 📖 **[Importing ROMs](importing-roms.md)** - Basic import methods
- 📦 **[Formatting ROMs](formatting-roms.md)** - Supported file formats
- 🎨 **[Customizing ROMs](customizing-roms.md)** - Artwork and metadata basics
- 🔧 **[Applying Mods & Patches](mods.md)** - ROM modification guide
- ⚙️ **[Troubleshooting](../../help/troubleshooting.md)** - Fix common issues

---

**Managing a massive collection?** Join the [Provenance Discord](https://discord.gg/provenance) to share tips with other power users! 🎮

*Advanced features like iCloud sync require Provenance Plus. Multi-disc support and CHD format available in all versions.*
