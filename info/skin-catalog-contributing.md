---
description: How to submit a skin to the Provenance online skin catalog so it appears in the built-in Skin Browser
---

# Contributing to the Skin Catalog

Provenance includes a built-in **Skin Browser** (Settings → Skins → Browse Catalog) that lets users discover and install community-created skins directly from the app. The catalog is a curated JSON file maintained in the Provenance repository — anyone can submit a skin to it via a pull request.

{% hint style="info" %}
Skins must be in `.deltaskin` or `.manicskin` format and hosted at a **publicly accessible download URL** to be included in the catalog.
{% endhint %}

---

## How the Catalog Works

The catalog is stored in two files that must always be kept in sync:

| File | Purpose |
|------|---------|
| `Scripts/catalog_seed.json` | Source of truth — edited by contributors |
| `PVUI/Sources/PVUIBase/Resources/catalog_seed.json` | Bundled copy — loaded by the app at runtime |

Both files must be committed together in every PR.

There are two ways to add skins: **auto-scrape** an existing community skin repository, or **add a single skin manually**.

---

## Option A: Auto-generate via Scraper

The repository includes a scraper script that crawls known community skin sources and regenerates the catalog automatically. This is the fastest way to add many skins at once.

### Prerequisites

```bash
pip install -r Scripts/requirements-scraper.txt
```

The script also works without extra packages using stdlib fallbacks (slower HTML parsing).

### Run the scraper

```bash
# Scrape all sources and write to Scripts/catalog_seed.json
python3 Scripts/scrape_skin_catalog.py \
    --source all \
    --output Scripts/catalog_seed.json

# Sync to the bundled app resources
cp Scripts/catalog_seed.json \
    PVUI/Sources/PVUIBase/Resources/catalog_seed.json
```

To avoid GitHub's 60 req/hr anonymous API rate limit, export a personal access token first:

```bash
export GITHUB_TOKEN="ghp_your_token_here"
python3 Scripts/scrape_skin_catalog.py --source all --output Scripts/catalog_seed.json
```

### Other useful scraper flags

```bash
# Dry run — no network requests, shows what would be scraped
python3 Scripts/scrape_skin_catalog.py --dry-run --source all

# Validate an existing catalog (checks schema + broken URLs)
python3 Scripts/scrape_skin_catalog.py --validate Scripts/catalog_seed.json

# Scrape one source only (options: delta-skins, broank, litritt)
python3 Scripts/scrape_skin_catalog.py --source delta-skins --output Scripts/catalog_seed.json
```

### Adding a new scraper source

To add support for a new community skin host, add a scraper function to `Scripts/scrape_skin_catalog.py` and register it in the `SOURCE_SCRAPERS` dictionary at the bottom of the file.

---

## Option B: Add a Skin Manually

Use this approach to add a single skin from any publicly accessible URL.

### Step 1: Generate a unique ID

Each catalog entry requires a 16-character hex ID derived from its source and download URL.

**Python:**

```python
import hashlib
source = "manual"
download_url = "https://example.com/MySkin.deltaskin"
skin_id = hashlib.sha256(f"{source}:{download_url}".encode()).hexdigest()[:16]
print(skin_id)
```

**Shell:**

```bash
printf 'manual:https://example.com/MySkin.deltaskin' | shasum -a 256 | cut -c1-16
```

### Step 2: Add the entry to catalog\_seed.json

Open `Scripts/catalog_seed.json` and add a new object to the `"skins"` array. Required fields are `id`, `name`, `systems`, `downloadURL`, and `source`. Sort entries by system code then by name for readability.

**Minimal valid entry:**

```json
{
  "id": "a1b2c3d4e5f60718",
  "name": "My Awesome GBA Skin",
  "author": "yourname",
  "systems": ["gba"],
  "gameTypeIdentifier": "com.rileytestut.delta.game.gba",
  "version": null,
  "downloadURL": "https://github.com/yourname/skins/raw/main/MyAwesomeGBA.deltaskin",
  "thumbnailURL": null,
  "screenshotURLs": [],
  "tags": [],
  "deviceSupport": [],
  "downloadCount": null,
  "rating": null,
  "lastUpdated": null,
  "fileSize": null,
  "source": "manual"
}
```

