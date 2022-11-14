# Make sure to have the server side running in V-REP:
# in a child script of a V-REP scene, add following command
# to be executed just once, at simulation start:
#
# simExtRemoteApiStart(19999)
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!
from datetime import date
import random
import time

import Lab1_Agents_Task1_World as World

# connect to the server
robot = World.init()
# print important parts of the robot
print(sorted(robot.keys()))
#timesnapOld = time.localtime(time.time()).tm_sec
timesnapOld = time.time_ns()
motorSpeed = dict(speedLeft=0, speedRight=0)

seq = 0

arrOfActions = [
    [0, 2],
    [3, 0.4],
    [0, 2],
    [1, -1],
    [2, 4],
    [4, 4],
    [0,5],
    [1,-1],
    [3,2],
    [2, 3]
]

while robot: # main Control loop
    #######################################################
    # Perception Phase: Get information about environment #
    #######################################################

    simulationTime = World.getSimulationTime()
    #if simulationTime%1000==0:
        # print some useful info, but not too often
    #    print ('Time:',simulationTime,\
    #           'ultraSonicSensorLeft:',World.getSensorReading("ultraSonicSensorLeft"),\
     #          "ultraSonicSensorRight:", World.getSensorReading("ultraSonicSensorRight"))

    ##############################################
    # Reasoning: figure out which action to take #
    ##############################################

    #timesnapNew = time.localtime(time.time()).tm_sec
    timesnapNew = time.time_ns()
    print(timesnapNew)
    if timesnapNew > (timesnapOld + 5000*1000):
        print("in loop")

        randomAction = random.randint(0,10)
        timesnapOld = timesnapNew
        print(arrOfActions[seq][0])
        match arrOfActions[seq][0]:
            case 0:
                motorSpeed = dict(speedLeft=arrOfActions[seq][1],speedRight=arrOfActions[seq][1])
            case 1:
                World.collectNearestBlock()
            case 2:
                motorSpeed = dict(speedLeft=-arrOfActions[seq][1],speedRight=-arrOfActions[seq][1])
            case 3:
                motorSpeed = dict(speedLeft=-arrOfActions[seq][1], speedRight=arrOfActions[seq][1])
            case 4:
                motorSpeed = dict(speedLeft=arrOfActions[seq][1], speedRight=-arrOfActions[seq][1])
            case _:
                motorSpeed = dict(speedLeft=1, speedRight=1)
        seq = seq + 1
    ########################################
    # Action Phase: Assign speed to wheels #
    ########################################
    # assign speed to the wheels
    World.setMotorSpeeds(motorSpeed)
    # try to collect energy block (will fail if not within range)
