---
description: 'How to rename, replace covert art and change other game info…'
---

# Customizing ROMs

ROMs in Provenance can be modified with the following customizations: _Cover Art, Title, Descriptions, Genre, Publisher, Release Date, Region, Play History_ — all fully editable from the Game Info View \(v1.5\) or with the following methods:

\*\*\*\*[**Replacing Cover Art**](customizing-roms.md#replacing-cover-art)  
**\*\*\[**Renaming Games  
**\]\(customizing-roms.md\#renaming\)\*\*\*\*\[**Editing Game Info\*\*\]\(customizing-roms.md\#editing-game-info\) · v1.5, _iOS only_

{% hint style="warning" %}
Please refer to the [Known Issues](customizing-roms.md#known-issues) regarding Customizing ROMs _before_ posting a new one.
{% endhint %}

## Replacing Cover Art

There are a couple methods of getting custom or replacement artwork into the app for iOS, and one for tvOS users, with a couple options, including single-drop mass-replacement:

* \*\*\*\*[**Pasting**](customizing-roms.md#pasting) \(from Mobile Browsers\) · for iOS _only_
* \*\*\*\*[**Uploading**](customizing-roms.md#uploading) \(via built-in Web Server\)° · for iOS & tvOS
  * Web Server UI 
  * WebDav Clients

° Mass-Replacing to restore Custom Art libraries or update multiple ROMs simultaneously is supported via Uploading _only_.

{% hint style="success" %}
**Requirements:**

* When uploading, _all_ of your image filenames _**must**_ match° your ROM filenames. \([Formatting](customizing-roms.md#images-left-behind2)\)
* _All_ image uploads _**must**_ be either `.png` or `.jpg` formats
{% endhint %}

° Images _without_ a matching ROM will stay in the directory until matched or deleted manually.

### Pasting

1. In iOS, locate an image 
   * _Mobile Browser, Apple Photos, Files \(iCloud Drive, Other Clouds, Remote Files apps, etc…_
   * Tap and hold or use whatever button gets you to… `Copy to Clipboard`
2. In Provenance \(iOS _only_\), lightly tap and hold for long press on the ROM you want to apply the replacement.
3. Select `Paste Custom Artwork`. Done.

### Uploading

1. Make sure your device's WiFi is turned on and connected to the _same network as your computer._
2. In Provenance: Turn on the Web Server:

   * Select the `+` button in the Game Library, or…
   * In Settings, select the `Import/Export` option.¹

   This is similar to [Importing ROMs](https://wiki.provenance-emu.com/installation-and-usage/roms/importing-roms).

#### Web Server UI <a id="exporting-footnote"></a>

1. On computer, go to the URL `http://[deviceip]` in the pop-up dialog.
2. Open the directory corresponding to your build…
   * `Cover Art` \(v1.4, previous\)
   * `Imports` \(v1.5+\)
3. Upload your images…
   * `Upload Files…` _button allows multiple file selections._
   * _Drag & Drop is also supported._

#### WebDav Clients

1. On computer, open a WebDav Client…
   * macOS Finder: `Menu Bar` → `Go` → `Connect to Server...`
2. Enter `http://[deviceip]:81` → `Connect as Guest` → Provenance mounts as a new drive.
3. Drag & Drop or Copy/Paste your images into:
   * `Cover Art` \(v1.4, previous\)
   * `Imports` \(v1.5+\)
4. _\(Optional\)_ tvOS: Enable Background Web Server option in Settings, if preferred.

¹ Exporting files \(ROMs, BIOS, Saves, Cover Art\) is also supported in both of the above methods.

**Mass-Replacing**

1. On Computer, store all your Custom Art files in _one folder._²
2. Update all ROMs with Custom Art all in one single drop into…
   * `Cover Art` \(v1.4, previous\)
   * `Imports` \(v1.5+\)

² Requires all the correct formatting requirements be met _before_ uploading.

### Formatting

* When uploading, _all_ of your image filenames _**must**_ match° your ROM filenames.
* _All_ image uploads _**must**_ be either `.png` or `.jpg` formats

**ROM\(s\):**

```text
[game].[romext]
```

**Image\(s\):**

Provenance v1.4, previous…

```text
[game].[romext].[imgext]
```

Provenance v1.5+:

```text
[game].[romext].[imgext] (Legacy format broken in beta. Do not use!)
or…
[game].[imgext]
```

{% hint style="info" %}
If images _do not_ have a matching ROM they will stay in the directory until it has a match or deleted manually.
{% endhint %}

## Renaming

1. In Provenance…
   * iOS: Tap & Hold for Long Press on the ROM you want to apply rename…
   * tvOS: Select ROM and Click/Press & Hold Remote or Controller Action Button…
2. Select `Rename` 
3. Type new name. `Done`

…or alternatively you can edit the game title the Game Info View _\(iOS only\)_

## Editing Game Info

1. In Provenance… on the ROM you wish to edit: 
   * Tap & Hold \(Long Press\), or… 
   * 3D Touch and Swipe Up to bring up Game Info¹
2. Tap & Hold \(Long Press\) on a field.
3. Type, Paste, or Reset.² `Done`

¹ Game Info requires v1.5+, Editing is supported in iOS _only_  
² Play History \(Play Count, Time Spent Playing\) can be reset, but not edited.

## **⚠️ Known Issues**

* Custom Cover Art [is not retained](https://github.com/Provenance-Emu/Provenance/issues/730) on Refresh Library option in Settings, _use at own risk._ \(you can always Mass Upload all of your custom artwork in one drop if you are using the Upload method \(instead of Pasting\), which is recommended, especially for large Custom Art libraries.
* Uploading ROMs + Custom Cover Art in one _archive_ may not yield a replacement until next Provenance quit/launch is cycled.
* Uploading Cover Art _before_ ROMs may not yield a replacement until next Provenance quit/launch is cycled.
* Custom Game Names are [not currently considered](https://github.com/Provenance-Emu/Provenance/issues/514) when doing Refresh Library.
* Exhaustive meta data web-scraping fallbacks to additional sources are _not_ currently implemented.
* Option to match ROMs manually or Search for Covers from within app is _not_ currently supported.
* Files with extra `.` in filename will cause a crash.

{% hint style="info" %}
🗯 If you are still stuck ask for [help](https://discord.gg/NhzgrXh) on our Discord.
{% endhint %}

