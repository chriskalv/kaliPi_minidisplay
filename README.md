kaliPi Mini Display
========================

A tiny screen on your kaliPi that shows the current IP of the device, its name and/or other useful things after booting up.

The intention of this project was to create a way to be able to instantly see the device's IP on the network, so one can directly SSH into it. Especially in large company networks with restricted NATs it can sometimes be a lengthy process to determine the IP of the kaliPi from the "outside".

The code is python-based. Assembly is pretty much lego-like.

## Hardware
+ KaliPi (consisting of a [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/), a [MicroSD Card](https://www.westerndigital.com/products/memory-cards/sandisk-extreme-uhs-i-microsd#SDSQXAF-032G-GN6MA) and a [Case](https://geekworm.com/collections/raspberry-pi/products/raspberry-pi-4-model-b-armor-aluminum-alloy-case-protective-shell))
+ [Adafruit PiOLED 128x32 Display](https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage)

<br></br>

| Close-up of the assembled device   |
| :-------------: | 
| [![](https://i.imgur.com/bUT98Rx.jpg?raw=true)](https://i.imgur.com/bUT98Rx.jpg)   |   

<br></br>

## Setup
These instructions assume your KaliPi is assembled and "ready to go".
1. Update/Upgrade your KaliPi: `sudo apt-get update && sudo apt-get upgrade -y`
2. Install pip3: `sudo apt-get install python3-pip`
3. Install PiOLED library: `sudo pip3 install adafruit-circuitpython-ssd1306`
4. Install PIL (needed for custom fonts): `sudo apt-get install python3-pil`
5. Edit/add the following lines to /boot/config.txt (`sudo nano /boot/config.txt`) and save the file in order to enable I2C and change the I2C core frequency to 100 kHz:
```python
dtparam=i2c_arm=on
dtparam=i2c_baudrate=1000000
```
6. Add the following line to /etc/modules (`sudo nano /etc/modules`) and save the file:
```python
i2c-dev
```
7. Reboot the device and test I2C functionality
8. Copy `stats.py` to your device, chmod and make it autorun on startup.
