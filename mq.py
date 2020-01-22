def numMagicSquaresInside(grid):
    
    ct = 0
    for i in range(0,len(grid)-2): # i is each row in grid
        for j in range(0,len(grid[i])-2): # j is each item in i 
            strs = grid[i][j:j+3] +  grid[i+1][j:j+3] + grid[i+2][j:j+3] # Find the contignous 3 numbers in the array
            t = set(strs) # covert strs list to  a set 
            mx,mn = max(t),min(t)
            if(len(t)==9 and mx==9 and mn==1):
                diag1 = grid[i+1][j+1] + grid[i][j] + grid[i+2][j+2]
                diag2 = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
                row1= sum(grid[i][j:j+3])
                row2= sum(grid[i+1][j:j+3])
                row3= sum(grid[i+2][j:j+3]) 
                col1=grid[i][j]+grid[i+1][j]+grid[i+2][j]
                col2=grid[i][j+1]+grid[i+1][j+1]+grid[i+2][j+1]
                col3=grid[i][j+2]+grid[i+1][j+2]+grid[i+2][j+2]
                if(diag1==diag2 and diag2==row1 and row1==row2 and row2==row3             and row3==col1 and col1==col2 and col2==col3):
                  ct+=1
    return ct

print(numMagicSquaresInside([[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]))