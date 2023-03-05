from math import sqrt
sqrt(9)
# OR
import math
math.sqrt(9)
# OR
from math import sqrt as squareroot
squareroot(9)

import time
current_time = time.time() #time.time() returns the current time in seconds since Thursday 1st January 1970
time.ctime(current_time) # converts a time, s, measured in seconds past the epoch into a human-readable string
time.sleep(3) # wait for at least 3 seconds then returns

import random
random.randint(1, 10) # generate random integers between 1 and 10, inclusive
random.random() # generates a real-valued random number in the interval 0,1. 1 is excluded
x = [1,2,3,4,5]
random.shuffle(x) # permutes the list into a random ordering in place, i.e. it does not return a permuted copy of the original list:
print(x)
random.sample(x, 2) #randomly selects 2 elements from list and returns a new list containing those elements