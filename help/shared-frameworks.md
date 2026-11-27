---
description: The Swift packages Provenance, iFly and iCube share, what each one does, and how to add one to your own app.
---

# Shared Frameworks

Provenance, [iFly](https://ifly-emu.com) (Dreamcast) and [iCube](https://icube-emu.com) (GameCube / Wii) are three apps built on the same parts. Anything two of them need lives in its own Swift package, in its own repository under [github.com/Provenance-Emu](https://github.com/Provenance-Emu), and each app depends on it by URL. A fix made once lands in all three.

None of these packages knows which app it is in. App group names, CloudKit containers, URL schemes and colors are passed in by the host app, so the packages work in any emulator frontend for Apple platforms, not only ours.

## The packages

| Package | What it does | Latest | Used by | Platforms |
|---|---|---|---|---|
| [SkinKit](#skinkit) | Controller skins: `.deltaskin` / `.manicskin` parsing, the Format 2 renderer, the skin manager and store browser, RetroArch overlay import, and the TV bezels around the picture (`SkinKitBezels`). | [0.10.0](https://github.com/Provenance-Emu/SkinKit/releases/tag/0.10.0) | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14 |
| [GamepadKit](#gamepadkit) | Controller handling: element-name mapping, positional fallback for plain HID pads, pad family detection, pause triggers, and a synthesized extended gamepad for pads iOS exposes without one (Switch Online SNES / N64 / Mega Drive, generic USB and Bluetooth pads). | [0.3.2](https://github.com/Provenance-Emu/GamepadKit/releases/tag/0.3.2) | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14 |
| [PVSystems](#pvsystems) | `SystemIdentifier` and per-system metadata: TheGamesDB / libretrodb / OpenVGDB IDs, RetroAchievements console IDs, the per-game BIOS manifest. | [1.0.3](https://github.com/Provenance-Emu/PVSystems/releases/tag/1.0.3) | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1 |
| [PVLookup](#pvlookup) | Game metadata, artwork and cheat lookup over libretrodb, OpenVGDB, TheGamesDB, ShiraGame and the libretro cheat database. Ships no database bytes; they are release assets fetched at build time. | [1.1.0](https://github.com/Provenance-Emu/PVLookup/releases/tag/1.1.0) | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1 |
| [PVPatchEngine](#pvpatchengine) | Streaming ROM and disc patch engine: IPS, BPS, UPS, PPF and xdelta3, with bounded memory and 64-bit offsets. C core, Swift API. | [1.0.3](https://github.com/Provenance-Emu/PVPatchEngine/releases/tag/1.0.3) | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14 |
| [PVWebServer](#pvwebserver) | HTTP and WebDAV server on one port, built on Network.framework, with a route registry. Powers the in-app file manager and uploads. | [1.3.5](https://github.com/Provenance-Emu/PVWebServer/releases/tag/1.3.5) | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 11, watchOS 9, visionOS 1 |
| [PVWidgets](#pvwidgets) | Home screen game widgets: grid and list drawn from the widget's real size, the Show and Layout options, cover decoding. | [0.1.0](https://github.com/Provenance-Emu/PVWidgets/tree/0.1.0) | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14, visionOS 1 |
| [PVLibrarySnapshot](#pvlibrarysnapshot) | The App Group snapshot and cover JPEGs an app writes for its extensions; the tvOS Top Shelf reads it. | [1.0.2](https://github.com/Provenance-Emu/PVLibrarySnapshot/releases/tag/1.0.2) | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14, visionOS 1 |
| [PVHelp](#pvhelp) | In-app help from a GitBook wiki repo: navigation, page fetch and cache, GitBook preprocessing, offline fallback. | [1.0.2](https://github.com/Provenance-Emu/PVHelp/releases/tag/1.0.2) | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1 |
| [PVRemoteLibrary](#pvremotelibrary) | One model of "a game somewhere": on this device, on an emulator content server, on a RomM share or on a nearby peer. Matching, merged library rows, an on-disk catalogue and cover cache. | [0.3.3](https://github.com/Provenance-Emu/PVRemoteLibrary/releases/tag/0.3.3) | Provenance, iFly, iCube | iOS 17, tvOS 17, macOS 14, visionOS 1 |
| [PVSyncRules](#pvsyncrules) | What an emulator app syncs: `SyncClassifier` (save state, battery save, ROM, BIOS), `SyncableFileType`, `SyncPolicy`. Pure value types, no I/O. | [1.0.5](https://github.com/Provenance-Emu/PVSyncRules/releases/tag/1.0.5) | iCube | iOS 17, tvOS 17, macOS 14 |
| [PVCloudSync](#pvcloudsync) | CloudKit sync of user files: scanning, planning, conflict resolution, tombstones, a local trash, retry policy and a CloudKit provider. | [1.1.2](https://github.com/Provenance-Emu/PVCloudSync/releases/tag/1.1.2) | Provenance, iCube | iOS 17, tvOS 17, macOS 14 |
| [PVContinuity](#pvcontinuity) | Nearby library discovery, trust, manifests and file transfer between devices on the same network. | [1.0.3](https://github.com/Provenance-Emu/PVContinuity/releases/tag/1.0.3) | iCube | iOS 17, tvOS 17, macOS 14 |
| [ContinuityKit](#continuitykit) | Cross-device "continue this game" handoff: manifests, transfer, Bonjour discovery, library browse. A different API and wire protocol from PVContinuity. | [1.0.3](https://github.com/Provenance-Emu/ContinuityKit/releases/tag/1.0.3) | iFly | iOS 16, tvOS 16, macOS 13, watchOS 9, visionOS 1 |
| [PVDependencies](#pvdependencies) | Prebuilt XCFrameworks of the third-party libraries the apps and packages share (SQLite.swift, ZIPFoundation): one copy per app, never compiled. | [1.0.0](https://github.com/Provenance-Emu/PVDependencies/releases/tag/1.0.0) | Provenance, iFly, iCube |  |

Versions, dates, platforms, languages and topics on this page are read from each repository once a day; the descriptions are written by hand.

## Adding a package

Every package is a plain SwiftPM package with version tags. In `Package.swift`:

```swift
dependencies: [
    .package(url: "https://github.com/Provenance-Emu/SkinKit.git", from: "0.10.0")
],
targets: [
    .target(name: "MyApp", dependencies: [
        .product(name: "SkinKitCore", package: "SkinKit")
    ])
]
```

In Xcode: **File → Add Package Dependencies…** and paste the repository URL.

A version marked *prebuilt XCFramework* resolves to a binary, so your app compiles none of the package. To build it from source instead, set `PV_BUILD_FROM_SOURCE=1` in the environment Xcode starts in and resolve packages again.

{% hint style="info" %}
Packages at `0.x` (SkinKit, GamepadKit, PVWidgets, PVRemoteLibrary) may break their API in a minor release. Pin them with `.upToNextMinor(from:)`.
{% endhint %}

## SkinKit

Controller skins: `.deltaskin` / `.manicskin` parsing, the Format 2 renderer, the skin manager and store browser, RetroArch overlay import, and the TV bezels around the picture (`SkinKitBezels`).

* **Repository:** [github.com/Provenance-Emu/SkinKit](https://github.com/Provenance-Emu/SkinKit)
* **Latest version:** [0.10.0](https://github.com/Provenance-Emu/SkinKit/releases/tag/0.10.0), released 2026-11-27 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/SkinKit/releases)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14
* **Languages:** Swift 99%
* **License:** [see the repository](https://github.com/Provenance-Emu/SkinKit)
* **Topics:** [controller-skin](https://github.com/topics/controller-skin), [crt-bezel](https://github.com/topics/crt-bezel), [delta-skins](https://github.com/topics/delta-skins), [deltaskin](https://github.com/topics/deltaskin), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [emuskin](https://github.com/topics/emuskin), [ios](https://github.com/topics/ios), [manicskin](https://github.com/topics/manicskin), [provenance](https://github.com/topics/provenance), [retroarch-overlay](https://github.com/topics/retroarch-overlay), [retrogaming](https://github.com/topics/retrogaming), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [swiftui](https://github.com/topics/swiftui), [touch-controls](https://github.com/topics/touch-controls), [tvos](https://github.com/topics/tvos), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/SkinKit.git", .upToNextMinor(from: "0.10.0"))
```

Skins themselves are in the [skin catalog](https://emuskins.com). See the [Skins guide](../info/skins-guide.md) and [Skin Format 2.0](../info/skin-format-2.md).

## GamepadKit

Controller handling: element-name mapping, positional fallback for plain HID pads, pad family detection, pause triggers, and a synthesized extended gamepad for pads iOS exposes without one (Switch Online SNES / N64 / Mega Drive, generic USB and Bluetooth pads).

* **Repository:** [github.com/Provenance-Emu/GamepadKit](https://github.com/Provenance-Emu/GamepadKit)
* **Latest version:** [0.3.2](https://github.com/Provenance-Emu/GamepadKit/releases/tag/0.3.2), released 2026-11-27 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/GamepadKit/releases)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14
* **Languages:** Swift 100%
* **License:** [MIT](https://github.com/Provenance-Emu/GamepadKit/blob/HEAD/LICENSE.md)
* **Topics:** [bluetooth-controller](https://github.com/topics/bluetooth-controller), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [game-controller](https://github.com/topics/game-controller), [gamecontroller](https://github.com/topics/gamecontroller), [gamepad](https://github.com/topics/gamepad), [hid](https://github.com/topics/hid), [ios](https://github.com/topics/ios), [mfi](https://github.com/topics/mfi), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [tvos](https://github.com/topics/tvos), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/GamepadKit.git", .upToNextMinor(from: "0.3.2"))
```

## PVSystems

`SystemIdentifier` and per-system metadata: TheGamesDB / libretrodb / OpenVGDB IDs, RetroAchievements console IDs, the per-game BIOS manifest.

* **Repository:** [github.com/Provenance-Emu/PVSystems](https://github.com/Provenance-Emu/PVSystems)
* **Latest version:** [1.0.3](https://github.com/Provenance-Emu/PVSystems/releases/tag/1.0.3), released 2026-11-25 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVSystems/releases)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1
* **Languages:** Swift 100%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVSystems)
* **Topics:** [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [game-systems](https://github.com/topics/game-systems), [ios](https://github.com/topics/ios), [libretro](https://github.com/topics/libretro), [metadata](https://github.com/topics/metadata), [provenance](https://github.com/topics/provenance), [retroachievements](https://github.com/topics/retroachievements), [retrogaming](https://github.com/topics/retrogaming), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [tvos](https://github.com/topics/tvos), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/PVSystems.git", from: "1.0.3")
```

## PVLookup

Game metadata, artwork and cheat lookup over libretrodb, OpenVGDB, TheGamesDB, ShiraGame and the libretro cheat database. Ships no database bytes; they are release assets fetched at build time.

* **Repository:** [github.com/Provenance-Emu/PVLookup](https://github.com/Provenance-Emu/PVLookup)
* **Latest version:** [1.1.0](https://github.com/Provenance-Emu/PVLookup/releases/tag/1.1.0), released 2026-11-25 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVLookup/releases)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1
* **Languages:** Swift 91%, Python 7%, Shell 2%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVLookup)
* **Topics:** [box-art](https://github.com/topics/box-art), [cheats](https://github.com/topics/cheats), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [game-metadata](https://github.com/topics/game-metadata), [ios](https://github.com/topics/ios), [libretrodb](https://github.com/topics/libretrodb), [openvgdb](https://github.com/topics/openvgdb), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [spm](https://github.com/topics/spm), [sqlite](https://github.com/topics/sqlite), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [thegamesdb](https://github.com/topics/thegamesdb), [tvos](https://github.com/topics/tvos), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/PVLookup.git", from: "1.1.0")
```

The databases are published as `databases-YYYY-MM-DD` releases on the repository; an app pins one by sha256 and bundles the zips.

## PVPatchEngine

Streaming ROM and disc patch engine: IPS, BPS, UPS, PPF and xdelta3, with bounded memory and 64-bit offsets. C core, Swift API.

* **Repository:** [github.com/Provenance-Emu/PVPatchEngine](https://github.com/Provenance-Emu/PVPatchEngine)
* **Latest version:** [1.0.3](https://github.com/Provenance-Emu/PVPatchEngine/releases/tag/1.0.3), released 2026-11-25 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVPatchEngine/releases)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14
* **Languages:** C 69%, Swift 31%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVPatchEngine)
* **Topics:** [bps](https://github.com/topics/bps), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [ios](https://github.com/topics/ios), [ips](https://github.com/topics/ips), [ppf](https://github.com/topics/ppf), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [rom-hacking](https://github.com/topics/rom-hacking), [rom-patcher](https://github.com/topics/rom-patcher), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [tvos](https://github.com/topics/tvos), [ups](https://github.com/topics/ups), [xcframework](https://github.com/topics/xcframework), [xdelta3](https://github.com/topics/xdelta3)

```swift
.package(url: "https://github.com/Provenance-Emu/PVPatchEngine.git", from: "1.0.3")
```

See [Applying Mods / Patches](../installation-and-usage/roms/mods.md) for what users see.

## PVWebServer

HTTP and WebDAV server on one port, built on Network.framework, with a route registry. Powers the in-app file manager and uploads.

* **Repository:** [github.com/Provenance-Emu/PVWebServer](https://github.com/Provenance-Emu/PVWebServer)
* **Latest version:** [1.3.5](https://github.com/Provenance-Emu/PVWebServer/releases/tag/1.3.5), released 2026-11-25 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVWebServer/releases)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 11, watchOS 9, visionOS 1
* **Languages:** Swift 86%, JavaScript 5%, Shell 4%, CSS 3%, HTML 1%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVWebServer)
* **Topics:** [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [file-upload](https://github.com/topics/file-upload), [http-server](https://github.com/topics/http-server), [ios](https://github.com/topics/ios), [network-framework](https://github.com/topics/network-framework), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [swift-server](https://github.com/topics/swift-server), [tvos](https://github.com/topics/tvos), [webdav](https://github.com/topics/webdav), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/PVWebServer.git", from: "1.3.5")
```

## PVWidgets

Home screen game widgets: grid and list drawn from the widget's real size, the Show and Layout options, cover decoding.

* **Repository:** [github.com/Provenance-Emu/PVWidgets](https://github.com/Provenance-Emu/PVWidgets)
* **Latest version:** [0.1.0](https://github.com/Provenance-Emu/PVWidgets/tree/0.1.0), released 2026-11-20 (source)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVWidgets/releases)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14, visionOS 1
* **Languages:** Swift 100%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVWidgets)
* **Topics:** [app-intents](https://github.com/topics/app-intents), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [home-screen-widgets](https://github.com/topics/home-screen-widgets), [ios](https://github.com/topics/ios), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [swiftui](https://github.com/topics/swiftui), [tvos](https://github.com/topics/tvos), [widgetkit](https://github.com/topics/widgetkit), [widgets](https://github.com/topics/widgets)

```swift
.package(url: "https://github.com/Provenance-Emu/PVWidgets.git", .upToNextMinor(from: "0.1.0"))
```

## PVLibrarySnapshot

The App Group snapshot and cover JPEGs an app writes for its extensions; the tvOS Top Shelf reads it.

* **Repository:** [github.com/Provenance-Emu/PVLibrarySnapshot](https://github.com/Provenance-Emu/PVLibrarySnapshot)
* **Latest version:** [1.0.2](https://github.com/Provenance-Emu/PVLibrarySnapshot/releases/tag/1.0.2), released 2026-11-25 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVLibrarySnapshot/releases)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14, visionOS 1
* **Languages:** Swift 100%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVLibrarySnapshot)
* **Topics:** [app-extensions](https://github.com/topics/app-extensions), [app-groups](https://github.com/topics/app-groups), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [ios](https://github.com/topics/ios), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [top-shelf](https://github.com/topics/top-shelf), [tvos](https://github.com/topics/tvos), [widgetkit](https://github.com/topics/widgetkit), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/PVLibrarySnapshot.git", from: "1.0.2")
```

## PVHelp

In-app help from a GitBook wiki repo: navigation, page fetch and cache, GitBook preprocessing, offline fallback.

* **Repository:** [github.com/Provenance-Emu/PVHelp](https://github.com/Provenance-Emu/PVHelp)
* **Latest version:** [1.0.2](https://github.com/Provenance-Emu/PVHelp/releases/tag/1.0.2), released 2026-11-25 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVHelp/releases)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14, watchOS 9, visionOS 1
* **Languages:** Swift 100%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVHelp)
* **Topics:** [documentation](https://github.com/topics/documentation), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [gitbook](https://github.com/topics/gitbook), [in-app-help](https://github.com/topics/in-app-help), [ios](https://github.com/topics/ios), [markdown](https://github.com/topics/markdown), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [tvos](https://github.com/topics/tvos), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/PVHelp.git", from: "1.0.2")
```

## PVRemoteLibrary

One model of "a game somewhere": on this device, on an emulator content server, on a RomM share or on a nearby peer. Matching, merged library rows, an on-disk catalogue and cover cache.

* **Repository:** [github.com/Provenance-Emu/PVRemoteLibrary](https://github.com/Provenance-Emu/PVRemoteLibrary)
* **Latest version:** [0.3.3](https://github.com/Provenance-Emu/PVRemoteLibrary/releases/tag/0.3.3), released 2026-11-26 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVRemoteLibrary/releases)
* **Used by:** Provenance, iFly, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14, visionOS 1
* **Languages:** Swift 100%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVRemoteLibrary)
* **Topics:** [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [game-library](https://github.com/topics/game-library), [ios](https://github.com/topics/ios), [library-sync](https://github.com/topics/library-sync), [provenance](https://github.com/topics/provenance), [remote-library](https://github.com/topics/remote-library), [retrogaming](https://github.com/topics/retrogaming), [romm](https://github.com/topics/romm), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [swift-package-manager](https://github.com/topics/swift-package-manager), [swiftui](https://github.com/topics/swiftui), [tvos](https://github.com/topics/tvos), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/PVRemoteLibrary.git", .upToNextMinor(from: "0.3.3"))
```

## PVSyncRules

What an emulator app syncs: `SyncClassifier` (save state, battery save, ROM, BIOS), `SyncableFileType`, `SyncPolicy`. Pure value types, no I/O.

* **Repository:** [github.com/Provenance-Emu/PVSyncRules](https://github.com/Provenance-Emu/PVSyncRules)
* **Latest version:** [1.0.5](https://github.com/Provenance-Emu/PVSyncRules/releases/tag/1.0.5), released 2026-11-25 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVSyncRules/releases)
* **Used by:** iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14
* **Languages:** Swift 100%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVSyncRules)
* **Topics:** [cloudkit](https://github.com/topics/cloudkit), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [file-sync](https://github.com/topics/file-sync), [icloud](https://github.com/topics/icloud), [ios](https://github.com/topics/ios), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [save-states](https://github.com/topics/save-states), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [tvos](https://github.com/topics/tvos), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/PVSyncRules.git", from: "1.0.5")
```

PVCloudSync and PVContinuity both build on it.

## PVCloudSync

CloudKit sync of user files: scanning, planning, conflict resolution, tombstones, a local trash, retry policy and a CloudKit provider.

* **Repository:** [github.com/Provenance-Emu/PVCloudSync](https://github.com/Provenance-Emu/PVCloudSync)
* **Latest version:** [1.1.2](https://github.com/Provenance-Emu/PVCloudSync/releases/tag/1.1.2), released 2026-11-25 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVCloudSync/releases)
* **Used by:** Provenance, iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14
* **Languages:** Swift 100%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVCloudSync)
* **Topics:** [cloudkit](https://github.com/topics/cloudkit), [conflict-resolution](https://github.com/topics/conflict-resolution), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [file-sync](https://github.com/topics/file-sync), [icloud](https://github.com/topics/icloud), [ios](https://github.com/topics/ios), [ios-swift](https://github.com/topics/ios-swift), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [save-states](https://github.com/topics/save-states), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [swift-package-manager](https://github.com/topics/swift-package-manager), [tvos](https://github.com/topics/tvos), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/PVCloudSync.git", from: "1.1.2")
```

## PVContinuity

Nearby library discovery, trust, manifests and file transfer between devices on the same network.

* **Repository:** [github.com/Provenance-Emu/PVContinuity](https://github.com/Provenance-Emu/PVContinuity)
* **Latest version:** [1.0.3](https://github.com/Provenance-Emu/PVContinuity/releases/tag/1.0.3), released 2026-11-27 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVContinuity/releases)
* **Used by:** iCube
* **Platforms:** iOS 17, tvOS 17, macOS 14
* **Languages:** Swift 100%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVContinuity)
* **Topics:** [bonjour](https://github.com/topics/bonjour), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [file-transfer](https://github.com/topics/file-transfer), [handoff](https://github.com/topics/handoff), [ios](https://github.com/topics/ios), [local-network](https://github.com/topics/local-network), [peer-to-peer](https://github.com/topics/peer-to-peer), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [swift-package-manager](https://github.com/topics/swift-package-manager), [swiftui](https://github.com/topics/swiftui), [tvos](https://github.com/topics/tvos), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/PVContinuity.git", from: "1.0.3")
```

## ContinuityKit

Cross-device "continue this game" handoff: manifests, transfer, Bonjour discovery, library browse. A different API and wire protocol from PVContinuity.

* **Repository:** [github.com/Provenance-Emu/ContinuityKit](https://github.com/Provenance-Emu/ContinuityKit)
* **Latest version:** [1.0.3](https://github.com/Provenance-Emu/ContinuityKit/releases/tag/1.0.3), released 2026-11-27 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/ContinuityKit/releases)
* **Used by:** iFly
* **Platforms:** iOS 16, tvOS 16, macOS 13, watchOS 9, visionOS 1
* **Languages:** Swift 100%
* **License:** [see the repository](https://github.com/Provenance-Emu/ContinuityKit)
* **Topics:** [bonjour](https://github.com/topics/bonjour), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [file-transfer](https://github.com/topics/file-transfer), [handoff](https://github.com/topics/handoff), [ios](https://github.com/topics/ios), [local-network](https://github.com/topics/local-network), [peer-to-peer](https://github.com/topics/peer-to-peer), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [spm](https://github.com/topics/spm), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [tvos](https://github.com/topics/tvos), [xcframework](https://github.com/topics/xcframework)

```swift
.package(url: "https://github.com/Provenance-Emu/ContinuityKit.git", from: "1.0.3")
```

## PVDependencies

Prebuilt XCFrameworks of the third-party libraries the apps and packages share (SQLite.swift, ZIPFoundation): one copy per app, never compiled.

* **Repository:** [github.com/Provenance-Emu/PVDependencies](https://github.com/Provenance-Emu/PVDependencies)
* **Latest version:** [1.0.0](https://github.com/Provenance-Emu/PVDependencies/releases/tag/1.0.0), released 2026-11-25 (prebuilt XCFramework)
* **Releases:** [all versions](https://github.com/Provenance-Emu/PVDependencies/releases)
* **Used by:** Provenance, iFly, iCube
* **Languages:** Shell 69%, Swift 31%
* **License:** [see the repository](https://github.com/Provenance-Emu/PVDependencies)
* **Topics:** [binary-framework](https://github.com/topics/binary-framework), [emulation](https://github.com/topics/emulation), [emulator](https://github.com/topics/emulator), [ios](https://github.com/topics/ios), [prebuilt](https://github.com/topics/prebuilt), [provenance](https://github.com/topics/provenance), [retrogaming](https://github.com/topics/retrogaming), [spm](https://github.com/topics/spm), [sqlite](https://github.com/topics/sqlite), [swift](https://github.com/topics/swift), [swift-package](https://github.com/topics/swift-package), [tvos](https://github.com/topics/tvos), [xcframework](https://github.com/topics/xcframework), [zipfoundation](https://github.com/topics/zipfoundation)

```swift
.package(url: "https://github.com/Provenance-Emu/PVDependencies.git", from: "1.0.0")
```

An app that uses PVLookup or SkinKit takes these libraries from here too: a package graph cannot hold this copy and the upstream package at once.

## Contributing

Change a package in its own repository, release it, then bump the version in each app that uses it. Pull requests are welcome on any of them; see [Contributing](contribute.md).

## See Also

* [Contributing](contribute.md)
* [Building from Source](../installation-and-usage/installing-provenance/building-from-source.md)
* [Skins](../info/skins-guide.md)
* [Open Source Licenses](../info/open-source-licenses.md)

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
