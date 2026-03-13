---
description: How to submit your skin to the Provenance community catalog so it appears in the built-in Skin Browser
---

# Contributing to the Skin Catalog

Provenance includes a built-in **Skin Browser** (Settings → Skins → Browse Catalog) that lets users discover and install community skins directly from the app. The catalog is maintained at [github.com/Provenance-Emu/skins](https://github.com/Provenance-Emu/skins) — a dedicated open-source repo anyone can contribute to.

**[🎮 Browse the catalog →](https://provenance-emu.com/skins)**

{% hint style="info" %}
Skins must be in `.deltaskin` or `.manicskin` format and hosted at a **publicly accessible URL** to be included.
{% endhint %}

---

## Submission Methods

### Option 1 — Web form (easiest)

Visit **[provenance-emu.com/skins/submit.html](https://provenance-emu.com/skins/submit.html)**, paste your skin URL, and click **Fetch Metadata**. The page will auto-extract the name and system from your skin file, then let you submit with one click. A bot opens the PR for you within ~60 seconds.

### Option 2 — GitHub Issue

[Open a skin submission issue](https://github.com/Provenance-Emu/skins/issues/new?template=submit-skin.yml) and paste your URL. The bot processes it automatically and comments back with a link to the pull request.

Supported URL types:
- Direct `.deltaskin` or `.manicskin` file
- GitHub repo containing skin files (all skins imported at once)
- GitHub release URL (all skin assets imported)

### Option 3 — Pull Request (advanced)

Fork [Provenance-Emu/skins](https://github.com/Provenance-Emu/skins), add a JSON file to `skins/{system}/`, and open a PR. CI validates your entry automatically on submission.

**Generate a unique ID:**

```bash
# Shell
printf 'manual:https://example.com/MySkin.deltaskin' | shasum -a 256 | cut -c1-16

# Python
import hashlib
hashlib.sha256("manual:https://example.com/MySkin.deltaskin".encode()).hexdigest()[:16]
```

**Minimal JSON entry** (`skins/gba/my-skin-name.json`):

```json
{
  "id": "a1b2c3d4e5f60718",
  "name": "My GBA Skin",
  "author": "yourname",
  "systems": ["gba"],
  "gameTypeIdentifier": "com.rileytestut.delta.game.gba",
  "downloadURL": "https://github.com/you/skins/raw/main/MySkin.deltaskin",
  "thumbnailURL": null,
  "screenshotURLs": [],
  "tags": [],
  "source": "manual"
}
```

### Option 4 — Register your repo for auto-crawl

If you maintain a GitHub repo of skins, [register it](https://github.com/Provenance-Emu/skins/issues/new?template=register-source.yml). The weekly crawler will scan your repo every Monday and automatically open PRs for any new skins it finds — no manual submission needed per skin.

---

## Hosting Your Own Skins on GitHub (Free)

GitHub is the best place to host skin files — it's free, permanent, and gives you stable download URLs.

1. **Create a public repo** at github.com (e.g. `yourname/skins`)
2. **Upload your `.deltaskin` / `.manicskin` files** — drag and drop in the GitHub web UI
3. **Get the raw URL**: click a file → **Raw** → copy the URL
4. **Submit** the repo or individual file URL via any method above

Raw URLs look like:
```
https://raw.githubusercontent.com/yourname/skins/main/MySkin.deltaskin
```

These URLs never change as long as the file stays in the same place. You can use GitHub Releases for versioned bundles.

{% hint style="success" %}
**Advantages over DeltaStyles:** instant updates, version history, no account required on a third-party site, and new systems supported by Provenance are added to the catalog before DeltaStyles updates their system list.
{% endhint %}

---

## Catalog JSON Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | **Yes** | 16-char hex. Generate with `sha256("source:downloadURL")[:16]`. |
| `name` | string | **Yes** | Display name in the Skin Browser. |
| `systems` | array | **Yes** | System codes — see table below. |
| `downloadURL` | string | **Yes** | Direct `.deltaskin` or `.manicskin` URL. |
| `source` | string | **Yes** | Short identifier, e.g. `"manual"` or `"yourname/repo"`. |
| `author` | string | No | Creator's name or handle. |
| `gameTypeIdentifier` | string | No | Delta-compatible GTI (auto-detected from skin file). |
| `thumbnailURL` | string | No | Preview image URL — strongly recommended. |
| `screenshotURLs` | array | No | Additional screenshots. |
| `tags` | array | No | e.g. `"dark"`, `"minimal"`, `"landscape"`. |
| `version` | string | No | Skin version string. |
| `fileSize` | number | No | File size in bytes. |
| `lastUpdated` | string | No | ISO 8601 date. |

---

## Supported Systems

| Code | System | `gameTypeIdentifier` |
|------|--------|----------------------|
| `gba` | Game Boy Advance | `com.rileytestut.delta.game.gba` |
| `gbc` | Game Boy Color / Game Boy | `com.rileytestut.delta.game.gbc` |
| `nes` | Nintendo Entertainment System | `com.rileytestut.delta.game.nes` |
| `snes` | Super Nintendo | `com.rileytestut.delta.game.snes` |
| `n64` | Nintendo 64 | `com.rileytestut.delta.game.n64` |
| `nds` | Nintendo DS | `com.rileytestut.delta.game.ds` |
| `genesis` | Sega Genesis / Mega Drive | `com.rileytestut.delta.game.genesis` |
| `unofficial` | Multi-system / other | *(none)* |

---

## See Also

- [Skins Guide](skins-guide.md) — Installing and using skins in Provenance
- [Contributing](../help/contribute.md) — General contribution guide

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
