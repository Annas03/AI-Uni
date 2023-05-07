
def arrange(stackA, stackB, stackC):

    while True:

        if(len(stackB) == 0 or (len(stackA)!=0 and stackB[0] - stackA[0] == 1)):
            stackB.insert(0, stackA[0])
            stackA.pop(0)
            continue
        if(len(stackA) != 0 and (len(stackC) == 0 or stackA[0] < stackC[0])):
            stackC.insert(0, stackA[0])
            stackA.pop(0)

        if(len(stackC) != 0 and len(stackB) != 0):
            if(len(stackA) != 0 and (stackA[0] - stackB[0] < 0)):
                stackB = arrange(stackA[:], stackB[:], [])
                stackA = stackC
                stackC = []
            elif(len(stackA) != 0 and (stackA[0] - stackC[0] < 0)):
                stackA = arrange(stackC[:], stackA[:], [])
                stackC = []
            elif (stackB[len(stackB)-1] > stackC[len(stackC)-1]):
                stackB = arrange(stackC[:], stackB[:], [])
                stackC = []
            else:
                stackC = arrange(stackB[:], stackC[:], [])
                stackB = []

        if(len(stackA) == 0):
            if(len(stackB) == 0):
                return stackC
            elif(len(stackC) == 0):
                return stackB

stackA = [1,2,3,4,5,6,7]
stackB = []
stackC = []
print(arrange(stackA, stackB, stackC))
