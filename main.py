import ev3dev.ev3 as ev3


class Robot:
    def __init__(self):
        # setup the sensors
        touch = ev3.TouchSensor()
        smallMotor = ev3.DcMotor()
