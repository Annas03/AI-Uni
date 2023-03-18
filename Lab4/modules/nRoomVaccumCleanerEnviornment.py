from modules.Enviornment import Environment
from modules.Room import Room

class nRoomVaccumCleanerEnvironment(Environment):
    def __init__(self, agent, rooms=2):
        if rooms < 2:
            print('rooms must be greater or equal to 2')
        else:
            self.Rooms = []
            self.allRoomsCleaned = False
            for i in range(rooms):
                self.Rooms.append(Room(str(i+1), 'dirty'))
            self.agent = agent
            self.currentRoom = self.Rooms[0]
            self.step = 1
            self.action = ""
            self.delay = 1000

    def executeStep(self, n=1):
        for i in range(len(self.Rooms)):
            if self.Rooms[i].status == 'clean': self.allRoomsCleaned = True
            else: self.allRoomsCleaned = False
        
        if self.allRoomsCleaned == True: self.displayResult()

        else:  
            for _ in range(0,n):
                self.displayPerception() 
                self.agent.sense(self)
                res = self.agent.act()
                self.action = res 
                if res == 'clean':
                    self.currentRoom.status = 'clean' 
                elif res == 'right':
                    self.currentRoom = self.Rooms[int(self.currentRoom.location)]
                else:
                    self.currentRoom = self.Rooms[int(self.currentRoom.location)-2]
                self.displayAction() 
                self.step += 1

    def executeAll(self): 
        raise NotImplementedError('action must be defined!')
    
    def displayPerception(self): 
        print("Perception at step %d is [%s,Room %s]"%(self.step,self.currentRoom.status,self.currentRoom.location))

    def displayAction(self): 
        print("------- Action taken at step %d is [%s]" %(self.step,self.action))

    def displayResult(self):
        print("------- All Rooms are Cleaned!!!")
        
    def delay(self,n=100):
        self.delay = n