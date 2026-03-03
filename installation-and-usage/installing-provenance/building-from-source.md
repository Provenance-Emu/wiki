---
description: 'Moderate: Install latest in-development build.'
---

# Building from Source

To get the very latest in-development build, you will need to build from source with Xcode. There are no shortcuts. Provenance is a large project with required dependencies and submodules that help enable efficient development. Check that you meet the requirements. Follow each and every step. Make no assumptions. **Do not** skip _anything._

1. [**Get Source**](building-from-source.md#get-source)
2. [**Setup**](building-from-source.md#setup) \(install requirements and dependencies\)
3. [**Build Source**](building-from-source.md#build-source) to device \(Xcode\)
4. _\(Optional\)_ [**Enable Advanced Features**](building-from-source.md#advanced-features)

{% hint style="warning" %}
The beta is in active-development.
{% endhint %}

{% hint style="danger" %}
DO NOT expect to use a beta without issues, losing your saves, or bugs.
{% endhint %}

{% hint style="success" %}
**Requirements**

* macOS 13.5+ (Ventura) minimum; macOS 14.0+ (Sonoma) recommended
  * on a Mac, Hackintosh or virtual machine \([Virtualizing macOS](https://wiki.provenance-emu.com/info/miscellaneous/virtualizing-macos)\)
* [Xcode](https://apps.apple.com/us/app/xcode/id497799835) 15.0+
* iOS 16+ / tvOS 16+ SDKs
* _Free_ [Apple Developer](https://9to5mac.com/2016/03/27/how-to-create-free-apple-developer-account-sideload-apps/) account \(at a minimum\) or a _paid_ account.

🛑 **DO NOT** enroll to join the full Developer Program or you will be locked into a _Pending_ payment state, unable to code-sign unless you pay or contact Apple to cancel the enrollment.

* Connections:
  * iPhone / iPad:    `Lightning` → `USB-A / USB-C` cable¹
  * Apple TV 4:      `USB-C` → `USB-A / USB-C` cable¹
  * Apple TV 4K:     `WiFi`²  \([Instructions](http://www.redmondpie.com/how-to-wirelessly-connect-apple-tv-4k-to-xcode-on-mac/)\)³

¹ Depends on which [ports](https://support.apple.com/en-us/HT201736) you have. _WiFi can be setup after._
² USB ports have been discontinued on Apple TV 4K+.
³ If using a virtual machine, you may need to [configure your network settings](../../info/miscellaneous/virtualizing-macos.md#cannot-detect-apple-tv-4k-over-wifi).
{% endhint %}

💢 If you get stuck, check out [Troubleshooting](building-from-source.md#troubleshooting).

## Get Source

**Source Options**

* 🔃  [**Clone**](building-from-source.md#clone) using…
  * ![](https://user-images.githubusercontent.com/3118097/37563629-48ec3f26-2a42-11e8-9fd8-784e9e830ebe.png) [Terminal](building-from-source.md#terminal)
  * ![](https://user-images.githubusercontent.com/3118097/37563630-4903ebbc-2a42-11e8-888a-09a94fc0058d.png) [Tower](building-from-source.md#tower)

### Clone

Cloning is how you pull the source code from GitHub. Choose your preferred method:

{% tabs %}
{% tab title="Terminal" %}
{% hint style="info" %}
The Terminal app can be found in: _/Applications/Utilities_
{% endhint %}

1. Make sure you have the latest version of the Xcode command-line tools installed: `xcode-select --install`
2. _(Optional)_ Choose an install directory with `cd [path]` (drag & drop a folder on Terminal after `cd` to get directory path).
3. Download source with HTTPS:
   ```
   git clone --recurse-submodules -j4 https://github.com/Provenance-Emu/Provenance.git
   ```
4. Continue to [Setup](building-from-source.md#setup)…
{% endtab %}

{% tab title="Tower (Git Client)" %}
Tower is a powerful commercial git client that can automate a lot of the tasks you'd otherwise be using commandline for, such as stashing changes. It is however, _not free._

1. Purchase/Download [Tower](https://www.git-tower.com/mac/)
2. Launch Tower and Add Your Service Account: `GitHub`
3. _(Optional)_ In Menubar: Select `Tower` → `Preferences` (or use `⌘,` shortcut):
   * Set a 'default directory for clone repositories' such as `~Documents/GitHub`
4. In Menubar: Select `File` → `Clone Git Repository` (or use `⌃⌘C` shortcut):
   * Remote URL: `https://github.com/Provenance-Emu/Provenance.git`
   * ☑️ Initialize Submodules
5. Continue to [Setup](building-from-source.md#setup)…
{% endtab %}
{% endtabs %}

~~**Download**~~

🚫 Due to the inclusion of submodules this method no longer works. **Do not** manually download source as `.zip`…

{% hint style="danger" %}
If building from active develop branch, we _will not_ be held responsible for any loss of your game data! Install _**at your own risk!**_ …and back up your files.
{% endhint %}

## Build Source

1. Open the Provenance Xcode workspace: ![](https://user-images.githubusercontent.com/3118097/37574056-3e07abe2-2adb-11e8-948c-acb4d539e658.png) `Provenance.xcworkspace`

   ⚠️ **Do not** use the .xcodeproj file or you will have build errors!

   ![](https://user-images.githubusercontent.com/3118097/37563995-73fdd65e-2a4a-11e8-949f-5aa8351dcbb2.png)

2. Go to Preferences via Menubar: `Xcode` → `Preferences` or use `⌘,` shortcut.
   * Select Accounts tab.
   * Click `+`
   * Sign in with your personal or developer Apple ID. If you don't have one, click `Create Apple ID` or go to [appleid.apple.com](https://appleid.apple.com/).

{% hint style="warning" %}
At minimum, sign up as a free [Apple Developer](https://9to5mac.com/2016/03/27/how-to-create-free-apple-developer-account-sideload-apps/) and do no more than agree to the terms.

🛑 DO NOT enroll to join the full Developer Program or you will be locked into a _Pending_ payment state, unable to code-sign unless you pay or contact Apple to cancel the enrollment.
{% endhint %}

Copy `CodeSigning.xcconfig.sample` to `CodeSigning.xcconfig` and modify the file replacing `DEVELOPMENT_TEAM` with your Team ID and `ORG_IDENTIFIER` with a bundle identifier that is registered to you.

If you have a paid Apple Developer account, you can find your Team ID at https://developer.apple.com/account/#/membership

If you have a free Apple Developer account, you need to generate a new signing certificate. To do so, follow the steps in [iOS App Signer][3] to create a new Xcode project and generate a provisioning profile. After saving the project, open `project.pbxproj` inside your newly created `.xcproj` and look for `DEVELOPMENT_TEAM`. Copy this value to `CodeSigning.xcconfig` and your unique identifier to `ORG_IDENTIFIER`.

Set `DEVELOPER_ACCOUNT_PAID = YES` if you used a paid Apple Developer account in order to automatically request the increased memory limit entitlement from Apple.

After updating `CodeSigning.xcconfig`, re-open the project (remember to use `Provenance.xcworkspace` when opening the project).

{% hint style="info" %}
 You can install a duplicate app for testing by using a different bundle ID than your previous/main install.
{% endhint %}

* If using a free Apple Developer account, **Turn OFF** these Capabilities for _all_ targets:
  * ![](https://user-images.githubusercontent.com/3118097/48986708-22f14800-f0cd-11e8-98ec-6f093375d969.png)  App Groups
  * ![](https://user-images.githubusercontent.com/3118097/48986708-22f14800-f0cd-11e8-98ec-6f093375d969.png)  iCloud
  * ![](https://user-images.githubusercontent.com/3118097/48986708-22f14800-f0cd-11e8-98ec-6f093375d969.png)  Multipath
  * ![](https://user-images.githubusercontent.com/3118097/48986708-22f14800-f0cd-11e8-98ec-6f093375d969.png)  Push Notifications
  * ![](https://user-images.githubusercontent.com/3118097/48986708-22f14800-f0cd-11e8-98ec-6f093375d969.png)  Siri

* Select a `-Release` profile from the Scheme Menu and connect your device\(s\) and select in the Destination Menu:

  ![](https://user-images.githubusercontent.com/3118097/41824506-165731fc-77c6-11e8-965d-ac56b65e560c.png)

  ![](https://user-images.githubusercontent.com/3118097/41824642-6fc72e52-77c8-11e8-88ad-7d4a464974ef.png)

* If you are…
  * Paid Apple Developer: Continue to [Enable Advanced Features…](building-from-source.md#advanced-features)
  * Free Apple Developer: Hit the `▶︎` \(Run\) button.
* Provenance will compile and run on your device. Unless testing, hit `◼︎` \(Stop\). _Done._

{% hint style="success" %}
**Build successful!** Provenance is now installed on your device. Free Apple developer provisioning expires every 7 days, but your data is preserved when re-signing.
{% endhint %}

💢 If you get stuck, check out [Troubleshooting](building-from-source.md#troubleshooting).

{% hint style="info" %}
Free Apple developer provisioning expires _every 7 days_, requiring reloading, but you will not lose any data.

_Paid_ Apple Developer provisioning may only require re-signing once a year.
{% endhint %}

## Advanced Features

{% hint style="warning" %}
**Requires** a _paid_ [Apple Developer](https://developer.apple.com/programs/) account.
{% endhint %}

1. If you haven't made one previously, add a new App Group ID: `group.[change-this].provenance` to your [Apple Developer](https://developer.apple.com/programs/) portal, or continue to next step and see if it allows you to add an App Group ID automatically when using `+` in App Groups.
2. \[Re-\]enable Capabilities on your target\(s\), with the following settings:

   * **iOS:**
     * Provenance:
       * ![](https://user-images.githubusercontent.com/3118097/48986709-2389de80-f0cd-11e8-8d98-119792b0bc4f.png)  App Groups
         * 🔲 `group.provenance-emu.provenance`
         * ☑️ `group.[change-this].provenance`
       * ![](https://user-images.githubusercontent.com/3118097/48986709-2389de80-f0cd-11e8-8d98-119792b0bc4f.png)  iCloud
       * ![](https://user-images.githubusercontent.com/3118097/48986709-2389de80-f0cd-11e8-8d98-119792b0bc4f.png)  Multipath
       * ![](https://user-images.githubusercontent.com/3118097/48986709-2389de80-f0cd-11e8-8d98-119792b0bc4f.png)  Push Notifications
       * ![](https://user-images.githubusercontent.com/3118097/48986709-2389de80-f0cd-11e8-8d98-119792b0bc4f.png)  Siri
     * Spotlight:
       * ![](https://user-images.githubusercontent.com/3118097/48986709-2389de80-f0cd-11e8-8d98-119792b0bc4f.png)  App Groups
       * ![](https://user-images.githubusercontent.com/3118097/48986709-2389de80-f0cd-11e8-8d98-119792b0bc4f.png) iCloud
         * 🔘Specify custom containers:
           *  🔲 \`iCloud.com.provenance-emu.provenance\`

              ☑️ \`iCloud.com.\[change-this\].provenance\`
   * **tvOS:**
     * ProvenanceTV:
       * ![](https://user-images.githubusercontent.com/3118097/48986709-2389de80-f0cd-11e8-8d98-119792b0bc4f.png)  App Groups
         * 🔲 `group.provenance-emu.provenance`
         * ☑️ `group.[change-this].provenance`
       * ![](https://user-images.githubusercontent.com/3118097/48986709-2389de80-f0cd-11e8-8d98-119792b0bc4f.png)  iCloud
       * ![](https://user-images.githubusercontent.com/3118097/48986709-2389de80-f0cd-11e8-8d98-119792b0bc4f.png)  Push Notifications
     * TopShelf:
       * ![](https://user-images.githubusercontent.com/3118097/48986709-2389de80-f0cd-11e8-8d98-119792b0bc4f.png) App Groups
         * 🔲 `group.provenance-emu.provenance`
         * ☑️ `group.[change-this].provenance`

   ![](../../.gitbook/assets/40277312-d8cb585a-5bd1-11e8-8292-29482e3b8fe6.gif)

3. Define the value for `PVAppGroupId` in `PVAppConstants.swift` with your App Group ID.

   ![](../../.gitbook/assets/37565204-feb06084-2a61-11e8-980e-39f10f0d3a05.png)

4. Hit the `▶︎` \(Run\) button to build to your device.
5. Provenance will compile and run on your device. Unless testing, hit `◼︎` \(Stop\). Done

{% hint style="warning" %}
If all else fails, delete Provenance folder and start over.
{% endhint %}

## Troubleshooting

If you are having trouble building or sideloading the app, check for your issue here or below in Known Issues.

<details>
<summary><strong>xcrun: error: unable to find utility "xcodebuild"</strong></summary>

Go to Xcode Preferences → Locations, and make sure to select an Xcode version for Command Line Tools.

</details>

<details>
<summary><strong>Unable to code-sign / install</strong></summary>

* Change the Bundle IDs of the app targets and extensions, as described in Build Source steps.
* If you are using a free Apple developer account, you can only install a total of 3 apps per Apple ID at a time. You must delete some apps you are signing, or install with different Apple ID and Bundle IDs.
* If you used to have a free Safari Developer Account which is no longer supported by Apple:
  1. Upgrade to a _paid_ [Apple Developer](https://developer.apple.com/programs/) account, or
  2. Use a different Apple ID that _is not_ an expired and deprecated Safari Developer account.

</details>

<details>
<summary><strong>Can't install after changing fork / pulling</strong></summary>

1. Check the Bundle IDs haven't been reset to the project defaults.
2. If not, select your team dropdown and reselect your team/name. Sometimes Xcode gets out of sync with the identity being used after a merge/pull/branch change, especially in the extension targets.

</details>

<details>
<summary><strong>Cycle in dependencies between targets… error</strong></summary>

Circular dependency error. Clean Build Folder (⇧⌘K) and/or nuke Xcode's derived data: `rm -rf ~/Library/Developer/Xcode/DerivedData` and restart Xcode.

</details>

<details>
<summary><strong>Stuttering sound or lag</strong></summary>

This probably means you built the _debug version_ by mistake (app will be named `Prov Debug` on Home Screen and Settings will show `DEBUG`). Re-build using `Provenance-Release` (iOS) or `ProvenanceTV-Release` (tvOS) option in Xcode.

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
<summary><strong>Mupen build error / missing submodules</strong></summary>

You are missing submodules. **Do not** download .zip from GitHub. Use Terminal. Go back to [Get Source](building-from-source.md#get-source) and **do not** skip any steps.

</details>

<details>
<summary><strong>Unsupported arch</strong></summary>

You are probably trying to build for a 32-bit device. Provenance only supports 64-bit devices. As a **workaround**: Remove the mupen64plus framework from the app's `Embed` and `Link` stages and from the `Build → Targets` list in the `Edit Scheme…` settings.

</details>

<details>
<summary><strong>Duplicate app</strong></summary>

If app installs or updates as a duplicate app instead of updating existing installation, you need to delete it and use the _same_ Bundle ID as your original build or you'll end up with a double installation.

</details>

<details>
<summary><strong>Linking… Failed</strong></summary>

Fails when switching from one target to another. In Xcode: Run `Clean` and/or `Clean Build Folder` and rebuild.

</details>

<details>
<summary><strong>git@github.com: Permission denied (publickey)</strong></summary>

Setup an [SSH Key on your GitHub account](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/), or add the following to your git config via `nano ~/.gitconfig`:

```bash
[url "https://github.com"]
insteadOf = ssh://git@github.com
```

</details>

<details>
<summary><strong>conflicting provisioning settings…Distribution</strong></summary>

In Build Settings for the targets with errors, manually reset all the Code Signing Identities that are `iOS Distribution` to be `iOS Developer`, and try building again.

</details>

## ⚠️ Known Issues

**something about database build error**

* This means there have been changes to the database model which is no longer compatible with your previous build. In order to update you _**must**_ clean install \(delete app and re-install, not build or install over over existing app\). If you would like to migrate your save games and states, you can refer to [Restoring Files](https://github.com/Provenance-Emu/Provenance/wiki/Restoring-Files).

🏍 You can install a duplicate app for testing by using a different bundle ID than your previous/main install.

{% hint style="info" %}
🗯 If you are still stuck try [debugging](../../help/troubleshooting.md) on your own or ask for [help](https://discord.gg/provenance) on our Discord.
{% endhint %}
