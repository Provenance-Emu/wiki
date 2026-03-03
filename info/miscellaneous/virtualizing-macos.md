---
description: Run macOS in a virtual machine to build Provenance from source without a Mac
---

# Virtualizing macOS

If you don't have a Mac but want to build Provenance from source, you can run macOS in a virtual machine. This guide covers setting up a macOS VM on Windows or Linux.

{% hint style="info" %}
**Most users don't need this.** Install Provenance from the [App Store](../../installation-and-usage/installing-provenance/app-store.md) or [sideload a pre-built .ipa](../../installation-and-usage/installing-provenance/sideloading.md) instead. A macOS VM is only needed for building from source.
{% endhint %}

---

## Virtualization Options

{% tabs %}
{% tab title="VMware (Windows)" %}
**Best for:** Windows users with Intel processors

### Requirements

- **CPU:** Intel processor with VT-x/VT-d support (AMD works but requires extra patches)
- **RAM:** 8 GB minimum (16 GB recommended)
- **Storage:** 80+ GB free disk space
- **Software:** [VMware Workstation Player](https://www.vmware.com/products/workstation-player.html) (free for personal use) or Workstation Pro

### Setup

1. **Install VMware Workstation** and the [VMware Unlocker](https://github.com/DrDonk/unlocker) (enables macOS as a guest OS option)
2. **Create a new VM:**
   - Select **Apple Mac OS X** as the guest OS
   - Allocate at least **4 GB RAM** (8 GB recommended for Xcode)
   - Set disk size to at least **80 GB** (Xcode alone is ~35 GB)
3. **Configure hardware:**
   - **Processors:** 2+ cores
   - **USB Controller:** Set to USB 2.0 (required for iOS device detection — USB 3.0 passthrough is unreliable in VMs)
   - Enable:
     - Automatically connect new USB devices
     - Show all USB input devices
     - Share Bluetooth devices with the virtual machine
4. **Install macOS** from your installation media
5. **Install VMware Tools** after macOS boots (improves graphics, clipboard sharing, and performance)

### Post-Install

1. **Update macOS** — Open System Settings → General → Software Update
2. **Install Xcode** — Download from the App Store (free, ~35 GB)
3. **Open Terminal** — Applications → Utilities → Terminal

Continue to [Building from Source](../../installation-and-usage/installing-provenance/building-from-source.md).
{% endtab %}

{% tab title="VirtualBox (Windows/Linux)" %}
**Best for:** Free, cross-platform option

### Requirements

- **CPU:** Intel or AMD with virtualization support
- **RAM:** 8 GB minimum
- **Storage:** 80+ GB free
- **Software:** [VirtualBox](https://www.virtualbox.org/) (free and open source)

### Setup

1. **Install VirtualBox** and the Extension Pack
2. **Create a new VM:**
   - Type: **Mac OS X**, Version: **macOS 64-bit**
   - RAM: **4096 MB** minimum (8192 MB recommended)
   - Create a virtual hard disk: **80 GB** or more (VDI, dynamically allocated)
3. **Configure VM settings:**
   - **System → Processor:** 2+ CPUs
   - **Display → Video Memory:** 128 MB
   - **USB:** Enable USB 2.0 (EHCI) Controller
4. **Apply required patches** — VirtualBox needs command-line tweaks to run macOS:
   ```bash
   VBoxManage modifyvm "YourVMName" --cpuidset 00000001 000106e5 00100800 0098e3fd bfebfbff
   VBoxManage setextradata "YourVMName" VBoxInternal/Devices/efi/0/Config/DmiSystemProduct "iMac19,1"
   VBoxManage setextradata "YourVMName" VBoxInternal/Devices/efi/0/Config/DmiBoardProduct "Mac-AA95B1DDAB278B95"
   VBoxManage setextradata "YourVMName" VBoxInternal/Devices/smc/0/Config/DeviceKey "ourhardworkbythesewordsguardedpleasedontsteal(c)AppleComputerInc"
   VBoxManage setextradata "YourVMName" VBoxInternal/Devices/smc/0/Config/GetKeyFromRealSMC 1
   ```
5. **Install macOS** and then install Xcode

{% hint style="warning" %}
VirtualBox macOS performance is generally worse than VMware. Expect longer build times.
{% endhint %}
{% endtab %}

{% tab title="UTM (macOS Host)" %}
**Best for:** Running a second macOS version on an existing Mac (Apple Silicon or Intel)

If you have a Mac but need a different macOS version for Xcode compatibility:

1. Download [UTM](https://mac.getutm.app/) (free from GitHub, or paid on App Store)
2. Download a macOS IPSW from [Apple](https://developer.apple.com/macos/) or use the built-in installer
3. Create a new VM → **Virtualize** → **macOS**
4. Allocate RAM and storage, then install

{% hint style="info" %}
On Apple Silicon Macs, UTM uses Apple's native Virtualization.framework for near-native performance.
{% endhint %}
{% endtab %}
{% endtabs %}

---

## Performance Tips

Virtual machines are slower than native hardware. These tips help:

- **Allocate adequate RAM** — 8 GB for the VM if your host has 16+ GB
- **Use an SSD** — VM disk I/O on a spinning hard drive is painfully slow
- **Close unnecessary host apps** — Free up CPU and RAM for the VM
- **Use Release builds** — When building Provenance in Xcode, always use the Release scheme (Debug builds are 5-10x slower and even more so in a VM)
- **Disable Spotlight indexing** inside the VM — System Settings → Siri & Spotlight → uncheck categories

---

## Troubleshooting

<details>
<summary><strong>iOS device not detected over USB</strong></summary>

- Make sure VMware/VirtualBox is **in focus** (click inside the macOS window) before plugging in your device — otherwise the host OS grabs the USB connection
- Set USB Controller to **USB 2.0** (not 3.0) in VM settings
- On the device, tap **Trust** when the "Trust This Computer?" dialog appears
- In VMware: VM menu → Removable Devices → verify your device is connected to the VM

</details>

<details>
<summary><strong>Cannot detect Apple TV 4K over WiFi</strong></summary>

Apple TV 4K uses WiFi for Xcode pairing (no USB port). VMs default to NAT networking, which blocks local network discovery.

**Fix:** Change the VM's network adapter from **NAT** to **Bridged** (or **Custom → VMnet0**) so the VM connects directly to your local network. This enables Bonjour/mDNS discovery needed for Apple TV pairing.

</details>

<details>
<summary><strong>macOS won't boot or shows a black screen</strong></summary>

- Verify your CPU supports hardware virtualization (Intel VT-x / AMD-V) — enable it in BIOS settings
- For VMware: Ensure the [Unlocker](https://github.com/DrDonk/unlocker) is properly installed
- For VirtualBox: Verify all command-line patches were applied correctly
- Try a different macOS version — some versions work better with certain VM software

</details>

<details>
<summary><strong>Display resolution is wrong or too small</strong></summary>

- **VMware:** Install VMware Tools, then use View → Autosize → Autofit Guest
- **VirtualBox:** Install Guest Additions (limited macOS support), or set resolution manually:
  ```bash
  VBoxManage setextradata "YourVMName" VBoxInternal2/EfiGraphicsResolution 1920x1080
  ```
- **In macOS:** System Settings → Displays → choose "Default for Display" or select a specific resolution

</details>

<details>
<summary><strong>Xcode build is extremely slow</strong></summary>

- Allocate more CPU cores and RAM to the VM
- Use an SSD for VM storage
- Build the **Release** scheme (not Debug)
- Close Xcode's Simulator — it's not needed when deploying to a physical device
- Consider using a pre-built .ipa via [sideloading](../../installation-and-usage/installing-provenance/sideloading.md) instead

</details>

---

## Alternative: Hackintosh

Instead of a VM, you can install macOS directly on compatible PC hardware (a "Hackintosh"). This gives near-native performance but requires compatible hardware and more setup effort.

**Resources:**
- [OpenCore Install Guide](https://dortania.github.io/OpenCore-Install-Guide/) — Modern Hackintosh bootloader
- [tonymacx86](https://www.tonymacx86.com/) — Hardware compatibility lists and guides

{% hint style="warning" %}
Hackintosh setups are not officially supported by Apple and require specific hardware. Research compatibility before attempting.
{% endhint %}

---

{% hint style="success" %}
**Reminder:** Most users should install from the [App Store](../../installation-and-usage/installing-provenance/app-store.md) or [sideload](../../installation-and-usage/installing-provenance/sideloading.md) instead of building from source. A macOS VM is only needed for compiling Provenance yourself.
{% endhint %}
