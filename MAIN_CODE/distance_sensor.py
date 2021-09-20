# distance sensor for feed bin

import RPi.GPIO as GPIO
import time


# if distance < 5:
#     print("100% FULL")
# elif distance < 15:
#     print("75% FULL")
# elif distance < 25:
#     print("50% FULL")
# else:
#     print("LESS THAN 25% FULL - REFILL HOPPER")

def get_hopper_level():
    GPIO.setmode(GPIO.BCM) # use GPIO pin numbers

    TRIG = 16
    ECHO = 25

    print ("Distance Measurement In Progress")

    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG, False) # set trigger pin to LOW
    print ("Waiting For Sensor To Settle")
    time.sleep(2) # slight delay


    # pulse to trigger pin
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start

    # distance calculation (cm)
    distance = pulse_duration * 17150
    if (distance >= 30.12):
        percentage = 0 # refill machine
    else:
        percentage = (30.12 - distance/30.12) * 100 # 30.12 is determined based on when the feeder has BackPressure
    distance = round(distance, 2) # round to 2 decimal places


    print ("Current Distance:",distance," cm")
    time.sleep(2)
    GPIO.cleanup()
    return percentage

if __name__ == "__main__":
    main()