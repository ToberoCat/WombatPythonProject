from src.ecer.dll.DLL import KIPR


def calibrate_compass():
    """
    Begin calibrating the compass.
    Will display the calibration parameter results which can be used in the future with set_compass_params
    """
    KIPR.calibrate_compass()

# todo get_compass_angle() schreiben hat void


def set_compass_params(meanX: float, meanY: float, w1: float, w2: float, div_E1: float, div_E2: float):
    """
    Set the compass parameters based on a previous calibration.
    :param meanX: a value provided by calibrate_compass
    :param meanY: a value provided by calibrate_compass
    :param w1: a value provided by calibrate_compass
    :param w2: a value provided by calibrate_compass
    :param div_E1: a value provided by calibrate_compass
    :param div_E2: a value provided by calibrate_compass
    """
    KIPR.set_compass_params(meanX, meanY, w1, w2, div_E1, div_E2)