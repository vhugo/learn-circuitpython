import time
# import board
# import busio as io

from adafruit_crickit import crickit
from adafruit_hcsr04 import HCSR04
from brain import vision, move


# motors = [crickit.dc_motor_1, crickit.dc_motor_2]
# sonar = HCSR04(board.A2, board.A3)
# look = vision.Look(crickit.servo_1, sonar)
# look.straight()
#
#
# #
# #  # Scan
# # look.left()
# # look.right()
# # look.straight()
# # print(look.best_way)
#
# sonar.deinit()

go = move.Go(crickit.dc_motor_1, crickit.dc_motor_2)
go.forward()
time.sleep(1)
go.stop()





#
# servo = crickit.servo_1
# # dc_motors = [crickit.dc_motor_1, crickit.dc_motor_2]
#
# current_look = look.ANGLE_STRAIGHT
# current_look = look.straight(servo, current_look)
# current_look = look.left(servo, current_look)
# current_look = look.right(servo, current_look)
# current_look = look.left(servo, current_look)
# current_look = look.straight(servo, current_look)


# current_steer = steer.ANGLE_STRAIGHT
# current_speed = 0.0
# default_speed = 0.5
#
# current_steer = steer.straight(servo, current_steer)
# current_speed = speed.backward(dc_motors, current_speed, default_speed)
# current_steer = steer.left(servo, current_steer)
# time.sleep(1)
# # current_speed = speed.backward(dc_motors, current_speed, default_speed)
# # current_steer = steer.left(servo, current_steer)
# # time.sleep(1)
# current_speed = speed.stop(dc_motors, current_speed, default_speed)
#

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
