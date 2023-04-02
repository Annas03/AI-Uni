solution = []

def queenIsSafe(row, column):
    # checking if row and diagonal is safe or not
    i = 0
    while(i<len(solution)-1):
        if solution[i] == row or abs(row - solution[i]) == abs(column - solution[i+1]):
            return False
        i+=2
    return True

def setQueen(column, queens):
    if queens == 8:
        return True
    for i in range(8):
        if queenIsSafe(i, column):
            queens+=1
            solution.append(i)
            solution.append(column)
            if setQueen(column+1, queens):
                return True
            else:
                solution.pop()
                solution.pop()
                queens-=1

    return False

queens = 0
setQueen(0,0)
print(solution)
