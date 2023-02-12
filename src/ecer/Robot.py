from abc import abstractmethod
from src.ecer.hyperparams import Hyperparams
from src.ecer.dll.DLL import KIPR
from time import time_ns


class AbstractRobot:
    def __init__(self, resource_path: str, shutdown_in: float = 115.0):
        """
        Creates a new robot
        :param resource_path: The path where resources are located
        :param shutdown_in: The time the robot should shut down automatically. Defaults to 115 seconds.
                            It's recommended to set it a little below the time you have until the robot should stop to
                            prevent disqualification due to inaccurate measurements.
        """
        self.__shutdown_in_nano = shutdown_in * 1e9

        Hyperparams.initialise(resource_path)
        KIPR.shut_down_in(shutdown_in)
        self.__schedule_loop()

    @abstractmethod
    def setup(self) -> None:
        """
        Gets called before the looping starts
        It's not recommended to start any new threads unless you carefully take care of them

        :return: Nothing
        """
        pass

    @abstractmethod
    def loop(self) -> None:
        """
        Gets called as many times as possible until the robot has to shut down.
        It's not recommended to start any new threads unless you carefully take care of them.
        Don't run heavy tasks like (almost) endless loops or any blocking delays. If you do it may result in the robot
        shutting down in time.

        :return: Nothing
        """
        pass

    def shutdown(self) -> None:
        """
        Gets called when the robot shuts down
        :return: Nothing
        """
        pass

    def __schedule_loop(self):
        self.setup()
        ends_at = time_ns() + self.__shutdown_in_nano
        try:
            while time_ns() >= ends_at:
                self.loop()
        finally:
            self.shutdown()
