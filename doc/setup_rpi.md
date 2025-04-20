# Image and setup instructions for Raspberry Pi

## Create a bootable SD card

Using the Raspberry Pi Imager, you can create a bootable SD card with the latest Raspberry Pi OS.

1. Download the Raspberry Pi Imager from the [Raspberry Pi website](https://www.raspberrypi.com/software/).
2. Insert the SD card into your computer.
   2.1 Or use a SSD drive with a USB adapter.
3. Open the Raspberry Pi Imager and select the OS you want to install.

## Enable SSH on Rpi

- from command line

```bash
sudo raspi-config
# then select: Interfacing Options > SSH > Enable
```

- from the boot partition

1. Insert the SD card into your computer.
2. Open the boot partition of the SD card.
3. Create a file named `ssh` (no extension) in the root of the boot partition.
