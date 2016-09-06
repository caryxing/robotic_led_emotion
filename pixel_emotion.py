#!/usr/bin/python
# A Library that drives the LEDs with reading specs from
# a set of JSON files, using neopixel library

import time
import json
from neopixel import *
from threading import Thread
import threading

# LED strip configuration:
LED_COUNT   = 12      # Number of LED pixels.
LED_PIN     = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA     = 5       # DMA channel to use for generating signal (try 5)
LED_INVERT  = False   # True to invert the signal (when using NPN transistor level shift)
LED_BRIGHTNESS = 255

EMOTION_FILE_LIST_PATH = "emotions.list"

class RobotEmot():
    def __init__(self):
        self.emotFileList = []
        self.emotBank = {}
        self.ledThread = None
        self.loadEmotList()
        self.loadEmotBank()
        self.ledThreadStop = threading.Event()
        self.strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
        self.strip.begin()
                                        

    def loadEmotList(self):
        with open(EMOTION_FILE_LIST_PATH, 'r') as emotList:
            for emotFileName in emotList:
                emotFileName = emotFileName[:-1]
                self.emotFileList.append(emotFileName)

                
    def loadEmotBank(self):
        for emotFile in self.emotFileList:
            with open(emotFile, 'r') as inputFile:
                emotion = json.load(inputFile)
                self.emotBank[emotion["name"]] = {"repeat": emotion["repeat"], "scene": emotion["scene"]}
                print("Emotion [%s] is loaded from %s." % (emotion["name"], emotFile))
                

    def offAll(self):
        for led in xrange(LED_COUNT):
            self.strip.setPixelColor(led, Color(0, 0, 0))

    def ledBlue(self, leds):
        for led in leds:
            self.strip.setPixelColor(led-1, Color(0, 0, 127))

    def ledRed(self, leds):
        for led in leds:
            self.strip.setPixelColor(led-1, Color(0, 127, 0))

    def ledGreen(self, leds):
        for led in leds:
            self.strip.setPixelColor(led-1, Color(127, 0, 0))

    def ledYellow(self, leds):
        for led in leds:
            self.strip.setPixelColor(led-1, Color(127, 127, 0))

    def ledWhite(self, leds):
        for led in leds:
            self.strip.setPixelColor(led-1, Color(127, 127, 127))

    def setEmotion(self, emotionCat, degree, block=False):
        if not block:
            if self.ledThread:
                self.ledThreadStop.set()
                self.ledThread.join()
                
            self.ledThreadStop.clear()
            self.ledThread = Thread(target=self.setEmotion_in, args=(emotionCat, degree, self.ledThreadStop))
            self.ledThread.start()
        else:
            self.setEmotion_in(emotionCat, degree)    
        
    def setEmotion_in(self, emotionCat, degree, stop=None):
        emotionName = emotionCat + '-' + str(degree)
        emotion = self.emotBank.get(emotionName, None)
        if not emotion:
            return False
        
        repeat = emotion["repeat"]
        scenes = emotion["scene"]
        for i in xrange(repeat):
            for scene in scenes:
                if stop and stop.is_set():
                    return
                self.offAll()
                self.ledBlue(scene.get("blue", []))
                self.ledRed(scene.get("red", []))
                self.ledGreen(scene.get("green", []))
                self.ledYellow(scene.get("yellow", []))
                self.ledWhite(scene.get("white", []))
                time.sleep(scene["last"]/float(1000))
                self.strip.show()
