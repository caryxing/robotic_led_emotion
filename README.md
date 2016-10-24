# Robotic LED Emotion
A software framework for robotic emotions expressed by NeoPixel LEDs.

# Installation
## Install rpi_ws281x first.
Refer to https://learn.adafruit.com/neopixels-on-raspberry-pi/software
```
sudo apt-get install build-essential python-dev git scons swig
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python setup.py install
```

## Download all the files in the project
```
git clone https://github.com/caryxing/robotic_led_emotion
```

## Run example codes
```
cd robotic_led_emotion
sudo python example.py
```
The example codes will run "happy" in level 1.

# Add a new emotion
* Add a new JSON file to describe the new emotion under the folder emotions/.
* Add the path to the new emotion to emotions.list file.
