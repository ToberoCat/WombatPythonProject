from threading import Timer
from typing import Protocol


class IStopable(Protocol):
    def stop(self):
        """
        Stop the stopable procedure
        :return: Nothing
        """
        pass


class RepeatedTimer:
    def __init__(self, interval: float, function, *args, **kwargs):
        """
        Create a new repeating timer
        :param interval: The interval the task should be executed at. Should be defined in seconds
        :param function: The function that gets executed
        :param args: The args to pass into the function
        :param kwargs: The dictionary-like args that should be passed to the function
        """
        self._timer = None
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.is_running = False
        self.__start()

    def __run(self):
        self.is_running = False
        self.__start()
        self.function(*self.args, **self.kwargs)

    def __start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self.__run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        """
        Stop the stopable procedure
        :return: Nothing
        """
        self._timer.cancel()
        self.is_running = False


class ScheduledTimer:
    def __init__(self, delay, function, *args, **kwargs):
        """
        Create a new scheduled timer. The given function will be executed after given delay only one.
        It creates a new thread, therefore isn't blocking the thread it got called in

        :param delay: The delay the function should wait before executing. Should be defined in seconds
        :param function: The function that get executed
        :param args: The args to pass into the function
        :param kwargs: The dictionary-like args that should be passed to the function
        """
        self._timer = None
        self.delay = delay
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.__start()

    def __start(self):
        self._timer = Timer(self.delay, self.__run)
        self._timer.start()

    def stop(self):
        """
        Stop the stopable procedure
        :return: Nothing
        """
        self._timer.cancel()

    def __run(self):
        self.function(*self.args, **self.kwargs)
