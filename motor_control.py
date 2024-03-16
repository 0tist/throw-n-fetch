from gpiozero import Servo
from time import sleep

# Setup the servo on GPIO18
servo = Servo(15)

try:
    while True:
        # Move the servo to the 0 degree position (neutral)
        servo.mid()
        print("Servo neutral position")
        sleep(1)

        # Move the servo to the -90 degree position (maximum backward)
        servo.min()
        print("Servo maximum backward position")
        sleep(1)

        # Move the servo to the +90 degree position (maximum forward)
        servo.max()
        print("Servo maximum forward position")
        sleep(1)

except KeyboardInterrupt:
    print("Program exited")
