---
description: 'How to format, convert, archive, or batch process ROMs.'
---

# Formatting ROMs

To avoid any issues with [Importing ROMs](https://github.com/Provenance-Emu/Provenance/wiki/Importing-ROMs), check to make sure your files are formatted correctly.

* ✅  [**Supported Formats**](formatting-roms.md#supported-formats)\*\*\*\*
  * [ROMs](formatting-roms.md#roms) · _by system_
  * [ROM Archives](formatting-roms.md#rom-archives)
  * [Multi-file ROMs](formatting-roms.md#multi-file-roms)
  * [Multi-disc Games](formatting-roms.md#multi-disc-games)
* 🔀  [**Converting Formats**](formatting-roms.md#converting-formats)\*\*\*\*
  * [Converting ROMs](formatting-roms.md#converting-roms)
  * [Editing Memory Cards](formatting-roms.md#editing-cards)
  * [UnECM](formatting-roms.md#unecm) · _restore original format from_ `.ecm` _files_
* ⏬  [**Archiving**](formatting-roms.md#archiving)\*\*\*\*
* ⏩  [**Batching**](formatting-roms.md#batching) · _batch renaming and \(re\)archiving_

{% hint style="warning" %}
Please refer to the [Known Issues](formatting-roms.md#known-issues) regarding Formatting ROMs, and read [Issues Usage](https://github.com/Provenance-Emu/Provenance/wiki/Issues-Usage) _before_ posting a new one.
{% endhint %}

## Supported Formats

### ROMs

<table>
  <thead>
    <tr>
      <th style="text-align:left">Manufacturer</th>
      <th style="text-align:left">System</th>
      <th style="text-align:left">Supported Format(s) / Extensions</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left">Atari</td>
      <td style="text-align:left">2600</td>
      <td style="text-align:left"><code>.a26</code>  <em>(.bin)</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">5200</td>
      <td style="text-align:left"><code>.a52</code>  <em>(.bin)</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">7800</td>
      <td style="text-align:left"><code>.a78</code>  <em>(.bin)</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Jaguar</td>
      <td style="text-align:left"><code>.j64</code>, <code>.jag</code>  <em>(.bin, .rom)</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Lynx</td>
      <td style="text-align:left"><code>.lnx</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Bandai</td>
      <td style="text-align:left">WonderSwan</td>
      <td style="text-align:left"><code>.ws</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">WonderSwan Color</td>
      <td style="text-align:left"><code>.wsc</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">NEC</td>
      <td style="text-align:left">PC Engine /
        <br />TurboGrafx-16</td>
      <td style="text-align:left"><code>.pce</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">PC Engine Super CD-ROM&#xB2; System /
        <br />TurboGrafx-CD</td>
      <td style="text-align:left"><code>.cue + .bin/iso</code>,
        <br /><code>.ccd + .img + .sub</code> 
        <br /><em>multi-file ROM</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">PC Engine SuperGrafx</td>
      <td style="text-align:left"></td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">PC-FX</td>
      <td style="text-align:left"><code>.cue + .bin/iso</code>,
        <br /><code>.ccd + .img + .sub</code> 
        <br /><em>multi-file ROM</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Nintendo</td>
      <td style="text-align:left">
        <p>Famicom /</p>
        <p>Nintendo Entertainment System</p>
      </td>
      <td style="text-align:left"><code>.nes</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Famicom Disk System</td>
      <td style="text-align:left"><code>.fds</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Game Boy</td>
      <td style="text-align:left"><code>.gb</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Super Famicom /
        <br />Super Nintendo Entertainment System</td>
      <td style="text-align:left"><code>.snes</code>, <code>.smc</code>, <code>.sfc</code>, <code>.fig</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Game Boy Color</td>
      <td style="text-align:left"><code>.gbc</code>, <code>.sgb</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Virtual Boy</td>
      <td style="text-align:left"><code>.vb</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Nintendo 64</td>
      <td style="text-align:left"><code>.n64</code>, <code>.z64</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Game Boy Advance</td>
      <td style="text-align:left"><code>.gba</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Pokemon mini</td>
      <td style="text-align:left"><code>.min</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Sega</td>
      <td style="text-align:left">SG-1000</td>
      <td style="text-align:left"><code>.sg</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Master System</td>
      <td style="text-align:left"><code>.sms</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Mega Drive /
        <br />Genesis</td>
      <td style="text-align:left"><code>.md</code>, <code>.smd</code>, <code>.gen</code>  <em>(.bin)</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Game Gear</td>
      <td style="text-align:left"><code>.gg</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Mega CD /
        <br />Sega CD</td>
      <td style="text-align:left"><code>.cue + .bin</code> 
        <br /><em>multi-file ROM</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">32X</td>
      <td style="text-align:left"><code>.32X</code>, <code>.32x</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Saturn</td>
      <td style="text-align:left"><code>.iso</code>,
        <br /><code>.cue + .bin/iso</code>,
        <br /><code>.ccd + .img + .sub</code>,
        <br /><code>.mds + .mdf</code> 
        <br /><em>multi-file ROM</em>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">SNK</td>
      <td style="text-align:left">Neo Geo Pocket</td>
      <td style="text-align:left"><code>.ngp</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"></td>
      <td style="text-align:left">Neo Geo Pocket Color</td>
      <td style="text-align:left"><code>.ngc</code>, <code>.ngpc</code>, <code>.npc</code>
      </td>
    </tr>
    <tr>
      <td style="text-align:left">Sony</td>
      <td style="text-align:left">Playstation</td>
      <td style="text-align:left"><code>.cue + .bin/img/iso</code>,
        <br /><code>.ccd + .img + .sub</code> 
        <br /><em>multi-file ROM</em>
      </td>
    </tr>
  </tbody>
</table>* Unsupported extension \(.ext\)? Try renaming it to a supported one, listed above.  …to batch process an entire library \(ie. change `.bin` → `.md` and re-archive all\), see [Batching](formatting-roms.md#batching).
* DO NOT rename multi-file ROMs unless you alter `.cue` file contents as well.
* _All_ multi-file ROMs _**must**_ be contained in a single-file archives.°  \([Instructions](formatting-roms.md#multi-file-roms)\)
* _All_ multi-disc games _**must**_ include a `.m3u` file in their archive.  \([Instructions](formatting-roms.md#multi-disc-games)\)

° Though not required, it's recommended to archive _all_ ROMs, individually.  


### ROM Archives

| Supported Formats |
| :--- |
| `.zip`, `.7z` |

{% hint style="danger" %}
Loose files _only_. DO NOT contain folder\(s\) within an archive \(this is a known issue and will result in crash\)!
{% endhint %}

## 

### Multi-file ROMs

A ROM consisting of multiple files such as `.bin` + `.cue` for CD-based games \(Sega CD, Playstation, etc…\) _**must**_ be contained together in a _single_ `.zip` or `.7z` archive as a ROMset _before_ importing and _both files are required_.¹

#### **ROMsets:**

**Examples of \[game\].7z contents:**

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
If **.ccd** based ROMsets are not importing correctly. Move **.sub** file into its system directory, manually, if they were mistakenly been left behind in Imports or Conflicts.
{% endhint %}

{% hint style="danger" %}
Loose files _only_. DO NOT contain folder\(s\) within an archive \(this is a known issue and will result in crash\)!
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
² If you rename any `.cue` based files in a ROMset, you _**must**_ change the contents of the `.cue` file _or they won't work._  
     
…archive filenames, however, are irrelevant as they are discarded after unarchiving.

{% hint style="info" %}
For a quick way to preview **.cue** files on macOS, install the [qlstephen QuickLook plugin](https://github.com/whomwah/qlstephen/releases).
{% endhint %}



### Multi-disc Games

All multi-disc games _**must**_ include a `.m3u` file _in_ their `.zip` or `.7z` ROMset \(multi-file\) archive. Disc numbering in filenames needs to be formatted _exactly_ as: `…(Disc #).ext`

{% hint style="warning" %}
If renaming and using ****a **.cue** based ****ROMset make sure to read the requirements for **.cue** files in [Multi-file ROMs](formatting-roms.md#multi-file-roms).
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

* **Cartridge-based ROMs** generally do not need converting. Formats like `.bin` vs `.md` or `gen` \(Sega Genesis\) or `.sfc` vs `.smc` \(Super Nintendo\) are generally just different filename extensions for the same format to simplify identifying shared formats across systems and avoid conflicts. They are basically interchangeable and you can simply rename them to a supported extension.
* _**CD-based ROMs**_ ****require certain supported formats…
  * If supported, you may just be missing an additional file like a `.cue` file for a multi-file rom. If so, you may want to check out the archives at [redump.org](http://redump.org) in order to restore it properly.
  * If your filetypes are not supported \(`.iso`, `.mds`, `.nrg`, etc…\) or have been restructured via `ecm` \(ie. `.bin.ecm`\) you may need to convert them with a disc image conversion app.

### Converting & Editing Memory Cards

* PSX memory card formats can be converted to `.mcr` and edited with apps like [MemcardRex](https://github.com/ShendoXT/memcardrex).

### UnECM

**Mac**

1. Install [Homebrew](https://brew.sh) _\(if you don't have it\)_ in Terminal¹ with:  


   `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

2. Install via Homebrew with: `brew install ecm`
3. Use `unecm [path to .ecm file]` to restore the original format. 

¹ The Terminal app can be found in: _/Applications/Utilities_  
 💢  If you get stuck or run into any errors, check out Troubleshooting.  


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
2. Open Keka and select `.7z` and the following settings: 
   * [x] Solid archive  
   * [x] Exclude Mac resource forks
   * [x] Delete file\(s\) after compression

**Archive**

1. Drag & Drop ROM file \(or files if multi-file ROM, such as `.cue + .bin`\) onto Keka. Done.

{% hint style="danger" %}
Loose files _only_. DO NOT contain folder\(s\) within an archive \(this is a known issue and will result in crash\)!
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

\`\`

## **⚠️ Known Issues**

* Folders within an archive will result in crash. Archive loose files _only._

\_\_

{% hint style="info" %}
🗯 If you are still stuck ask for [help](https://discord.gg/NhzgrXh) on our Discord.
{% endhint %}

