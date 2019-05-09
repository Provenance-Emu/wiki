---
description: How to restore files if lost or deleted.
---

# Restoring Files

{% hint style="info" %}
ROUGH DRAFT ··· Follow the [Doc Updates](https://github.com/Provenance-Emu/Provenance/projects/7) project for status
{% endhint %}

If you are moving from v1.4 to v1.5b, changing your Bundle ID, or upgrading builds that have undergone database changes which require the app to be clean installed, **you will need to backup your save games and ROMs or you will lose them all!** 

At the moment exporting or restoring files such can only be done manually…

{% hint style="warning" %}
**DO NOT** rely on the beta as your main playing build - to install a secondary app for testing alongside a stable release at the same time, use an alternate Bundle ID.
{% endhint %}

{% hint style="warning" %}
**DO NOT** rely solely on Save States, they are not guaranteed to be compatible between app versions due to core updates, etc… Before updating the app, launch the games you to salvage and create in-game saves to be safe.
{% endhint %}

### Exporting & Restoring Files

1. In Provenance, either… 
   * Turn on the Web Server and load it via WebDav, or…
   * Open Apple Files and go to `On My Device/Provenance` or `Cloud Drive/Provenance`.
2. Pull all the files you need from `Battery/` and `Save States/`, if you don't have your ROMs offline somewhere, obtain them from the `com.provenance.[system]/` folders.
   * Make sure your ROM file names don't change by the time you put them back, they _**must match verbatim**_, and pay attention to the folder structures. DO NOT rename anything!
   * [WebDav usage help](../../installation-and-usage/roms/importing-roms.md#uploading)
3. After replacing Provenance… Manually place your files back the way you found them \(you may have to recreate folder structures or let them be recreated\).
   * You should probably open your game at least once before this and save a state so it creates its base folders.
4. After placing your files into the new folder structure, you \[may\] need to Build the app over itself once more in order for them to be migrated into new structure properly at buildtime
   * When complete, these migrated Save States will not have screenshots as the new ones do, etc…

{% hint style="info" %}
If your files do not migrate over, you can attempt to replace a new save state or battery save file with previous files and change the names to the new ones as a workaround.
{% endhint %}



