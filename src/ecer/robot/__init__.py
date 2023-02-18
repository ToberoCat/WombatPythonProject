import time
from abc import abstractmethod

from src.ecer.dll.DLL import KIPR
from src.ecer.hyperparams import Hyperparams
from src.ecer.robot.Components import BaseRobotComponent


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
        self.__components = []

        Hyperparams.initialise(resource_path)
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
    def loop(self, delta_time: float) -> None:
        """
        Gets called as many times as possible until the robot has to shut down.
        It's not recommended to start any new threads unless you carefully take care of them.
        Don't run heavy tasks like (almost) endless loops or any blocking delays. If you do it may result in the robot
        shutting down in time.

        :param delta_time: The time between two loop calls
        :return: Nothing
        """
        pass

    def shutdown(self) -> None:
        """
        Gets called when the robot shuts down
        :return: Nothing
        """
        pass

    def add_component(self, component: BaseRobotComponent) -> None:
        """
        Add a component to the general event loop
        :param component: The component you want to add
        :return: Nothing
        """
        self.__components.append(component)

    def __schedule_loop(self):
        self.setup()
        for component in self.__components:
            component.setup()

        last = time.time()
        ends_at = last + self.__shutdown_in_nano
        try:
            while last < ends_at:
                current = time.time()
                delta = current - last

                self.loop(delta)
                for component in self.__components:
                    component.loop(delta)

                last = current
        finally:
            for component in self.__components:
                component.shutdown()
            self.shutdown()
