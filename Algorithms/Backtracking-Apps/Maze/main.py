from Maze_class import *


def readvaluepair(infile):
    line = infile.readline()
    valA, valB = line.split()
    return int(valA), int(valB)


def buildMaze(filename):
    infile = open(filename, "r")
    r, c = readvaluepair(infile)
    maze = Maze(r, c)
    r, c = readvaluepair(infile)
    maze.setStart(r, c)
    r, c = readvaluepair(infile)
    maze.setEnd(r, c)
    for i in range(maze.numRows):
        tmp = infile.readline()
        for j in range(maze.numCols):
            if tmp[j] == "*":
                maze.setWall(i, j)
    infile.close()
    return maze


def main():
    maze = buildMaze("maze.txt")
    if maze.Find():
        print("Path found.")
        maze.draw()
    else:
        print("Path not found.")


main()
