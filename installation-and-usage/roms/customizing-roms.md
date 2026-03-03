---
description: Rename games, replace cover art, and edit game metadata
---

# Customizing ROMs

Provenance lets you personalize your game library. You can replace cover art, rename games, and edit detailed game metadata — all from within the app.

**Customizable fields:** Cover Art, Title, Description, Genre, Publisher, Release Date, Region, Play History

{% hint style="warning" %}
Please refer to the [Known Issues](customizing-roms.md#known-issues) regarding customizing ROMs before posting a new one.
{% endhint %}

---

## Replacing Cover Art

{% tabs %}
{% tab title="Paste from Clipboard (iOS)" %}
The quickest way to replace a single game's artwork:

1. **Find an image** in Safari, Photos, Files, or any app
2. **Tap and hold** the image → **Copy**
3. Open **Provenance** → **long-press** the game you want to update
4. Select **Paste Custom Artwork**
5. The cover art updates immediately
{% endtab %}

{% tab title="Upload via Web Server" %}
Best for **bulk replacement** and **tvOS** (which doesn't support pasting).

1. Start the Web Server in Provenance:
   - Tap the **+** button in the Game Library, or
   - Settings → **Import/Export**
2. On your computer, open `http://[device-ip]` in a browser
3. Open the **Imports** folder
4. Upload your image files (`.png` or `.jpg`)
5. Provenance matches images to ROMs by filename

**WebDAV alternative:**
1. Connect to `http://[device-ip]:81` via Finder (Mac) or a WebDAV client
2. Drop images into the **Imports** folder
{% endtab %}

{% tab title="Mass Replacement" %}
Replace artwork for your entire library at once:

1. On your computer, gather all cover art files in **one folder**
2. Name each image to match its ROM filename (see [Formatting](#formatting) below)
3. Upload all images to the **Imports** folder via Web Server or WebDAV
4. Provenance auto-matches images to games

{% hint style="info" %}
Mass replacement via upload is the recommended method for large libraries. Pasting works one game at a time.
{% endhint %}
{% endtab %}
{% endtabs %}

### Formatting

For cover art to auto-match, image filenames must correspond to ROM filenames:

**ROM file:**
```
Super Mario World.sfc
```

**Matching cover art:**
```
Super Mario World.png
```

**Requirements:**
- Image format must be `.png` or `.jpg`
- Filename (minus extension) must match the ROM filename exactly
- Images without a matching ROM will remain in the directory until matched or manually deleted

---

## Renaming Games

{% tabs %}
{% tab title="iOS" %}
1. **Long-press** the game in your library
2. Select **Rename**
3. Type the new name → tap **Done**
{% endtab %}

{% tab title="tvOS" %}
1. **Select** the game and **press and hold** the Remote or Controller action button
2. Select **Rename**
3. Type the new name → select **Done**
{% endtab %}

{% tab title="Via Game Info (iOS)" %}
1. **Long-press** the game → select **Game Info**
2. **Long-press** the Title field
3. Edit the title → tap **Done**
{% endtab %}
{% endtabs %}

---

## Editing Game Info

Edit detailed metadata for any game (iOS only):

1. **Long-press** a game in your library
2. Select **Game Info** (or 3D Touch and swipe up)
3. **Long-press** any editable field:
   - Title
   - Description
   - Genre
   - Publisher
   - Release Date
   - Region
4. Type, paste, or reset the field → tap **Done**

{% hint style="info" %}
**Play History** (play count, time spent) can be **reset** but not manually edited.
{% endhint %}

---

## Known Issues

<details>
<summary><strong>Cover art lost on "Refresh Library"</strong></summary>

Custom cover art [is not retained](https://github.com/Provenance-Emu/Provenance/issues/730) when using the Refresh Library option in Settings. If you use custom artwork, keep backups of your image files so you can re-upload them via the Web Server after a refresh.

</details>

<details>
<summary><strong>Cover art doesn't appear after uploading</strong></summary>

- Upload **ROMs first**, then cover art — uploading art before its matching ROM may not match immediately
- Uploading ROMs + cover art in a single archive may delay matching
- **Fix:** Force quit Provenance and relaunch to trigger re-matching

</details>

<details>
<summary><strong>Custom game names reset on Refresh Library</strong></summary>

Custom names are [not currently preserved](https://github.com/Provenance-Emu/Provenance/issues/514) during Refresh Library. Avoid refreshing if you've renamed many games.

</details>

<details>
<summary><strong>Files with extra dots in filename cause a crash</strong></summary>

Filenames with multiple `.` characters (e.g., `Game.v2.1.zip`) can cause issues. Rename the file to use only one dot before the extension (e.g., `Game v2-1.zip`).

</details>

<details>
<summary><strong>Metadata not auto-matching for some ROMs</strong></summary>

ROMs that fail checksum matching (translations, hacks, homebrew) won't auto-populate metadata. You can manually edit game info from the Game Info view.

</details>

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
