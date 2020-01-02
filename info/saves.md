---
description: Game Saves and Saves States.
---

# Game Saves

{% hint style="warning" %}
**ROUGH DRAFT**
{% endhint %}

There are two ways to save your progress in Provenance: the native in-game save, known as _Battery Saves_, and freezing the state of the emulator anywhere in a game called _Save States_.

* \*\*\*\*[**Battery Saves**](saves.md#battery-saves)\*\*\*\*
  * [Saving Games](saves.md#saving-games)
  * [Supported Formats](saves.md#supported-formats)
  * [Converting Formats](saves.md#converting-formats)
  * [Importing Saves](saves.md#importing-saves)
* \*\*\*\*[**Save States**](saves.md#save-states)\*\*\*\*
  * [Saving States](saves.md#saving-states)
  * [Importing States](saves.md#importing-saves)

## Battery Saves

A Battery Save is the term used to describe a save file that is created by a game \(as opposed to a Save State which is created by the emulator\). The format of a battery save is determined by the developers of the game when it was originally programmed, so it does not change if an emulator core is updated or changed.

### Saving Games

A battery save file is created by the game when you use the game's built-in save functionality. For example, if you are playing Pokemon for Gameboy, and you choose to save the game from the game's main menu, it will create a save file in `Battery Saves/[ROM-Filename]/[ROM-Filename].sav`.

### Supported Formats

| Manufacturer | System | Supported Format\(s\) / Extensions |
| :--- | :--- | :--- |
| Sony | Playsation | `.mcr` |
| Others… |  | `.sav` |

_\(more details coming…\)_

### Converting Formats

#### PSX/PS1

If you have memory card files from another emulator you can convert them to `.mcr` via:

* Windows: [MemcardRex](https://github.com/ShendoXT/memcardrex)

### Importing Saves

Since these files are created and managed by the game, you are able to move them between emulator implementations and they should still work as intended, unlike save states which are emulator dependent, unless they are of a different format, and will require conversion.

It makes things easier if you run the game at least once within Provenance so that it can create the required directories and filename structures.  


1. Start the web server in Provenance.
2. Navigate to `Battery States/[ROM-Filename]/`
3. Upload your save file into this folder.
4. Make sure the save's filename is `[ROM-Filename].sav` \(rename it to match if it is not\).
5. Stop the web server.
6. Load the ROM.
7. Use the game's native in-game loading to load the game.

{% hint style="warning" %}
If the game does not show the save, make sure the file name is correct as described above. If it still does not show, then it's possible that the save was created with a different region, or version of a ROM that uses a different save format and will only be compatible with the ROM version/region it was created with.
{% endhint %}

## Save States

Save states are 'snapshots' of a game's progress. Save states differ from the save functionality built into most games \(Battery Saves\) — because they are produced by the emulator itself, they carry none of the limitations that the game or console may otherwise impose. You can create any number of save states you like, as frequently as you like, and loading them will take you back to precisely where you were in the game when they were taken \(even in the middle of a battle or cut-scene\).

You may use a game's built-in save mechanism instead of or in addition to save states, if you like, however…

{% hint style="danger" %}
Save state compatibility between updates is _**NOT**_ a guarantee as they can break due to changes in an emulator core implementation.
{% endhint %}

### Saving States

To create a save state, press the menu button while playing a game. Choose the Save States option. From here you can press the `+` button to create a new save state. You can also tap on an existing save state and choose to overwrite that state with a new one. This cannot be undone, so be sure that you either backup the save state before doing this if you wish to keep it.

Provenance can automatically create a save state whenever the app is backgrounded, or when you return to the Game Library. The next time you run the game, you will have the option of re-loading from the most recent automatic save state or not. \(If you don't see this, you may have already told it not to display the dialogue anymore.\) The option to auto-load a save state is in the Settings menu.

### Loading States

To load from an existing save state, press the menu button after loading a ROM. Here you will find all of the save states you've manually created, as well as the automatic states. Tapping on a save state will present a menu allowing you to load the state.

### Deleting States

From the Save States screen, tap on an existing state and choose Delete from the menu. This cannot be undone, so be sure to backup the save if you want to keep it before deleting it from Provenance.



{% hint style="warning" %}
Save states are generally limited to the emulator core they were created with — if you change cores, your old save states will no longer work. If an emulator core is updated by an app update, there is a possibility that save states may not be compatible with the new version if it changed the way it handles save states.

This should also be considered when exporting save states and attempting to play them in another emulator -- unless the other emulator is exactly the same core and version, it is highly unlikely that the save state will work. For this case, battery saves should be used.
{% endhint %}

#### 

