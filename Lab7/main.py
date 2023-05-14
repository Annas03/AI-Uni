import random
def toProve(x,y,z):
    return 5*x**3 - 6*y**2 + 8*z - 1

def Fitness(x,y,z):
    fitness = toProve(x,y,z)
    if fitness == 0:
        return 99999
    else:
        return abs(1/fitness)
    
# Generate Solutions/Population/Generation 0
solutions = []
for _ in range(10000):
    solutions.append((random.uniform(0, 10000), random.uniform(0, 10000), random.uniform(0, 10000)))

for i in range(1000):
    
    # Generate RankedSolutions
    rankedSolutions = []
    for s in solutions:
        rankedSolutions.append((Fitness(s[0],s[1],s[2]), s))
    rankedSolutions.sort(reverse=True)

    print("---Generation {i}---")

    bestSolutions = rankedSolutions[:1000]

    print(bestSolutions[0])

    # Mixing bestSolutions
    bestElementX = []
    bestElementY = []
    bestElementZ = []
    for i in bestSolutions:
        bestElementX.append(i[1][0])
        bestElementY.append(i[1][1])
        bestElementZ.append(i[1][2])
    
    # Creating a Optimized Generation
    newGen = []
    for _ in range(10000):
        newGen.append((random.choice(bestElementX),random.choice(bestElementY),random.choice(bestElementZ)))
    
    solutions = newGen