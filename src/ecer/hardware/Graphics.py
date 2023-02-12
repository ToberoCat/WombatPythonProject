from src.ecer.dll.DLL import KIPR

# todo enum Keycode fuer get_key_state


def get_left_button() -> bool:
    """
    Returns the state of the mouse's left button.
    :return: 1 for pressed, 0 for not pressed
    """
    return KIPR.get_mouse_left_button() == 1


def get_mouse_middle_button() -> bool:
    """
    Returns the state of the mouse's middle button.
    :return: 1 for pressed, 0 for not pressed
    """
    return KIPR.get_mouse_middle_button() == 1


def get_right_button() -> bool:
    """
    Returns the state of the mouse's right button.
    :return: 1 for pressed, 0 for not pressed
    """
    return KIPR.get_mouse_right_button() == 1






