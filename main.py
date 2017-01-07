import ev3dev.ev3 as ev3


class Robot:
    def __init__(self):
        # setup the sensors
        touch = ev3.TouchSensor()
        smallMotor = ev3.DcMotor()


if __name__ == "__main__":
    print "Starting up"
    robot = Robot()
