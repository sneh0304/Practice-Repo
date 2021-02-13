#Grid game problem from Goldman sachs OA. Similar to game of life leetcode problem.
def gridGame(grid, k, rules):
    neighbours = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]
    temp = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
    
    for i in range(k):
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                count = 0
                for p in range(len(neighbours)):
                    r = m
                    c = n
                    r += neighbours[p][0]
                    c += neighbours[p][1]
                    if r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0]):
                        if grid[r][c] == 1:
                            count += 1
                temp[m][n] = count
        print(temp)
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if rules[temp[m][n]] == 'alive':
                    grid[m][n] = 1
                else:
                    grid[m][n] = 0
        
    return grid
        
a = gridGame([[0,1,1,0], [1,1,0,0]], 2, ['dead','alive','alive','dead','dead','dead','dead','dead','dead'])

print(a)