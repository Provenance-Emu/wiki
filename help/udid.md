---
description: Locating your UDID.
---

Your iDevice UDID may be requested for inclusion in OTA (over-the-air) builds.

Here is how you can locate that UDID.

## On device

### Method 1

You can get it here: https://get.udid.io/.

1. Click install
2. <img src="https://messapps.com/wp-content/uploads/2016/08/Install.png"/>
3. Enter passcode
    <img src="https://messapps.com/wp-content/uploads/2016/08/passcode.png"/>
4. Click on “Install”
    <img src="https://messapps.com/wp-content/uploads/2016/08/Install-again.png"/>
5. Tap to find UDID
6. Repeat again points 1-3
7. You will get your UDID
    <img src="https://messapps.com/wp-content/uploads/2016/08/udid.png"/>

## macOS

### Method 1 (About this Mac)

1. Connect your iPhone to Mac.
2. Go to About This Mac.
3. Click on System Report and by USB.
4. Under the USB 3.0 Bus, you’ll see your iPhone between all the other USB devices connected to your Mac.
5. Select your iPhone from the bottom part of the window, copy the Serial Number (you may need to add a dash (-) after the eighth digit in the serial number).

### Method 2 (iTunes)

1. Open up the latest version of iTunes and connect your iOS device to your computer.
2. Select your iOS device by clicking the device’s image located at the upper-left corner of iTunes’s UI.
3. Select your iOS device
4. On the next screen, a window should appear listing your phone’s Capacity, Phone Number, and Serial Number.
5. By clicking on Serial Number once, the prompt should change to display your UDID.

## Windows

### Method 1 (iTunes)

1. Open up the latest version of iTunes and connect your iOS device to your computer.
2. Select your iOS device by clicking the device’s image located at the upper-left corner of iTunes’s UI.
3. Select your iOS device
4. On the next screen, a window should appear listing your phone’s Capacity, Phone Number, and Serial Number.
5. By clicking on Serial Number once, the prompt should change to display your UDID.

## Linux

### Method 1 (cli)

1. Connect device to USB
2. Run this shell command
```sh
lsusb -v 2> /dev/null | grep -e "Apple Inc" -A 2
```
