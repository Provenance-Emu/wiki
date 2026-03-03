---
description: Open games directly using Provenance's URL scheme
---

# Launch ROMs via URL

Provenance registers a custom URL scheme (`provenance://`) that lets you launch games directly from Safari, Shortcuts, home screen bookmarks, or other apps.

---

## URL Scheme Syntax

```
provenance://open?[parameter]=[value]
```

### Parameters

You can identify a game using any of these parameters (or combine them):

| Parameter | Description | Example |
|-----------|-------------|---------|
| `md5` | Game's MD5 hash (exact match) | `provenance://open?md5=85260599FDADA2E137053A8647AA0D06` |
| `title` | Game title (exact match, URL-encoded) | `provenance://open?title=Super%20Mario%20World` |
| `system` | System identifier (use with `title`) | `provenance://open?title=Sonic&system=com.provenance.genesis` |

### Combining Parameters

Use `title` + `system` together when you have games with the same name on different systems:

```
provenance://open?title=Tetris&system=com.provenance.gb
provenance://open?title=Tetris&system=com.provenance.nes
```

{% hint style="info" %}
If `system` is provided but invalid, the game will **not** open — even if a title match exists. Double-check your system identifier.
{% endhint %}

---

## System Identifiers

Use these identifiers with the `system` parameter:

| System | Identifier |
|--------|------------|
| **Nintendo** | |
| NES / Famicom | `com.provenance.nes` |
| Famicom Disk System | `com.provenance.fds` |
| SNES / Super Famicom | `com.provenance.snes` |
| Nintendo 64 | `com.provenance.n64` |
| Game Boy | `com.provenance.gb` |
| Game Boy Color | `com.provenance.gbc` |
| Game Boy Advance | `com.provenance.gba` |
| Virtual Boy | `com.provenance.vb` |
| Pokemon mini | `com.provenance.pokemonmini` |
| Nintendo DS | `com.provenance.nds` |
| Nintendo 3DS | `com.provenance.3ds` |
| **Sega** | |
| SG-1000 | `com.provenance.sg1000` |
| Master System | `com.provenance.mastersystem` |
| Genesis / Mega Drive | `com.provenance.genesis` |
| Game Gear | `com.provenance.gamegear` |
| Sega CD / Mega-CD | `com.provenance.segacd` |
| Sega 32X | `com.provenance.32x` |
| Sega Saturn | `com.provenance.saturn` |
| Dreamcast | `com.provenance.dreamcast` |
| **Sony** | |
| PlayStation | `com.provenance.psx` |
| PSP | `com.provenance.psp` |
| **Atari** | |
| Atari 2600 | `com.provenance.2600` |
| Atari 5200 | `com.provenance.5200` |
| Atari 7800 | `com.provenance.7800` |
| Atari Lynx | `com.provenance.lynx` |
| Atari Jaguar | `com.provenance.jaguar` |
| **NEC** | |
| PC Engine / TurboGrafx-16 | `com.provenance.pce` |
| TurboGrafx-CD | `com.provenance.pcecd` |
| PC Engine SuperGrafx | `com.provenance.sgx` |
| PC-FX | `com.provenance.pcfx` |
| **SNK** | |
| Neo Geo Pocket | `com.provenance.ngp` |
| Neo Geo Pocket Color | `com.provenance.ngpc` |
| **Bandai** | |
| WonderSwan | `com.provenance.ws` |
| WonderSwan Color | `com.provenance.wsc` |
| **Other** | |
| ColecoVision | `com.provenance.colecovision` |

---

## Use Cases

### Add a Game to Your Home Screen

Create a "shortcut" icon that launches directly into a game:

1. Open **Safari** on your iPhone/iPad
2. Type the URL in the address bar:
   ```
   provenance://open?title=Super%20Mario%20World
   ```
3. Tap **Share** (the share icon) → **Add to Home Screen**
4. Name it (e.g., "Super Mario World") and tap **Add**
5. Tap the new icon to launch directly into the game

{% hint style="info" %}
The home screen icon will use a generic Safari bookmark icon. For a custom icon, use the Shortcuts app method below.
{% endhint %}

### iOS Shortcuts Automation

Build Shortcuts workflows that launch games:

{% tabs %}
{% tab title="Simple Game Launcher" %}
1. Open the **Shortcuts** app
2. Tap **+** to create a new shortcut
3. Add action: **Open URLs**
4. Enter: `provenance://open?title=Your%20Game%20Name`
5. Tap the shortcut name → **Add to Home Screen**
6. Choose a custom icon and name
{% endtab %}

{% tab title="Game Picker Menu" %}
Create a menu that lets you choose from your favorite games:

1. Open **Shortcuts** → tap **+**
2. Add action: **Choose from Menu**
3. Add options for each game (e.g., "Mario", "Zelda", "Sonic")
4. Under each option, add **Open URLs** with the matching URL:
   - `provenance://open?title=Super%20Mario%20World`
   - `provenance://open?title=Legend%20of%20Zelda`
   - `provenance://open?title=Sonic%20the%20Hedgehog&system=com.provenance.genesis`
5. Add to Home Screen with a custom icon
{% endtab %}
{% endtabs %}

### Link from Other Apps

Use the URL scheme anywhere that supports links:

- **Notes app** — Paste URLs as tappable links to organize your game collection
- **Reminders** — Link a game for "play later" lists
- **Web pages** — Create an HTML page with links to your games
- **Other automation apps** — Scriptable, Toolbox Pro, etc.

---

## URL Encoding

Game titles with special characters must be URL-encoded:

| Character | Encoded | Example |
|-----------|---------|---------|
| Space | `%20` | `Super%20Mario%20Bros` |
| Apostrophe | `%27` | `Kirby%27s%20Adventure` |
| Colon | `%3A` | `Castlevania%3A%20SOTN` |
| Ampersand | `%26` | `Toejam%20%26%20Earl` |
| Parentheses | `%28` `%29` | `Pokemon%20%28Red%29` |

{% hint style="info" %}
**Tip:** The Shortcuts app handles URL encoding automatically when you use the "URL Encode" action. Safari also auto-encodes when you type in the address bar.
{% endhint %}

---

## Troubleshooting

<details>
<summary><strong>URL opens Provenance but no game launches</strong></summary>

- **Title mismatch:** The title must match exactly as it appears in your Provenance library (including capitalization and punctuation). Check your library for the exact name.
- **Invalid system ID:** If using the `system` parameter, verify the identifier from the table above. An invalid system ID causes the lookup to fail silently.
- **Game not imported:** The game must already be in your library. URLs don't import games — they only open existing ones.

</details>

<details>
<summary><strong>"Cannot Open Page" error in Safari</strong></summary>

- Provenance must be installed on the device
- Make sure the URL starts with `provenance://` (not `http://`)
- Check for typos in the URL

</details>

<details>
<summary><strong>Shortcut doesn't work</strong></summary>

- In Shortcuts, make sure you're using the **Open URLs** action (not "Open App")
- Verify the URL is correct by testing it in Safari first
- Ensure Provenance is allowed in Settings → Shortcuts

</details>

---

{% hint style="success" %}
**Pro tip:** Use the `md5` parameter for the most reliable matching — it uniquely identifies a ROM regardless of title or system. Find a game's MD5 in Provenance by long-pressing → Game Info.
{% endhint %}
