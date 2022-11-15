# Make sure to have the server side running in V-REP:
# in a child script of a V-REP scene, add following command
# to be executed just once, at simulation start:
#
# simExtRemoteApiStart(19999)
# then start simulation, and run this program.
#
# IMPORTANT: for each successful call to simxStart, there
# should be a corresponding call to simxFinish at the end!
import Lab1_Agents_Task1_World as World

# connect to the server
robot = World.init()
# print important parts of the robot
print(sorted(robot.keys()))
counter = 0

while robot: # main Control loop
    #######################################################
    # Perception Phase: Get information about environment #
    #######################################################
    simulationTime = World.getSimulationTime()
    # if simulationTime%1000==0:
    #     # print some useful info, but not too often
    #     print ('Time:',simulationTime,\
    #            'ultraSonicSensorLeft:',World.getSensorReading("ultraSonicSensorLeft"),\
    #            "ultraSonicSensorRight:", World.getSensorReading("ultraSonicSensorRight"))

    ##############################################
    # Reasoning: figure out which action to take #
    ##############################################
    motorSpeed = dict(speedLeft=2, speedRight=2)
    if counter == 0:
        motorSpeed = dict(speedLeft=2, speedRight=2)
    elif counter == 1:
        motorSpeed = dict(speedLeft=-0.3, speedRight=0.3)
    elif counter == 2:
        motorSpeed = dict(speedLeft=2, speedRight=2)
    elif counter == 3:
        motorSpeed = dict(speedLeft=-1.5, speedRight=-1.5)
        counter = 0
    elif counter == 4:
        motorSpeed = dict(speedLeft=-0.5, speedRight=0.5)
        counter = 0
    
    if simulationTime%10000 == 0:
        counter +=1
    ########################################
    # Action Phase: Assign speed to wheels #
    ########################################
    # assign speed to the wheels
    World.setMotorSpeeds(motorSpeed)
    # try to collect energy block (will fail if not within range)
    if simulationTime%10000==0:
        print ("Trying to collect a block...",World.collectNearestBlock())
