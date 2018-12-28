
def dfs(x,y):
    if(x == width+2 or x == -1 or y == height+2 or y == -1):
        return
    if(visited[y][x] == True or board[y][x] == 1 or board[y][x] == 2):
        return
    visited[y][x] = True
    board[y][x] = 2
    dfs(x,y+1)
   
    dfs(x+1,y)
 
    dfs(x-1,y)
    dfs(x,y-1)
    visited[y][x] = False
    


count = 0;
height,width = map(int, input().split())
board = [[0 for i in range(width + 2)]]
visited = [[False for i in range(width + 2)]]



for i in range(height):
    line = input()
    temp = [0]
    temp2 = [False for _ in range(width + 2)]
    for c in line:
        temp.append(int(c))
        
    temp.append(0)
    board.append(temp)
    visited.append(temp2)
board.append([0 for i in range(width + 2)])
visited.append([False for i in range(width + 2)])

dfs(0,0)

for i in range(len(board)):
    for j in range(len(board[i])):
        print(board[i][j],end = "")
    print()


