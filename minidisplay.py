# Import libraries for...
# ...timing stuff
import time
import subprocess
# ...MAC address extraction
from getmac import get_mac_address as gma
# ...the display
from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Create the I2C interface
i2c = busio.I2C(SCL, SDA)

# Create the SSD1306 OLED class
disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear display
disp.fill(0)
disp.show()

# Create blank image for drawing (1-bit color)
width = disp.width
height = disp.height
image = Image.new("1", (width, height))

# Get drawing object to draw on image
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image
draw.rectangle((0, 0, width, height), outline=0, fill=0)

# Define some constants to allow easy resizing of shapes
padding = -2
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes
x = 0

# Load font (has to be in the same directory as minidisplay.py)
font = ImageFont.truetype('/var/minidisplay/visitor.ttf', 14)

# Alternatively load the default font with "font = ImageFont.load_default()"
# Some other fonts can be found here: http://www.dafont.com/bitmap.php

while True:
    # Draw a black filled box to clear the image
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Get monitoring data
    mac = gma()
    # Monitoring scripts are from here: https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d' ' -f1"
    IP = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "hostname | cut -d' ' -f1"
    hostname = subprocess.check_output(cmd, shell=True).decode("utf-8")

    # Write text
    draw.text((x, top + 0), "Name: " + hostname, font=font, fill=255)
    draw.text((x, top + 12), "IP: " + IP, font=font, fill=255)
    draw.text((x, top + 24), "(" + mac + ")", font=font, fill=255)

    # Display image
    disp.image(image)
    disp.show()
    time.sleep(10)
