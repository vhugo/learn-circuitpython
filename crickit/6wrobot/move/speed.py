import time

ACCELERATION = 0.1


def _range_speed(current_speed, speed):
    direction = 1
    acc = ACCELERATION
    speed = float(speed)
    current_speed = float(current_speed)

    if speed < current_speed:
        direction = -1

    speed_range = [current_speed]
    new_speed = current_speed

    while new_speed != speed:
        new_speed += (direction * acc)

        if (new_speed >= speed and direction > 0) or \
           (new_speed <= speed and direction < 0):
            new_speed = speed

        # print("Current: {} Expected: {} Direction:{} Speed:{}".format(
        # current_speed, speed, direction, new_speed))
        speed_range.append(speed)

    return speed_range


def forward(motors, current_speed, max_speed):
    print("moving FORWARD")

    for speed in _range_speed(current_speed, max_speed):
        for midx in range(len(motors)):
            if midx % 2 == 1:
                motors[midx].throttle = -1 * speed
                continue
            motors[midx].throttle = speed
        time.sleep(0.1)
    return max_speed


def backward(motors, current_speed, max_speed):
    print("moving BACKWARD")

    for speed in _range_speed(current_speed, max_speed):
        for midx in range(len(motors)):
            if midx % 2 == 1:
                motors[midx].throttle = speed
                continue
            motors[midx].throttle = -1 * speed
        time.sleep(0.1)
    return max_speed


def stop(motors, current_speed, max_speed):
    print("STOP moving")

    for motor in motors:
        motor.throttle = 0
    time.sleep(0.1)
    return 0
