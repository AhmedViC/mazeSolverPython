from time import sleep



def isValid(y,x, maze):
    if(y >= len(maze) or x>=len(maze[y]) or y<0 or x<0):
        return False;
    return True;    



def printMaze(maze):
  
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j],end=' ')

        print('\n') 

               

