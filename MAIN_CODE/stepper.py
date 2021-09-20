import time 
import RPi.GPIO as GPIO

# This code snippet is for Version 1.2 

# import the library
from RpiMotorLib import RpiMotorLib
    
GpioPins = [18, 17, 27, 22]
#GpioPins = [23, 24, 10, 9]

# Declare an named instance of class pass a name and type of motor
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "Nema")
time.sleep(0.5)

# call the function pass the parameters
# motor_run(GPIOPins, wait, steps, counterclockwise, verbose, steptype, initdelay)
mymotortest.motor_run(GpioPins , 0.001, 5000, False, False, "half", .05)

# good practise to cleanup GPIO at some point before exit
GPIO.cleanup()