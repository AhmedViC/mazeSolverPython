from time import sleep
from Path import *


def isValid(y,x, maze):
    if(y >= len(maze) or x>=len(maze[y]) or y<0 or x<0):
        return False;
    return True;    



def printMaze(maze):
  
    print('---------------------------------------------')
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print(maze[i][j],end=' ')

        print('\n') 

def menu():

    print('Welcome To maze solver using python')
    print('1- Create a custome Maze')
    print('2- Test program with default maze')
    print('3- Test with Your custome maze')
    print('0- to exit')


    choice = int(input())
    return choice

def mazeSolve(defaultMaze,currentPath):
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
                    print('moved up')
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
        
def createMaze():
    newMaze = []
   
    print('W for A wall')
    print('E for an end')
    print('P for a Path')
    print('1 to save and exit')
    counter = 0;
    while True:
        newRow=[]
        counter=len(newMaze)+1
        print('Enter Row Number ',counter,' ','ENTER 1 TO EXIT')
        str = input()
        if str=='1':
            printMaze(newMaze)
            return newMaze
            
        else:
            str = str.replace(' ','')
            for i in range(len(str)):
                if str[i]=='W' or str[i]=='E' or str[i]=='P':
                        newRow.append(str[i])
                else:
                    print('enter only valid characters')
                    newRow=[]
                    break   
            if len(newRow)!=0:
                newMaze.append(newRow)
             


                    
                





               

