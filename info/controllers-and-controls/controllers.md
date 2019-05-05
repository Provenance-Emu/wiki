---
description: 'Supported, Classified and Rated Controllers/Gamepads'
---

# Controllers

* **🖲** [**Controller Types**](controllers.md#controller-types)\*\*\*\*
  * [MFi ](./#mfi-controllers)
  * [Steam](./#steam-controller-pseudo-mfi)
  * [iCade](./#icade-controllers)
* **🕹** [**Controller Forms**](controllers.md#controller-forms)\*\*\*\*
* **🎮** [**Controllers**](controllers.md#profiles) · Supported, Classified & Rated
* **🎛** [**Controls**](controllers.md#controls)\*\*\*\*

## Controller Types

### MFi Controllers

Certified MFi Controllers are the standard complying to Apple's Gamepad profile\(s\). They are the easiest and most compatible controllers to use not just for Provenance, but iOS and tvOS in general.

#### **MFi Profiles**

MFi controllers exist in a few different formats made distinct as profiles in Apple's SDK.

| Profile | ❚❚ | ✜ | A | B | X | Y | -- | == | ⓁⓇ | ③③ | ◀︎ | ▶︎ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Micro | ● | ● | ● | ● |  |  |  |  |  |  |  |  |
| Standard | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |
| Extended | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |
| Extended2\* | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |

{% hint style="info" %}
Technically, there is only one Extended profile in the SDK, but we make the previous generation \(which excluded L3 and R3\) distinct within Provenance and refer to the updated profile as Extended2.
{% endhint %}

Due to Apple's shortsightedness, all MFi controllers lack certain buttons to be equivalent to any modern gaming standard \(PS4, Xbox, etc…\) made accessible in Provenance in various ways:

1. For systems without trigger buttons:
   * L2: Select, R2: Start
2. For PSX, N64, and on… 
   * MFi+ Combos
   * UI Buttons within Pause Menu
3. Missing Buttons Always On-Screen \(iOS only\) _Beta, not all systems supported_
4. MFi Controls

### Steam Controller \(pseudo MFi\)

Valve's Steam Controller uses its own protocol different from MFi, and not a virtual keyboard hack like iCade types, but we can conform it to the MFi Extended Gamepad protocol and still obtain input from the extra buttons as a sort of MFi hybrid, however limited to use only within the app \(cannot navigate the system such as MFi can do with tvOS\). 

{% hint style="info" %}
Currently, Steam Controller will not reconnect automatically, requiring app relaunch.
{% endhint %}

| Profile | ❚❚ | ✜ | A | B | X | Y | -- | == | ⓁⓇ | ③③ | ◀︎ | ▶︎ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Extended2+ | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |

**Trackpad Modes:**

* Button Mode \(default\): like d-pad, c-buttons
* Touch Mode: like touch analog

**Stick Modes:**

* Analog Mode \(default\)
* D-Pad Mode

```text
L-Pad Toggle = ◉ L-Pad Click + ◀︎ (Back)
R-Pad Toggle = ◉ R-Pad Click + ▶︎ (Forward)
Stick Toggle = ◉ Stick Click + ◀︎ (Back)
```

Currently, ◀︎ \(Back\) / Select and ▶︎ \(Forward\) / Start will work with PSX, and N64 via MFi+ \(full support coming later…\)

* Requires [Steam Controller BLE firmware](https://support.steampowered.com/kb_article.php?ref=7728-QESJ-4420) via Steam Beta program.
* [MFi Controls](https://bit.ly/2LDZNzI)

### iCade Controllers

Before MFi, there were various controllers using non-standardized virtual keyboard hacks to get gamepad input. Because of this they are not as fluid or as granular as you can get from MFi or a Steam controller as they are using key mappings and not variable numerical data \(as would be needed for thumbstick coordinates and trigger sensitivity, etc…\), however they tend to have more buttons available. Another drawback is that you cannot use two iCades simultaneously, as Apple only allows one 'keyboard' connected at a time… 

{% hint style="warning" %}
 iCade and MFi can **not** be used together simultaneously without conflict/bugs, currently.
{% endhint %}

* _iCade control maps coming later…_

## Controller Forms

### Form-fitting

Form fitting controllers attach to your devices, in either a PSP sort of way \(GameVice\) or with a clamp that mounts the device above the controller. Some are powered by the device, others self-powered via battery and connect over bluetooth. Great for iPhone. Decent for iPads. Generally useless for Apple TV, unless you have a bluetooth device with remove-able or collapse-able clamp.

### Standalone

Standalone controllers are familiar to that of Playstation or Xbox. Recommended for iPads, and the absolute for Apple TV.

## Controllers

### Profiles

**Key**:   ● = Supported

| Profile | ❚❚ | ✜ | A | B | X | Y | -- | == | ⓁⓇ | ③③ | ◀︎ | ▶︎ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Micro | ● | ● | ● | ● |  |  |  |  |  |  |  |  |
| Standard | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |
| Standard+ | ● | ● | ● | ● | ● | ● | ● |  |  |  | ● | ● |
| Extended | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |
| Extended+ | ● | ● | ● | ● | ● | ● | ● | ● | ● |  | ● | ● |
| Extended2 | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |
| Extended2+ | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |

### Controllers

**Key**:   ● = Supported / Ideal   \|   ○ = Supported

<table>
  <thead>
    <tr>
      <th style="text-align:left">Controller</th>
      <th style="text-align:left">iPhone</th>
      <th style="text-align:left">iPad</th>
      <th style="text-align:left">aTV</th>
      <th style="text-align:left">Type</th>
      <th style="text-align:left">Profile</th>
      <th style="text-align:left">Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/Gamevice-Controller-Gamepad-iPhone-Certified-Compatible/dp/B077LZJ679/">GameVice: iPhone</a> 
        <br
        />X&#x280; not supported</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
      <td style="text-align:left">MFi</td>
      <td style="text-align:left">Extended</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25CF;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/Gamevice-Controller-Gamepad-12-9-inch-Certified-Accessories/dp/B01MFCXJZD/">GameVice: iPad Pro 12.9&quot;</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left"></td>
      <td style="text-align:left">MFi</td>
      <td style="text-align:left">Extended</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25CB;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/Controller-Gamepad-Gamevice-Certified-Accessories-Patented/dp/B01MR4VLJW/">GameVice: iPad Mini</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left"></td>
      <td style="text-align:left">MFi</td>
      <td style="text-align:left">Extended</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25D0;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/Rotor-Riot-Certified-Controller-Compatible/dp/B07J1J7D6Z/">Rotor Riot</a>
      </td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">MFi</td>
      <td style="text-align:left">Extended2</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25CF;&#x25D0;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/Steam-Controller-SteamOS/dp/B016KBVBCS/">Steam Controller</a>
      </td>
      <td style="text-align:left">&#x25CB;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">pMFi</td>
      <td style="text-align:left">Extended2+</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25CF;&#x25D0;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/SteelSeries-Nimbus-Wireless-Gaming-Controller/dp/B01AZC3III/">SteelSeries Nimbus</a> 
        <br
        />+ <a href="https://www.amazon.com/TPFOON-Smartphone-Cellphone-Steelseries-Controller/dp/B07DLY5PB4/">clamp</a>
      </td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">MFi</td>
      <td style="text-align:left">Extended</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25CF;&#x25D0;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/SteelSeries-Bluetooth-Wireless-Controller-69026/dp/B00QTSR5GO/">SteelSeries Stratus XL: iOS</a>
      </td>
      <td style="text-align:left">&#x25CB;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">MFi</td>
      <td style="text-align:left">Extended</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25CF;&#x25D0;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/SteelSeries-Stratus-Bluetooth-Wireless-Controller/dp/B015WKY3IM/">SteelSeries Stratus XL</a>
      </td>
      <td style="text-align:left">&#x25CB;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">iCade</td>
      <td style="text-align:left">Extended+</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25D0;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/SteelSeries-Stratus-Wireless-Gaming-Controller/dp/B00HSB2EZI/">SteelSeries Stratus</a>
      </td>
      <td style="text-align:left">&#x25CB;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">MFi</td>
      <td style="text-align:left">Extended</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25CB;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/HORI-HORIPAD-ULTIMATE-Wireless-Controller/dp/B06Y2512L8/">Horipad Ultimate</a>
      </td>
      <td style="text-align:left">&#x25CB;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">MFi</td>
      <td style="text-align:left">Extended</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25D0;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/Wireless-Controller-bluetooth-Android-windows/dp/B01N4M9LQY/">8bitdo N30</a> /
        <a
        href="https://www.amazon.com/FC30-Game-Controller-PC-Mac-Linux/dp/B00FEEGZVU/">F30</a>^*</td>
      <td style="text-align:left">&#x25CB;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">iCade</td>
      <td style="text-align:left">Standard+</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25D0;&#x25CB;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/8bitdo-Wireless-Bluetooth-Controller-Joystick/dp/B014QP2H1E/">8bitdo SN30</a> /
        <a
        href="https://www.amazon.com/8Bitdo-SF30-Controller-Windows-macOS-Android/dp/B0748S3GXG/">SF30</a>^*
          <br />+ <a href="https://www.amazon.com/8Bitdo-Xstander-Holder-SFC30-SNES30/dp/B017SFNW0E/">clamp</a>
      </td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">iCade</td>
      <td style="text-align:left">Standard+</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25D0;&#x25CB;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/Wireless-Bluetooth-Controller-Classic-Joystick/dp/B018K3Q4KS/">8bitdo N30</a> /
        <a
        href="https://www.amazon.com/FC30-Game-Controller-PC-Mac-Linux/dp/B00FEEGZVU/">F30Pro</a>^*
          <br />+ <a href="https://www.amazon.com/Xtander-Wireless-8Bitdo-Controller-Gamepad/dp/B01N9PWDZ3/">clamp A</a> ,
          <a
          href="https://www.amazon.com/Gam3Gear-Xtander-Wireless-NES30-Pro-Controller/">B</a>
      </td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
      <td style="text-align:left">iCade</td>
      <td style="text-align:left">Extended+</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25D0;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/8BITDO-Wireless-Controller-Android-Windows/dp/B0156IC8M8/">8bitdo Zero</a>
      </td>
      <td style="text-align:left">&#x25CB;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left">iCade</td>
      <td style="text-align:left">Standard+</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25CB;&#x25CB;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/Logitech-PowerShell-Controller-Battery-Generation/dp/B00FHREO8K/">Logitech Powershell</a> 
        <br
        />5/5s/SE/iPod5T <em>only</em>
      </td>
      <td style="text-align:left">&#x25CB;</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
      <td style="text-align:left">MFi</td>
      <td style="text-align:left">Standard</td>
      <td style="text-align:left">&#x25CF;&#x25CF;&#x25D0;&#x25CB;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left">
        <p><a href="https://www.amazon.com/PowerA-MOGA-Ace-Power-Electronic-Games/dp/B00H01EXM8/">MOGA Ace</a> 
        </p>
        <p>5/5c/5s/SE <em>only</em>
        </p>
      </td>
      <td style="text-align:left">&#x25CF;</td>
      <td style="text-align:left"></td>
      <td style="text-align:left"></td>
      <td style="text-align:left">MFi</td>
      <td style="text-align:left">Standard</td>
      <td style="text-align:left">&#x25CF;&#x25D0;&#x25CB;&#x25CB;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/MOGA-Rebel-Premium-iOS-Gaming-Controller/dp/B00PG0C85Y">MOGA Rebel</a>^</td>
      <td
      style="text-align:left">&#x25CF;</td>
        <td style="text-align:left">&#x25CF;</td>
        <td style="text-align:left">&#x25CF;</td>
        <td style="text-align:left">iCade</td>
        <td style="text-align:left">Extended</td>
        <td style="text-align:left">&#x25CF;&#x25CF;&#x25CF;&#x25D0;&#x25CB;</td>
    </tr>
    <tr>
      <td style="text-align:left"><a href="https://www.amazon.com/C-T-R-L-i-Mobile-Gamepad-not-machine-specific/dp/B00NSGA1K2">Mad Catz Micro C.T.R.L.i</a>^</td>
      <td
      style="text-align:left">&#x25CF;</td>
        <td style="text-align:left">&#x25CF;</td>
        <td style="text-align:left">&#x25CF;</td>
        <td style="text-align:left">MFi</td>
        <td style="text-align:left">Extended</td>
        <td style="text-align:left">&#x25CF;&#x25CF;&#x25CB;&#x25CB;&#x25CB;</td>
    </tr>
  </tbody>
</table>^ Discontinued, some can still be obtained.  
\* Requires [legacy firmware](http://support.8bitdo.com/) to work with iOS/tvOS.  


{% hint style="info" %}
Check out the controller phone mounts made by [UtorCase](https://utorcase.com/).
{% endhint %}



⭐️Later adding specific controller reviews, pros/cons, retro-nostalgia recommendations…

## Controls

A full list of mapped controls for Standard and Extended MFi gamepad profiles per system can be found in [MFi Controls](https://bit.ly/2LDZNzI).

_iCade control maps coming later…_

