from abc import abstractmethod


class BaseRobotComponent:
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