#!/usr/bin/python3

#########################################################
## CS 2500 (Fall 2014), Assignment #2, Question #2     ##
## Script File Name: maze2.py                          ##
## Student Name: Bradley Gavan                         ##
## Login Name: X bmg610                                ##
## MUN #: X 201208634                                  ##
## This programs reads a maze and solves it itself. It ##
## firstly reads a maze from an inputed file and then  ##
## writes it as a list of lists. Secondly it checks    ##
## that the maze is indeed valid (it has a proper      ##
## border, contains one exit, contains one starting    ##
## point and has no inappropriate characters.  Next it ##
## prints the maze.  Then it creates a stack which     ##
## includes the current position and a list of possible##
## moves.  It also creates a second stack contain only ##
## the current position.  It then pops the stack       ##
## looking for a valid move.  Once a valid move is     ##
## found, it changes the current position and replaces ##
## the former position with an 'X'.  After if finds a  ##
## valid move, it pushes the new position onto the     ##
## position stack and pushes the position and list of  ##
## moves onto the moves stack.  It continues like this ##
## until the exit is reached, at which point the       ##
## program prints that you won.                        ##
#########################################################

import sys

def stackMoves():
  global x
  global y
  global stack
  global stackPosition
  findPosition()
  l = []
  l.append(x)
  l.append(y)
  stackPosition.append(l)
  stack.append(l)
  stack.append('r')
  stack.append('l')
  stack.append('d')
  stack.append('u')

  
def printMaze():
	for line in maze:
		print(line)

def findPosition():
   global x
   global y
   x = 0
   for line in maze:
      if '*' in line:
         y = line.index('*')
         break
      else:
         x = x + 1
         
def checkValidMaze():
   borderDollaSign = 0
   dollaSignCount = 0
   asterixCount = 0
   i = 0
   j = 0
   m = len(maze[0])
   for line in maze:
      for a in line:
         if ord(a) == ord('$'):
            dollaSignCount = dollaSignCount + 1
         elif ord(a) == ord('*'):
            asterixCount = asterixCount + 1
   if dollaSignCount != 1 or asterixCount != 1:
      print('Invalid maze1')
      sys.exit()    
   for b in maze[0]:
      if ord(b) == ord('$'):
         borderDollaSign = borderDollaSign + 1
      elif ord(b) != ord('#') and ord(b) != ord('$'):
         print('Invalid maze2')
         sys.exit()
   for c in maze[len(maze)-1]:
      if ord(c) == ord('$'):
         borderDollaSign = borderDollaSign + 1
      elif ord(c) != ord('#') and ord(c) != ord('$'):
         print('Invalid maze3')
         sys.exit()
   for d in maze[i][0]:
      if ord(b) == ord('$'):
         borderDollaSign = borderDollaSign + 1
      elif ord(d) != ord('#') and ord(d) != ord('$'):
         print('Invalid maze4')
         sys.exit()
      else:
         i = i + 1
   for e in maze[j][m-1]:
      if ord(b) == ord('$'):
         borderDollaSign = borderDollaSign + 1
      elif ord(e) != ord('#') and ord(e) != ord('$'):
         print('Invalid maze5')
         sys.exit()
      else: 
         j = j + 1
   for f in maze:
      for g in f:
         if ord(g) != ord('#')and ord(g) != ord('$') and ord(g) != ord('-') and ord(g) != ord('*'):
            print(g)
            print('Invalid maze6')
            sys.exit()
   if len(maze) < 3:
      print('Invalid maze7')
      sys.exit()
   for h in maze:
      if len(h) != m:
         print('Invalid maze7')
         sys.exit()
   
x = 0
y = 0
direction = 0
stack = []
stackPosition = []
fin= open(sys.argv[1], 'r')
maze = list()
for line in fin:
	l = list(line)
	l = l[0:len(l)-1]
	maze.append(l)
   
checkValidMaze()
printMaze()
print()
stackMoves()

while (True):
  direction = stack.pop()
  if direction == 'l':
     if maze[x][y-1] == '$':
        print("Congratulations, you win!")
        sys.exit()
     elif maze[x][y-1] == '#':
        pass   
     elif maze[x][y-1] == 'X':
        pass
     else:
        maze[x][y] = 'X'
        maze[x][y-1] = '*'
        stackMoves()
        
  elif direction == 'r':
     if maze[x][y+1] == '$':
        print("Congratulations, you win!")
        sys.exit()
     elif maze[x][y+1] == '#':
        pass
     elif maze[x][y+1] == 'X':
        pass
     else:
        maze[x][y] = 'X'
        maze[x][y+1] = '*'
        stackMoves()
      
  elif direction == 'u':
     if maze[x-1][y] == '$':
        print("Congratulations, you win!")
        sys.exit()
     elif maze[x-1][y] == '#':
        pass 
     elif maze[x-1][y] == 'X':
        pass  
     else:
        maze[x][y] = 'X'
        maze[x-1][y] = '*'
        stackMoves()
    
  elif direction == 'd':
     if maze[x+1][y] == '$':
        print("Congratulations, you win!")
        sys.exit()
     elif maze[x+1][y] == '#':
        pass
     elif maze[x+1][y] == 'X':
        pass   
     else:
        maze[x][y] = 'X'
        maze[x+1][y] = '*'
        stackMoves()
  else:
     x = direction[0]
     y = direction[1]
     maze[x][y] = 'X'
     position = stackPosition.pop()
     position = stackPosition.pop()
     x = position[0]
     y = position[1]
     maze[x][y] = '*'
      
  printMaze()
  print(stack)
  

      