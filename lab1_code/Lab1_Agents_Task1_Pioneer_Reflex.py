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
motorSpeed = dict(speedRight=2,speedLeft=2)

while robot: # main Control loop
    #######################################################
    # Perception Phase: Get information about environment #
    #######################################################
    simulationTime = World.getSimulationTime()
    if simulationTime%1000==0:
        # print some useful info, but not too often
        print ('Time:',simulationTime,\
               'ultraSonicSensorLeft:',World.getSensorReading("ultraSonicSensorLeft"),\
               "ultraSonicSensorRight:", World.getSensorReading("ultraSonicSensorRight"))

    distToNearestEnergy = World.getSensorReading("energySensor").get('distance')
    dirToNearestEnergy = World.getSensorReading("energySensor").get('direction')
    dirOfRobot = World.robotDirection()
    rightDist = World.getSensorReading('ultraSonicSensorRight')
    leftDist = World.getSensorReading('ultraSonicSensorLeft')
    ##############################################
    # Reasoning: figure out which action to take #
    ##############################################


    if float(rightDist) < 0.5 or float(leftDist) < 0.5 * 1.20:
        World.avoidWalls()
    elif distToNearestEnergy < 0.5:
        World.collectNearestBlock()
    else:
        motorSpeed = dict(speedRight=2,speedLeft=2)

    ########################################
    # Action Phase: Assign speed to wheels #
    ########################################
    # assign speed to the wheels
    World.setMotorSpeeds(motorSpeed)
    # try to collect energy block (will fail if not within range)
    if simulationTime%10000==0:
        print ("Trying to collect a block...",World.collectNearestBlock())
