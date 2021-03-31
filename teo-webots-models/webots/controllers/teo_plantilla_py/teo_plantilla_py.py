"""teo_plantilla_py controller."""

import controller
import math
import time


l0 = 0.329
l1 = 0.215+0.090
A = l0+l1

def fwdKin(q0, q1):
    # __1__
    
    print("fwdKin: input (q1 q2):", q0, q1)
    u = l0*math.cos(q0) + l1*math.cos(q0+q1)
    v = l0*math.sin(q0) + l1*math.sin(q0+q1)
    print("fwdKin: intermediate (u v):", u, v)
    x = v
    z = A-u
    print("fwdKin: output (x z):", x, z)
    return [x, z]

def invKin(x, z):
    # __2__
    print("invKin: input (x z):", x, z)
    u = A-z
    v = x
    print("invKin: intermediate (u v):", u, v)
    q1 = math.acos((u**2+v**2-l0**2-l1**2)/(2*l0*l1))
    q0 = math.atan2(v,u) - math.atan2((l1*math.sin(q1)),(l0+l1*math.cos(q1)))
    print("invKin: output (q0 q1):", math.degrees(q0), math.degrees(q1))
    return [q0, q1]

# create the Robot instance.


robot = controller.Robot()

motor_q0 = robot.getDevice("r_shoulder_pitch")
motor_q1 = robot.getDevice("r_elbow_pitch")

# target 0
## target 0: setPosition

# __3__
target0_q0 = math.radians(45) # use helper: math.radians()
target0_q1 = math.radians(45) # use helper: math.radians()
motor_q0.setPosition(target0_q0)
motor_q1.setPosition(target0_q1)
robot.step(1000)
time.sleep(1)

## target 0: perform fwdKin

[target0_x, target0_z] = fwdKin(target0_q0, target0_q1)

## target 0: check if invKin works to recover original joint space targets

[recovered0_q0, recovered0_q1] = invKin(target0_x, target0_z)

# Movimiento 1
target11_x = target0_x
target11_z = target0_z+0.3

[target11_q0, target11_q1] = invKin(target11_x, target11_z)

# Movimiento 2
target1_x = target0_x-0.1
target1_z = target0_z+0.2

[target1_q0, target1_q1] = invKin(target1_x, target1_z)

# Movimiento 3
target12_x = target0_x
target12_z = target0_z

[target12_q0, target12_q1] = invKin(target12_x, target12_z)



# Movimiento 4
target3_x = target0_x-0.1
target3_z = target0_z-0.2

[target3_q0, target3_q1] = invKin(target3_x, target3_z)


# Movimiento 5
target4_x = target0_x-0.2
target4_z = target0_z-0.3

[target4_q0, target4_q1] = invKin(target4_x, target4_z)

# Movimiento 6
target5_x = target0_x-0.3
target5_z = target0_z-0.35

[target5_q0, target5_q1] = invKin(target5_x, target5_z)

# Movimiento 7
target6_x = target0_x-0.4
target6_z = target0_z-0.38

[target6_q0, target6_q1] = invKin(target6_x, target6_z)

# Movimiento 8
target7_x = target0_x-0.5
target7_z = target0_z-0.38

[target7_q0, target7_q1] = invKin(target7_x, target7_z)

# Movimiento 9
target8_x = target0_x-0.6
target8_z = target0_z-0.38

[target8_q0, target8_q1] = invKin(target8_x, target8_z)

# Movimiento 10
target9_x = target0_x-0.7
target9_z = target0_z-0.38
[target9_q0, target9_q1] = invKin(target9_x, target9_z)




# Main loop:
# - toggle between target 1, target 2, target 3 and back again
# - perform simulation steps until Webots is stopping the controller
while True:
   
    motor_q0.setPosition(target11_q0)
    motor_q1.setPosition(target11_q1)
    if -1 == robot.step(1000):
        break
    time.sleep(0.5)

    motor_q0.setPosition(target1_q0)
    motor_q1.setPosition(target1_q1)
    if -1 == robot.step(1000):
        break
    time.sleep(0.5)

    motor_q0.setPosition(target12_q0)
    motor_q1.setPosition(target12_q1)
    if -1 == robot.step(1000):
        break
    time.sleep(0.5)


    # __5__
    
    #motor_q0.setPosition(target2_q0)
    #motor_q1.setPosition(target2_q1)
    #if -1 == robot.step(1000):
    #    break
    #time.sleep(1)
    motor_q0.setPosition(target3_q0)
    motor_q1.setPosition(target3_q1)
    if -1 == robot.step(1000):
        break
    time.sleep(0.5)
    motor_q0.setPosition(target4_q0)
    motor_q1.setPosition(target4_q1)
    if -1 == robot.step(1000):
        break
    time.sleep(0.5)
    motor_q0.setPosition(target5_q0)
    motor_q1.setPosition(target5_q1)
    if -1 == robot.step(1000):
        break
    time.sleep(0.5)
    motor_q0.setPosition(target6_q0)
    motor_q1.setPosition(target6_q1)
    if -1 == robot.step(1000):
        break
    time.sleep(0.5)
    motor_q0.setPosition(target7_q0)
    motor_q1.setPosition(target7_q1)
    if -1 == robot.step(1000):
        break
    time.sleep(0.5)
    motor_q0.setPosition(target8_q0)
    motor_q1.setPosition(target8_q1)
    if -1 == robot.step(1000):
        break
    time.sleep(0.5)
    motor_q0.setPosition(target9_q0)
    motor_q1.setPosition(target9_q1)
    if -1 == robot.step(1000):
        break
    time.sleep(0.5)

"""teo_basic_py controller."""

from controller import Robot
# create the Robot instance.

robot = Robot()

# list devices of robot.
n_devices = robot.getNumberOfDevices()
print(n_devices) # 56

for i in range(n_devices):
    print(robot.getDeviceByIndex(i).getName())

r_shoulder_pitch = robot.getDevice("r_shoulder_pitch")

# get the time step of the current world.
timestep = int(robot.getBasicTimeStep())
print(timestep) # 32

# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    r_shoulder_pitch.setPosition(45.0*3.14/180.0)

