from gpiozero import Servo
from time import sleep

servo = Servo(4)  # GPIO pin 17

while True:
    servo.min()  # Move servo to minimum position
    sleep(1)
    servo.mid()  # Move servo to middle position
    sleep(1)
    servo.max()  # Move servo to maximum position
    sleep(1)
