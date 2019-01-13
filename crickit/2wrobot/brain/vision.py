import time

ANGLE_STRAIGHT = 60
ANGLE_LEFT = 180
ANGLE_RIGHT = 0
ANGLE_INCREMENT = 5
ANGLE_MOVE_SPEED = 0.05

class Look:
    best_angle = ANGLE_STRAIGHT
    farthest_obstacle = 0

    def __init__(self, servo, sonar, config={}):
        self.servo = servo
        self.sonar = sonar
        self.current_angle = config.get("current_angle", ANGLE_STRAIGHT)
        self.angle_straight = config.get("angle_straight", 100)
        self.angle_left = config.get("angle_left", ANGLE_LEFT)
        self.angle_right = config.get("angle_right", ANGLE_RIGHT)
        self.angle_increment = config.get("angle_increment", ANGLE_INCREMENT)
        self.angle_move_speed = config.get("angle_move_speed", ANGLE_MOVE_SPEED)
        self.best_angle = ANGLE_STRAIGHT
        self.find_obstacle_distance()


    def _turn(self, angle):
        inc = self.angle_increment
        if angle < self.current_angle:
            inc *= -1

        angle += inc
        for angle in range(self.current_angle, angle, inc):
            self.servo.angle = angle

            if self.find_obstacle_distance() > 0:
                self.best_angle=angle

            time.sleep(self.angle_move_speed)

        self.current_angle = angle

    def find_obstacle_distance(self):
        try:
            measurement = self.sonar.distance
            if measurement > self.farthest_obstacle:
                self.farthest_obstacle = measurement
                return measurement

        except:
            pass

        return 0


    @property
    def best_way(self):
        if self.best_angle > ANGLE_STRAIGHT:
            return "go left ANGLE: {} DISTANCE: {}".format(self.best_angle, self.farthest_obstacle)
        else:
            return "go right ANGLE: {} DISTANCE: {}".format(self.best_angle, self.farthest_obstacle)


    def left(self):
        print("servo LEFT")
        self._turn(self.angle_left)


    def right(self):
        print("servo RIGHT")
        self._turn(self.angle_right)


    def straight(self):
        print("servo STRAIGHT")
        self._turn(self.angle_straight)
