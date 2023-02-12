from src.ecer.dll.DLL import KIPR

def battery_charging() -> bool:
    """
    Whether the battery is charging
    :return: 0: not charging 1: charging
    """
    return KIPR.battery_charging() == 1


def power_level() -> float:
    """
    The device's power level
    :return: The device's current battery capacity 0: 0% 1: 100%
    """
    return KIPR.power_level()


def power_level_life() -> float:
    """
    The device's power level (LiFePO4 chemistry)
    :return: The device's current battery capacity 0: 0% 1: 100%
    """
    return  KIPR.power_level_life()


def power_level_lipo() -> float:
    """
    The device's power level (LiPo chemistry)
    :return: The device's current battery capacity 0: 0% 1: 100%
    """
    return KIPR.power_level_lipo()


def power_level_nimh() -> float:
    """
    The device's power level (NiMH chemistry)
    :return: The device's current battery capacity 0: 0% 1: 100%
    """
    return KIPR.power_level_nimh()