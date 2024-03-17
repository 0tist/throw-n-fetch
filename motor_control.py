import pigpio
import time

servoPIN = 4
pi = pigpio.pi()  # Connect to local Pi.

try:
    while True:
        pi.set_servo_pulsewidth(servoPIN, 500)  # Small pulse for one direction
        time.sleep(0.5)
        pi.set_servo_pulsewidth(servoPIN, 1500)  # Medium pulse for neutral position
        time.sleep(0.5)
        pi.set_servo_pulsewidth(servoPIN, 2500)  # Large pulse for the other direction
        time.sleep(0.5)
finally:
    pi.set_servo_pulsewidth(servoPIN, 0)  # Turn off pulse
    pi.stop()
