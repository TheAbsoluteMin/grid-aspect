import time
import easygopigo3 as easy

gopigo = easy.EasyGoPiGo3()
servo = gopigo.init_servo("servo")

distPerRev = 62.8318530718 #20*pi mm
ticksPerRev = 1440 #120*12
servoDown = 45 #horn moves to release pen
servoUp = 0 #horn starts with pen up
X = 0
Y = 0

def setUp():
    gopigo.set_motor_limits(gopigo.MOTOR_LEFT, dps = 150)
    gopigo.set_motor_limits(gopigo.MOTOR_RIGHT, dps = 150)
    gopigo.offset_motor_encoder(gopigo.MOTOR_LEFT, gopigo.get_motor_encoder(gopigo.MOTOR_LEFT))
    gopigo.offset_motor_encoder(gopigo.MOTOR_RIGHT, gopigo.get_motor_encoder(gopigo.MOTOR_RIGHT))
    penUp()

def penUp():
    servo.rotate_servo(servoUp)
    time.sleep(0.5)

def penDown():
    servo.rotate_servo(servoDown)
    time.sleep(0.5)

def distToTicks(distTotal, distRev):
    turns = distTotal/distRev
    return int(turns*ticksPerRev)

def motorState():
    xMotor = gopigo.get_motor_status(gopigo.MOTOR_LEFT) != 0
    yMotor = gopigo.get_motor_status(gopigo.MOTOR_RIGHT) != 0
    return xMotor or yMotor

def go(newX, newY):
    global X, Y
    distToX = newX - X
    distToY = newY - Y
    xTicks = distToTicks(distToX, distPerRev)
    yTicks = distToTicks(distToY, distPerRev)
    xMotorStart = gopigo.get_motor_encoder(gopigo.MOTOR_LEFT)
    yMotorStart = gopigo.get_motor_encoder(gopigo.MOTOR_RIGHT)

    if xTicks != 0:
        gopigo.set_motor_position(gopigo.MOTOR_LEFT, xMotorStart+xTicks)
    if yTicks != 0:
        gopigo.set_motor_position(gopigo.MOTOR_RIGHT, yMotorStart+yTicks)

    while motorState():
        time.sleep(0.02)

    X = newX
    Y = newY

def reset():
    penUp()
    go(0,0)

setUp()
try:
    go(30,30)
    penDown()
    go(80,30)
    go(80,80)
    go(30,80)
    go(30,30) #square
    penUp()

except KeyboardInterrupt:
    print("emergency stop")
    pass

finally:
    reset()
    gopigo.reset_all()