### Step 3: Validate the JSON

```bash
python3 -m json.tool Scripts/catalog_seed.json > /dev/null && echo "Valid JSON"
```

### Step 4: Sync to app resources

```bash
cp Scripts/catalog_seed.json \
    PVUI/Sources/PVUIBase/Resources/catalog_seed.json
```

---

## Catalog JSON Schema Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `id` | string | **Yes** | 16-character hex. Generate with `sha256("source:downloadURL")[:16]`. Must be unique. |
| `name` | string | **Yes** | Display name shown in the Skin Browser. |
| `author` | string or null | No | Skin creator's name or handle. |
| `systems` | string array | **Yes** | Short system codes (e.g. `["gba"]`). See table below. |
| `gameTypeIdentifier` | string or null | No | Delta-compatible game type identifier. |
| `version` | string or null | No | Skin version string. |
| `downloadURL` | string | **Yes** | Direct download URL for the `.deltaskin` or `.manicskin` file. |
| `thumbnailURL` | string or null | No | Preview image URL (JPEG or PNG). Shown in the browser grid. |
| `screenshotURLs` | string array | No | Additional in-use screenshot URLs. |
| `tags` | string array | No | Optional tags, e.g. `"landscape"`, `"dark"`, `"minimal"`. |
| `deviceSupport` | string array | No | Device hints, e.g. `["iphone-x", "iphone-legacy"]`. |
| `downloadCount` | number or null | No | Download count from source, if known. |
| `rating` | number or null | No | Rating 0.0–5.0, if known from source. |
| `lastUpdated` | string or null | No | ISO 8601 date the skin file was last updated. |
| `fileSize` | number or null | No | File size in bytes, if known. |
| `source` | string | **Yes** | Short source identifier, e.g. `"delta-skins.github.io"` or `"manual"`. |

---

## Supported Systems

| Short Code | System | `gameTypeIdentifier` |
|-----------|--------|----------------------|
| `gba` | Game Boy Advance | `com.rileytestut.delta.game.gba` |
| `gbc` | Game Boy Color / Game Boy | `com.rileytestut.delta.game.gbc` |
| `nes` | Nintendo Entertainment System | `com.rileytestut.delta.game.nes` |
| `snes` | Super Nintendo | `com.rileytestut.delta.game.snes` |
| `n64` | Nintendo 64 | `com.rileytestut.delta.game.n64` |
| `nds` | Nintendo DS | `com.rileytestut.delta.game.ds` |
| `genesis` | Sega Genesis / Mega Drive | `com.rileytestut.delta.game.genesis` |
| `unofficial` | Multi-system / other | *(none)* |

To add a new system, update the `SYSTEM_MAP` dictionary in `Scripts/scrape_skin_catalog.py`.

---

## Submitting a PR

1. **Target the `develop` branch** — not `master`.
2. **Commit both files** together: `Scripts/catalog_seed.json` and `PVUI/Sources/PVUIBase/Resources/catalog_seed.json`.
3. **PR title format:**
   - Single skin: `feat(skins): add "Skin Name" to catalog`
   - Bulk refresh: `chore(skins): refresh skin catalog from scraper`
4. **Verify the download URL** is publicly accessible — paste it into a browser and confirm the file downloads before submitting.
5. **Include a thumbnail URL** when possible so users can preview the skin in the browser grid.
6. **One skin per PR** for manual additions. Bulk scraper refreshes are fine as a single PR.
7. **Check for duplicates** — search `catalog_seed.json` for the skin's `downloadURL` before adding.

---

## See Also

- [Skins Guide](skins-guide.md) — Installing and using skins in Provenance
- [Contributing](../help/contribute.md) — General contribution guide for the Provenance project

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
