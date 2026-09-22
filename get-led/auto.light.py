import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26  
photo = 6 
 
GPIO.setup(led, GPIO.OUT) 
GPIO.setup(photo, GPIO.IN)
period = 1.0
 
try:
    while True:
        state = GPIO.input(photo)
        GPIO.output(led, not state)
        time.sleep(period)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()