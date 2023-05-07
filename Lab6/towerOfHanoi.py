
def arrange(stackA, stackB, stackC):
    while True:
        if(len(stackA) == 0):
            if(len(stackB) == 0):
                return stackC
            elif(len(stackC) == 0):
                return stackB
            elif (stackB[len(stackB)-1] > stackC[len(stackC)-1]):
                temp1 = stackC[:]
                temp2 = stackB[:]
                stackB = arrange(temp1, temp2, [])
                stackC = []
            else:
                temp1 = stackB[:]
                temp2 = stackC[:]
                stackC = arrange(temp1, temp2, [])
                stackB = []
            continue
            
        if(len(stackB) == 0 or stackB[0] - stackA[0] == 1):
            stackB.insert(0, stackA[0])
            stackA.pop(0)
            continue
        if((len(stackC) == 0 or stackA[0] < stackC[0]) and len(stackA) != 0):
            stackC.insert(0, stackA[0])
            stackA.pop(0)

        if(len(stackC) != 0 and len(stackB) != 0):
            if(len(stackA) != 0 and (stackA[0] - stackB[0] < 0)):
                temp1 = stackA[:]
                temp2 = stackB[:]
                stackB = arrange(temp1, temp2, [])
                stackA = stackC
                stackC = []
            elif(len(stackA) != 0 and (stackA[0] - stackC[0] < 0)):
                temp1 = stackC[:]
                temp2 = stackA[:]
                stackA = arrange(temp1, temp2, [])
                stackC = []
            elif (stackB[len(stackB)-1] > stackC[len(stackC)-1]):
                temp1 = stackC[:]
                temp2 = stackB[:]
                stackB = arrange(temp1, temp2, [])
                stackC = []
            else:
                temp1 = stackB[:]
                temp2 = stackC[:]
                stackC = arrange(temp1, temp2, [])
                stackB = []


stackA = [1,2,3,4]
stackB = []
stackC = []
print(arrange(stackA, stackB, stackC))