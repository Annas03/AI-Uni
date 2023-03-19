import time
from modules.VaccumAgent import VaccumAgent
from modules.TwoRoomVaccumCleanerEnvironment import TwoRoomVaccumCleanerEnvironment
from modules.ThreeRoomVaccumCleanerEnviornment import ThreeRoomVaccumCleanerEnvironment
from modules.nRoomVaccumCleanerEnviornment import nRoomVaccumCleanerEnvironment

vcagent = VaccumAgent()
env = nRoomVaccumCleanerEnvironment(vcagent,3) 
env.executeStep(5)

print(vcagent.score)

 