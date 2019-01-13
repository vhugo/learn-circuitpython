import time
import board
import busio as io

from adafruit_crickit import crickit
# from adafruit_apds9960 import apds9960
from move import steer, speed

# i2c = io.I2C(board.SCL, board.SDA)
# sensor = apds9960.APDS9960(i2c)

servo = crickit.servo_1
dc_motors = [crickit.dc_motor_1, crickit.dc_motor_2]

current_steer = steer.ANGLE_STRAIGHT
current_speed = 0.0
default_speed = 0.5

current_steer = steer.straight(servo, current_steer)
current_speed = speed.backward(dc_motors, current_speed, default_speed)
current_steer = steer.left(servo, current_steer)
time.sleep(1)
# current_speed = speed.backward(dc_motors, current_speed, default_speed)
# current_steer = steer.left(servo, current_steer)
# time.sleep(1)
current_speed = speed.stop(dc_motors, current_speed, default_speed)


# while True:
#     current_speed = speed.forward(dc_motors, current_speed, default_speed)
#     time.sleep(1)
#
#     current_steer = steer.left(servo, current_steer)
#     time.sleep(5)

#     current_speed = speed.stop(dc_motors, current_speed, default_speed)
#     time.sleep(5)
#
#     current_speed = speed.backward(dc_motors, current_speed, default_speed)
#     time.sleep(1)
#
#     current_speed = speed.stop(dc_motors, current_speed, default_speed)
#     time.sleep(5)


    #
    # current_steer = steer.straight(servo, current_steer)
    # time.sleep(5)
    #
    # current_steer = steer.right(servo, current_steer)
    # time.sleep(5)
    #
    # current_steer = steer.straight(servo, current_steer)
    # time.sleep(5)
