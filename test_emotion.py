#
import sys
from pixel_emotion import RobotEmot
import time

if __name__ == "__main__":
    ledEmotion = RobotEmot()
    ledEmotion.setEmotion(sys.argv[1], int(sys.argv[2]), block=True)

