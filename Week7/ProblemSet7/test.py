    def isInWall(self):
        x_robot, y_robot = self.getRobotPosition().getX(), self.getRobotPosition().getY()
        x_room , y_room = self.getRoom().getWidth(), self.getRoom().getHeight()
        if (int(x_robot) >= x_room) or (int(y_robot) >= y_room) or (int(x_robot) == 0) or (int(y_robot) == 0):
            return True
        else:
            return False

        x_robot, y_robot = self.getRobotPosition().getX(), self.getRobotPosition().getY()
        
        def getNewPosition():
            x_robot, y_robot = self.getRobotPosition().getX(), self.getRobotPosition().getY()
            x_room , y_room = self.getRoom().getWidth(), self.getRoom().getHeight()
            new = random.choice([(x_robot+1, y_robot), (x_robot, y_robot+1), (x_robot-1, y_robot), (x_robot, y_robot-1)])
            new_x , new_y = new
            if new_x < 0:
                new_x = -new_x
            if new_y < 0:
                new_y = -new_y
            if new_x > x_room:
                new_x = x_room
            if new_y > y_room:
                new_y = y_room
            new_pos = Position(new_x, new_y)
            #print new_pos
            if self.getRoom().isPositionInRoom(new_pos): 
                return self.setRobotPosition(new_pos)
            else:
                return self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.getSpeed())

        if self.getRoom().isPositionInRoom(self.getRobotPosition()):
            if self.getRoom()[(int(x_robot), int(y_robot))] == False:
                self.getRoom().cleanTileAtPosition(self.getRobotPosition())
                return getNewPosition()
            else:
                return getNewPosition()
        else:
            return self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.getSpeed())

        if self.isInWall():
            return self.getRobotPosition().getNewPosition(self.getRobotDirection(), self.getSpeed())
  