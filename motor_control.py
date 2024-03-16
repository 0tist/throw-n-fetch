import pigpio

# Connect to the pigpio daemon
pi = pigpio.pi()

# Set GPIO pin connected to the motor as an output
motor_pin = 4
pi.set_mode(motor_pin, pigpio.OUTPUT)

# Set PWM frequency (optional, default is 800 Hz)
pi.set_PWM_frequency(motor_pin, 1000)  # Set PWM frequency to 1000 Hz

# Set PWM duty cycle (0-1000)
duty_cycle = 500  # Example duty cycle
pi.set_PWM_dutycycle(motor_pin, duty_cycle)

# To stop the motor:
# pi.set_PWM_dutycycle(motor_pin, 0)

# Disconnect from the pigpio daemon when done
pi.stop()
