# MazeSolver

A simple rectangular m x n maze can be specified as m n-length strings in a file
such that position (x,y) in the maze corresponds to a wall(#), corridor(-), current
position(*) or goal($). A sample 3 x 5 maze is as follows:

#####

#--*#

#$###

The upper left, upper right, lower left and lower right corners of the maze have
co-ordinates (0,0), (0,n-1), (m-1,0), and (m-1,n-1), respectively, on the 2-D
integer plane. A move on the 2-D integer plane can be specified as follows:


"up": y = y - 1
"down": y = y + 1
"left": x = x - 1
"right": x = x + 1

maze1.py


A script takes as command-line
arguments a maze file. The maze should be printed out and the user should be
asked what direction they wish to move in the maze by entering a
{u,d,l,r,q}(where entering a q will quit the game). The maze should be printed
with the current position updated. If the outcome of the move would hit a wall
(i.e move to a position with a {#} in it) don’t move the current position and
inform the user that a wall was hit. If the move would move the current position
to a location with a $ in it the program should end and the user should be
informed that the maze has been solved.


Your script should check to see if the maze file that is being read is a valid
maze. A valid maze must be m*n in dimensions, it must have one and only one
* and $. Column 0 and n-1 and Row 0 and m-1 has to only contain # symbols
and one symbol in one of those columns and rows can contain a $.Question #2
Modify maze1.py so that instead of the user entering in which direction to
move next, the script will automatically solve the maze making one move at a
time.
Write and document a Python script maze2.py which takes as command-line
arguments a maze file. Your script should always try to move up before down,
down before left and left before right. Your script should use a stack to move
around the maze and should never try to same move in the same position twice.
