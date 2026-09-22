import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 5  
photo = 6 
 
GPIO.setup(LED_PIN, GPIO.OUT) 
GPIO.setup(PHOTO_PIN, GPIO.IN)
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