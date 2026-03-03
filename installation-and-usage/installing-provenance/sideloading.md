---
description: Easy. Install pre-built releases (or pre-releases).
---

# Sideloading

Prebuilt .ipa releases can sideloaded onto your devices and must be re-signed using your own developer profile\(s\).

## **Download Provenance**

1. First, download a [Release](https://github.com/Provenance-Emu/Provenance/releases) or Prerelease of Provenance (unless using AltStore, direct source download link in AltStore insructions).
2. Choose a sideloading method:

### **Sideloading Options:**

* ❇️  [**AltStore**](sideloading.md#altstore) · macOS/Window)
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
3. Select your device in Impactor.
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

{% hint style="info" %}
🗯 If you are still stuck ask for [help](https://discord.gg/provenance) on our Discord.
{% endhint %}
