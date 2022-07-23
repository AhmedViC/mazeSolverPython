from Path import *
from functions import *
defaultMaze = [
    ['P','P','W','P'],
    ['P','W','W','P'],
    ['P','W','W','P'],
    ['E','P','P','P']
    ]


# W: WALL
# P:PATH
# E: END
# D: dead end

isDefaultMaze = True
newMaze = []
currentPath = []
x = 1
y = 0
while True:
    choice = menu()
    if(choice==1):
        newMaze= createMaze()
        isDefaultMaze = False
    elif(choice==2):
        currentPath = []
        print('The maze:')
        printMaze(defaultMaze)
        if not isDefaultMaze:
            print('initial location: [Row][Col] ex: 2 1')
            y = input("Row:")
            x = input("Col:")
            while not isValid(y,x,defaultMaze):
                print('invalid location')
                y = input("Row:")
                x = input("Col:")

        currentPath.append(Path(y,x))        
        mazeSolve(defaultMaze,currentPath)
    elif choice==0:
        quit()
    elif choice==3:
        if len(newMaze)==0:
            print('there is no custom maze yet..')
            continue
        else:
            currentPath = []
            printMaze(newMaze)
            print('initial location: [Row][Col] ex: 2 1')
            y = int(input("Row:"))
            x = int(input("Col:"))
            while not isValid(y,x,newMaze):
                print('invalid location')
                y = input("Row:")
                x = input("Col:")
            currentPath.append(Path(y,x))   
            mazeSolve(newMaze,currentPath)    






