---
description: '"What if I don''t have a Mac?"'
---

# Virtualizing macOS

Technically, a Mac is not required to install Provenance. Only macOS is, which you can run on a custom built Hackintosh \(check out [tonymacx86](https://www.tonymacx86.com/)\) or run as a virtual machine on another system like Windows.

**Virtualization Options**

* \*\*\*\*[**Windows**](virtualizing-macos.md#windows) · macOS on Windows

### Windows

{% hint style="success" %}
**Requirements**

* Intel processor with support for hardware virtualization 
* VMWare \(Virtual Workstation\)
* Virtual copy of macOS
  * Includes 5 files: **.nvram, .vmdk, .vmsd, .vmx, .vmxf** _\(keep all files in same folder\)_
  * macOS High Sierra · _\(any copy of macOS will do, but needs updating after install\)_
{% endhint %}

#### Setup

1. Install and Open VMWare.
2. Setup a new virtual machine…
   * Select File → New Virtual Machine for install wizard _or…_
   * Select `.vmx` file of your Virtual Disk files manually through File → Open
3. Before powering, sertup `Power and Edit` option:  
   1. Set memory for at least 2GB, 4GB is adequate. Hard Disk should be at least 150 GB
   2. Select USB Controller and set USB Compatibility to 2.0 \(required or it will not detect your iPhone, even if you have USB 3.0\) and enable these options:
      1. ☑️ Automatically connect new USB devices 
      2. ☑️ Show all USB input devices
      3. ☑️ Share Bluetooth devices with the virtual machine. 

#### Launch

1. Start macOS via `Power on this Virtual Machine` \(Virtual Machines will run slower than actual computers, so

   expect some loading time\). 

   * If there is an issue with the display resolution, go to `System Preferences`…
     * `⚙️System Preferences` in Dock _or…_  
     * `` Menu → `System Preferences`
   * Select Display, then `Default for Display` \(Adjustments can also be made in the `View` menu of VMWare `Autosize`\)

2. Update: Open App Store and select `Updates`. Update macOS and iTunes \(this may take a while\). 
3. Install Xcode: After updating, download Xcode via App Store \(free\).
4. Locate Terminal in `Applications/Utilities/Terminal` \(remember this location or drag the app to the Dock for later\).

#### Installing Provenance

Continue to [Installing Provenance](../../installation-and-usage/installing-provenance/)…

## 💢 Troubleshooting

If you are having trouble getting things to work on a virtual machine, check for your issue here.

#### Device not detected over USB or keeps connecting/disconnecting…

* Before you plug in your device, make sure that VMWare is in focus and macOS active \(mouse clicked within macOS screen\)—or it won't get picked up by the VM and will be fighting for it with the host system.

#### Cannot detect Apple TV 4K over wifi…

* Try changing he network adapter from "NAT" to custom and choose example "VMnet0" so i connects directly to your local network for broadcasting \(solution discussed in [KODI forum](https://forum.kodi.tv/archive/index.php?thread-325982.html)\).

