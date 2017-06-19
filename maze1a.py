#!/usr/bin/python3

#########################################################
## CS 2500 (Fall 2014), Assignment #2, Question #1     ##
## Script File Name: maze1.py                          ##
## Student Name: Bradley Gavan                         ##
## Login Name: X bmg610                                ##
## MUN #: X 201208634                                  ##
## This programs reads a maze and prompts the user to  ##
## solve it.  It firstly reads a maze from an inputed  ##
## file and then writes it as a list of lists. Secondly##
## it checks that the maze is indeed valid (it has a   ##
## proper border, contains one exit, contains one      ##
## starting point and has no inappropriate characters. ##
## Next it prints the maze for the user to see.  Then  ##
## it finds the starting position and asks the user to ##
## input what direction they would like to move in. If ##
## the inputed direction is a valid move, it changes   ##
## the current position and replaces the former        ##
## position with an 'X'.  And continues like this until##
## the exit is reached, at which point the program     ##
## prints that you won.  They program can be exited at ##
## any time by input the direction as 'q'.             ##
#########################################################

import sys

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
fin= open(sys.argv[1], 'r')
maze = list()
for line in fin:
	l = list(line)
	l = l[0:len(l)-1]
	maze.append(l)
   
checkValidMaze()
printMaze()

while (direction != 'q'):
  findPosition()
  direction = input('What direction would you like to move in?')

  if direction == 'l':
     if maze[x][y-1] == '#':
        print('Error, try again')
     elif maze[x][y-1] == '$':
        print("Congratulations, you win!")
        printMaze()
        sys.exit()
     else:
        maze[x][y] = 'X'
        maze[x][y-1] = '*'
        printMaze()           
  elif direction == 'r':
     if maze[x][y+1] == '#':
        print('Error, try again')
     elif maze[x][y+1] == '$':
        print("Congratulations, you win!")
        printMaze()
        sys.exit()
     else:
        maze[x][y] = 'X'
        maze[x][y+1] = '*'
        printMaze()        
  elif direction == 'u':
     if maze[x-1][y] == '#':
        print('Error, try again')
     elif maze[x-1][y] == '$':
        print("Congratulations, you win!")
        printMaze()
        sys.exit()
     else:
        maze[x][y] = 'X'
        maze[x-1][y] = '*'
        printMaze()
  elif direction == 'd':
     if maze[x+1][y] == '#':
        print('Error, try again')
     elif maze[x+1][y] == '$':
        print("Congratulations, you win!")
        printMaze()
        sys.exit()
     else:
        maze[x][y] = 'X'
        maze[x+1][y] = '*'
        printMaze()

  
sys.exit()
      