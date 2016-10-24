# Robotic LED Emotion
A software framework for robotic emotions expressed by NeoPixel LEDs.

# Installation
Install rpi_ws281x first.
Refer to https://learn.adafruit.com/neopixels-on-raspberry-pi/software
```
sudo apt-get update
sudo apt-get install build-essential python-dev git scons swig
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python setup.py install
```