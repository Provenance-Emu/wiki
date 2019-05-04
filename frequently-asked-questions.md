# Frequently Asked Questions

## Disclaimer

{% hint style="warning" %}
_Before_ posting new issues or asking the team or community, please check these Frequently Asked Questions or search the 💢[Troubleshooting](help/troubleshooting.md) and sub-sections within each of the wikis.
{% endhint %}

### Why—

🛑 **STOP!** _Before you continue…_

> #### Where did you install the app from?

* **Official Provenance GitHub**: 👍 [_skip ahead_](frequently-asked-questions.md#skipped)\_\_
* **Elsewhere**: 👎 _read below…_

🚫 3rd-party builds are NOT supported nor approved. They are… not current, probably buggy and generally unsafe _\(unapproved modifications, malware, adware and may require backdoor profiles\)_, and when Apple revokes their misused profiles, you will probably lose your games and saves: 

1. Delete the 3rd-party app and any profiles they may have installed. 
2. Boycott them _\(stop using, sharing, or supporting their sites\)._ 
3. Re-install from the _official_ source _only_: [Installing Provenance](installation-and-usage/installing-provenance/)

—or we cannot help you.

{% hint style="info" %}
The 3rd-parties _**do not**_ help this community _whatsoever,_ causing us wasted time with limited resources…they also unrightly profit off of the work of this open source team that works for free.
{% endhint %}

## Frequently Asked Questions <a id="skipped"></a>

### How do I install or update Provenance? <a id="install"></a>

Refer to [Installing](installation-and-usage/installing-provenance/) or [Updating](installation-and-usage/installing-provenance/updating.md).

### Is jailbreak required? <a id="jailbreak"></a>

No.

### Is there a Cydia repo? <a id="cydia"></a>

No.

### Why does Provenance not install? <a id="install-fail"></a>

Make sure you follow _each_ and _every_ step when [Installing](https://github.com/jasarien/Provenance/wiki/Installing-Provenance). **Do not** skip anything or make any assumptions. If stuck, refer to [Troubleshooting](https://github.com/Provenance-Emu/Provenance/wiki/Installing-Provenance/#troubleshooting-alt). If still stuck…ask for [help](https://discord.gg/NhzgrXh) on our Discord.

### What systems are supported? <a id="systems"></a>

A full list of currently supported systems can be found on the [Supported Systems](https://github.com/Provenance-Emu/Provenance/wiki/Supported-Systems) wiki.

### Can I use a controller? <a id="controller"></a>

Yes. Controllers using Apple's standardized MFi format are 100% supported. Provenance also supports some non-standard iCade-type controllers \(8bitdo, etc\) and Valve's Steam Controller. See [Controllers & Controls](https://github.com/Provenance-Emu/Provenance/wiki/Controllers-&-Controls).

### What are the controls? <a id="controls"></a>

A full list of mapped controls for MFi gamepad profiles per system can be found in [Controls](https://bit.ly/2LDZNzI). \(iCade controller map coming later, if still supported by Apple\).

### What controller\(s\) do you recommend? <a id="controllers"></a>

An ongoing list of supported and recommended controllers and reviews can be found in [Controllers](info/controllers-and-controls/controllers.md).

### Where can I get ROMs, or BIOS? <a id="roms"></a>

Due to copyright law, we cannot share ROMs or where to obtain them. You are legally allowed to make personal backup copies of your own purchased games for personal use as ROMs. Anything outside of this, you are on your own.

{% hint style="warning" %}
**DO NOT** ask us or the community where to obtain ROMs or BIOS files.
{% endhint %}

### What if I don't have a Mac? <a id="no-mac"></a>

* You don't need a Mac if you are [side-loading](https://github.com/Provenance-Emu/Provenance/wiki/Installing-Provenance/#side-loading) a release, which is cross-platform.
* If [building from source](https://github.com/Provenance-Emu/Provenance/wiki/Installing-Provenance/#building), you don't technically need a Mac, just macOS. Using a custom built Hackintosh or virtual machine \([Virtualizing macOS](https://github.com/Provenance-Emu/Provenance/wiki/Virtualizing-macOS)\) with macOS would suffice. If these are not an option, side-load the current release or wait for the next release \(beta is build _only_\).

### Can I install without a computer? <a id="no-computer"></a>

Currently, there _**is not a safe method**_ for you install the app to your device\(s\) from the internet via web-signing—any 3rd party sites hosting the app are not approved nor endorsed by the Provenance team. **Do not use them.**

### Will you release an .ipa of the beta? <a id="prerelease"></a>

No. We are a very small team, and managing various pre-releases at different states of development would only slow us down and complicate testing and bug-reporting with fragmentation. If you would like to contribute via beta-testing, it is required that you are able to keep pace with active development and build from source as we do. Otherwise, you'll have to wait for final release.

### When is the \[next\] release? <a id="release-date"></a>

As a small team, we prefer to not make promises we will break with release dates. You are welcome to check development status via our [Releases Roadmap](https://github.com/Provenance-Emu/Provenance/milestones?direction=asc&sort=title&state=open) and [Projects](https://github.com/Provenance-Emu/Provenance/projects) \(though they are subject to change\) and join the community on our [Discord](https://discord.gg/4TK7PU5) server.

### Why is the app crashing at launch? <a id="crash"></a>

This is usually due to one of the following reasons…

* You are using a free Apple developer account, which requires you to re-sign every 7 days. You can…
  * [Side-load](https://github.com/Provenance-Emu/Provenance/wiki/Installing-Provenance/#side-loading) using the same Apple ID used previously.
  * [Build](https://github.com/Provenance-Emu/Provenance/wiki/Installing-Provenance/#building) over the app using the same Bundle IDs used previously.
  * [Upgrade](https://developer.apple.com/programs/) to a paid Apple developer account and use the app indefinitely.
* You were using an unsupported 3rd party build of the app and Apple revoked the provisioning profile as it violates their terms of use. You should…
  1. Delete the 3rd-party app and any profiles they may have installed.
  2. Boycott them \(stop using, sharing, or supporting their sites\).
  3. Re-install from the _official_ source _only:_ [Installing Provenance](https://github.com/jasarien/Provenance/wiki/Installing-Provenance)

{% hint style="warning" %}
If using beta this could be a bug… check the open [Issues](https://github.com/Provenance-Emu/Provenance/issues), specifically labelled: [crash](https://github.com/Provenance-Emu/Provenance/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aopen+label%3Acrash)
{% endhint %}

### Why does _\[insert game here\]_ not work or crash? <a id="game-fail"></a>

Could be any number of the following reasons: 1. You could have a _bad_ ROM. Replace it. 2. You might be attempting to load a ROM for an unsupported system. Check [Supported Systems](https://github.com/Provenance-Emu/Provenance/wiki/Supported-Systems). 3. Your ROMs might not be using a supported extension or file format \(such as `.bin` for Atari or Sega systems\). Refer to [Formatting ROMs](https://github.com/Provenance-Emu/Provenance/wiki/Formatting-ROMs). 4. If multi-file ROM \(ie. `.cue + .bin`\), check if the filenames match the .cue file contents. Refer to Formatting ROMs: [Multi-File ROMs](https://github.com/Provenance-Emu/Provenance/wiki/Formatting-ROMs/#multi-file-roms). 5. Multi-disc Games require an `.m3u` file in order to swap discs, specific filename formatting. Refer to Formatting ROMs: [Multi-Disc Games](https://github.com/Provenance-Emu/Provenance/wiki/Formatting-ROMs/#multi-disc-games). 6. Your BIOS files might be wrong, even if named correctly. Check md5 hashes of your BIOS files as compared to what is listed in [BIOS Requirements](https://github.com/Provenance-Emu/Provenance/wiki/BIOS-Requirements) to be certain. 5. Unfortunately, not all emulator cores feature 100% compatibility with all ROMs. If the system has more than one core option \[which is shown at launch \(ie. NES: `FCEUX` vs `mednafen`\), unless you've specified a preferred core for that particular ROM or system\], try the alternate core for that game specifically. Some emulation core teams have compiled and maintain compatibility lists \(such as Yabause \(Sega Saturn\)\), which can be found linked in our [Supported Systems](https://github.com/Provenance-Emu/Provenance/wiki/Supported-Systems) wiki.

### What format do ROMs need to be? <a id="format"></a>

File format and/or filename requirements are specified in [Formatting ROMs](https://github.com/Provenance-Emu/Provenance/wiki/Formatting-ROMs).

### How do I convert ROM or Memory Card formats? <a id="convert"></a>

Refer to Formatting ROMs: [Converting Formats](https://github.com/Provenance-Emu/Provenance/wiki/Formatting-ROMs/#converting-formats).

### How do I enable dark mode on Apple TV? <a id="dark-mode-atv"></a>

Provenance supports the system-wide Dark mode of tvOS. To enable it go to tvOS `Settings` → `General` → `Appearance` → `Dark ✓`

### Why is the app running slow or stuttering? <a id="slow"></a>

* You might have built the _debug version_ by mistake \(app will be named **Prov Debug** on Home Screen and the version displayed in Settings will be `DEBUG`\)… If so, [Re-build](https://github.com/Provenance-Emu/Provenance/wiki/Installing-Provenance/#building) using **Provenance-Release** \(iOS\) or **ProvenanceTV-Release** \(tvOS\) in Xcode.
* On older devices, to speed up N64, change `#define FORCE_RICE_VIDEO 0` to `#define FORCE_RICE_VIDEO 1` in [MupenGameCore.m](https://github.com/Provenance-Emu/Provenance/blob/574f6834573392b57d9b6c5b58d84620844700a8/PVMupen64Plus/MupenGameCore.m#L34)
* All cores should run full speed on any generation Apple TV, or iPhone 7 or newer.
* Turn off Smoothing and CRT effects in the application settings.
* Devices as old as iPad 2 should run up to 16 bit generation systems at full speed. A complete performance comparison has not been done but this is a general guideline based on user reports and developer testing.

### How can I contribute? <a id="contribute"></a>

* **Development**: We are always looking for new devs. The best way to get started is to browse the open [Issues](https://github.com/Provenance-Emu/Provenance/issues) and submit code as a [PR \(Pull Request\)](https://github.com/Provenance-Emu/Provenance/pulls) to our GitHub with a fix.
* **Beta-testing**: Testers¹ are welcome, but _only_ when following these rules: 

1. Read [Issues Usage](https://github.com/Provenance-Emu/Provenance/wiki/Issues-Usage)
2. Only report against the very latest `develop` build² 
3. Pay attention to \#git-updates activity on Discord or the [commit history](https://github.com/Provenance-Emu/Provenance/commits/develop) on GitHub. 
4. Check the [Issues](https://github.com/Provenance-Emu/Provenance/issues) and [PRs](https://github.com/Provenance-Emu/Provenance/pulls) on our GitHub, before reporting bugs. 
5. Be very conscious of the active conversations in the \#bugs channel on Discord.  ¹ There is a major difference in just 'using' the beta and actually participating in beta-testing. ² You can install the beta alongside of stable release if you use an alternate Bundle ID.

* **Web**: We are looking for a web dev \(preferably a dev/designer hybrid\) that can help us upgrade and maintain our .com \(WordPress\).
* **Content**: We are looking for advocates who are interested in recording content for YouTube with the app in action.
* **Moderators**: We are looking for moderators for our Discord to help maintain and moderate the community. If interested, start by joining our [Discord](https://discord.gg/4TK7PU5) and helping other users to boost your rank in the levels system that awards experience for user participation.
* **Helpers**: You are welcome to offer assistance to new users in the [\#help](https://discord.gg/NhzgrXh) channel on our Discord.

## 

🗯 If you cannot find the answers you're looking for… you may ask for [help](https://discord.gg/NhzgrXh) on our Discord.

### 

