#!/bin/bash

sudo apt-get -y install python3 python3-dev python3-pip

pip3 install pygame
pip3 install numpy
pip3 install rpi_ws281x adafruit-circuitpython-neopixel
pip3 install evdev

#python3.7 -m pip install numpy
#python3.7 -m pip install pygame
#python3.7 -m pip install rpi_ws281x adafruit-circuitpython-neopixel
#python3.7 -m pip install evdev