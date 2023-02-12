

from src.ecer.dll.DLL import KIPR


def digital(port: int):
    return KIPR.digital(port)


def get_output(port: int) -> bool:
    """
    Gets the current digital mode

    :param port:The port ID the motor is plugged into

    :return:1 for output mode, 0 for input mode
    """
    return KIPR.digital(port) == 1


def get_pullup(port: int) -> bool:
    """
    Gets the current digital pullup state

    :param port:The port ID the motor is plugged into
    :return:1 for active, 0 for inactive
    """
    return KIPR.get_digital_pullup(port) == 1

def get_value(port: int) -> int:
    """
    Gets the current value of the digital port.

    :param port: The port ID the motor is plugged into
    :return:Gets the current value of the digital port.
    """

    return KIPR.get_digital_value(port)


def set_output(port: int, out: int):
    """
    Sets the digital mode.

    :param port:The port to modify.
    :param out:1 for output mode, 0 for input mode.
    """
    KIPR.set_output(port)
    KIPR.set_output(out)



def set_pullup(port: int, pullup: int):
    """
    Sets the current digital pullup state

    :param port:The port to modify
    :param pullup:	The pullup state 1: active 0: inactive

    """
    KIPR.set_output(port)
    KIPR.set_output(pullup)


def set_value(port: int, value: int):
    """
    Sets the value of the digital port in output mode.

    :param port:The port to modify
    :param value:The value that you want

    """
    KIPR.set_output(port)
    KIPR.set_output(value)
