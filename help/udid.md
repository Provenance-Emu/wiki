---
description: How to find your device's UDID for development or beta testing
---

# UDID Registration

A **UDID** (Unique Device Identifier) is a 40-character string that uniquely identifies your Apple device. You may need it for:

- Joining OTA (over-the-air) beta distributions
- Registering your device on an Apple Developer account for sideloading
- Troubleshooting device-specific issues

---

## How to Find Your UDID

{% tabs %}
{% tab title="iPhone / iPad (On-Device)" %}
### Using a web tool

1. Open Safari on your device and visit [udid.tech](https://udid.tech) or [ipsw.me/device-finder](https://ipsw.me/device-finder)
2. Follow the prompts to install a temporary configuration profile
3. Your UDID will be displayed — tap to copy it
4. The profile can be removed afterward in Settings → General → VPN & Device Management

{% hint style="info" %}
These tools install a temporary profile to read your UDID. The profile can be safely removed after you've copied the identifier.
{% endhint %}
{% endtab %}

{% tab title="macOS (Finder)" %}
### Using Finder (macOS Catalina and later)

1. Connect your iPhone/iPad to your Mac via USB
2. Open **Finder** and select your device under **Locations** in the sidebar
3. Click the **device name** or **model** at the top of the pane
4. A summary appears showing Capacity, Phone Number, and **Serial Number**
5. **Click on Serial Number** — it cycles through: Serial Number → UDID → ECID → Model Number
6. When UDID is displayed, **right-click** → **Copy UDID**

### Using System Information

1. Connect your device via USB
2. Click  → **About This Mac** → **More Info** → **System Report**
3. Select **USB** in the sidebar
4. Find your device under the USB bus
5. The **Serial Number** shown here is your UDID (you may need to add a dash after the 8th character)
{% endtab %}

{% tab title="Windows" %}
### Using Apple Devices app

1. Install the [Apple Devices app](https://apps.microsoft.com/detail/9NP83LWLPZ9K) from the Microsoft Store
2. Connect your iOS device via USB
3. Select your device by clicking its image
4. A summary shows Capacity, Phone Number, and **Serial Number**
5. **Click on Serial Number** — it changes to display your UDID
6. Right-click to copy
{% endtab %}

{% tab title="Linux" %}
### Using lsusb

1. Connect your device via USB
2. Run:
```sh
lsusb -v 2> /dev/null | grep -e "Apple Inc" -A 2
```
3. The serial number shown is your UDID

### Using libimobiledevice

For more reliable detection, install `libimobiledevice`:
```sh
# Debian/Ubuntu
sudo apt install libimobiledevice-utils

# Fedora
sudo dnf install libimobiledevice-utils

# Then run:
idevice_id -l
```
{% endtab %}
{% endtabs %}

---

## Registering Your UDID

Once you have your UDID, it needs to be registered on an Apple Developer account:

**If you're a developer:**
1. Log in to [developer.apple.com](https://developer.apple.com)
2. Go to **Certificates, Identifiers & Profiles** → **Devices**
3. Click **+** to register a new device
4. Enter a name and paste your UDID
5. Click **Continue** → **Register**

**If you're joining a beta:**
- Send your UDID to the developer who invited you (they'll register it on their account)

{% hint style="warning" %}
Free Apple Developer accounts can register up to **10 devices per year** (across all device types). Paid accounts support up to 100 devices per device type.
{% endhint %}

---

{% hint style="info" %}
Need help? Ask on [Discord](https://discord.gg/provenance).
{% endhint %}
