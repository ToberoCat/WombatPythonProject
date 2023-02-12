from src.ecer.dll.DLL import KIPR


def calibrate() -> bool:
    """
    Not Yet Implemented
    :return:1: success 0: failure
    """
    return KIPR.gyro_calibrate() == 1


def gyro_x() -> int:
    """
    Gets the sensed x rotation
    :return:The latest signed x rotation value
    """
    return KIPR.gyro_x()


def gyro_y() -> int:
    """
    Gets the sensed y rotation
    :return:The latest signed y rotation value
    """
    return KIPR.gyro_y()


def gyro_z() -> int:
    """
    Gets the sensed z rotation
    :return:The latest signed z rotation value
    """
    return KIPR.gyro_z()