from src.ecer.dll.DLL import KIPR


def disable_all():
    """
    Disable all motors
    """
    KIPR.allof()


def disable_motor(port: int):
    """
    Disable a specific motor on a port
    :param port: The port ID the motor is plugged into
    """
    KIPR.off(port)


def get_position(port: int) -> int:
    """
    Get the position of the motor. This position is calculated and can be resetted using :reset_motor_calculated_position
    :param port: The port of the motor
    :return: The position of the motor
    """
    return KIPR.get_motor_position_counter(port)


def reset_position(port: int):
    """
    Reset the motor position without moving the position of the motor
    :param port: The port of the motor
    """
    KIPR.clear_motor_position_counter(port)


def move_at_velocity(port: int, velocity: int) -> int:
    """
    Set a goal velocity in ticks per second.
    detailed The range is -1500 to 1500, though motor position accuracy may be decreased outside -1000 to 1000.

    :param port: The port of the motor
    :param velocity:
    :return: Don't know yet ToDo: Check what the return value is
    """
    return KIPR.move_at_velocity(port, velocity)


def move_to_position(port: int, speed: int, goal_position: int) -> int:
    """
    Set a goal position (in ticks) for the motor to move to.
    detailed There are approximately 1500 ticks per motor revolution.
    detailed This function is more accurate if speeds between -1000 and 1000 are used.

    :param port: The port of the motor
    :param speed: The speed to move at, between -1500 and 1500 ticks / second
    :param goal_position: The position to move to (in ticks)
    :return: Don't know yet ToDo: Check what the return value is
    """
    return KIPR.move_to_position(port, speed, goal_position)


def move_relative_position(port: int, speed: int, delta_pos: int) -> int:
    """
    Set a goal position (in ticks) for the motor to move to, relative to the current position.

    :param port: The motor port.
    :param speed: The speed to move at, between -1500 and 1500 ticks / second
    :param delta_pos: The position to move to (in ticks) given the current position
    :return: Don't know yet ToDo: Check what the return value is
    """
    KIPR.move_relative_position(port, speed, delta_pos)


def freeze(port: int) -> int:
    """
    Active braking to stop a motor.

    :param port: The motor port.
    :return: Don't know yet ToDo: Check what the return value is
    """
    return KIPR.freeze(port)


# ToDo: Make a async method using promises
def is_motor_done(port: int) -> bool:
    """
    Check if the motor has reached its goal.

    :param port: The motor port.
    :return: True of motor at the targeted point
    """
    return KIPR.get_motor_done(port) != 1


def wait_until_motor_done(port: int):
    """
    Wait until the motor is at its goal.

    :param port: The motor port.
    """
    KIPR.block_motor_done(port)


def set_percentage_power(port: int, pwm: int):
    """
    Set the motor pwm (percent power) command.

    :param pwm: A new motor pwm command between 0 and 100
    :param port: The motor port.
    """
    KIPR.setpwm(port, pwm)


def get_percentage_power(port: int) -> int:
    """
    Get the current motor pwm command.

    :param port: The motor port.
    :return: Percentage of the motor
    """
    return KIPR.getpwm(port)


def move_forward(port: int):
    """
    Moves the given motor forward at full power.

    :param port: the motor's port.
    """
    KIPR.fd(port)


def move_backward(port: int):
    """
    Moves the given motor backward at full power.

    :param port: the motor's port.
    """
    KIPR.bk(port)


def move_motor(port: int, percentage: int):
    """
    Moves a motor at a percent velocity.

    :param port: The motor port.
    :param percentage: 	The percent of the motors' velocity, between -100 and 100.
    :return:
    """
    KIPR.motor(port, percentage)
