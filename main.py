from Path import *
from function import *
defaultMaze = [
    ['W','W','P','W','W','P','P','P','P','W','W','W'],
    ['W','W','P','P','P','P','W','W','P','W','P','P'],
    ['W','W','P','W','W','P','W','W','P','W','P','W'],
    ['W','W','W','W','W','P','W','W','W','W','P','W'],
    ['W','W','W','W','W','P','W','W','P','W','P','W'],
    ['W','W','E','P','P','P','W','W','P','W','P','W'],
    ]


# W: WALL
# P:PATH
# E: END
# D: dead end
currentPath = []
currentPath.append(Path(1,11))


while True:
    
    y = currentPath[len(currentPath)-1].y
    x= currentPath[len(currentPath)-1].x
    defaultMaze[y][x] = 'X'
    printMaze(defaultMaze)
    sleep(3)
    if isValid(y+1,x,defaultMaze):
        if defaultMaze[y+1][x]=='E' :
            defaultMaze[y+1][x]='X'
            print('moved Down, and Won!')
            printMaze(defaultMaze)
            break
        elif defaultMaze[y+1][x]=='P':
            print('moved down..')
            currentPath.append(Path(y+1,x))
            continue
    if isValid(y-1,x,defaultMaze):
        if defaultMaze[y-1][x]=='E':
            defaultMaze[y-1][x]='X'
            printMaze(defaultMaze)
            print("moved up, You won!")
            break
        elif defaultMaze[y-1][x]=='P':
            currentPath.append(Path(y-1,x))
            continue 
    if isValid(y,x-1,defaultMaze):
        if defaultMaze[y][x-1]=='E':
            defaultMaze[y][x-1]='X'
            printMaze(defaultMaze)
            print("moved left, You won!")
            break
        elif defaultMaze[y][x-1]=='P':
            currentPath.append(Path(y,x-1))
            print("moved left")
            continue  
    if isValid(y,x+1,defaultMaze):
        if defaultMaze[y][x+1]=='E':
            defaultMaze[y][x+1]='X'
            printMaze(defaultMaze)
            print("moved right, You won!")
            break
        elif defaultMaze[y][x+1]=='P':
            currentPath.append(Path(y,x+1))
            print("moved right")
            continue  

    if currentPath.pop():

        print('move Back')
        defaultMaze[y][x] = 'D'
    if(len(currentPath)==0):
        print('not solvable')   
        break    
   




