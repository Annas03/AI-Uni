from modules.Agent import Agent
import time
class VaccumAgent(Agent):
    def __init__(self):
        self.score = 0
        pass
    def sense(self,env):
        self.environment = env
    def scoring(self, action, roomStatus = ''):
        if roomStatus == 'dirty': self.score -= 10
        if action == 'right' or action == 'left':
            self.score -= 1 
        if action == 'clean':
            self.score += 25
    def act(self):
        if self.environment.currentRoom.status == 'dirty':
            time.sleep(2)  # assuming that agent takes two seconds to clean a room
            self.scoring('clean', 'dirty')
            return 'clean'
        if int(self.environment.currentRoom.location) < len(self.environment.Rooms):
            time.sleep(1)  # assuming that agent takes One second to move to a room.
            self.scoring('right')
            return 'right'
        else:
            time.sleep(1)  # assuming that agent takes One second to move to a room.
            self.scoring('left')
            return 'left'
        # if self.environment.rooms == 2:
        #     if self.environment.currentRoom.status == 'dirty': return 'clean'
        #     if self.environment.currentRoom.location == 'A': return 'right' 
        #     return 'left'
        # else:
        #     if self.environment.currentRoom.status == 'dirty': return 'clean'
        #     if self.environment.currentRoom.location == 'A': return 'right'
        #     if self.environment.currentRoom.location == 'B': return 'right'
        #     return 'left'