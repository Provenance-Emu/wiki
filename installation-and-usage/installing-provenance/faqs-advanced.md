---
description: Advanced installation FAQ for sideloading, building from source, and developer workflows
---

# Advanced Installation FAQ

This FAQ is for advanced users who are sideloading or building Provenance from source. **Most users should install from the App Store** - see the main [FAQ](../../faqs.md) instead.

---

## Sideloading

<a id="no-mac"></a>
<details>
<summary><strong>What if I don't have a Mac?</strong></summary>

**Sideloading (cross-platform):**
- ✅ Windows, Mac, Linux all supported
- Use [AltStore](https://altstore.io/) or [Sideloadly](https://sideloadly.io/)
- Download `.ipa` from [GitHub Releases](https://github.com/Provenance-Emu/Provenance/releases)

**Building from source (requires macOS):**
- ❌ Windows/Linux cannot build iOS apps
- ✅ Use a Hackintosh or macOS virtual machine ([Virtualizing macOS](../../info/miscellaneous/virtualizing-macos.md))
- ✅ Or sideload the pre-built release instead

</details>

<a id="no-computer"></a>
<details>
<summary><strong>Can I install without a computer?</strong></summary>

**Officially: No safe method exists.**

❌ **DO NOT** use 3rd-party signing services - they:
- Install malware, adware, or tracking profiles
- Get revoked by Apple (you lose your games/saves)
- Violate Apple's terms (can brick your device)
- Steal your Apple ID credentials

**Legitimate options:**
1. ✅ **App Store** - Install directly on device (no computer needed)
2. ✅ **Borrow a friend's computer** - Sideload once, re-sign every 7 days
3. ✅ **Use a paid Apple Developer account** - Provisioning lasts 1 year

</details>

<a id="install-fail"></a>
<details>
<summary><strong>Why does Provenance not install?</strong></summary>

**Common issues:**

1. **Certificate error / "Untrusted Developer"**
   - Settings → General → VPN & Device Management
   - Trust the developer profile

2. **"App is already installed"**
   - Delete existing Provenance first
   - Or use a different bundle ID when building

3. **"Provisioning profile expired"**
   - Free Apple Developer accounts expire every 7 days
   - Re-sign with AltStore/Sideloadly
   - Or upgrade to paid account ($99/year)

4. **AltStore/Sideloadly errors**
   - Make sure the [Apple Devices app](https://apps.microsoft.com/detail/9NP83LWLPZ9K) (formerly iTunes) and iCloud are installed (Windows)
   - Update AltServer to latest version
   - Check firewall isn't blocking connection

**Full guide:** [Sideloading](sideloading.md)

</details>

<details>
<summary><strong>How do I re-sign every 7 days?</strong></summary>

**Free Apple Developer accounts** expire provisioning profiles every 7 days.

**Options:**

1. **AltStore (easiest)**
   - Install AltServer on your Mac/PC
   - Keep it running - auto-refreshes every 6 days
   - No manual work needed!

2. **Manual re-signing**
   - Use Sideloadly, iOS App Signer, or Xcode
   - Re-install `.ipa` every 6-7 days
   - Data/saves are preserved

3. **Upgrade to paid account**
   - $99/year Apple Developer Program
   - Provisioning lasts 1 year (re-sign annually)

</details>

<details>
<summary><strong>What is a provisioning profile?</strong></summary>

A **provisioning profile** is a file that allows an app to run on a specific device. It contains:
- Your Apple Developer certificate
- App bundle ID
- List of authorized devices (UDIDs)
- Expiration date

**Free accounts:**
- Max 3 apps simultaneously
- 7-day expiration
- Max 10 devices per year

**Paid accounts:**
- Unlimited apps
- 1-year expiration
- Unlimited devices

**Where to find:** Xcode → Preferences → Accounts → [Your Apple ID] → Manage Certificates

</details>

---

## Building from Source

<a id="cydia"></a>
<details>
<summary><strong>Is there a Cydia repo?</strong></summary>

**No.** Provenance is not distributed via Cydia.

If you're jailbroken, you can still install Provenance via:
- App Store (recommended)
- Sideloading (works on jailbroken devices)
- Building from source

</details>

<a id="prerelease"></a>
<details>
<summary><strong>Will you release an .ipa of the beta?</strong></summary>

**Beta builds are available** on GitHub:
- [Releases](https://github.com/Provenance-Emu/Provenance/releases) - Stable releases
- [Actions](https://github.com/Provenance-Emu/Provenance/actions) - Dev builds (requires GitHub login)

**Note:** Beta builds may be unstable. Use at your own risk.

**App Store users:** Subscribe to Provenance Plus for TestFlight beta access (official, stable betas).

</details>

<a id="release-date"></a>
<details>
<summary><strong>When is the next release?</strong></summary>

**Check development status:**
- [Milestones](https://github.com/Provenance-Emu/Provenance/milestones) - Planned releases
- [Projects](https://github.com/Provenance-Emu/Provenance/projects) - Current work
- [Discord](https://discord.gg/provenance) - Community discussion

**We don't commit to release dates** - small team, releases when ready.

**App Store users:** Updates are automatic - no need to track releases!

</details>

<details>
<summary><strong>Why is my build slower than the App Store version?</strong></summary>

**You probably built the DEBUG version.**

**How to tell:**
- App name: **Prov Debug** (not "Provenance")
- Settings → Version shows `DEBUG`

**Fix:**
1. Open project in Xcode
2. Select scheme: **Provenance-Release** (iOS) or **ProvenanceTV-Release** (tvOS)
3. Build and run
4. ✅ Release version is 5-10x faster!

**Why debug is slow:**
- Extra logging and validation
- No compiler optimizations
- Memory leak detection overhead
- Designed for development, not gameplay

</details>

---

## Developer Workflows

<details>
<summary><strong>How do I use Provenance Plus features when sideloading?</strong></summary>

**Requirement:** Use a **unique bundle ID** when building.

**Steps:**
1. Open project in Xcode
2. Select **Provenance** target
3. **Signing & Capabilities** tab
4. Change **Bundle Identifier** to something unique:
   - Default: `com.provenance-emu.provenance`
   - Yours: `com.yourname.provenance` (or anything unique)
5. Build and install
6. Subscribe to Provenance Plus in-app
7. ✅ Plus features (iCloud sync, etc.) now work

**Why?** App Store version uses the default bundle ID. Sideloaded apps with the same ID can't verify subscriptions.

</details>

<details>
<summary><strong>Can I run beta and stable side-by-side?</strong></summary>

**Yes!** Use different bundle IDs for each.

**Setup:**
1. **Stable:** Keep default bundle ID
2. **Beta:** Change to `com.yourname.provenance-beta`
3. Build and install both

**Result:** Two separate apps, independent data.

**Note:** Only enable iCloud sync on ONE version to avoid conflicts.

</details>

### Where did you install the app from?

**Why we ask:**

3rd-party signing services are dangerous:
- ❌ Inject malware, adware, tracking
- ❌ Steal Apple ID credentials
- ❌ Get revoked by Apple (lose all data)
- ❌ Violate Apple ToS

**Official sources only:**
- ✅ **App Store** (safest)
- ✅ **GitHub Releases** (sideload yourself)
- ✅ **Build from source** (Xcode)

**If you used a 3rd-party service:**
1. Delete the app immediately
2. Remove any profiles (Settings → General → VPN & Device Management)
3. Change your Apple ID password
4. Re-install from official source

**We cannot support 3rd-party builds** - they cause:
- Broken features
- Crashes
- Security vulnerabilities
- Data loss when profiles are revoked

---

## Troubleshooting Advanced Installation

<details>
<summary><strong>App crashes at launch after 7 days</strong></summary>

**Cause:** Free Apple Developer provisioning expired.

**Solutions:**
1. ✅ **Re-sign with AltStore** - Automatic refresh every 6 days
2. ✅ **Re-sign with Sideloadly** - Manual re-install every 6-7 days
3. ✅ **Upgrade to paid account** - Lasts 1 year

**Data safe?** Yes! Saves/ROMs are preserved when re-signing.

</details>

<details>
<summary><strong>"Unable to install Provenance"</strong></summary>

**Fixes:**

1. **Check storage space** — Provenance is 2.5 GB, need ~5 GB free for installation
2. **Delete existing version** — Remove old Provenance first, or use different bundle ID
3. **Update Xcode / signing tools** — Xcode → Check for Updates; Update AltStore/Sideloadly
4. **Verify Apple ID** — Xcode → Preferences → Accounts → Remove and re-add Apple ID

</details>

<details>
<summary><strong>Xcode says "Signing certificate expired"</strong></summary>

**Cause:** Your Apple Developer certificate expired.

**Fix (free account):**
1. Xcode → Preferences → Accounts
2. Select your Apple ID
3. Click **Manage Certificates**
4. Delete old certificate
5. Click **+** → **iOS Development**
6. ✅ New certificate created

**Fix (paid account):**
1. Go to [developer.apple.com](https://developer.apple.com)
2. Certificates → Revoke old one
3. Create new certificate
4. Download and install in Xcode

</details>

<details>
<summary><strong>Can't find my UDID</strong></summary>

**UDID** = Unique Device Identifier (only needed for sideloading/development)

**How to find:**
1. Connect device to Mac
2. Open **Finder** → Select device
3. Click serial number → Changes to UDID
4. Right-click → **Copy**

**Or use online tools:**
- [ipsw.me/device-finder](https://ipsw.me/device-finder)
- [udid.tech](https://udid.tech)

**Full guide:** [UDID Registration](../../help/udid.md)

</details>

---

## Beta Testing

<details>
<summary><strong>How do I become a beta tester?</strong></summary>

**Option 1: Provenance Plus (recommended)**
- Subscribe to Provenance Plus
- Get TestFlight beta access
- Official, stable betas
- Priority support

**Option 2: Build from source**
- Clone `develop` branch from GitHub
- Build in Xcode
- Very latest code (may be unstable)
- Report bugs on GitHub Issues

**Beta tester requirements:**
1. ✅ Read [Issues Usage](https://github.com/Provenance-Emu/Provenance/wiki/Issues-Usage)
2. ✅ Only report against latest build
3. ✅ Check existing issues before reporting
4. ✅ Follow \#git-updates on Discord

**Note:** Using beta ≠ beta testing. Active participation required!

</details>

---

## Still Need Help?

{% hint style="success" %}
💬 Join our [Discord](https://discord.gg/provenance) - \#advanced-help channel

🐛 Found a bug? Report on [GitHub Issues](https://github.com/Provenance-Emu/Provenance/issues)

📖 General questions? See main [FAQ](../../faqs.md)
{% endhint %}

---

*For most users, we recommend installing from the App Store instead of sideloading or building from source.*
