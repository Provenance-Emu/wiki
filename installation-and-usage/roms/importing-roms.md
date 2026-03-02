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

## Uploading

1. Make sure your device's WiFi is turned on and connected to the _same network as your computer._
2. In Provenance: Turn on the Web Server:
   * Select the `+` button in the Game Library, or…
   * In Settings, select the `Import/Export` option.\)
3. Web Server Active. Make note of the `[device-ip]` 
   * Web UI: `http://[device-ip]`
   * WebDAV: `http://[device-ip]:81`

⏬ Mass-uploading ROM libraries or uploading multiple ROMs simultaneously is supported.  
↩️ [Restoring](../../info/miscellaneous/restoring-files.md) files \(ROMs, BIOS, Saves, Cover Art\) is also supported in both methods.

### Web Server UI

1. On computer, go to the URL `http://[device-ip]` in the pop-up dialog.
2. Open the directory corresponding to your build…
   * `roms` \(v1.4, previous\)
   * `Imports` \(v1.5+\)
3. Upload your ROMs…
   * `Upload Files…` _button allows multiple file selections._
   * _Drag & Drop is also supported._

### WebDAV Clients

1. On computer, open a WebDAV Client…
   * macOS Finder: `Menu Bar` → `Go` → `Connect to Server...`
2. Enter `http://[deviceip]:81` → `Connect as Guest` → Provenance mounts as a new drive.
3. Drag & Drop or Copy/Paste your ROMs into:
   * `roms` \(v1.4, previous\)
   * `Imports` \(v1.5+\)
4. _\(Optional\)_ tvOS: Enable Background Web Server option in Settings, if preferred.

{% hint style="info" %}
⏬ Mass-uploading is supported, just drag & drop multiple files.
{% endhint %}

## Downloading

1. Open a Mobile Browser \(Safari, Chrome, etc\)…
2. Navigate to your preferred ROM host site, find your ROM and download it.
3. Once downloaded, it will show the ROM file and tap either… 
   * `Open in "Provenance"` → Done. or…
   * `More…` and tap `Copy to Provenance` → Done.

## Copying

### Mobile Apps

1. Open app where ROMs are stored or accessible…
   * _Apple Files \(_[_iCloud Drive_](https://www.apple.com/icloud/icloud-drive)_,_ [_Dropbox_](https://apps.apple.com/us/app/dropbox/id327630330)_,_ [_Google Drive_](https://apps.apple.com/us/app/google-drive/id507874739)_,_ [_Nextcloud_](https://apps.apple.com/us/app/nextcloud/id1125420102)_,_ [_FileBrowser_](https://apps.apple.com/us/app/filebrowser-computers-cloud/id364738545)_, etc…\)_
2. Navigate to your ROMs directory and tap the ROM you wish to copy to Provenance _or_ its button that gets you to a `Share` or `Export` option, depending on the app.
3. Locate and tap `Copy to Provenance` option. Done.

### AirDrop

1. Open AirDrop window via macOS Finder.
2. Drag & Drop file\(s\) onto yourself/your device.
3. Locate and tap `Copy to Provenance` option. Done.

👤 If you don't see yourself in AirDrop, try setting to `Contacts Only` or `Everyone` on both devices.  
⏬ Mass-copying is supported, just drag & drop multiple files.

## Injecting

### ~~iTunes~~ (Discontinued)

⚠️ iTunes was discontinued with macOS Catalina (2019). iTunes File Sharing is no longer supported. Use **Finder** on macOS Catalina and later (connect device via USB, open Finder, select device, go to the Files tab), or use a third-party tool listed below.

### Other Tools

1. Connect device to computer and open [DiskAid](https://imazing.com/diskaid), [iExplorer](https://macroplant.com/iexplorer), [iPhone Explorer](https://www.macblurayplayer.com/iphone-explorer-mac.htm), or similar app… ↩️
2. Locate Provenance App.
3. Navigate to… 
   * `Documents/roms`  \(v1.4, previous…\)
   * `Documents/Imports`  \(v1.5+\)  

```text
 \(if the folder doesn't exist inside `Documents`, create it\)  
```

1. Drag your ROMs into the `roms` \(v1.4\) or `Imports` \(v1.5\) folder. Done.

↩️ [Restoring](../../info/miscellaneous/restoring-files.md) files \(ROMs, saves, cover art\) is usually supported in these apps…

## **💢 Troubleshooting**

* Multiple ROMs from one archive? You may be using a Region Pack ROM, meaning more than one version of the same ROM is in your archive. Unarchive the set, isolate single region ROM file\(s\), \[[re-archive](formatting-roms.md#archiving), and…\] re-import the single region ROM, individually.

## **⚠️ Known Issues**

* Sometimes _loose_ `.bin` for CD-based game files are picked up as Sega Genesis/MegaDrive ROMs. Please refer to [Multi-file ROMs](formatting-roms.md#multi-file-roms) and [Multi-disc Games](formatting-roms.md#multi-disc-games) \(v1.4\).
* CD-based, or multi-file ROMs and especially multi-disc games need to be uploaded and processed _one at a time_, until the Game Importer can be built to handle these in a queue. If yours are broken, it's best to delete the game\(s\) from the app UI, and delete any file remnants in the file system in ROMs \(com.provenance.\[system\]\) and from Imports using the WebUI, WebDav or an iOS file manager, and re-upload.
* Failed checksum ROMs \(translations, hacks, etc…\) will not be matched automatically.
* Exhaustive meta data web-scraping fallbacks to additional sources for meta data are _not_ currently implemented.
* Uploading ROMs + [Custom Cover Art](customizing-roms.md) in _one archive_ may not yield a replacement until the next time Provenance is quit \(with App Switcher\) and relaunched.

{% hint style="info" %}
🗯 If you are still stuck ask for [help](https://discord.gg/NhzgrXh) on our Discord.
{% endhint %}

