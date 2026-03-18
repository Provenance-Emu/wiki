---
description: Easy. Install pre-built releases (or pre-releases).
---

# Sideloading

Prebuilt .ipa releases can be sideloaded onto your devices and must be re-signed using your own developer profile\(s\).

## **Download Provenance**

1. First, download a [Release](https://github.com/Provenance-Emu/Provenance/releases) or Prerelease of Provenance (unless using AltStore, direct source download link in AltStore instructions).
2. Choose a sideloading method:

### **Sideloading Options:**

* ❇️  [**AltStore**](sideloading.md#altstore) · macOS/Windows
* 🖋  [**iOS App Signer**](sideloading.md#ios-app-signer) · macOS + Xcode or Configurator
* 🧪  [**AltDeploy**](sideloading.md#altdeploy) · macOS

{% hint style="success" %}
**Requirements**

* _Free_ [Apple Developer](https://9to5mac.com/2016/03/27/how-to-create-free-apple-developer-account-sideload-apps/) account \(at a minimum\) or a _paid_ account.
  ****

  🛑 **DO NOT** enroll to join the full Developer Program or you will be locked into a _Pending_ payment state, unable to code-sign unless you pay or contact Apple to cancel the enrollment.

* Connections:
  * iPhone / iPad:    `Lightning` → `USB-A / USB-C` cable¹
  * Apple TV 4:      `USB-C` → `USB-A / USB-C` cable¹
  * Apple TV 4K:     `WiFi`²  \([Instructions](http://www.redmondpie.com/how-to-wirelessly-connect-apple-tv-4k-to-xcode-on-mac/)\)³

¹ Depends on which [ports](https://support.apple.com/en-us/HT201736) you have. _WiFi can be setup after._
² USB ports have been discontinued on Apple TV 4K+.
³ If using a virtual machine, you may need to [configure your network settings](../../info/miscellaneous/virtualizing-macos.md#cannot-detect-apple-tv-4k-over-wifi).
{% endhint %}

{% hint style="danger" %}
Sideloading from 3rd party sources _**is not supported**_.
{% endhint %}

💢  If you get stuck, check out [Troubleshooting](sideloading.md#troubleshooting).

{% tabs %}
{% tab title="❇️ AltStore" %}
AltStore source is available at [this link](altstore://source?url=https://provenance-emu.com/apps.json) — click in Mobile Safari once you have AltStore installed.

1. Download and launch [AltStore](https://altstore.io).
2. Connect your device (you may need to open **Finder** and choose `Trust…` when it pops up).
3. Follow instructions via altstore.io and the app as it guides you.
4. Put the Provenance .ipa in your iCloud Drive somewhere and install via AltStore app by using the `+` button in the upper left of the My Apps screen.

{% hint style="info" %}
Free Apple developer provisioning expires _every 7 days_, but AltStore can keep track of and handle renewal for you. Re-sideloading will not cause you to lose any data.
{% endhint %}

{% hint style="warning" %}
Windows AltStore has not been tested by the Provenance team. Support may be limited.
{% endhint %}
{% endtab %}

{% tab title="🖋 iOS App Signer" %}
1. Download and launch [iOS App Signer](https://dantheman827.github.io/ios-app-signer/).
2. Select `.ipa` file and resign it to yourself, selecting the Provenance Bundle ID you've used in the past. If you don't have one, create one:
   🆔 Bundle ID: `com.[change-this].provenance` — replace `[change-this]` with something unique like your username.
3. Connect your device. ⚠️ If you haven't yet, register your device to your Apple ID in Xcode. Easiest way is to make a dummy app in Xcode and have it automatically create the provisioning ([Example](https://dantheman827.github.io/ios-app-signer/#tab-bar)).
4. Install:
   * [Xcode](https://apps.apple.com/us/app/xcode/id497799835): Window → Devices and Simulators → Select your device → Drop the `.ipa` onto Installed Apps.
   * [Configurator](https://support.apple.com/apple-configurator): Double-click your device → Apps → Drop the `.ipa` here.
5. On device: Go to `Settings` → `General` → `Profiles & Device Management`, tap on your certificate and then `Trust`.
6. _Done._ (If using a free developer account, repeat from step 4 after it **expires in 7 days**)

{% hint style="info" %}
Free Apple developer provisioning expires _every 7 days_, requiring reloading, but you will not lose any data.
{% endhint %}
{% endtab %}

{% tab title="🧪 AltDeploy" %}
1. Download and launch [AltDeploy](https://github.com/pixelomer/AltDeploy/releases).
2. Connect your device (you may need to open **Finder** and choose `Trust…` when it pops up).
3. Select your device in AltDeploy.
4. Drag & drop `.ipa` file onto Impactor.
5. Enter your Apple ID.
6. If _not_ using 2-Factor Authentication, enter your account password, otherwise:
   1. Login to your [Apple ID](https://appleid.apple.com/) online and `Generate` an App-Specific Password under Security section.
   2. Enter your App-Specific Password in AltDeploy, verbatim.
7. Install:
   * [Xcode](https://apps.apple.com/us/app/xcode/id497799835): Window → Devices and Simulators → Select your device → Drop the `.ipa` onto Installed Apps.
   * [Configurator](https://support.apple.com/apple-configurator): Double-click your device → Apps → Drop the `.ipa` here.
8. On device: Go to `Settings` → `General` → `Profiles & Device Management`, tap on your certificate and then `Trust`.
9. _Done._ (If using a free developer account, repeat from step 4 after it **expires in 7 days**)

{% hint style="info" %}
Free Apple developer provisioning expires _every 7 days_, requiring reloading, but you will not lose any data.
{% endhint %}
{% endtab %}
{% endtabs %}

## 💢 Troubleshooting

<details>
<summary><strong>Cannot authenticate</strong></summary>

If using 2-Factor Authentication, you will need to go to [Apple ID](https://appleid.apple.com/) settings and generate an App-Specific Password. Enter it verbatim in your sideloading tool.

</details>

<details>
<summary><strong>Unable to code-sign / install</strong></summary>

* If you are using a free Apple developer account, you can only install a total of 3 apps per Apple ID at a time. Delete some apps you are signing, or install with a different Apple ID and Bundle IDs.
* If you used to have a free Safari Developer Account (no longer supported by Apple):
  1. Upgrade to a _paid_ [Apple Developer](https://developer.apple.com/programs/) account, or
  2. Use a different Apple ID that _is not_ an expired and deprecated Safari Developer account.

</details>

<details>
<summary><strong>—application-identifier entitlement does not match…</strong></summary>

This means you need to match the Bundle IDs with the ones from your previous sideload or build on your device. If you don't know it, or used a 3rd party web-sign (unsupported), we recommend you [backup your files](../../info/miscellaneous/restoring-files.md), delete the app and try to clean-install.

</details>

<details>
<summary><strong>Your maximum App ID limit has been reached…</strong></summary>

You have made too many Bundle IDs (App IDs) in one week on a free Apple developer account. Stop making new Bundle IDs and revert to one you already made. If all else fails, use a different Apple ID, and make only one new, unique Bundle ID with it (and save it for later when you need to re-sign in 7 days).

</details>

<details>
<summary><strong>Duplicate app</strong></summary>

If app installs or updates as a duplicate instead of updating existing installation, you need to delete it and use the _same_ Bundle ID as your original build or you'll end up with a double installation.

</details>

<details>
<summary><strong>App installs but crashes immediately on launch</strong></summary>

This is the most common issue with Sideloadly, LiveContainer, ATVLoadly, and Raspberry Pi-based signing tools. The app appears to install fine but quits to the home screen within 1–2 seconds of opening.

**Most likely cause: entitlement stripping**

When third-party tools re-sign the IPA, they sometimes strip or fail to re-inject entitlements that Provenance requires (Metal GPU access, game controller support, background audio, JIT, etc.). iOS and tvOS silently kill the app the moment it tries to use a capability it's not entitled to.

**What to try, in order:**

1. **Check the crash log first** — see the [Reading Crash Logs](#reading-crash-logs) section below. The crash reason tells you exactly what failed.

2. **Try a different signing tool** — if ATVLoadly or Sideloadly crashed it, try AltStore instead (or vice versa). Different tools handle entitlement injection differently.

3. **Use a paid Apple Developer account ($99/year)** — free accounts have restrictions on which entitlements can be granted. Some capabilities (like certain background modes) are blocked entirely on free accounts.

4. **Re-download the IPA** — a partially downloaded or corrupt IPA can produce a valid-looking install that crashes. Delete and re-download from [GitHub Releases](https://github.com/Provenance-Emu/Provenance/releases).

5. **Delete the app fully and reinstall** — stale data from a previous install with a different bundle ID can cause conflicts.

**Tool-specific notes:**

| Tool | Common cause | Workaround |
|------|-------------|------------|
| **Sideloadly** | May strip some entitlements by default | Enable "Advanced Options → Remove Support Files" = OFF; try "Normal" signing mode |
| **LiveContainer** | No JIT support; Metal access restricted in container sandbox | LiveContainer is not officially supported — use AltStore instead |
| **ATVLoadly / Raspberry Pi** | Community tool; entitlement handling is inconsistent | Update to latest ATVLoadly; check the [ATVLoadly GitHub](https://github.com/ipa-meister/atvloadly) for known issues |
| **AltStore (free)** | Free account entitlement limits | Works best; use the official [Provenance AltStore source](altstore://source?url=https://provenance-emu.com/apps.json) |

{% hint style="warning" %}
**LiveContainer** runs apps in a sandboxed container without installing them. Provenance uses Metal for rendering and requires real GPU access. LiveContainer's sandboxing actively interferes with this and is **not supported**. Install Provenance normally via AltStore instead.
{% endhint %}

</details>

---

## 📋 Reading Crash Logs

When Provenance crashes on launch, the device records exactly why. Finding that log tells you (and us) precisely what went wrong — this is far more useful than "it just crashes."

### macOS — Console.app (easiest)

1. Connect your iPhone/iPad or Apple TV via USB (or WiFi for Apple TV 4K)
2. Open **Console.app** (in `/Applications/Utilities/`)
3. Select your device in the left sidebar under **Devices**
4. In the search bar, type `Provenance` and press Enter
5. Launch Provenance on the device — watch the log fill in real time
6. Look for lines marked `fault` or `error`, especially around process termination

To save the log: **File → Export** or select all and copy.

{% hint style="info" %}
For crash reports specifically: in Console.app, go to **Crash Reports** in the left sidebar, find `Provenance` entries, and open them. They contain the full stack trace.
{% endhint %}

### macOS — Xcode

1. Connect your device
2. Open Xcode → **Window → Devices and Simulators**
3. Select your device → click **View Device Logs**
4. Filter by `Provenance` in the search box
5. The most recent crash will be at the top

You can also stream live logs: in Terminal, run:
```bash
xcrun devicectl device syslog stream --device-name "My iPhone" 2>&1 | grep -i provenance
```
(Replace `My iPhone` with your device name as shown in Finder.)

### Windows — Apple Devices App + libimobiledevice

There is no Windows equivalent of Console.app, but you can get logs via:

**Option A — iMazing** (paid, easiest on Windows)
- Install [iMazing](https://imazing.com/) and connect your device
- Go to **Manage Apps → Provenance → Logs**

**Option B — libimobiledevice** (free, command line)
1. Install [libimobiledevice for Windows](https://github.com/libimobiledevice-win32/imobiledevice-net/releases) or use the binaries at [libimobiledevice.org](https://libimobiledevice.org/)
2. Connect device, trust the computer when prompted
3. Run in Command Prompt:
   ```
   idevicesyslog.exe | findstr Provenance
   ```
4. Launch Provenance and watch the output

**Option C — 3uTools** (free GUI)
- Install [3uTools](http://www.3u.com/), connect device
- Go to **Toolbox → Real-time Log** and filter by `Provenance`

### Linux — libimobiledevice

```bash
# Install
sudo apt install libimobiledevice-utils   # Debian/Ubuntu
sudo pacman -S libimobiledevice           # Arch

# Stream logs
idevicesyslog | grep -i provenance
```

Connect your device via USB and trust the computer first (`idevicepair pair`).

### On-Device — Settings Analytics (no computer needed)

iOS saves crash reports locally:

1. **Settings → Privacy & Security → Analytics & Improvements**
2. Tap **Analytics Data**
3. Look for files starting with `Provenance-` — sort by date, the most recent crash is at the top
4. Tap to open — scroll to the `Exception Type` and `Termination Reason` lines near the top

The key fields to share when asking for help:
- `Exception Type` (e.g., `EXC_CRASH`, `EXC_BAD_ACCESS`)
- `Termination Reason` (e.g., `Namespace CODESIGNING, Code 0x1` = entitlement issue)
- `Application Specific Information`

### Apple TV — Reading Logs 🍎📺

Apple TV has no touchscreen and no USB port on the 4K models, so this is trickier.

**Method 1: Mac Console.app over WiFi (recommended)**

1. On Apple TV: **Settings → Remotes and Devices → Remote App and Devices** — make sure your Mac appears
2. On Mac: Open **Xcode → Window → Devices and Simulators**, wait for your Apple TV to appear (may take a moment on WiFi)
3. Once it appears in Xcode, it will also show up in **Console.app** under Devices
4. In Console.app, select the Apple TV and filter by `Provenance`
5. Launch Provenance on the Apple TV — the crash reason appears in real time

**Method 2: Xcode Device Logs over WiFi**

1. Xcode → **Window → Devices and Simulators** → select Apple TV
2. Click **View Device Logs**
3. Recent crashes appear here within a few seconds of happening

**Method 3: Apple TV 4 (USB-C only) — direct cable**

The original Apple TV 4 has a USB-C port. Connect it to your Mac and it shows up in Console.app and Xcode the same as an iPhone.

**Method 4: Pair via ideviceinstaller (ATVLoadly users)**

If you set up ATVLoadly, your Raspberry Pi is already paired. You can stream logs from the Pi:
```bash
idevicesyslog | grep -i provenance
```

{% hint style="warning" %}
Apple TV 4K (2nd gen+) has no physical port. You **must** use WiFi pairing via Xcode or Console.app. If Xcode hasn't paired with your Apple TV before, go to **Xcode → Preferences → Accounts** and add your Apple ID first.
{% endhint %}

---

## 🔗 External Resources

If you're still stuck, these guides cover sideloading in depth:

**Sideloading tools:**
- [AltStore Setup Guide (altstore.io)](https://altstore.io) — official, regularly updated
- [Sideloadly Guide (iosgods.com)](https://iosgods.com/topic/130167-how-to-use-sideloadly-to-sideload-ipa-files/) — step-by-step with screenshots
- [ATVLoadly GitHub](https://github.com/ipa-meister/atvloadly) — includes Raspberry Pi setup and known issues

**Crash log reading:**
- [How to Get Crash Logs from iPhone — iGeeksBlog](https://www.igeeksblog.com/how-to-get-crash-logs-from-iphone/) — Console.app walkthrough with screenshots
- [libimobiledevice project](https://libimobiledevice.org/) — cross-platform device tools (Windows/Linux log streaming)

**Community help:**
- [Provenance Discord](https://discord.gg/provenance) — `#sideloading-help` channel; include your crash log excerpt

{% hint style="info" %}
🗯 If you are still stuck ask for [help](https://discord.gg/provenance) on our Discord.
{% endhint %}
