import RPi.GPIO as GPIO
import time

SERVO_PIN = 10


class BenderEyes:
    def __init__(self):
        self.duty_cycle = 7.5     # Should be the centre for a SG90

        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SERVO_PIN, GPIO.OUT)

        # Create PWM channel on the servo pin with a frequency of 100Hz
        self.pwm_servo = GPIO.PWM(SERVO_PIN, 50)
        self.pwm_servo.start(self.duty_cycle)

    def move(self, val):
        self.pwm_servo.ChangeDutyCycle(val)
        # self.pwm_servo.ChangeDutyCycle(val)

    def cleanup(self):
        self.pwm_servo.stop()
