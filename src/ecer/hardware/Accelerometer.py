from src.ecer.dll.DLL import KIPR


def accel_calibrate() -> bool:
    """
    Initiates a calibration of the accelerometer

    :return:1: success 0: failure
    """
    return KIPR.accel_calibrate() == 1


def accel_x() -> int:
    """
    Gets the sensed x acceleration
    \description +/- 2G range, 1024 per G
    \description This should be approximately
    0 when at rest and flat on a table.

    :return:The latest signed x acceleration value
    """
    return KIPR.accel_x()


def accel_y() -> int:
    """
    Gets the sensed y acceleration
     \description +/- 2G range, 1024 per G \description
     This should be approximately 0
    when at rest and flat on a table.

    :return:The latest signed y acceleration value
    """
    return KIPR.accel_y()


def accel_z() -> int:
    """
    Gets the sensed z acceleration
    \description +/- 2G range, 1024 per G \description
     This should be approximately -1024
     when at rest and flat on a table.

    :return:The latest signed z acceleration value
    """
    return KIPR.accel_z()
