# noise detection using audio sensor

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM) # use GPIO pin numbers
sound = 8
GPIO.setup(sound, GPIO.IN) # setup GPIO pin as input

# buffer for false alarms if needer
#time.sleep(20)
def noise_detect():
    cnt = 0
    while True:
        if GPIO.input(sound):
            cnt = cnt + 1
            print("sound detected " + str(cnt))
            subprocess.run("pkill -9 -f motion_detection.py", shell=True)
            call(["python3", "picam.py"])
            # do something

noise_detect()