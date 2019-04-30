# Controllers

* **🖲 Controller Types**
  * [MFi Controllers](./#mfi-controllers)
    * [Gamepad Profiles](./#mfi-profiles)
  * [Steam Controller](./#steam-controller-pseudo-mfi)
  * [iCade Controllers](./#icade-controllers)
* **🕹 Controller Forms**
  * Form-fitting
  * Standalone
* **🎮 Controllers** · Supported, Classified & Rated
* **🎛  Controls**
  * MFi Controls
  * iCade Controls  ·  _\(coming later…\)_

### Controller Types

#### MFi Controllers

Certified MFi Controllers are the standard complying to Apple's Gamepad profile\(s\). They are the easiest and most compatible controllers to use not just for Provenance, but iOS and tvOS in general.

#### **MFi Profiles**

MFi controllers exist in a few different formats made distinct as profiles in Apple's SDK.

| Profile | ❚❚ | ✜ | A | B | X | Y | -- | == | ⓁⓇ | ③③ | ◀︎ | ▶︎ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Micro | ● | ● | ● | ● |  |  |  |  |  |  |  |  |
| Standard | ● | ● | ● | ● | ● | ● | ● |  |  |  |  |  |
| Extended | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |  |
| Extended2\* | ● | ● | ● | ● | ● | ● | ● | ● | ● | ● |  |  |

\*Technically, there is only one Extended profile in the SDK, but we make the previous generation distinct within Provenance.  


Due to Apple's shortsightedness, all MFi controllers lack certain buttons to be equivalent to any modern gaming standard \(PS4, Xbox, etc…\) made accessible in Provenance in various ways:

1. For pre-PSX Systems: systems without Trigger buttons\): Using L2, R2 \(Select, Start\)
2. For PSX, N64, and on… 
   1. MFi+ Combos
   2. Pause Menu
3. \(iOS only\) Missing Buttons Always On-Screen _Beta, not all systems supported_
4. MFi Controls

#### Steam Controller \(pseudo MFi\)

Valve's Steam Controller uses its own protocol different from MFi, and not a virtual keyboard hack like iCade types, but we can conform it to the MFi Extended Gamepad protocol and still obtain input from the extra buttons as a sort of MFi hybrid, however limited to use only within the app \(cannot navigate the system such as MFi can do with tvOS\).   
⚠️  Currently, Steam Controller will not reconnect automatically, requiring app relaunch.

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
* [MFi](https://bit.ly/2LDZNzI)\(\#controls\)

#### iCade Controllers

Before MFi, there were various controllers using non-standardized virtual keyboard hacks to get gamepad input. Because of this they are not as fluid or as granular as you can get from MFi or a Steam controller as they are using key mappings and not variable numerical data \(as would be needed for thumbstick coordinates and trigger sensitivity, etc…\), however they tend to have more buttons available. Another drawback is that you cannot use two iCades simultaneously, as Apple only allows one 'keyboard' connected at a time…   
⚠️  iCade and MFi cannot be combined without bugs, atm…

* _iCade control maps coming later…_

### Controller Forms

#### Form-fitting

Form fitting controllers attach to your devices, in either a PSP sort of way \(GameVice\) or with a clamp that mounts the device above the controller. Some are powered by the device, others self-powered via battery and connect over bluetooth. Great for iPhone. Decent for iPads. Generally useless for Apple TV, unless you have a bluetooth device with remove-able or collapse-able clamp.

#### Standalone

Standalone controllers are familiar to that of Playstation or Xbox. Recommended for iPads, and the absolute for Apple TV.

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

| Controller | iPhone | iPad | aTV | Type | Profile | Rating |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| [GameVice: iPhone](https://www.amazon.com/Gamevice-Controller-Gamepad-iPhone-Certified-Compatible/dp/B077LZJ679/) XR not supported&lt;/sub&gt; | ● |  |  | MFi | Extended | ●●●●○ |
| [GameVice: iPad Pro 12.9"](https://www.amazon.com/Gamevice-Controller-Gamepad-12-9-inch-Certified-Accessories/dp/B01MFCXJZD/) |  | ● |  | MFi | Extended | ●●●○○ |
| [GameVice: iPad Mini](https://www.amazon.com/Controller-Gamepad-Gamevice-Certified-Accessories-Patented/dp/B01MR4VLJW/) |  | ● |  | MFi | Extended | ●●●◐○ |
| [Rotor Riot](https://www.amazon.com/Rotor-Riot-Certified-Controller-Compatible/dp/B07J1J7D6Z/) | ● | ● | ● | MFi | Extended2 | ●●●●◐ |
| [Steam Controller](https://www.amazon.com/Steam-Controller-SteamOS/dp/B016KBVBCS/) | ○ | ● | ● | pMFi | Extended2+ | ●●●●◐ |
| [SteelSeries Nimbus](https://www.amazon.com/SteelSeries-Nimbus-Wireless-Gaming-Controller/dp/B01AZC3III/) + [clamp](https://www.amazon.com/TPFOON-Smartphone-Cellphone-Steelseries-Controller/dp/B07DLY5PB4/) | ● | ● | ● | MFi | Extended | ●●●●◐ |
| [SteelSeries Stratus XL: iOS](https://www.amazon.com/SteelSeries-Bluetooth-Wireless-Controller-69026/dp/B00QTSR5GO/) | ○ | ● | ● | MFi | Extended | ●●●●◐ |
| [SteelSeries Stratus XL](https://www.amazon.com/SteelSeries-Stratus-Bluetooth-Wireless-Controller/dp/B015WKY3IM/) | ○ | ● | ● | iCade | Extended+ | ●●●◐○ |
| [SteelSeries Stratus](https://www.amazon.com/SteelSeries-Stratus-Wireless-Gaming-Controller/dp/B00HSB2EZI/) | ○ | ● | ● | MFi | Extended | ●●●○○ |
| [Horipad Ultimate](https://www.amazon.com/HORI-HORIPAD-ULTIMATE-Wireless-Controller/dp/B06Y2512L8/) | ○ | ● | ● | MFi | Extended | ●●●◐○ |
| [8bitdo N30](https://www.amazon.com/Wireless-Controller-bluetooth-Android-windows/dp/B01N4M9LQY/) / [F30](https://www.amazon.com/FC30-Game-Controller-PC-Mac-Linux/dp/B00FEEGZVU/)^\* | ○ | ● | ● | iCade | Standard+ | ●●◐○○ |
| [8bitdo SN30](https://www.amazon.com/8bitdo-Wireless-Bluetooth-Controller-Joystick/dp/B014QP2H1E/) / [SF30](https://www.amazon.com/8Bitdo-SF30-Controller-Windows-macOS-Android/dp/B0748S3GXG/)^\* + [clamp](https://www.amazon.com/8Bitdo-Xstander-Holder-SFC30-SNES30/dp/B017SFNW0E/) | ● | ● | ● | iCade | Standard+ | ●●◐○○ |
| [8bitdo N30](https://www.amazon.com/Wireless-Bluetooth-Controller-Classic-Joystick/dp/B018K3Q4KS/) / [F30Pro](https://www.amazon.com/FC30-Game-Controller-PC-Mac-Linux/dp/B00FEEGZVU/)^\* + [clamp A](https://www.amazon.com/Xtander-Wireless-8Bitdo-Controller-Gamepad/dp/B01N9PWDZ3/) , [B](https://www.amazon.com/Gam3Gear-Xtander-Wireless-NES30-Pro-Controller/) |  |  |  | iCade | Extended+ | ●●●◐○ |
| [8bitdo Zero](https://www.amazon.com/8BITDO-Wireless-Controller-Android-Windows/dp/B0156IC8M8/) | ○ | ● | ● | iCade | Standard+ | ●●○○○ |
| [Logitech Powershell](https://www.amazon.com/Logitech-PowerShell-Controller-Battery-Generation/dp/B00FHREO8K/)  5/5s/SE/iPod5T-only | ○ |  |  | MFi | Standard | ●●◐○○ |
| [MOGA Ace](https://www.amazon.com/PowerA-MOGA-Ace-Power-Electronic-Games/dp/B00H01EXM8/) 5/5c/5s/SE-only&lt;/sub&gt; | ● |  |  | MFi | Standard | ●◐○○○ |
| [MOGA Rebel](https://www.amazon.com/MOGA-Rebel-Premium-iOS-Gaming-Controller/dp/B00PG0C85Y)^ | ● | ● | ● | iCade | Extended | ●●●◐○ |

^ Discontinued, some can still be obtained.  
 \* Requires [legacy firmware](http://support.8bitdo.com/) to work with iOS/tvOS.  


⭐️Later adding specific controller reviews, pros/cons, retro-nostalgia recommendations…

