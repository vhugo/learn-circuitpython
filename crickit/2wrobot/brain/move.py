import time

ACCELERATION = 0.1
MAX_SPEED = 0.3

class Go:
    current_speed = 0.0


    def __init__(self, left_motor, right_motor, config={}):
        self.mleft = left_motor
        self.mright = right_motor
        self.acceleration = config.get("acceleration", ACCELERATION)
        self.max_speed = config.get("max_speed", MAX_SPEED)


    def _range_speed(self):
        direction = 1

        if self.max_speed < self.current_speed:
            direction = -1

        speed_range = [self.current_speed]
        new_speed = self.current_speed

        while new_speed != self.max_speed:
            new_speed += (direction * self.acceleration)

            if (new_speed >= self.max_speed and direction > 0) or \
               (new_speed <= self.max_speed and direction < 0):
                new_speed = self.max_speed

            print("current_speed: {}", new_speed)
            speed_range.append(new_speed)

        return speed_range


    def forward(self):
        print("moving FORWARD")

        for gas in self._range_speed():
            self.current_speed = gas
            self.mright.throttle = self.mleft.throttle = -1 * self.current_speed
            time.sleep(0.1)


    def backward(self):
        print("moving BACKWARD")

        for gas in self._range_speed():
            self.current_speed = gas
            self.mleft.throttle = self.mright.throttle = self.current_speed
            time.sleep(0.1)


    def left(self):
        print("moving LEFT")

        for gas in self._range_speed():
            self.current_speed = gas
            self.mright.throttle = self.current_speed
            self.mleft.throttle = -1 * self.current_speed
            time.sleep(0.1)


    def right(self):
        print("moving LEFT")

        for gas in self._range_speed():
            self.current_speed = gas
            self.mright.throttle = -1 * self.current_speed
            self.mleft.throttle = self.current_speed
            time.sleep(0.1)


    def stop(self):
        print("STOP moving")

        self.current_speed = 0
        self.mleft.throttle = self.current_speed
        self.mright.throttle = self.current_speed
        time.sleep(0.1)
