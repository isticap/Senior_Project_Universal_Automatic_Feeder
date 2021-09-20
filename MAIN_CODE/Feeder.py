# this file contains functions to control the feeder
import picam
import subprocess
import time
import guli

import os
from multiprocessing import Pool

# calling the record function will start a 10 second recording of video and audio
def record():
    picam.main()

# calling the motion detection function with start motion detection
def motion_detection():
    print("motion detection started")
    # subprocess.call(["python3", "motion_detection.py"])
    subprocess.run("python3 motion_detection.py &", shell=True)

# calling the noise detection function will start noise detection
def noise_detection():
    print("noise detection started")
    # subprocess.call(["python3", "noise_detection.py"])
    subprocess.run("python3 noise_detection.py &", shell=True)

# calling the distance detection function will return the current fill level of the hopper
def distance_detection():
    print("checking hopper fill level")
    subprocess.call(["python3", "distance_sensor.py"])

# calling the noise and motion detection function will start motion detection and noise detection in parallel
def noise_and_motion_detection():
    subprocess.run("python3 motion_detection.py & python3 noise_detection.py", shell=True)

# noise and motion function forever
def noise_and_motion_forever():
    guli.GuliVariable("var").setValue(5)
    while True:
        if guli.GuliVariable("var").get() == 5:
            noise_and_motion_detection()
            guli.GuliVariable("var").setValue(0)
        time.sleep(2)

# motion detection forever
def motion_forever():
    guli.GuliVariable("var").setValue(5)
    while True:
        if guli.GuliVariable("var").get() == 5:
            motion_detection()
            guli.GuliVariable("var").setValue(0)
        time.sleep(2)

# noise detection forever
def noise_forever():
    guli.GuliVariable("var").setValue(5)
    while True:
        if guli.GuliVariable("var").get() == 5:
            noise_detection()
            guli.GuliVariable("var").setValue(0)
        time.sleep(2)

# process killer function
def kill_processes():
    subprocess.run("pkill -9 -f noise_detection.py", shell=True)
    subprocess.run("pkill -9 -f motion_detection.py", shell=True)

# def main():
#    return 0

if __name__ == "__main__":