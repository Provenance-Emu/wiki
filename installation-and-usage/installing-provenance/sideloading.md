---
description: Easy. Install pre-built releases (or pre-releases).
---

# Sideloading

Prebuilt .ipa releases can sideloaded onto your devices and must be re-signed using your own developer profile\(s\).

#### **Sideloading Options:**

* 🔨  [**Cydia Impactor** ](sideloading.md#cydia-impactor)· macOS/Windows
* 🖋  [**iOS App Signer**](sideloading.md#ios-app-signer) · macOS + Xcode or Configurator

{% hint style="success" %}
**Requirements**

* _Free_ [Apple Developer](https://9to5mac.com/2016/03/27/how-to-create-free-apple-developer-account-sideload-apps/) account \(at a minimum\) or a _paid_ account.  
  ****

  🛑 **DO NOT** enroll to join the full Developer Program or you will be locked into a _Pending_ payment state, unable to code-sign unless you pay or contact Apple to cancel the enrollment.  

* Connections:
  * iPhone / iPad:    `Lightning` → `USB-A / USB-C` cable¹
  * Apple TV 4:      `USB-C` → `USB-A / USB-C` cable¹
  * Apple TV 4K:     `WiFi`²  \([Instructions](http://www.redmondpie.com/how-to-wirelessly-connect-apple-tv-4k-to-xcode-on-mac/)\)

¹ Depends on which [ports](https://support.apple.com/en-us/HT201736) you have. WiFi can be setup after.  
² USB ports have been discontinued on Apple TV 4K+.
{% endhint %}

{% hint style="danger" %}
Sideloading from 3rd party sources _**is not supported**_.
{% endhint %}

💢  If you get stuck, check out [Troubleshooting](sideloading.md#troubleshooting).

## Cydia Impactor

1. Download a [Release](https://github.com/Provenance-Emu/Provenance/releases) or [Prerelease](https://builds.provenance-emu.com/) of Provenance. The _prerelease build server is not working but the latest prebuilt files can be found here for now…_
   1. _\*\*\*\*_[_**Provenance v1.5b 2773 - iOS**_ ](https://drive.google.com/a/sevand.co/file/d/1-H-uXjcA56Hgmi_GXcaxn6kLQmCi4q1k/view?usp=sharing) _\(.ipa\)_
   2. \_\_[_**Provenance v1.5b 2773 - tvOS**_](https://drive.google.com/a/sevand.co/file/d/1-ORX0wIcd6TgDVW_Ywo8WcnkOoLVzXD6/view?usp=sharing) _****\(.ipa\)_
2. Download and launch [Cydia Impactor](http://www.cydiaimpactor.com/).
3. Connect your device \(you may need to launch iTunes and choose `Trust…` when it pops up\).
4. Select your device in Impactor.
5. Drag & drop `.ipa` file onto Impactor.
6. Enter your Apple ID.
7. If _not_ using 2-Factor Authentication, enter your account password, otherwise…

   1. _\(If you haven't yet\),_ login to your [Apple ID](https://appleid.apple.com/) online and `Generate` an App-Specific Password, under Security section \(and write it down somewhere for later use\).
   2. Enter your App-Specific Password in Cydia Impactor, verbatim.

  
   ⚠️ If it fails to verify code signature, try resigning the .ipa with…

   * Web: [appsigner.io](https://appsigner.io/) \(free devs only\)
   * macOS \(only\): [iOS App Signer](https://dantheman827.github.io/ios-app-signer/)  —return to step 5.  🆔 Bundle ID: `com.[change-this].provenance`  Replace `[change-this]` with something unique like your username. 

   🚸 If Impactor still fails, try [Option 2](sideloading.md#ios-app-signer) \(macOS only\).  

8. On device: Go to `Settings` → `General` → `Profiles & Device Management`, tap on your certificate and then `Trust`
9. _Done._  \(If using a free developer account, repeat from step 3 after it _**expires in 7 days**_\)

{% hint style="info" %}
Free Apple developer provisioning expires _every 7 days_, requiring reloading, but you will not lose any data.

_Paid_ Apple Developer provisioning may only require re-signing once a year.
{% endhint %}

## iOS App Signer

1. Download a [Release](https://github.com/Provenance-Emu/Provenance/releases) or [Prerelease](https://builds.provenance-emu.com/) of Provenance. The _prerelease build server is not working but the latest prebuilt files can be found here for now…_
   1. _\*\*\*\*_[_**Provenance v1.5b 2773 - iOS**_ ](https://drive.google.com/a/sevand.co/file/d/1-H-uXjcA56Hgmi_GXcaxn6kLQmCi4q1k/view?usp=sharing) _\(.ipa\)_
   2. \_\_[_**Provenance v1.5b 2773 - tvOS**_](https://drive.google.com/a/sevand.co/file/d/1-ORX0wIcd6TgDVW_Ywo8WcnkOoLVzXD6/view?usp=sharing) _****\(.ipa\)_
2. Download and launch [iOS App Signer](https://dantheman827.github.io/ios-app-signer/).
3. Select `.ipa` file and resign it to yourself, selecting the Provenance Bundle ID you've used in the past if you already have one. If you don't have one, try creating one here if it lets you or proceed to step 4 and return to this.    🆔 Bundle ID: `com.[change-this].provenance`  Replace `[change-this]` with something unique like your username. 
4. Connect your device. ⚠️If you haven't yet, register your device to your Apple ID in Xcode. Easiest way to do this is to make dummy app in Xcode and have it automatically create the provisioning when you enter your Bundle ID  \([Example](https://dantheman827.github.io/ios-app-signer/#tab-bar)\).
5. Install:
   * [Xcode](https://itunes.apple.com/us/app/xcode/id497799835): Window → Devices and Simulators: Select your device. Drop the new `.ipa` file onto Installed Apps.
   * [Configurator](https://support.apple.com/apple-configurator): Double-click your device → Apps: Drop the new `.ipa` file here.
6. On device: Go to `Settings` → `General` → `Profiles & Device Management`, tap on your certificate and then `Trust`
7. _Done._ \(If using a free developer account, repeat from step 4 after it _**expires in 7 days**_\)

{% hint style="info" %}
Free Apple developer provisioning expires _every 7 days_, requiring reloading, but you will not lose any data.
{% endhint %}

## 💢 Troubleshooting

#### Cannot authenticate

* If using 2-Factor Authentication, you will need to go to [Apple ID](https://appleid.apple.com/) settings and make a key and save it for use in Cydia Impactor, type it verbatim.

#### Unable to code-sign / install…

* If you are using a free Apple developer account, you can only install a total of 3 apps per Apple ID at a time. You must use delete some apps you are signing, or install with different Apple ID and Bundle IDs.
* If you used to have a free Safari Developer Account which is no longer supported by Apple, you have two options: 

  1\) Upgrade to a _paid_ [Apple Developer](https://developer.apple.com/programs/) account. 

  2\) Use a different Apple ID that _is not_ an expired and deprecated Safari Developer account.

#### **—application-identifier entitlement does not match…**

* This means you need to match the Bundle IDs with the ones from your previous sideload or build on your device. If you don't know it, or used a 3rd party web-sign \(unsupported\), we recommend you [backup your files](../../info/miscellaneous/restoring-files.md), delete the app and try to clean-install.

#### **Your maximum App ID limit has been reached…**

* You have made too many Bundle IDs \(App IDs\) in one week on a free Apple developer account. Stop making new Bundle IDs and revert to one you already made. You are chasing the wrong problem. If all else fails, use a different Apple ID, and make only one new, unique Bundle ID with it \(and save it for later when you need to re-sign in 7 days\).

#### Duplicate app

* If app installs or updates as a duplicate app instead of updating existing installation, you need to delete it and use the _same_ Bundle ID as your original build or you'll end up with a double installation…



{% hint style="info" %}
🗯 If you are still stuck ask for [help](https://discord.gg/NhzgrXh) on our Discord.
{% endhint %}

