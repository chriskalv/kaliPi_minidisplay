kaliPi Mini Display
========================

A tiny screen on your kaliPi that shows the name, current IP and MAC address of your device.

This project mainly intends to support acquiring a device's IP on a network more quickly. Especially in large company networks with restricted NATs it can sometimes be a lengthy process to determine the IP from the "outside".

The code is python-based. Assembly is pretty much lego-like.

## Hardware
+ KaliPi (consisting of a [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/), a [MicroSD Card](https://www.westerndigital.com/products/memory-cards/sandisk-extreme-uhs-i-microsd#SDSQXAF-032G-GN6MA) and a [Case](https://geekworm.com/collections/raspberry-pi/products/raspberry-pi-4-model-b-armor-aluminum-alloy-case-protective-shell))
+ [Adafruit PiOLED 128x32 Display](https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage)

<br></br>
| Close-up of the assembled device (see the PiOLED at the top left)   |
| :-------------: | 
| [![](https://i.imgur.com/EokJJlH.jpg?raw=true)](https://i.imgur.com/EokJJlH.jpg)   |   
<br></br>

## Setup
These instructions assume your KaliPi is assembled and "ready to go".
1. Update/Upgrade your KaliPi: `sudo apt-get update && sudo apt-get upgrade -y`
2. Install software:
```
sudo apt-get install python3-pip
sudo pip3 install adafruit-circuitpython-ssd1306
sudo apt-get install python3-pil
sudo pip install getmac
```
3. Edit/add the following lines in the config file (`sudo nano /boot/config.txt`) and save it in order to enable I2C and change the I2C core frequency to 100 kHz:
```python
dtparam=i2c_arm=on
dtparam=i2c_baudrate=100000
```
4. Add the following line to /etc/modules (`sudo nano /etc/modules`) and save the file:
```python
i2c-dev
```
5. Reboot the device and test I2C functionality by entering `sudo i2cdetect -y 1`. If said command returns the following output, I2C is working as intended.
<p align="center">
  <img class="74057-asset img-responsive" srcset="https://cdn-learn.adafruit.com/assets/assets/000/074/057/medium260/adafruit_products_i2c.png?1554480832 260w, https://cdn-learn.adafruit.com/assets/assets/000/074/057/medium640/adafruit_products_i2c.png?1554480832 640w, https://cdn-learn.adafruit.com/assets/assets/000/074/057/medium800/adafruit_products_i2c.png?1554480832 800w, https://cdn-learn.adafruit.com/assets/assets/000/074/057/large1024/adafruit_products_i2c.png?1554480832 1024w" sizes="(max-width: 768px) 100vw, (max-width: 1024px) 65vw, (max-width: 1365px) 47vw, 750px" src="https://cdn-learn.adafruit.com/assets/assets/000/074/057/medium800/adafruit_products_i2c.png?1554480832" alt="adafruit_products_i2c.png">
</p>

6. Copy `minidisplay.py` and the `visitor.ttf` font to your device, preferably into a new folder.
7. Make the script execute on bootup. One way of achieving this is adding these lines to /etc/rc.local (`sudo nano /etc/rc.local`):
```python
sudo python3 /var/minidisplay/minidisplay.py &
exit 0
```
8. After that, add the permission to execute rc.local by entering `sudo chmod +x /etc/rc.local`.
9. Reboot. You're done.

<br></br>
