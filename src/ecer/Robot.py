from abc import abstractmethod
from src.ecer.hyperparams import Hyperparams
from src.ecer.dll.DLL import KIPR
import time


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
        self.__scheduled = []

        Hyperparams.RESOURCE_PATH = resource_path
        KIPR.shut_down_in(int(shutdown_in))
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

    def repeat_every_interval(self, ticks: int, callback: classmethod) -> None:
        """
        Schedule a repeating task.
        :param ticks: The ticks that should pass between the execution
        :param callback: The method that should get run
        :return: Nothing
        """
        self.__scheduled.append((ticks, callback))

    def __schedule_loop(self):
        self.setup()
        ends_at = time.time() + self.__shutdown_in_nano
        try:
            tick = 0
            while time.time() < ends_at:
                tick += 1
                for task in self.__scheduled:
                    if tick % task[0] == 0:
                        task[1]()
                self.loop()
        finally:
            self.shutdown()
