---
description: What skin format 2.0 is, and where its documentation lives
---

# Skin Format 2.0

{% hint style="warning" %}
**Format 2.0 is a work in progress.** The format, its tools and its docs are still changing, and app support is rolling out. Classic `.deltaskin` and `.manicskin` skins keep working.
{% endhint %}

Format 2.0 is a new way to make controller skins. A classic skin is a set of images with fixed button positions for each device and orientation. A 2.0 skin is one `skin.json` file that describes the controller as a tree of screens, controls and artwork, and a compatible app lays that tree out for the screen in front of it.

A 2.0 skin is baked into a normal `.deltaskin` archive. The archive also carries a classic layout and artwork, so apps that only read the classic format can still install and use it. You import it into Provenance the same way as any other skin: see the [Skins Guide](skins-guide.md#how-to-import-skins).

## Where the docs are

The format's documentation lives on **[emuskins.com/format](https://emuskins.com/format/)**, the site behind Provenance's skin catalog. It is kept there, not in this wiki, so there is one copy for every app that uses the format.

| Page | What it covers |
|:---|:---|
| [Overview](https://emuskins.com/format/) | What a 2.0 skin is and what the baked archive contains |
| [Tutorial](https://emuskins.com/format/tutorial.html) | Build a GameCube controller in six steps |
| [Examples](https://emuskins.com/format/examples.html) | Sources to preview and copy from |
| [Playground](https://emuskins.com/format/playground.html) | Edit a source in the browser, with a live preview and validator |
| [Reference](https://emuskins.com/format/reference.html) | Every node, field and allowed value |

To move or resize the parts of a classic skin that already exists, use the [skin editor](https://emuskins.com/edit.html).

## Making a 2.0 skin

1. Write a `skin.json`. The [tutorial](https://emuskins.com/format/tutorial.html) walks through one, and the [playground](https://emuskins.com/format/playground.html) checks it as you type.
2. Bake it into a `.deltaskin` with `skinkit-bake` from [SkinKit](https://github.com/Provenance-Emu/SkinKit). Step 6 of the tutorial has the command.
3. Import the archive into Provenance and check both orientations.
4. [Submit it to the catalog](skin-catalog-contributing.md) so it shows up in the in-app Skin Browser.

## For developers

- **[SkinKit](https://github.com/Provenance-Emu/SkinKit)** — The open-source Swift package Provenance, iCube and iFly share for loading, rendering and baking skins
- **[Format 2.0 design](https://github.com/Provenance-Emu/SkinKit/blob/main/docs/specs/2026-11-03-skin-format-2-design.md)** — The full specification
- **[JSON Schema](https://emuskins.com/format/skin-2.0.schema.json)** — Machine-readable schema that the reference is generated from
- **[Conversion notes](https://emuskins.com/format/migration.html)** — For emulator developers replacing a controller that code generates

Questions and feedback are welcome on [Discord](https://discord.gg/provenance) or in the [SkinKit issues](https://github.com/Provenance-Emu/SkinKit/issues).
