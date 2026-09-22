import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 200)
k = 0.0
pwm.start(k)
 
try:
    while True:
        pwm.ChangeDutyCycle(k)
        time.sleep(0.05)
        k += 1.0
        if k > 100.0:
            k = 0.0
except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()