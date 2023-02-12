from src.ecer.dll.DLL import KIPR


def analog(port: int) -> int:
    """
    Gets the 12-bit analog value of a port.
    :param port:[in] port A value
     between 0 and 5 specifying
    the sensor to read from.
    :return:The latest 12-bit value of
    the port (a value in the range 0 to 4095).
    """
    return KIPR.analog(port)


def analog10(port: int) -> int:
    """
    Gets the 10-bit analog value of a port.
    :param port:[in] port A value between 0 and 5
    specifying the sensor to read from.
    :return:The latest 10-bit value of the port
     (a value in the range 0 to 1023).
    """
    return KIPR.analog10(port)


def analog8(port: int) -> int:
    """
    Gets the 8-bit analog value of a port.
    :param port:[in] port A value between 0 and 5 specifying
     the sensor to read from.
    :return:The latest 8-bit value of the port
    (a value in the range 0 to 255).
    """
    return KIPR.analog8(port)


def analog_et(port: int) -> int:
    """
    Gets the 10-bit analog value of an ET sensor on the given port.
    :param port:[in] port A value between 0 and 7 specifying
     the ET sensor to read from.
    :return:The latest 10-bit value of the port
     (a value in the range 0 to 1023).
    """
    return KIPR.analog_et(port)


def get_analog_pullup(port: int) -> str:
    """
    Gets the analog pullup status for one portt.
    :param port:[in] port A value between 0 and 7 specifying
     the analog sensor to read from.
    :return:The status of the analog pullup on the specified port
    """
    return KIPR.get_analog_pullup(port)


def set_analog_pullup(port: int, pullup: int):
    """
    Sets analog pullup status for one port.
    :param port:[in] port A value between 0 and 5
     specifying the analog sensor to read from.
    :param pullup:[in] pullup A value of 0 (inactive) or 1 (active).
    """
    KIPR.set_analog_pullup(port, pullup)
