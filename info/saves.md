---
description: Game Saves and Save States.
---

# Game Saves

There are two ways to save your progress in Provenance: the native in-game save, known as _Battery Saves_, and freezing the state of the emulator anywhere in a game called _Save States_.

* [**Battery Saves**](saves.md#battery-saves)
  * [Saving Games](saves.md#saving-games)
  * [Supported Formats](saves.md#supported-formats)
  * [Converting Formats](saves.md#converting-formats)
  * [Importing Battery Saves](saves.md#importing-battery-saves)
  * [Exporting Battery Saves](saves.md#exporting-battery-saves)
* [**Save States**](saves.md#save-states)
  * [Saving States](saves.md#saving-states)
  * [Loading States](saves.md#loading-states)
  * [Deleting States](saves.md#deleting-states)
  * [Importing Save States](saves.md#importing-save-states)
* [**iCloud Sync**](saves.md#icloud-sync)

## Battery Saves

A Battery Save is the term used to describe a save file that is created by a game \(as opposed to a Save State which is created by the emulator\). The format of a battery save is determined by the developers of the game when it was originally programmed, so it does not change if an emulator core is updated or changed.

### Saving Games

A battery save file is created by the game when you use the game's built-in save functionality. For example, if you are playing Pokemon for Game Boy, and you choose to save the game from the game's main menu, Provenance stores the save file at `Battery States/[ROM-Filename]/[ROM-Filename].sav`.

### Supported Formats

| Manufacturer | System | Supported Format\(s\) / Extension\(s\) |
| :--- | :--- | :--- |
| Sony | PlayStation \(PS1\) | `.mcr` |
| Sony | PlayStation Portable \(PSP\) | `.VMP` |
| Nintendo | NES | `.sav` |
| Nintendo | Super NES \(SNES\) | `.srm` |
| Nintendo | Nintendo 64 | `.srm`, `.eep`, `.fla`, `.mpk`, `.sra` |
| Nintendo | Game Boy / Game Boy Color | `.sav` |
| Nintendo | Game Boy Advance | `.sav` |
| Sega | Genesis / Mega Drive | `.srm` |
| Sega | Game Gear | `.sav` |
| Sega | Saturn | `.bcr` |
| Atari | Lynx | `.sav` |
| SNK | Neo Geo Pocket / Color | `.sav` |
| Others | Most systems | `.sav` |

### Converting Formats

#### PSX / PS1

If you have memory card files from another emulator, you can convert them to `.mcr` using:

* Windows: [MemcardRex](https://github.com/ShendoXT/memcardrex)
* Mac / Linux: [mymc](http://www.csclub.uwaterloo.ca:11068/mymc/) \(primarily PS2, but supports PS1 cards\)

### Importing Battery Saves

Since battery saves are created and managed by the game, you can move them between emulator implementations and they should still work as intended — unlike save states, which are emulator-dependent.

It makes things easier if you run the game at least once within Provenance so that it can create the required directories and filename structure.

The save filename must match your ROM's filename \(without extension\). For example, if your ROM is `Pokemon Red (USA).gb`, the battery save must be named `Pokemon Red (USA).sav`.

#### Via Files App or iCloud Drive \(Recommended\)

1. Open the **Files** app on your iPhone, iPad, or Mac.
2. Navigate to **On My iPhone/iPad** → **Provenance** → **Battery States**.
3. Open the folder named after your ROM.
4. Copy your save file into this folder, renaming it to `[ROM-Filename].sav` \(or `.mcr` for PlayStation\) if needed.
5. Launch the ROM in Provenance and use the game's native in-game load to load your save.

#### Via Web Server

1. Start the web server in Provenance \(`+` button in Game Library, or **Settings → Import/Export**\).
2. On your computer, open the URL shown in the dialog and navigate to `Battery States/[ROM-Filename]/`.
3. Upload your save file into this folder.
4. Rename the file to `[ROM-Filename].sav` if it doesn't already match.
5. Stop the web server.
6. Load the ROM and use the game's native in-game load to access your save.

#### Via Mac Finder \(USB\)

1. Connect your iOS device to your Mac via USB.
2. Open **Finder** and select your device in the sidebar.
3. Click the **Files** tab and expand **Provenance**.
4. Navigate to **Battery States** → **\[ROM-Filename\]**.
5. Drag your save file into this folder, renaming it to `[ROM-Filename].sav` if needed.
6. Load the ROM in Provenance and use the game's native in-game load.

{% hint style="warning" %}
If the game does not show the save, make sure the filename matches your ROM filename exactly \(case-sensitive\). If it still doesn't work, the save may have been created with a different region or version of the ROM and will only be compatible with that exact ROM version/region.
{% endhint %}

### Exporting Battery Saves

To back up your battery saves or move them to another emulator:

#### Via Files App

1. Open the **Files** app on your device.
2. Navigate to **On My iPhone/iPad** → **Provenance** → **Battery States**.
3. Open the folder for your game.
4. Long-press the save file and choose **Copy** or **Share** to export it to iCloud Drive, AirDrop, or another destination.

#### Via Mac Finder \(USB\)

1. Connect your iOS device to your Mac via USB.
2. Open **Finder**, select your device, and click the **Files** tab.
3. Expand **Provenance** → **Battery States** → **\[ROM-Filename\]**.
4. Drag the save file to your Mac.

## Save States

Save states are 'snapshots' of a game's progress. Save states differ from the save functionality built into most games \(Battery Saves\) — because they are produced by the emulator itself, they carry none of the limitations that the game or console may otherwise impose. You can create any number of save states you like, as frequently as you like, and loading them will take you back to precisely where you were in the game when they were taken \(even in the middle of a battle or cut-scene\).

You may use a game's built-in save mechanism instead of or in addition to save states, if you like, however…

{% hint style="danger" %}
Save state compatibility between updates is _**NOT**_ a guarantee as they can break due to changes in an emulator core implementation.
{% endhint %}

### Saving States

To create a save state, press the menu button while playing a game. Choose the **Save States** option. From here you can press the `+` button to create a new save state. You can also tap on an existing save state and choose to overwrite it. This cannot be undone, so back up the save state before overwriting if you want to keep it.

Provenance can automatically create a save state whenever the app is backgrounded or when you return to the Game Library. The next time you run the game, you will have the option of reloading from the most recent automatic save state. \(If you don't see this prompt, you may have already told it not to display the dialog anymore.\) The auto-save and auto-load options are configurable in **Settings**.

### Loading States

To load from an existing save state, press the menu button after loading a ROM. Here you will find all of the save states you've manually created, as well as automatic states. Tapping on a save state will present a menu allowing you to load the state.

### Deleting States

From the Save States screen, tap on an existing state and choose **Delete** from the menu. This cannot be undone, so be sure to back up the save state before deleting if you want to keep it.

### Importing Save States

Save states are emulator-specific. Importing a save state from another emulator will only work reliably if it was created with an identical core and version.

#### Via Web Server

1. Start the web server in Provenance.
2. Navigate to `Save States/[ROM-Filename]/`.
3. Upload your save state file into this folder.
4. Stop the web server, then load the ROM.
5. Open the **Save States** menu to load your imported state.

#### Via Mac Finder \(USB\)

1. Connect your iOS device to your Mac via USB.
2. Open **Finder**, select your device, and click the **Files** tab.
3. Expand **Provenance** → **Save States** → **\[ROM-Filename\]**.
4. Drag your save state file into this folder.
5. Load the ROM in Provenance and access the Save States menu to load it.

{% hint style="warning" %}
Save states are generally limited to the emulator core they were created with — if you change cores, your old save states will no longer work. If an emulator core is updated by an app update, save states may not be compatible with the new version if it changed the way it handles save states.

This should also be considered when exporting save states to use in another emulator — unless the other emulator is exactly the same core and version, it is highly unlikely that the save state will work. For cross-emulator compatibility, battery saves should be used instead.
{% endhint %}

## iCloud Sync

Provenance can sync both battery saves and save states across your devices using iCloud.

**Apple TV:** iCloud sync via CloudKit is **free** for all tvOS users. Since Apple TV has no permanent local storage, saves are automatically backed up to the cloud so you never lose progress.

**iPhone, iPad, and Mac:** iCloud sync requires a **Provenance Plus** subscription \($3.99/month or $39.99/year\).

### What Syncs

| Data | Free | Provenance Plus |
| :--- | :--- | :--- |
| Battery saves \(local\) | ✅ | ✅ |
| Save states \(local\) | ✅ | ✅ |
| Apple TV CloudKit sync | ✅ FREE | ✅ |
| iPhone / iPad / Mac sync | ❌ | ✅ |
| Multi-device save sync | ❌ | ✅ |

### Enable iCloud Sync

1. Subscribe to **Provenance Plus** in-app \(**Settings → Provenance Plus**\).
2. Go to **Settings → iCloud Sync** and toggle **ON**.
3. Enable on all your devices using the same Apple ID.
4. Wait for the initial sync to complete \(may take a while for large save libraries\).

{% hint style="info" %}
For troubleshooting iCloud sync issues or managing large synced libraries, see [Advanced ROM Management — iCloud Sync](../installation-and-usage/roms/advanced-management.md#icloud-sync-for-large-collections).
{% endhint %}
