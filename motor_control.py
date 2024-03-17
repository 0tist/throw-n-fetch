import RPi.GPIO as GPIO
import time

servoPIN = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

pwm = GPIO.PWM(servoPIN, 50)  # GPIO 4 for PWM with 50Hz
pwm.start(0)  # Initialization

try:
    while True:
        pwm.ChangeDutyCycle(2.5)  # Turn towards 0 degree
        time.sleep(0.5)
        pwm.ChangeDutyCycle(7.5)  # Turn towards 90 degree
        time.sleep(0.5)
        pwm.ChangeDutyCycle(12.5)  # Turn towards 180 degree
        time.sleep(0.5)
finally:
    pwm.stop()
    GPIO.cleanup()
