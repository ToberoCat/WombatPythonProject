import random

from src.ecer.Robot import AbstractRobot
from src.ecer.control.Movement import Mover
from src.ecer.hyperparams.Hyperparams import get_hyperparameters

class ExampleRobot(AbstractRobot):
    def __init__(self):
        super().__init__("path/to/res/folder", 117)  # Sets the path to the resources folder and the seconds until the
        # robot has to be shutdown
        self.general_settings = get_hyperparameters("general-settings") # Reads in the hyperparameter file
        self.mover = Mover(
            self.general_settings.get_int("left-motor"),
            self.general_settings.get_int("right-motor")
        )  # Creates a new motor mover

    def setup(self) -> None:
        self.mover.move_forward(1000)  # Set the motors moving forward as long as you don't change their velocity

    def loop(self) -> None:
        if random.randint(0, 100) == 50:  # Let the robot make a curve randomly
            self.mover.move_curve(50)

    def shutdown(self) -> None:
        self.mover.reset_motor()  # Cleanup everything you used in the shutdown method


if __name__ == "__main__":
    ExampleRobot()
