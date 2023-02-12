from src.ecer.hardware.Motor import move_at_velocity


class Mover:
    def __init__(self, left_motor, right_motor):
        self.left_motor = left_motor
        self.right_motor = right_motor

    def move_forward(self, amount: int):
        move_at_velocity(self.left_motor, -amount)
        move_at_velocity(self.right_motor, amount)

    def move_backward(self, amount: int):
        move_at_velocity(self.left_motor, amount)
        move_at_velocity(self.right_motor, amount)

    def move_curve(self, amount: int):
        move_at_velocity(self.left_motor, amount)
        move_at_velocity(self.right_motor, -amount)

    def reset_motor(self):
        move_at_velocity(self.left_motor, 0)
        move_at_velocity(self.right_motor, 0)
