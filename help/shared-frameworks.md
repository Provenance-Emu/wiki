---
description: The Swift packages Provenance, iFly and iCube share, what each one does, and how to add one to your own app.
---

# Shared Frameworks

Provenance, [iFly](https://ifly-emu.com) (Dreamcast) and [iCube](https://icube-emu.com) (GameCube / Wii) are three apps built on the same parts. Anything two of them need lives in its own Swift package, in its own repository under [github.com/Provenance-Emu](https://github.com/Provenance-Emu), and each app depends on it by URL. A fix made once lands in all three.

None of these packages knows which app it is in. App group names, CloudKit containers, URL schemes and colors are passed in by the host app, so the packages work in any emulator frontend for Apple platforms, not only ours.

## The packages

| Package | What it does | Used by | Platforms |
|---|---|---|---|
| [SkinKit](#skinkit) | Controller skins: `.deltaskin` / `.manicskin` parsing, the Format 2 renderer, the skin manager and store browser, RetroArch overlay import, and the TV bezels around the picture (`SkinKitBezels`). | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14 |
| [GamepadKit](#gamepadkit) | Controller handling: element-name mapping, positional fallback for plain HID pads, pad family detection, pause triggers, and a synthesized extended gamepad for pads iOS exposes without one (Switch Online SNES / N64 / Mega Drive, generic USB and Bluetooth pads). | Adoption in progress (`0.1.0`) | iOS 17.4, tvOS 17.4, macOS 14 |
| [PVSystems](#pvsystems) | `SystemIdentifier` and per-system metadata: TheGamesDB / libretrodb / OpenVGDB IDs, RetroAchievements console IDs, the per-game BIOS manifest. | Provenance, iFly | iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1 |
| [PVLookup](#pvlookup) | Game metadata, artwork and cheat lookup over libretrodb, OpenVGDB, TheGamesDB, ShiraGame and the libretro cheat database. Ships no database bytes; they are release assets fetched at build time. | Provenance, iFly | iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1 |
| [PVPatchEngine](#pvpatchengine) | Streaming ROM and disc patch engine: IPS, BPS, UPS, PPF and xdelta3, with bounded memory and 64-bit offsets. C core, Swift API. | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14 |
| [PVWebServer](#pvwebserver) | HTTP and WebDAV server on one port, built on Network.framework, with a route registry. Powers the in-app file manager and uploads. | Provenance, iCube | iOS 17, tvOS 17, macOS 11, watchOS 9, visionOS 1 |
| [PVWidgets](#pvwidgets) | Home screen game widgets: grid and list drawn from the widget's real size, the Show and Layout options, cover decoding. | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14, visionOS 1 |
| [PVLibrarySnapshot](#pvlibrarysnapshot) | The App Group snapshot and cover JPEGs an app writes for its extensions; the tvOS Top Shelf reads it. | Provenance, iCube | iOS 17, tvOS 17, macOS 14, visionOS 1 |
| [PVHelp](#pvhelp) | In-app help from a GitBook wiki repo: navigation, page fetch and cache, GitBook preprocessing, offline fallback. | Provenance, iCube | iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1 |
| [PVRemoteLibrary](#pvremotelibrary) | One model of "a game somewhere": on this device, on an emulator content server, on a RomM share or on a nearby peer. Matching, merged library rows, an on-disk catalogue and cover cache. | Provenance | iOS 17, tvOS 17, macOS 14, visionOS 1 |
| [PVSyncRules](#pvsyncrules) | What an emulator app syncs: `SyncClassifier` (save state, battery save, ROM, BIOS), `SyncableFileType`, `SyncPolicy`. Pure value types, no I/O. | iCube | iOS 17, tvOS 17, macOS 14 |
| [PVCloudSync](#pvcloudsync) | CloudKit sync of user files: scanning, planning, conflict resolution, tombstones, a local trash, retry policy and a CloudKit provider. | iCube | iOS 17, tvOS 17, macOS 14 |
| [PVContinuity](#pvcontinuity) | Nearby library discovery, trust, manifests and file transfer between devices on the same network. | iCube | iOS 17, tvOS 17, macOS 14 |
| [ContinuityKit](#continuitykit) | Cross-device "continue this game" handoff: manifests, transfer, Bonjour discovery, library browse. A different API and wire protocol from PVContinuity. | iFly | iOS 16, tvOS 16, macOS 13, watchOS 9, visionOS 1 |

Most names start with `PV`, after Provenance. The three ending in `Kit` (SkinKit, GamepadKit, ContinuityKit) started outside Provenance and kept their names.

## Adding a package

Every package is a plain SwiftPM package with version tags. In `Package.swift`:

```swift
dependencies: [
    .package(url: "https://github.com/Provenance-Emu/PVSystems.git", from: "1.0.0")
],
targets: [
    .target(name: "MyApp", dependencies: [
        .product(name: "PVSystems", package: "PVSystems")
    ])
]
```

In Xcode: **File → Add Package Dependencies…** and paste the repository URL.

{% hint style="info" %}
Packages at `0.x` (SkinKit, GamepadKit, PVWidgets, PVRemoteLibrary) may break their API in a minor release. Pin them with `.upToNextMinor(from:)`.
{% endhint %}

## SkinKit

Controller skins: `.deltaskin` / `.manicskin` parsing, the Format 2 renderer, the skin manager and store browser, RetroArch overlay import, and the TV bezels around the picture (`SkinKitBezels`).

* **Repository:** [github.com/Provenance-Emu/SkinKit](https://github.com/Provenance-Emu/SkinKit)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14

Skins themselves are in the [skin catalog](https://emuskins.com). See the [Skins guide](../info/skins-guide.md) and [Skin Format 2.0](../info/skin-format-2.md).

## GamepadKit

Controller handling: element-name mapping, positional fallback for plain HID pads, pad family detection, pause triggers, and a synthesized extended gamepad for pads iOS exposes without one (Switch Online SNES / N64 / Mega Drive, generic USB and Bluetooth pads).

* **Repository:** [github.com/Provenance-Emu/GamepadKit](https://github.com/Provenance-Emu/GamepadKit)
* **Used by:** Adoption in progress (`0.1.0`)
* **Platforms:** iOS 17.4, tvOS 17.4, macOS 14

## PVSystems

`SystemIdentifier` and per-system metadata: TheGamesDB / libretrodb / OpenVGDB IDs, RetroAchievements console IDs, the per-game BIOS manifest.

* **Repository:** [github.com/Provenance-Emu/PVSystems](https://github.com/Provenance-Emu/PVSystems)
* **Used by:** Provenance, iFly
* **Platforms:** iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1

## PVLookup

Game metadata, artwork and cheat lookup over libretrodb, OpenVGDB, TheGamesDB, ShiraGame and the libretro cheat database. Ships no database bytes; they are release assets fetched at build time.

* **Repository:** [github.com/Provenance-Emu/PVLookup](https://github.com/Provenance-Emu/PVLookup)
* **Used by:** Provenance, iFly
* **Platforms:** iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1

The databases are published as `databases-YYYY-MM-DD` releases on the repository; an app pins one by sha256 and bundles the zips.

## PVPatchEngine

Streaming ROM and disc patch engine: IPS, BPS, UPS, PPF and xdelta3, with bounded memory and 64-bit offsets. C core, Swift API.

* **Repository:** [github.com/Provenance-Emu/PVPatchEngine](https://github.com/Provenance-Emu/PVPatchEngine)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14

See [Applying Mods / Patches](../installation-and-usage/roms/mods.md) for what users see.

## PVWebServer

HTTP and WebDAV server on one port, built on Network.framework, with a route registry. Powers the in-app file manager and uploads.

* **Repository:** [github.com/Provenance-Emu/PVWebServer](https://github.com/Provenance-Emu/PVWebServer)
* **Used by:** Provenance, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 11, watchOS 9, visionOS 1

## PVWidgets

Home screen game widgets: grid and list drawn from the widget's real size, the Show and Layout options, cover decoding.

* **Repository:** [github.com/Provenance-Emu/PVWidgets](https://github.com/Provenance-Emu/PVWidgets)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14, visionOS 1

## PVLibrarySnapshot

The App Group snapshot and cover JPEGs an app writes for its extensions; the tvOS Top Shelf reads it.

* **Repository:** [github.com/Provenance-Emu/PVLibrarySnapshot](https://github.com/Provenance-Emu/PVLibrarySnapshot)
* **Used by:** Provenance, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14, visionOS 1

## PVHelp

In-app help from a GitBook wiki repo: navigation, page fetch and cache, GitBook preprocessing, offline fallback.

* **Repository:** [github.com/Provenance-Emu/PVHelp](https://github.com/Provenance-Emu/PVHelp)
* **Used by:** Provenance, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1

## PVRemoteLibrary

One model of "a game somewhere": on this device, on an emulator content server, on a RomM share or on a nearby peer. Matching, merged library rows, an on-disk catalogue and cover cache.

* **Repository:** [github.com/Provenance-Emu/PVRemoteLibrary](https://github.com/Provenance-Emu/PVRemoteLibrary)
* **Used by:** Provenance
* **Platforms:** iOS 17, tvOS 17, macOS 14, visionOS 1

## PVSyncRules

What an emulator app syncs: `SyncClassifier` (save state, battery save, ROM, BIOS), `SyncableFileType`, `SyncPolicy`. Pure value types, no I/O.

* **Repository:** [github.com/Provenance-Emu/PVSyncRules](https://github.com/Provenance-Emu/PVSyncRules)
* **Used by:** iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14

PVCloudSync and PVContinuity both build on it.

## PVCloudSync

CloudKit sync of user files: scanning, planning, conflict resolution, tombstones, a local trash, retry policy and a CloudKit provider.

* **Repository:** [github.com/Provenance-Emu/PVCloudSync](https://github.com/Provenance-Emu/PVCloudSync)
* **Used by:** iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14

## PVContinuity

Nearby library discovery, trust, manifests and file transfer between devices on the same network.

* **Repository:** [github.com/Provenance-Emu/PVContinuity](https://github.com/Provenance-Emu/PVContinuity)
* **Used by:** iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14

## ContinuityKit

Cross-device "continue this game" handoff: manifests, transfer, Bonjour discovery, library browse. A different API and wire protocol from PVContinuity.

* **Repository:** [github.com/Provenance-Emu/ContinuityKit](https://github.com/Provenance-Emu/ContinuityKit)
* **Used by:** iFly
* **Platforms:** iOS 16, tvOS 16, macOS 13, watchOS 9, visionOS 1

## Contributing

Change a package in its own repository, tag a release, then bump the version in each app that uses it. Pull requests are welcome on any of them; see [Contributing](contribute.md).

## See Also

* [Contributing](contribute.md)
* [Building from Source](../installation-and-usage/installing-provenance/building-from-source.md)
* [Skins](../info/skins-guide.md)
* [Open Source Licenses](../info/open-source-licenses.md)

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
