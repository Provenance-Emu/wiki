---
description: Easy. Install pre-built releases (or pre-releases).
---

# Side-loading

Prebuilt .ipa releases can side-loaded onto your devices and must be re-signed using your own developer profile\(s\).

#### **Side-loading Options:**

* 🔨  [**Cydia Impactor** ](side-loading.md#cydia-impactor)· macOS/Windows
* 🖋  [**iOS App Signer**](side-loading.md#ios-app-signer) · macOS + Xcode a/o Configurator

{% hint style="success" %}
**Requirements**

* _Free_ [Apple Developer](https://9to5mac.com/2016/03/27/how-to-create-free-apple-developer-account-sideload-apps/) account \(at a minimum\)   
  ****

  🛑 **DO NOT** enroll to join the Developer Program or you will be locked into a _Pending_ payment state, unable to code-sign unless you pay or contact Apple to cancel the enrollment.  

* Connections:
  * iPhone / iPad:    `Lightning` → `USB-A / USB-C` cable¹
  * Apple TV 4:      `USB-C` → `USB-A / USB-C` cable¹
  * Apple TV 4K:     `WiFi`²  \([Instructions](http://www.redmondpie.com/how-to-wirelessly-connect-apple-tv-4k-to-xcode-on-mac/)\)

¹ Depends on which [ports](https://support.apple.com/en-us/HT201736) you have. WiFi can be setup after.  
² USB ports have been discontinued on Apple TV 4K+.
{% endhint %}

{% hint style="danger" %}
Side-loading from 3rd party sources _**is not supported**_.
{% endhint %}

💢  If you get stuck, check out Troubleshooting.



### Cydia Impactor

1. Download a [Release](https://github.com/Provenance-Emu/Provenance/releases) or [Prerelease](https://builds.provenance-emu.com/) of Provenance.
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

   🚸 If Impactor still fails, try [Option 2](side-loading.md#ios-app-signer) \(macOS only\).  

8. On device: Go to `Settings` → `General` → `Profiles & Device Management`, tap on your certificate and then `Trust`
9. _Done._  \(If using a free developer account, repeat from step 3 after it _**expires in 7 days**_\)

{% hint style="info" %}
Free Apple developer provisioning expires _every 7 days_, requiring reloading, but you will not lose any data.
{% endhint %}

### iOS App Signer

1. Download a [Release](https://github.com/Provenance-Emu/Provenance/releases) or [Prerelease](https://builds.provenance-emu.com/) of Provenance.
2. Download and launch [iOS App Signer](https://dantheman827.github.io/ios-app-signer/).
3. Select `.ipa` file and resign it to yourself, selecting the Provenance Bundle ID you've used in the past if you have one already have one. If you don't have one, try creating one here if it lets you or proceed to step 4 and return to this.    🆔 Bundle ID: `com.[change-this].provenance`  Replace `[change-this]` with something unique like your username. 
4. Connect your device. ⚠️If you haven't yet, register your device to your Apple ID in Xcode. Easiest way to do this is to make dummy app in Xcode and have it automatically create the provisioning when you enter your Bundle ID  \([Example](https://dantheman827.github.io/ios-app-signer/#tab-bar)\).
5. Install:
   * [Xcode](https://itunes.apple.com/us/app/xcode/id497799835): Window → Devices and Simulators: Select your device. Drop the new `.ipa` file onto Installed Apps.
   * [Configurator](https://support.apple.com/apple-configurator): Double-click your device → Apps: Drop the new `.ipa` file here.
6. _Done._ \(If using a free developer account, repeat from step 4 after it _**expires in 7 days**_\)

{% hint style="info" %}
Free Apple developer provisioning expires _every 7 days_, requiring reloading, but you will not lose any data.
{% endhint %}

  


