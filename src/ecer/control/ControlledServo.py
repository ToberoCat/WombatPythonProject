from src.ecer.hardware import Servo


class ControlledServo:
    def __init__(self, port: int, servo_min, servo_max):
        self.port = port
        self.min = servo_min
        self.max_without_min = servo_max - servo_min

        Servo.enable_servo(port)
        self.set(0)

    def set(self, rotation):
        Servo.set_servo(self.port, int(rotation * self.max_without_min + self.min))
