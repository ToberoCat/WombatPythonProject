from src.ecer.dll.DLL import KIPR


def magneto_calibrate() -> bool:
    """
    Initiates a calibration of the magnetometer
    :return: 1: success 0: failure
    """
    return KIPR.magneto_calibrate()


def magneto_x() -> int:
    """
    Gets the sensed x magneto value
    :return: The latest signed x magneto value
    """
    return KIPR.magneto_x()


def magneto_y() -> int:
    """
    Gets the sensed y magneto value
    :return:
    """
    return KIPR.magneto_y()


def magneto_z() -> int:
    """
    Gets the sensed z magneto value
    :return:
    """
    return KIPR.magneto_z()