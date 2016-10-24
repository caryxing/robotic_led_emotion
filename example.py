#
import sys
from pixel_emotion import RobotEmot

if __name__ == "__main__":
    ledEmotion = RobotEmot()
    ledEmotion.setEmotion("happy", 1)
