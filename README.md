---
This branch mocks event objects queried by O365 to eliminate
the need for a Microsoft account.
It focuses on getting data from the dongle successfully sent
to displays.
---


# Meeting room displays

Bluetooth mesh based long lasting meeting room displays.

This repository provides the code for the displays as well as the server
application that fetches the meeting room appointments from an office 365
calendar and sends the information to the configured displays. The server
application will use a usb dongle to send the data to the displays.

## Hardware
The dongle used for the server application is the Nordic nRF52840 Dongle:
https://www.nordicsemi.com/Software-and-tools/Development-Kits/nRF52840-Dongle

The displays use the Nordic nRF52840 DK:
https://www.nordicsemi.com/Software-and-Tools/Development-Kits/nRF52840-DK

and the waveshare 7.5 inch e-paper HAT:
https://www.waveshare.com/wiki/7.5inch_e-Paper_HAT

please note that at the moment only revision 1 of the e-Paper HAT is working.

## Checkout and init
The project is based on zephyr RTOS. To clone this repository as well as
everything needed call:
```bash
west init -m https://github.com/michaeleggers/meeting_room_displays.git
git checkout mock-o365
west update
```
## Use the display <-> room config
Rename config.py.template to config.py. The file resides in server/.
Note that on this branch, the server will be stuck in an endless send, receive loop
when a display that is present in config.py is not connected!

## Udev rule
To make it easier to flash the dongle it is recommended to apply the provided
Udev rule. It will create a symlink which will always have the same name no
matter which ttyACM enumeration it got.
```bash
sudo cp meeting_room_displays/20_DiplayDongleUDev.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger
```

### If Udev does not work

Change Makefile and config.py to use ttyACM0. Most of the time this will work.
Make sure you set write permission-bits for /dev/ttyACM0:
```
sudo chmod 666 /dev/ttyACM0
```
And change the ownership by:
```
sudo chown <username> /dev/ttyACM0
```

## Installing Zephyr SDK
To install the SDK follow the steps provided in the official
[Zephyr documentation](https://docs.zephyrproject.org/latest/getting_started/index.html).

## Installing nrfutil
In order to flash the Nordic dongle the nrfutil package is required.
Install it via pip:
```
pip install nrfutil
```

## Install nrfjprog
nrfjprog is required to flash/debug the nRF52840 development kit (in this case: the display). Download the tool 
[here](https://www.nordicsemi.com/Products/Development-tools/nrf-command-line-tools/download).
Debian based systems may install the `.deb` package via
```
sudo dpkg -i <nrf-debian-package-name>.deb
```

nrfjprog requires SEGGER's JLink Software in order to run. Download the appropriate installer for
your system [here](https://www.segger.com/downloads/jlink).
As in the previous step, Debian based systems may use the `.deb` and install it the same way as above.

## Adding the user to the dialout group
Make sure to add the user who is working on this project to the `dialout` group so
that she can access `/dev/<tty-device>` (eg. the dongle):
```
sudo usermod -a -G dialout <username>
```
Do not forget to start a new terminal afterwards.

## Build
To build one of the components use the provided make file in
meeting_room_displays/app/

E.g. to build and flash a display call:
```bash
make display
```

By default the displays address is 0x030c. To change that do eg.
```bash
make display DISPLAY_ADDRESS=0x030d
```
to change the address to 0x030d. Add the display to server/config.py!

To build and flash the dongle:
Insert the dongle into a USB port and press the reset button. A red
LED will light up. Then call:
```bash
make dongle
```

## Issues
Sometimes the udev rule won't work and `ttyDisplayDongle` won't show up
in `/dev/`. In that case uncomment the section at the very bottom
in `app/Makefile`.

