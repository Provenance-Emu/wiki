---
description: 'How to format, convert, archive, or batch process ROMs.'
---

# Formatting ROMs

To avoid any issues with [Importing ROMs](https://github.com/Provenance-Emu/Provenance/wiki/Importing-ROMs), check to make sure your files are formatted correctly.

* ✅  [**Supported Formats**](formatting-roms.md#supported-formats)\*\*\*\*
  * [ROMs](formatting-roms.md#roms) · _by system_
  * [ROM Archives](formatting-roms.md#rom-archives)
  * [Multi-file ROMs](formatting-roms.md#multi-file-roms)
  * [Multi-disc Games](formatting-roms.md#multi-disc-games)
* 🔀  [**Converting Formats**](formatting-roms.md#converting-formats)\*\*\*\*
  * [Converting ROMs](formatting-roms.md#converting-roms)
  * [Editing Memory Cards](formatting-roms.md#converting-and-editing-memory-cards)
  * [UnECM](formatting-roms.md#unecm) · _restore original format from_ `.ecm` _files_
* ⏬  [**Archiving**](formatting-roms.md#archiving)\*\*\*\*
* ⏩  [**Batching**](formatting-roms.md#batching) · _batch renaming and \(re\)archiving_

{% hint style="warning" %}
Please refer to the [Known Issues](formatting-roms.md#known-issues) regarding Formatting ROMs, and read [Issues Usage](https://github.com/Provenance-Emu/Provenance/wiki/Issues-Usage) _before_ posting a new one.
{% endhint %}

## Supported Formats

### ROMs

| Manufacturer | System | Supported Format\(s\) / Extensions |
| :--- | :--- | :--- |


| Atari | 2600 | `.a26` _\(.bin\)_ |
| :--- | :--- | :--- |


|  | 5200 | `.a52` _\(.bin\)_ |
| :--- | :--- | :--- |


|  | 7800 | `.a78` _\(.bin\)_ |
| :--- | :--- | :--- |


|  | Jaguar | `.j64`, `.jag` _\(.bin, .rom\)_ |
| :--- | :--- | :--- |


|  | Lynx | `.lnx` |
| :--- | :--- | :--- |


| Bandai | WonderSwan | `.ws` |
| :--- | :--- | :--- |


|  | WonderSwan Color | `.wsc` |
| :--- | :--- | :--- |


| NEC | PC Engine / TurboGrafx-16 | `.pce` |
| :--- | :--- | :--- |


|  | PC Engine Super CD-ROM² System / TurboGrafx-CD | `.cue + .bin/iso`, `.ccd + .img + .sub` _multi-file ROM_ |
| :--- | :--- | :--- |


|  | PC Engine SuperGrafx |  |
| :--- | :--- | :--- |


|  | PC-FX | `.cue + .bin/iso`, `.ccd + .img + .sub` _multi-file ROM_ |
| :--- | :--- | :--- |


<table>
  <thead>
    <tr>
      <th style="text-align:left">Nintendo</th>
      <th style="text-align:left">
        <p>Famicom /</p>
        <p>Nintendo Entertainment System</p>
      </th>
      <th style="text-align:left"><code>.nes</code>
      </th>
    </tr>
  </thead>
  <tbody></tbody>
</table>

|  | Famicom Disk System | `.fds` |
| :--- | :--- | :--- |


|  | Game Boy | `.gb` |
| :--- | :--- | :--- |


|  | Super Famicom / Super Nintendo Entertainment System | `.snes`, `.smc`, `.sfc`, `.fig` |
| :--- | :--- | :--- |


|  | Game Boy Color | `.gbc`, `.sgb` |
| :--- | :--- | :--- |


|  | Virtual Boy | `.vb` |
| :--- | :--- | :--- |


|  | Nintendo 64 | `.n64`, `.z64` |
| :--- | :--- | :--- |


|  | Game Boy Advance | `.gba` |
| :--- | :--- | :--- |


|  | Pokemon mini | `.min` |
| :--- | :--- | :--- |


| Sega | SG-1000 | `.sg` |
| :--- | :--- | :--- |


|  | Master System | `.sms` |
| :--- | :--- | :--- |


|  | Mega Drive / Genesis | `.md`, `.smd`, `.gen` _\(.bin\)_ |
| :--- | :--- | :--- |


|  | Game Gear | `.gg` |
| :--- | :--- | :--- |


|  | Mega CD / Sega CD | `.cue + .bin` _multi-file ROM_ |
| :--- | :--- | :--- |


|  | 32X | `.32X`, `.32x` |
| :--- | :--- | :--- |


|  | Saturn | `.iso`, `.cue + .bin/iso`, `.ccd + .img + .sub`, `.mds + .mdf` _multi-file ROM_ |
| :--- | :--- | :--- |


| SNK | Neo Geo Pocket | `.ngp` |
| :--- | :--- | :--- |


|  | Neo Geo Pocket Color | `.ngc`, `.ngpc`, `.npc` |
| :--- | :--- | :--- |


| Sony | Playstation | `.cue + .bin/img/iso`, `.ccd + .img + .sub` _multi-file ROM_ |
| :--- | :--- | :--- |


* DO NOT rename multi-file ROMs unless you alter `.cue` file contents as well.
* _All_ multi-file ROMs _**must**_ be contained in a single-file archives.°  \([Instructions](formatting-roms.md#multi-file-roms)\)
* _All_ multi-disc games _**must**_ include a `.m3u` file in their archive.  \([Instructions](formatting-roms.md#multi-disc-games)\)

° Though not required, it's recommended to archive _all_ ROMs, individually.

### ROM Archives

| Supported Formats |
| :--- |
| `.zip`, `.7z` |

{% hint style="danger" %}
Loose files _only_. DO NOT contain folder\(s\) within an archive \(this is a known issue and will result in a crash\)!
{% endhint %}

### Multi-file ROMs

A ROM consisting of multiple files such as `.bin` + `.cue` for CD-based games \(Sega CD, Playstation, etc…\) _**must**_ be contained together in a _single_ `.zip` or `.7z` archive _before_ importing and _both files are required_.¹

**Examples of ROM archive contents:**

```text
    [game].bin
    [game].cue
```

```text
    [game] (Track 1).bin
    [game] (Track 2).bin
    [game].cue
```

```text
    [game].ccd
    [game].img
    [game].sub
```

{% hint style="warning" %}
If **.ccd** based ROMs are not importing correctly, move files into the system directory, manually, when left behind in Imports or Conflicts.
{% endhint %}

{% hint style="danger" %}
Loose files _only_. DO NOT contain folder\(s\) within an archive \(this is a known issue and will result in a crash\)!
{% endhint %}

#### **.cue Files:**

`.cue` files are plain text and will generally look something like this \(unless it specifies additional audio track details\). The name of the referenced file: `.bin`, `.img`, `.iso`… specified file _**must**_ match verbatim the name of the actual file.²

**Contents of \[game\].cue**:

```text
FILE "[game].bin" BINARY
  TRACK 01 MODE2/2352
    INDEX 01 00:00:00
```

¹ If you need to restore a missing/damaged `.cue` file, check out the archives at [redump.org](http://redump.org).  
² If you rename any files of a`.cue` based multi-file ROM, you _**must**_ change the contents of the `.cue` file _or they won't work._

…archive filenames, however, are irrelevant as they are discarded after unarchiving.

{% hint style="info" %}
For a quick way to preview **.cue** files on macOS, install the [qlstephen QuickLook plugin](https://github.com/whomwah/qlstephen/releases).
{% endhint %}

### Multi-disc Games

All multi-disc games _**must**_ include a `.m3u` file _in_ their `.zip` or `.7z` multi-file ROM archive. Disc numbering in filenames needs to be formatted _exactly_ as: `…(Disc #).ext`

{% hint style="warning" %}
If renaming and using **\*\*a** .cue **based \*\***ROM make sure to read the requirements for **.cue** files in [Multi-file ROMs](formatting-roms.md#multi-file-roms).
{% endhint %}

**Contents of Final Fantasy VII \(USA\).7z**:

```text
    Final Fantasy VII (USA) (Disc 1).bin
    Final Fantasy VII (USA) (Disc 1).cue
    Final Fantasy VII (USA) (Disc 2).bin
    Final Fantasy VII (USA) (Disc 2).cue
    Final Fantasy VII (USA) (Disc 3).bin
    Final Fantasy VII (USA) (Disc 3).cue
    Final Fantasy VII (USA).m3u
```

`.m3u` files can be created as plain text and _**must**_ _contain_ and _match exactly_ the names of _all_ and _only_ the `.cue` or `.ccd` files for the game.³

**Contents of Final Fantasy VII \(USA\).m3u**:

```text
Final Fantasy VII (USA) (Disc 1).cue
Final Fantasy VII (USA) (Disc 2).cue
Final Fantasy VII (USA) (Disc 3).cue
```

³ `.m3u` filenames are independent of the `.bin/.cue` files, but a truncated name is recommended, removing " \(Disc \#\)" from the .m3u filename \(including the space\).

{% hint style="info" %}
For a quick way to preview **.m3u** files on macOS, install the [qlstephen QuickLook plugin](https://github.com/whomwah/qlstephen/releases).
{% endhint %}

## Converting Formats

### Converting ROMs

* **Cartridge-based ROMs** generally do not need converting. Formats like `.bin` vs `.md` or `.gen` \(Sega Genesis\) or `.sfc` vs `.smc` \(Super Nintendo\) are generally just different filename extensions for the same format to simplify identifying shared formats across systems and avoid conflicts. They are basically interchangeable and you can simply rename them to a supported extension.
* **CD-based ROMs** require certain supported formats…
  * If you have part of a supported multi-file ROM, but are missing the additional file\(s\) such as `.cue` , `.ccd`, `.sub`… to complete it, you may want to check out the archives at [redump.org](http://redump.org) in order to restore it properly, or try replacing the ROM entirely from a different source.
  * If your filetypes are not supported, you may need to convert them with a disc image conversion app.
  * If your files have been restructured via **ecm** \(ie. `.bin.ecm`\) they will need to be reverted: [unECM](formatting-roms.md#unecm).

### Converting & Editing Memory Cards

* PSX memory card formats can be converted to `.mcr` and edited with apps like [MemcardRex](https://github.com/ShendoXT/memcardrex).

### UnECM

**Mac**

1. Install [Homebrew](https://brew.sh) _\(if you don't have it\)_ in Terminal with:

   `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

2. Install via Homebrew with: `brew install ecm`
3. Use `unecm [path to .ecm file]` to restore the original format. 

{% hint style="info" %}
The Terminal app can be found in: _/Applications/Utilities_
{% endhint %}

**Windows**

Use these [Instructions](https://www.lifewire.com/ecm-file-2620956), for now.

## Archiving

#### Mac <a id="archiving-mac"></a>

**Requirements:**

* [Keka](http://www.kekaosx.com)

**Setup**

1. Set your default app unarchiving \(`.zip`, `.7z`, `.rar`, etc…\) to Keka:
   1. Select a single archive per filetype and File→Get Info \(`⌘I`\)
   2. Change `Open with:` to Keka and hit `Change All…`.
2. Open Keka and select `.7z` or .`zip` and the following settings:

   ☑️Solid archive `.7z`

   ☑️Exclude Mac resource forks

   ☑️Delete file\(s\) after compression

**Archive**

1. Drag & Drop ROM file \(or files if multi-file ROM, such as `.cue + .bin`\) onto Keka. Done.

{% hint style="danger" %}
Loose files _only_. DO NOT contain folder\(s\) within an archive \(this is a known issue and will result in a crash\)!
{% endhint %}

#### Windows <a id="archiving-windows"></a>

_\(coming later…\)_

\_\_

## Batching

⚠️ This only applies to single file ROMs. DO NOT batch process multi-file ROMs using the methods below.

**Mac**

1. Setup and Requirements from Archiving.

**If Unarchiving, first…**

1. In Finder, Select all \(`⌘A`\) ROM archives and File→Open \(`⌘O`\) to unarchive all. 
2. When complete, the Finder should still have all the archives selected. Delete them all \(`⌘␡`\).

**If Renaming files…**

1. In Finder, Select all \(`⌘A`\) ROMs and Right-Click to `Rename items…` _Example:_ `Replace Text:` Find: `.bin` Replace with… `.md`

**If Re-archiving…**

1. In Keka, enable:  ☑️Archive as single files
2. In Finder, Select all \(`⌘A`\) ROMs and drop them all onto Keka. Done.

#### Windows <a id="batching-windows"></a>

**If Renaming files…**

1. Open the Command Prompt with `⊞R` and type `cmd` 
2. Enter `cd` and the \[file-path\] to a set of ROMs.  \[file-path\]: right-click the folder and select "Properties" and apply via copy/paste.
3. _Example:_ `rename *.bin *.md`

## **⚠️ Known Issues**

* Folders within an archive will result in crash. Archive loose files _only._

\_\_

{% hint style="info" %}
🗯 If you are still stuck ask for [help](https://discord.gg/NhzgrXh) on our Discord.
{% endhint %}

