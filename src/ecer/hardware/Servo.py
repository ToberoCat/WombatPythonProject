from src.ecer.dll.DLL import KIPR


def set_servo(port: int, rotation: int):
    """
        Set a new servo goal position.

        Parameters
        port	The port of the servo
        rotation	The new servo position, between 0 and 2047

    """
    KIPR.set_servo_position(port, rotation)


def enable_servo(port: int):
    """
    Enable a specific servo.

    :param port: The port, between 0 and 3, to enable
    """
    KIPR.enable_servo(port)


def disable_servos(port: int):
    """Disable all four servo channels."""
    KIPR.disable_servos(port)


def disable_servo(port: int):
    """
    Disable a specific servo.
    :param port:The port, between 0 and 3, to enable

    """
    KIPR.disable_servo(port)


def enable_servos(port: int):
    """Enable all four servo channels."""
    KIPR.enable_servos(port)


def get_position(port: int) -> int:
    """
    Get the most recent commanded servo position.
    :param port: The port of the servo
    :return: 's last position as an 11 bit integer (which is an integer between 0 and 2047)
    """
    return KIPR.get_servo_position(port)


def get_enabled(port: int):
    """
    Check if a servo is enabled.
    :param port: The port, between 0 and 3
    :return: The servo enable setting 0: disabled 1: enabled
    """
    KIPR.get_servo_enabled(port)


def set_enabled(port: int, enabeld: int):
    """
    Enable or disable a specific servo.
    :param port:    The port, between 0 and 3, to enable
    :param enabeld: The new enable setting 0: disabled 1: enabled
    """
    KIPR.set_servo_enabled(port, enabeld)


def set_position(port: int, position: int):
    """
    Set a new servo goal position.
    :param port: 	The port of the servo
    :param position: The new servo position, between 0 and 2047
    """
    KIPR.set_servo_position(port, position)
