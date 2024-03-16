import RPi.GPIO as GPIO
import time

# Use GPIO numbers not pin numbers
GPIO.setmode(GPIO.BCM)

# Pin to use for the output
pin = 15

# Set up the GPIO pin as an output
GPIO.setup(pin, GPIO.OUT)

try:
    while True:
        # Set the pin high
        GPIO.output(pin, GPIO.HIGH)
        print("Pin set to high.")
        time.sleep(1)  # Wait for 1 second

        # Set the pin low
        GPIO.output(pin, GPIO.LOW)
        print("Pin set to low.")
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Clean up GPIO on CTRL+C exit
    GPIO.cleanup()

GPIO.cleanup()  # Clean up GPIO on normal exit
