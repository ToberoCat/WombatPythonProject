from src.ecer.hardware import Servo

HEIGHT_SERVO_PORT = 1
CLAW_SERVO_PORT = 0
HORIZONTAL_HEIGHT = 1500


class Claw:
    def __init__(self, port: int):
        self.port = port
        Servo.enable_servo(self.port)

    def close_claw(self):
        Servo.set_servo(self.port, 637)

    def open_claw(self):
        Servo.set_servo(self.port, 0)


class LiftArm:
    def __init__(self, port: int):
        self.port = port
        Servo.enable_servo(self.port)

    def lift(self, amount: int):
        val = Servo.get_position(self.port) + amount
        Servo.set_servo(self.port, val)

    def lower(self, amount: int):
        val = Servo.get_position(self.port) - amount
        Servo.set_servo(self.port, val)

    def set(self, amount: int):
        Servo.set_servo(self.port, amount)

    def horizontal(self):
        Servo.set_servo(self.port, HORIZONTAL_HEIGHT)