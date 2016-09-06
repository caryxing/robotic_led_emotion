#
import sys
from pixel_emotion import RobotEmot

if __name__ == "__main__":
    ledEmotion = RobotEmot()
    ledEmotion.setEmotion(sys.argv[1], int(sys.argv[2]))

