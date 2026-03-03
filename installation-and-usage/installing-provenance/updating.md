---
description: How to update your Provenance installation
---

# Updating Provenance

How you update depends on how you installed Provenance:

{% tabs %}
{% tab title="App Store (Automatic)" %}
**App Store updates are automatic** — no action needed.

To verify you're on the latest version:
1. Open the **App Store**
2. Tap your profile icon (top right)
3. Scroll to Provenance — tap **Update** if available

**Tip:** Make sure **Automatic Downloads** is enabled in Settings → App Store so updates install in the background.
{% endtab %}

{% tab title="Sideloaded (.ipa)" %}
To update a sideloaded installation:

1. Download the latest `.ipa` from [GitHub Releases](https://github.com/Provenance-Emu/Provenance/releases)
2. Re-sign and install using your sideloading tool ([AltStore](sideloading.md), Sideloadly, iOS App Signer)
3. Install **over** your existing version — use the **same Bundle ID** to preserve data

{% hint style="info" %}
Installing over an existing sideloaded version preserves your ROMs, saves, and settings. Using a different Bundle ID creates a separate installation.
{% endhint %}

Full guide: [Sideloading](sideloading.md)
{% endtab %}

{% tab title="Built from Source (Terminal)" %}
If you built from source, pull the latest changes and rebuild:

1. Navigate to your Provenance directory:
   ```bash
   cd /path/to/Provenance
   ```

2. Pull the latest source:

   **Option A — Overwrite local changes** (easiest, reapply Bundle ID after):
   ```bash
   git pull origin develop
   ```

   **Option B — Preserve local changes** (keeps your Bundle ID and code modifications):
   ```bash
   git stash
   git reset --hard HEAD
   git pull origin develop
   git stash pop
   ```

3. Update submodules and open in Xcode:
   ```bash
   make update
   make open
   ```

4. In Xcode:
   - If you used Option A, reapply your Bundle ID and signing settings
   - If you used Option B, just press **Run** (your settings are preserved)
5. Provenance compiles and installs on your device
{% endtab %}

{% tab title="Built from Source (Tower)" %}
If you use [Tower](https://www.git-tower.com/) as your Git client:

1. Open Provenance in Tower (Repositories → double-click **Provenance**)
2. With the `develop` branch selected (HEAD), click **Fetch**
3. If the branch shows pending changes, click **Pull**
4. Click **Stash Changes** if you have local modifications
5. After pulling, click **Apply Stash** to restore your changes
6. In Terminal:
   ```bash
   cd /path/to/Provenance
   make update
   make open
   ```
7. In Xcode, press **Run** to build and install
{% endtab %}
{% endtabs %}

---

## Command-Line Build Shortcuts

If you've already completed the [first-time setup](building-from-source.md), you can update and build entirely from Terminal:

```bash
# iPhone / iPad
make ios

# Apple TV
make tvos
```

These commands pull the latest source, update submodules, and build in one step.

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
