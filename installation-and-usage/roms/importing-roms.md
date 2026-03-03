---
description: How to import ROMs into Provenance.
---

# Importing ROMs

Provenance supports multiple ways to import ROMs and BIOSes, including _single-drop_ mass-uploading:

* ⬆️  [**Uploading**](importing-roms.md#uploading)¹ \(via built-in Web Server\) · for iOS & tvOS
  * Web Server UI
  * WebDav Clients
* ⬇️  [**Downloading**](importing-roms.md#downloading) \(from Mobile Browsers\) · for iOS _only_
* ➡️  [**Copying**](importing-roms.md#copying) · for iOS _only_
  * Mobile Apps
  * AirDrop · macOS → iOS¹ _or_  iOS → iOS
* ⤵️  [**Injecting**](importing-roms.md#injecting) \(with Desktop Apps\) · for iOS and ATV4 _only_
  * ~~iTunes~~ (discontinued; use Finder on macOS or third-party tools)
  * Other Tools

¹ Mass-uploading ROM libraries or uploading multiple ROMs simultaneously is supported.²  
² Avoid mass-uploading multi-disc ROMs.

{% hint style="success" %}
**Requirements**

* 🛑 _All_ ROMs _**must**_ be [formatted correctly](formatting-roms.md) before importing. \([Formatting ROMs](formatting-roms.md)\)
* ☑️ Certain systems _**require**_ [BIOS](../bios-requirements.md) files in order to play ROMs. \([BIOS Requirements](../bios-requirements.md)\)
{% endhint %}

{% hint style="warning" %}
Please refer to the [Known Issues](importing-roms.md#known-issues) regarding Importing ROMs, and read [Issues Usage](https://github.com/Provenance-Emu/Provenance/wiki/Issues-Usage) _before_ posting a new one.
{% endhint %}

💢 If you run into any problems, check out [Troubleshooting](importing-roms.md#troubleshooting).

{% tabs %}
{% tab title="⬆️ Uploading (Web Server)" %}
**For iOS & tvOS** · Supports mass-uploading

1. Make sure your device's WiFi is turned on and connected to the _same network as your computer._
2. In Provenance: Turn on the Web Server:
   * Select the `+` button in the Game Library, or…
   * In Settings, select the `Import/Export` option.
3. Web Server Active. Make note of the `[device-ip]`:
   * Web UI: `http://[device-ip]`
   * WebDAV: `http://[device-ip]:81`

**Web Server UI:**
1. On computer, go to `http://[device-ip]` in your browser.
2. Open the `Imports` folder.
3. Upload ROMs — `Upload Files…` button supports multiple file selections, and Drag & Drop works too.

**WebDAV Clients:**
1. macOS Finder: `Menu Bar` → `Go` → `Connect to Server...`
2. Enter `http://[device-ip]:81` → `Connect as Guest` → Provenance mounts as a new drive.
3. Drag & Drop or Copy/Paste ROMs into the `Imports` folder.

↩️ [Restoring](../../info/miscellaneous/restoring-files.md) files (ROMs, BIOS, Saves, Cover Art) is also supported via both methods.
{% endtab %}

{% tab title="⬇️ Downloading (Browser)" %}
**For iOS only**

1. Open a Mobile Browser (Safari, Chrome, etc).
2. Navigate to your preferred ROM host site, find your ROM and download it.
3. Once downloaded, tap the ROM file and choose:
   * `Open in "Provenance"` → Done. or…
   * `More…` → `Copy to Provenance` → Done.
{% endtab %}

{% tab title="➡️ Copying (Files/AirDrop)" %}
**For iOS only**

**From Mobile Apps:**
1. Open app where ROMs are stored or accessible (Apple Files, [iCloud Drive](https://www.apple.com/icloud/icloud-drive), [Dropbox](https://apps.apple.com/us/app/dropbox/id327630330), [Google Drive](https://apps.apple.com/us/app/google-drive/id507874739), [Nextcloud](https://apps.apple.com/us/app/nextcloud/id1125420102), [FileBrowser](https://apps.apple.com/us/app/filebrowser-computers-cloud/id364738545), etc.)
2. Navigate to your ROM and tap `Share` or `Export`.
3. Tap `Copy to Provenance`. Done.

**Via AirDrop:**
1. Open AirDrop window via macOS Finder.
2. Drag & Drop file(s) onto yourself/your device.
3. Tap `Copy to Provenance`. Done.

👤 If you don't see yourself in AirDrop, try setting to `Contacts Only` or `Everyone` on both devices.
⏬ Mass-copying is supported — drag & drop multiple files.
{% endtab %}

{% tab title="⤵️ Injecting (Desktop)" %}
**For iOS and Apple TV 4 only**

⚠️ iTunes was discontinued with macOS Catalina (2019). Use **Finder** on macOS Catalina+ (connect device via USB, open Finder, select device, go to the Files tab), or use a third-party tool:

**Third-party tools:**
1. Connect device to computer and open [DiskAid](https://imazing.com/diskaid), [iExplorer](https://macroplant.com/iexplorer), [iPhone Explorer](https://www.macblurayplayer.com/iphone-explorer-mac.htm), or similar app.
2. Locate Provenance App.
3. Navigate to `Documents/Imports`. Create the folder if it doesn't exist.
4. Drag your ROMs into the folder. Done.

↩️ [Restoring](../../info/miscellaneous/restoring-files.md) files (ROMs, saves, cover art) is usually supported in these apps.
{% endtab %}
{% endtabs %}

## Troubleshooting & Known Issues

<details>
<summary><strong>Multiple ROMs from one archive?</strong></summary>

You may be using a Region Pack ROM, meaning more than one version of the same ROM is in your archive. Unarchive the set, isolate single region ROM file(s), [re-archive](formatting-roms.md#archiving), and re-import the single region ROM individually.

</details>

<details>
<summary><strong>Loose .bin files detected as wrong system</strong></summary>

Sometimes loose `.bin` files for CD-based games are picked up as Sega Genesis/MegaDrive ROMs. Use `.cue + .bin` pairs or `.chd` format instead. See [Multi-file ROMs](formatting-roms.md#multi-file-roms) and [Multi-disc Games](formatting-roms.md#multi-disc-games).

</details>

<details>
<summary><strong>CD-based / multi-disc ROMs breaking on import</strong></summary>

CD-based, multi-file ROMs and especially multi-disc games need to be uploaded and processed _one at a time_. If yours are broken, delete the game(s) from the app UI, delete any file remnants in the file system (ROMs and Imports folders) using the WebUI, WebDAV, or a file manager, and re-upload.

</details>

<details>
<summary><strong>ROM metadata not matching</strong></summary>

- Failed checksum ROMs (translations, hacks, etc.) will not be matched automatically.
- Exhaustive metadata web-scraping fallbacks are not currently implemented.
- Uploading ROMs + [Custom Cover Art](customizing-roms.md) in one archive may not yield a replacement until Provenance is quit and relaunched.

</details>

{% hint style="info" %}
🗯 If you are still stuck ask for [help](https://discord.gg/provenance) on our Discord.
{% endhint %}

