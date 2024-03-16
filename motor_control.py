import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Motor pins (replace with your GPIO pins)
pinForward = 23
pinBackward = 24

# Set up the motor pins
GPIO.setup(pinForward, GPIO.OUT)
GPIO.setup(pinBackward, GPIO.OUT)


# Function to control motor direction
def motor_forward():
    GPIO.output(pinForward, GPIO.HIGH)
    GPIO.output(pinBackward, GPIO.LOW)


def motor_backward():
    GPIO.output(pinForward, GPIO.LOW)
    GPIO.output(pinBackward, GPIO.HIGH)


def motor_stop():
    GPIO.output(pinForward, GPIO.LOW)
    GPIO.output(pinBackward, GPIO.LOW)


try:
    while True:
        motor_forward()
        time.sleep(5)  # Motor runs forward for 5 seconds
        motor_stop()
        time.sleep(1)  # Motor stops for 1 second
        motor_backward()
        time.sleep(5)  # Motor runs backward for 5 seconds
        motor_stop()
        time.sleep(1)  # Motor stops for 1 second
finally:
    GPIO.cleanup()  # Clean up the GPIO pins on exit
