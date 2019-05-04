---
description: How to restore files if lost or deleted.
---

# Restoring Files

```text
ROUGH DRAFT
```

If you are moving from v1.4 to v1.5b \(beta, changing your Bundle ID, or upgrading beta builds that have undergone database changes which require the app to be clean installed, you will need to backup your save games and ROMs or you will lose them all.

At the moment exporting or restoring files such can only be done manually…

⚠️ DO NOT rely on the beta as your main playing build - to install the beta "sidecar" or alongside a stable release at the same time, use a different Bundle ID.  


### Exporting & Restoring Files

1. In Provenance, turn on Web Server via `Imports/Exports`
2. Use the Web UI or WebDav \(recommend the WebDav method\), or iOS Apple Files app \(in On My Device&gt;Provenance\) and pull all the files you need from `Battery/` and `Save States/`
   * Make sure your ROM file names don't change by the time you put them back, they _**must match verbatim**_, and pay attention to the folder structures. DO NOT rename anything!
   * [WebDav usage help](https://github.com/Provenance-Emu/Provenance/wiki/Customizing-ROMs#webdav-clients)
3. After replacing Provenance… Manually place your files back the way you found them \(you may have to recreate folder structures or let them be recreated\).
   * You should probably open your game at least once and save a state so it creates its base folders.
4. After placing your files into the new folder structure, you \[may\] need to Build the app over itself once more in order for them to be migrated into new structure properly at buildtime
   * When complete, these migrated Save States will not have screenshots as the new ones do, etc…

⚠️ DO NOT manually place the ROMs files themselves, in case they are not detected and added to database. Use `Imports` folder to re-import your ROM library \(this might actually work now, but fair warning of uncertainty\).  


ROUGH DRAFT ··· Follow the [Doc Updates](https://github.com/Provenance-Emu/Provenance/projects/7) project for status

