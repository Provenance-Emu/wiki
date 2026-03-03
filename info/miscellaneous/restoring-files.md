---
description: How to back up and restore ROMs, saves, BIOS files, and other data
---

# Restoring Files

Whether you're switching devices, reinstalling Provenance, or migrating from a sideloaded build to the App Store version, this guide covers how to back up and restore your data.

---

## What Can Be Backed Up?

| Data | Location | Notes |
|------|----------|-------|
| **Battery saves** (in-game saves) | `Battery/` | Most important — these are your actual game progress |
| **Save states** | `Save States/` | Quick-save snapshots; may not survive app version changes |
| **ROMs** | `com.provenance.[system]/` folders | Your game files |
| **BIOS files** | `BIOS/` | System firmware files |
| **Cover art** | `Custom Artwork/` | Any custom images you've added |
| **Controller skins** | Skins storage | Custom `.deltaskin` files |

{% hint style="warning" %}
**Save states are not guaranteed to be compatible across app versions.** Core updates can break save state compatibility. Always create **in-game saves** (battery saves) before updating Provenance.
{% endhint %}

---

## Option 1: iCloud Sync (Easiest)

If you use **Provenance Plus**, iCloud automatically syncs your library, saves, BIOS files, custom artwork, and skins across all your devices.

**What syncs:**
- ROMs and game library
- Battery saves and save states
- BIOS files
- Controller skins
- Custom cover art
- Settings and preferences

**How to enable:**
1. Open Provenance → Settings
2. Enable **iCloud Sync**
3. Data syncs automatically in the background

**Restoring on a new device:**
1. Install Provenance from the App Store
2. Sign in with the same Apple ID
3. Subscribe to Provenance Plus (or restore your subscription)
4. Enable iCloud Sync — your library will download automatically

{% hint style="info" %}
**Apple TV users:** iCloud/CloudKit sync is included free — no Provenance Plus subscription required.
{% endhint %}

---

## Option 2: Manual Backup via Files App (iOS/iPadOS)

### Backing up

1. Open the **Files** app on your device
2. Navigate to **On My iPhone** (or **On My iPad**) → **Provenance**
3. You'll see folders like `Battery/`, `Save States/`, and system-specific ROM folders
4. **Select the folders you want to back up** → tap **Share** → save to:
   - iCloud Drive
   - A computer via AirDrop
   - Any cloud storage (Dropbox, Google Drive, etc.)

### Restoring

1. Install Provenance (fresh install or update)
2. **Launch Provenance once** and open a game briefly — this creates the folder structure
3. Open the **Files** app → navigate to **Provenance**
4. Copy your backed-up files back into the matching folders:
   - Battery saves → `Battery/`
   - Save states → `Save States/`
   - ROMs → import via normal [import methods](../../installation-and-usage/roms/importing-roms.md)

{% hint style="warning" %}
**Do NOT rename files.** ROM filenames must match exactly — Provenance links saves to ROMs by filename. If a filename changes, the app won't associate your saves with the correct game.
{% endhint %}

---

## Option 3: Manual Backup via Web Server

Best for **bulk transfers** and **Apple TV** (which doesn't have the Files app).

### Backing up

1. Open Provenance → tap **+** (or Settings → Import/Export) to start the Web Server
2. Note the IP address shown (e.g., `http://192.168.1.42`)
3. On your computer:

{% tabs %}
{% tab title="Web Browser" %}
1. Go to `http://[device-ip]` in your browser
2. Browse to `Battery/`, `Save States/`, and ROM folders
3. Download the files you need
{% endtab %}

{% tab title="WebDAV (Finder/Explorer)" %}
1. **Mac:** Finder → Go → Connect to Server → `http://[device-ip]:81`
2. **Windows:** Map Network Drive → `http://[device-ip]:81`
3. Connect as Guest
4. Provenance mounts as a drive — copy files to your computer
{% endtab %}
{% endtabs %}

### Restoring

1. Start the Web Server in Provenance (same steps as above)
2. Upload your files back:
   - **ROMs and BIOS:** Upload to the `Imports/` folder — Provenance auto-sorts them
   - **Battery saves:** Place directly into `Battery/`
   - **Save states:** Place directly into `Save States/`

---

## Option 4: Desktop File Manager (USB)

For direct USB access to Provenance's files:

1. Connect your device to your computer via USB
2. **macOS (Catalina+):** Open **Finder** → select your device → **Files** tab → **Provenance**
3. **Windows/older macOS:** Use a third-party tool:
   - [iMazing](https://imazing.com/) (recommended)
   - [iExplorer](https://macroplant.com/iexplorer)
   - [DiskAid](https://imazing.com/diskaid)
4. Browse Provenance's file structure and copy files in either direction

---

## Migrating Between Install Methods

### Sideloaded → App Store

The App Store and sideloaded versions use **separate data directories**. To migrate:

1. **Back up** from the sideloaded version (Files app, Web Server, or USB — see above)
2. **Delete** the sideloaded version
3. **Install** from the App Store
4. **Restore** your backed-up files into the new installation
5. If using Provenance Plus, enable iCloud Sync to prevent future data loss

### App Store → Sideloaded (or vice versa with different Bundle IDs)

Same process — back up, install the new version, restore files.

---

## Folder Structure Reference

```
Provenance/
├── Imports/              ← Drop ROMs and BIOS here for auto-import
├── Battery/              ← In-game saves (most important!)
├── Save States/          ← Quick-save state files
├── BIOS/                 ← System firmware files
│   └── com.provenance.[system]/
├── Custom Artwork/       ← User-added cover art
└── com.provenance.[system]/  ← ROM storage by system
    ├── com.provenance.nes/
    ├── com.provenance.snes/
    ├── com.provenance.gba/
    └── ...
```

---

## Troubleshooting

<details>
<summary><strong>Saves don't appear after restoring</strong></summary>

- Verify filenames match exactly (including extensions and capitalization)
- Launch the game once to create the folder structure, then quit and place your save files
- Force quit Provenance and reopen to refresh the database

</details>

<details>
<summary><strong>Save states crash or don't load</strong></summary>

Save states are tied to specific emulator core versions. If you've updated Provenance (or switched cores), old save states may be incompatible. **Battery saves** (in-game saves) are always compatible — use those for long-term game progress.

</details>

<details>
<summary><strong>ROMs show as "Unknown" after restoring</strong></summary>

Provenance matches ROMs by checksums (MD5/CRC). If you see unmatched games:
1. Long-press the game → **Game Settings** → manually assign the system
2. Or delete and re-import the ROM through the standard [import process](../../installation-and-usage/roms/importing-roms.md)

</details>

<details>
<summary><strong>Can't access Provenance folder in Files app</strong></summary>

- Make sure you're looking under **On My iPhone/iPad**, not iCloud Drive (unless you have iCloud Sync enabled)
- If the Provenance folder doesn't appear, launch and quit Provenance once to create it
- Check Settings → Provenance → ensure file access is enabled

</details>

---

{% hint style="success" %}
**Best practice:** Enable **Provenance Plus iCloud Sync** and let backups happen automatically. For extra safety, create in-game saves (not just save states) for your most important games.
{% endhint %}
