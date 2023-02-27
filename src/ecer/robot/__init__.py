import time
from abc import abstractmethod
from typing import TypeVar, Type

from src.ecer.Utils import IStopable
from src.ecer.dll.DLL import KIPR
from src.ecer.hyperparams import Hyperparams
from src.ecer.robot.Components import BaseRobotComponent

TPS_TO_CM_D = 6.25 - 125 / 24
C = TypeVar('C', bound=BaseRobotComponent)


def approximate_travel_time(traverse_velocity: int, distance: float):
    """
    Approximate the time it will take the robot to travel a given distance at given velocity

    :param traverse_velocity: The avg velocity the robot will be moving at. Should range from ]0;1500]
    :param distance: The distance it should cover
    :return: The time in seconds it will take the robot to pass this section
    """
    return distance / (1 / 96 * traverse_velocity + TPS_TO_CM_D)


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
        self.__threads = []
        self.enabled_components = []

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

    def all_setup(self) -> None:
        pass

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

    def add_component(self, component: C) -> None:
        """
        Add a component to the general event loop
        :param component: The component you want to add
        :return: Nothing
        """
        component.robot = self
        component.enable()
        self.__components.append(component)

    def get_component(self, component_type: Type[C]) -> C:
        """
        Receive a component from the specified type when one got registered
        :param component_type: Type of component
        :return: The component. None if no component was found
        """
        for component in self.__components:
            if type(component) == component_type:
                return component

    def register_thread(self, thread: IStopable):
        """
        Register a thread that automatically shutdowns with the robot
        :param thread:
        :return:
        """
        self.__threads.append(thread)

    def __schedule_loop(self):
        self.setup()
        for component in self.__components:
            component.setup()

        self.all_setup()
        last = time.time()
        ends_at = last + self.__shutdown_in_nano
        try:
            while last < ends_at:
                current = time.time()
                delta = current - last

                self.loop(delta)
                for component in self.enabled_components:
                    component.loop(delta)

                last = current
        finally:
            for thread in self.__threads:
                thread.stop()

            for component in self.enabled_components:
                component.shutdown()
            self.shutdown()
