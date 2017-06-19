#!/usr/bin/python3

import sys

#



def printMaze():
	for line in maze:
		print(line)
		
def findPosition():
    x = 0
    for line in maze:
		if '*' in line:
			y = line[x].index('*')
		else:
			x = x + 1
	return x
	return y


x=0
y=0
fin= open(sys.argv[1], 'r')
maze = list()

for z in fin:
   maze.append(z)
   
printMaze()


findPosition()

print(maze[0][0])
print(maze[x][y])




