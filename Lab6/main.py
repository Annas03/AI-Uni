solution = []

def backtrack(perm, sol, level):
    for i in range(len(perm)):
        temp = []
        sol.append(perm[i])
        for j in range(len(perm)):
            temp.append(perm[j])
        temp.remove(perm[i])
        if len(temp) == 0:
            t_sol = []
            for m in range(len(sol)):
                t_sol.append(sol[m])
            solution.append(t_sol)
            sol.pop()
            sol.pop()
            return
        else:
            backtrack(temp, sol, level+1)
    if(len(sol)!=0):
        sol.pop()


backtrack([1,2,3,4], [], 0)
print(solution)