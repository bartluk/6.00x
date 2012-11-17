# 6.00x Problem Set 7: Simulating robots

import math
import random

import ps7_visualize
import pylab

# For Python 2.7:
from ps7_verify_movement27 import testRobotMovement

# If you get a "Bad magic number" ImportError, comment out what's above and
# uncomment this line (for Python 2.6):
# from ps7_verify_movement26 import testRobotMovement


# === Provided class Position
class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).
        """
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: float representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)

    def __str__(self):  
        return "(%0.2f, %0.2f)" % (self.x, self.y)


# === Problem 1
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        assert (width > 0 and height > 0)
        self.width, self.height = width, height
        self.room = {(w, h):False for w in range(width+1) for h in range(height+1)}

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getRoom(self):
        return self.room
 
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        temp = (int(math.floor(pos.getX()/1)), int(math.floor(pos.getY()/1)))
        self.getRoom()[temp] = True
        return self.room

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        temp = (int(math.floor(m/1)), int(math.floor(n/1)))
        return self.getRoom()[temp]  == True
    
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.getHeight() * self.getWidth()

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        count = 0
        for item in self.getRoom().items():
            if True in item:
                count +=1
        return count 

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        #return Position(random.random()*self.getWidth(), random.random()*self.getHeight())
        x = random.uniform(0,self.getWidth())
        y = random.uniform(0,self.getHeight())
        return Position(x,y)


    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        #Reject negative numbers
        if pos.getX() < 0 or pos.getY() < 0:
            return False
        #Reject outside numbers
        elif pos.getX() >= self.getWidth() or pos.getY() >= self.getHeight():
            return False
        
        return True

    def getCoverage(self):
        return float(self.getNumCleanedTiles())/float(self.getNumTiles())

    def __str__(self):
        return "(%d, %d), with %d, cleaned %d , coverage %0.2f" % (self.getWidth(), self.getHeight(), self.getNumTiles(), self.getNumCleanedTiles(), self.getCoverage())



class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        #assert isinstance(room, RectangularRoom) and type(speed) == float and speed > 0
        self.room, self.speed = room, speed
        self.robotDirection = random.randint(0,359)
        self.robotPosition = self.room.getRandomPosition()
        self.room.cleanTileAtPosition(self.robotPosition)
        

    def getRoom(self):
        return self.room

    def getSpeed(self):
        return self.speed

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.robotPosition
    
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.robotDirection

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        assert isinstance(position, Position)
        self.robotPosition = position
        return self.robotPosition

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.robotDirection = direction
        return self.robotDirection

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        room = self.getRoom()        
        robotNextPosition = self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.getSpeed())
        if room.isPositionInRoom(robotNextPosition):
            self.setRobotPosition(robotNextPosition)
            room.cleanTileAtPosition(robotNextPosition)
        else:
            self.setRobotDirection(random.randint(0,359))

        #raise NotImplementedError

# Uncomment this line to see your implementation of StandardRobot in action!
#testRobotMovement(StandardRobot, RectangularRoom)


# === Problem 3
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    time_steps = 0.0
    visualize = False

    for trial in xrange(0,num_trials):
        if visualize:
            anim = ps7_visualize.RobotVisualization(num_robots, width, height)
        room = RectangularRoom(width, height)
        list_robots = [robot_type(room, speed) for robot in range(num_robots)]
        while ((float(room.getNumCleanedTiles())/float(room.getNumTiles())) < min_coverage):
            for robot in list_robots:
                robot.updatePositionAndClean()
            time_steps += 1.0
            if visualize:
                anim.update(room, list_robots)
    if visualize:
        anim.done()
    return time_steps/num_trials

#print runSimulation(10, 1.0, 30, 30, 1, 3, StandardRobot)

    #raise NotImplementedError


# === Problem 4
class RandomWalkRobot(Robot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement strategy: it
    chooses a new direction at random at the end of each time-step.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        #raise NotImplementedError

        room = self.getRoom()
        robotPosition = self.getRobotPosition()
        robotDirection = self.getRobotDirection()
        self.setRobotDirection(random.randint(0,359))
        nextPosition = robotPosition.getNewPosition(robotDirection, self.getSpeed())
        if room.isPositionInRoom(nextPosition):
            self.setRobotPosition(nextPosition)
            room.cleanTileAtPosition(nextPosition)

#print runSimulation(1, 1.0, 8, 8, 0.3, 1, RandomWalkRobot)

# === Problem 5
#
# 1) Write a function call to showPlot1 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#

#
# 2) Write a function call to showPlot2 that generates an appropriately-labeled
#     plot.
#
#       (... your call here ...)
#
#

def showPlot1(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    num_robot_range = range(1, 11)
    times1 = []
    times2 = []
    for num_robots in num_robot_range:
        print "Plotting", num_robots, "robots..."
        times1.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, StandardRobot))
        times2.append(runSimulation(num_robots, 1.0, 20, 20, 0.8, 20, RandomWalkRobot))
    plot1 = pylab.figure()
    pylab.plot(num_robot_range, times1)
    pylab.plot(num_robot_range, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    #pylab.show()
    plot1.savefig('plot1.png')


    
def showPlot2(title, x_label, y_label):
    """
    What information does the plot produced by this function tell you?
    """
    aspect_ratios = []
    times1 = []
    times2 = []
    for width in [10, 20, 25, 50]:
        height = 300/width
        print "Plotting cleaning time for a room of width:", width, "by height:", height
        aspect_ratios.append(float(width) / height)
        times1.append(runSimulation(2, 1.0, width, height, 0.8, 200, StandardRobot))
        times2.append(runSimulation(2, 1.0, width, height, 0.8, 200, RandomWalkRobot))
    plot2 = pylab.figure()
    pylab.plot(aspect_ratios, times1)
    pylab.plot(aspect_ratios, times2)
    pylab.title(title)
    pylab.legend(('StandardRobot', 'RandomWalkRobot'))
    pylab.xlabel(x_label)
    pylab.ylabel(y_label)
    #pylab.show()
    plot2.savefig('plot2.png')
    
if __name__ == '__main__':
    showPlot1('Time It Takes 1 - 10 Robots To Clean 80% Of A Room', 'Number of robots', 'Time / steps')
    showPlot2('Time It Takes A Robot To Clean 80% Of Variously Shaped Rooms', 'Aspect Ratio', 'Time / steps')