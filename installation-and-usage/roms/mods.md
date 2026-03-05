---
description: "Apply ROM hacks, patches, translations, and mods to your games — IPS/BPS patching, SBI files for PSX, and high-resolution N64 texture packs"
tags: ["mod", "modding", "patching", "patches", "n64", "psx", "sbi", "ips"]
---

# Modding ROMs

**\#️⃣**  [**Patching**](mods.md#patching) ****· _applying translations, hacks, etc…_  
❇️  [**High Resolution Textures**](mods.md#high-resolution-textures-n-64) \(N64\)

## Patching

A great resource for ROM hacks and translations can be found at [romhacking.net](https://www.romhacking.net). Note that usually the target ROM version needed is specified with MD5, CRC32 or SHA-1 checksum for the exact ROM to patch—make sure it matches your target file. 

To apply the patches you will need a patcher for the various formats:

* Mac: 
  * [MultiPatch](http://projects.sappharad.com/tools/multipatch.html): `.ips`, `.bps`, `.ups`, `.ppf`, `.bsdiff`, `.bdf`, `.xdelta`, `.dat`
* Windows: 
  * [Floating IPS](https://github.com/Alcaro/Flips): `.ips`, `.bps`
  * [XDelta](https://sourceforge.net/projects/xdelta3-gui): `.xdelta`

#### Hash Checksums

 To obtain the hash checksum of a ROM, you can use the following commands in Terminal… 

```text
md5 [path to file or drag and drop file here]
```

```text
crc32 [path to file or drag and drop file here]
```

```text
shasum [path to file or drag and drop file here]
```

{% hint style="info" %}
Although it's best to use the exact ROM required as listed…_sometimes_ a patch will still work without an exact match, but cannot be guaranteed to work 100% even if it seems to have successfully patched. This might be necessary as there are some exact ROMs that are nearly impossible to obtain, but _do this as a last resort and at your own risk._
{% endhint %}

## **SBI Files \(PSX\)**

SBI Files are archives that contains the protection information that those PAL games got and that are needed to run those protected games in emulators. 

SBI Files are not copyrighted, as they're not the ROM itself.

### Obtaining

These are supplied by a 3rd party, use at your own risk.

https://psxdatacenter.com/sbifiles.html

### Usage

Simply copy the obtained .SBI file and place it in the same directory as the game you wish to patch, with matching filename.
```sh
My Game.bin
My Game.cue
My Game.sbi
```

## **High Resolution Textures \(N64\)**

The option is enabled by default since if it doesn't find textures for the current ROM nothing happens. To use hi-res texture packs you need to copy them to the directory `com.provenance.n64/hires_texture/{ROM NAME}` The ROM NAME isn't the file name, but instead the identifier for the ROM in the header of the ROM file. If you don't know what it is, you can view the console output at load where it says something like, `Mupen (3): Name: SUPER MARIO 64` So in this example, if I wanted to load hi res textures for Mario 64 I would put them in, `com.provenance.n64/hires_texture/SUPER MARIO 64`‌

Hi-Res packs come in folders with sub-folders. Just copy all the folders in the path as described above, mupen will find the right textures in sub folders.‌

Texture packs can be downloaded at [textures.emulation64.com](http://textures.emulation64.com/index.php?id=downloads)‌

For some reason this site splits larger texture packs into multiple zips. Just download all the zips and copy all their contents into the directory for your ROM as described above.‌

Hi-Res texture pack don't seem to noticeably degrade performance \(on original ATV4 testing\). For me Mario 64 runs at 100% with dips here and there, and with hi-res texture packs applied, frame rates were the same as far as I could tell but visually everything was crisper. It seems that texture handling is not the bottle neck of performance for glupen64plus on iOS.‌

![Texture structure and WebDav in Finder](https://i.imgur.com/esrYOyl.jpg)

​



{% hint style="info" %}
🗯 If you are still stuck ask for [help](https://discord.gg/provenance) on our Discord.
{% endhint %}

