import time

ANGLE_STRAIGHT = 100
ANGLE_LEFT = 70
ANGLE_RIGHT = 130
STEER_INCREMENT = 5


def _range_steer(current_angle, angle):
    inc = STEER_INCREMENT
    if angle < current_angle:
        inc *= -1

    # print("increment: current angle:{} angle:{} inc:{}".format(
    #     current_angle, angle, inc))

    angle += inc
    return range(current_angle, angle, inc)


def left(servo, current_angle):
    print("servo LEFT")
    for angle in _range_steer(current_angle, ANGLE_LEFT):
        servo.angle = angle
        time.sleep(0.1)
    return ANGLE_LEFT


def right(servo, current_angle):
    print("servo RIGHT")
    for angle in _range_steer(current_angle, ANGLE_RIGHT):
        servo.angle = angle
        time.sleep(0.1)
    return ANGLE_RIGHT


def straight(servo, current_angle):
    print("servo STRAIGHT")
    for angle in _range_steer(current_angle, ANGLE_STRAIGHT):
        servo.angle = angle
        time.sleep(0.1)
    return ANGLE_STRAIGHT
