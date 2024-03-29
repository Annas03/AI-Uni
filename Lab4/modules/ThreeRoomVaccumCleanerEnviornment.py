from modules.Enviornment import Environment
from modules.Room import Room

class ThreeRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent):
        self.rooms = 3
        self.r1 = Room('A', 'dirty')
        self.r2 = Room('B','dirty')
        self.r3 = Room('C','dirty')
        self.agent = agent
        self.currentRoom = self.r1
        self.step = 1
        self.action = ""
    def executeStep(self,n=1): 
        for _ in range(0,n):
            self.displayPerception() 
            self.agent.sense(self)
            res = self.agent.act()
            self.action = res 
            if res == 'clean':
                self.currentRoom.status = 'clean' 
            elif res == 'right':
                if self.currentRoom.location == 'A':
                    self.currentRoom = self.r2
                else:
                    self.currentRoom = self.r3
            else:
                if self.currentRoom.location == 'B':
                    self.currentRoom = self.r1
                else:
                    self.currentRoom = self.r2
            self.displayAction() 
            self.step += 1
    def executeAll(self): 
        raise NotImplementedError('action must be defined!')
    def displayPerception(self): 
        print("Perception at step %d is [%s,%s]"%(self.step,self.currentRoom.status,self.currentRoom.location))
    def displayAction(self): 
        print("------- Action taken at step %d is [%s]" %(self.step,self.action))
    def delay(self,n=100):
        self.delay = n