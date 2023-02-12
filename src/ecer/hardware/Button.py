from src.ecer.dll.DLL import KIPR


def a_button() -> bool:
    """Gets the A button's state (pressed or not pressed.)

    :return: 1 for pressed, 0 for not pressed
    """
    return KIPR.a_button() == 1


def a_clicked() -> bool:
    """Gets the A button's state (pressed or not pressed.)
    This function blocks until the button is no longer pressed.

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.a_button_clicked() == 1


def any_button() -> bool:
    """Determines whether or not any of the buttons are pressed.

    :return:1 for pressed, 0 for not pressed
    """
    return KIPR.any_button() == 1


def b_button() -> bool:
    """1 for pressed, 0 for not pressed

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.b_button() == 1


def b_clicked() -> bool:
    """Gets the A button's state (pressed or not pressed.)
    This function blocks until the button is no longer pressed.

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.b_button_clicked() == 1


def black_button() -> bool:
    """ Gets the black button's state (pressed or not pressed.)

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.black_button() == 1


def c_button() -> bool:
    """Gets the C button's state (pressed or not pressed.)

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.c_button() == 1


def c_clicked():
    """Gets the B button's state (pressed or not pressed.)
    This function blocks until the button is no longer pressed.


    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.c_button_clicked() == 1


def extra_hide():
    """Hides the X, Y, and Z buttons. This is the default.

    """

    return KIPR.extra_buttons_hide() == 1


def extra_show():
    """ Shows the X, Y, and Z buttons.

    """

    return KIPR.extra_buttons_show()


def get_extra_visible():
    """Determines whether or not the X, Y, and Z buttons are visible.

    """

    return KIPR.get_extra_buttons_visible()


def left_button() -> bool:
    """Gets the left button's state (pressed or not pressed.)

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.left_button()


def right_button() -> bool:
    """ Gets the right button's state (pressed or not pressed.)

    :return: 1 for pressed, 0 for not pressed (But returning flipped)
    """

    return KIPR.right_button()


def set_a_text(text: str):
    """Updates the A button's text.

    :param text: The text to display. Limit of 16 characters
    """

    return KIPR.set_a_button_text(text)


def set_b_text(text: str):
    """Updates the B button's text.

    :param text:The text to display. Limit of 16 characters.

    """

    return KIPR.set_b_button_text(text)


def set_c_text(text: str):
    """Updates the C button's text.

    :param text: the text to display. Limit of 16 characters.

    """

    return KIPR.set_c_button_text(text)


def set_extra_visible(visible: int):
    """Sets whether or not the X, Y, and Z buttons are visible.

    :param visible: not important
    """

    return KIPR.set_extra_buttons_visible(visible)


def set_x_text(text: str):
    """Updates the X button's text.

    :param text: The text to display. Limit of 16 characters.

    """

    return KIPR.set_x_button_text(text)


def set_y_text(text: str):
    """Updates the Y button's text.

    :param text: the text to display. Limit of 16 characters.
    """

    return KIPR.set_y_button_text(text)


def set_z_text(text: str):
    """Updates the Z button's text.

    :param text: the text to display. Limit of 16 characters.

    """

    return KIPR.set_z_button_text(text)


def side_button():
    """Gets the side button's state (pressed or not pressed.)

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.side_button()


def side_clicked() -> bool:
    """ Gets the Z button's state (pressed or not pressed.)
        This function blocks until the button is no longer pressed.


    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.side_button_clicked() == 1


def x_button() -> bool:
    """Gets the C button's state (pressed or not pressed.)

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.x_button() == 1


def x_clicked() -> bool:
    """Gets the C button's state (pressed or not pressed.)
        This function blocks until the button is no longer pressed.

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.x_button_clicked() ==1


def y_button() -> bool:
    """ Gets the Y button's state (pressed or not pressed.)

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.y_button() == 1


def y_clicked() -> bool:
    """Gets the X button's state (pressed or not pressed.)
        This function blocks until the button is no longer pressed.

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.y_button_clicked() == 1


def z_button() -> bool:
    """ Gets the Z button's state (pressed or not pressed.)

    :return: 1 for pressed, 0 for not pressed
    """

    return KIPR.z_button() == 1


def z_clicked() -> bool:
    """Gets the Y button's state (pressed or not pressed.)
        This function blocks until the button is no longer pressed.

    :return:1 for pressed, 0 for not pressed
    """

    return KIPR.z_button_clicked() == 1
