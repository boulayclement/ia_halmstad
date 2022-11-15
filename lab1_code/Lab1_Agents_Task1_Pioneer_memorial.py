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



def moveToNearestBlock():
    if dirToNearestEnergy < -0.4:
        motorSpeed = dict(speedRight=2,speedLeft=-1)
    elif dirToNearestEnergy > 0.4:
        motorSpeed = dict(speedRight=-1,speedLeft=2)
    else:
        motorSpeed = dict(speedRight=3,speedLeft=3)
    return motorSpeed

# connect to the server
robot = World.init()
# print important parts of the robot
print(sorted(robot.keys()))
motorSpeed = dict(speedRight=2,speedLeft=2)
changeStratTiming = World.getSimulationTime()
counter = 0
lastTurn = ""

while robot: # main Control loop
    #######################################################
    # Perception Phase: Get information about environment #
    #######################################################
    simulationTime = World.getSimulationTime()
    if simulationTime%2000==0:
        # print some useful info, but not too often
        print ('Time:',simulationTime,\
               'ultraSonicSensorLeft:',World.getSensorReading("ultraSonicSensorLeft"),\
               "ultraSonicSensorRight:", World.getSensorReading("ultraSonicSensorRight"),\
                "dirneeart:", dirToNearestEnergy)

    blocks = World.findEnergyBlocks()
    distToNearestEnergy = World.getSensorReading("energySensor").get('distance')
    dirToNearestEnergy = blocks[counter][3]
    dirOfRobot = World.robotDirection()
    rightDist = World.getSensorReading('ultraSonicSensorRight')
    leftDist = World.getSensorReading('ultraSonicSensorLeft')
    ##############################################
    # Reasoning: figure out which action to take #
    ##############################################


    if float(rightDist) < 0.5 or float(leftDist) < 0.5 * 1.20:
        # if rightDist < 0.2:
        #     motorSpeed = dict(speedLeft=-1,speedRight=3)
        #     lastTurn = "left"
        # elif leftDist < 0.2 * 1.20:
        #     motorSpeed = dict(speedLeft=3,speedRight=-1)
        #     lastTurn = "right"
        World.avoidWalls()
    elif distToNearestEnergy < 0.5 and distToNearestEnergy > -0.5:
        changeStratTiming = World.getSimulationTime()
        World.collectNearestBlock()
        counter = 0
    else:
        if simulationTime - changeStratTiming > 50000:
            print("Pass", lastTurn)
            # if (lastTurn == "left"):
            # World.execute(dict(speedLeft=-2, speedRight=2),1000,-1)
            # elif lastTurn=="right":
            #     World.execute(dict(speedLeft=2, speedRight=-2),1000,-1)
            World.execute(dict(speedLeft=-2, speedRight=-2),10000,-1)
            World.execute(moveToNearestBlock(),10000,-1)
            if counter >= len(blocks):
                counter = 0
            else:
                counter += 1
            dirToNearestEnergy = blocks[counter][3]
            changeStratTiming = simulationTime
            print("Block next", blocks[counter][0])
        motorSpeed = moveToNearestBlock()

    ########################################
    # Action Phase: Assign speed to wheels #
    ########################################
    # assign speed to the wheels
    World.setMotorSpeeds(motorSpeed)
    # try to collect energy block (will fail if not within range)
    if simulationTime%10000==0:
        print ("Trying to collect a block...",World.collectNearestBlock())

