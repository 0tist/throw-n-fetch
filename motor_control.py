import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

try:
    while True:
        # Generate a PWM signal manually
        GPIO.output(17, True)
        time.sleep(0.0015)  # Adjust the sleep time for the correct servo angle
        GPIO.output(17, False)
        time.sleep(0.02)  # Complete the cycle
finally:
    GPIO.cleanup()
