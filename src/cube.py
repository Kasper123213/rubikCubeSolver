from copy import deepcopy
from surface import Surface
from OpenGL.GL import *
from OpenGL.raw.GLU import gluCylinder, gluDisk, gluQuadricTexture

class Cube:

    surfaces = [
                                                              [[Surface('W') for _ in range(3)] for _ in range(3)],
        [[Surface('G') for _ in range(3)] for _ in range(3)], [[Surface('R') for _ in range(3)] for _ in range(3)], [[Surface('B') for _ in range(3)] for _ in range(3)],
                                                              [[Surface('Y') for _ in range(3)] for _ in range(3)],
                                                              [[Surface('O') for _ in range(3)] for _ in range(3)],
    ]

    #colors
    cube =[
                                                        [['W'for _ in range(3)]for _ in range(3)],
           [['G'for _ in range(3)]for _ in range(3)],   [['R'for _ in range(3)]for _ in range(3)],    [['B'for _ in range(3)]for _ in range(3)],
                                                        [['Y'for _ in range(3)]for _ in range(3)],
                                                        [['O'for _ in range(3)]for _ in range(3)]
           ]



    def setCube(self, colors):
        for surface in range(6):
            for row in range(3):
                for col in range(3):
                    self.cube[surface][row][col] = colors[surface+row+col]



    def printCube(self):
        for i in range(3):
            print("\t"*4, " ", self.cube[0][i])
        print()
        for i in range(3):
            print(self.cube[1][i],",", end = "")
            print(" ",self.cube[2][i],",", end = "")
            print(" ",self.cube[3][i])
        print()
        for j in range(2):
            for i in range(3):
                print("\t"*4, " ", self.cube[4+j][i])
            print()

    def swapFours(self, arg0, arg1, arg2, arg3):
        temp = self.cube[arg1[0]][arg1[1]][arg1[2]]
        self.cube[arg1[0]][arg1[1]][arg1[2]] = self.cube[arg0[0]][arg0[1]][arg0[2]]

        temp2 = self.cube[arg2[0]][arg2[1]][arg2[2]]
        self.cube[arg2[0]][arg2[1]][arg2[2]] = temp


        temp = self.cube[arg3[0]][arg3[1]][arg3[2]]
        self.cube[arg3[0]][arg3[1]][arg3[2]] = temp2

        self.cube[arg0[0]][arg0[1]][arg0[2]] = temp




    def rotateSurface(self, surfaceIndex, toLeft):
        surface = deepcopy(self.cube[surfaceIndex])

        if toLeft:
            for i in range(3):
                for j in range(3):
                    self.cube[surfaceIndex][i][j] = surface[j][2-i]
        else:
            for i in range(3):
                for j in range(3):
                    self.cube[surfaceIndex][j][2-i] = surface[i][j]




    #####################_moves_#############################
    #b moves
    def moveB(self):
        for i in range(3):
            self.swapFours((0,0,i),(1,2-i,0),(4,2,2-i),(3,i,2))

        self.rotateSurface(5, True)


    def moveb(self):
        for i in range(3):
            self.swapFours((0,0,i),(1,2-i,0),(4,2,2-i),(3,i,2))
            self.swapFours((0,1,i),(1,2-i,1),(4,1,2-i),(3,i,1))

        self.rotateSurface(5, True)


    #f moves

    def moveF(self):
        for i in range(3):
            self.swapFours((0,2,i),(3,i,0),(4,0,2-i),(1,2-i,2))

        self.rotateSurface(2, False)

    def movef(self):
        for i in range(3):
            self.swapFours((0,2,i),(3,i,0),(4,0,2-i),(1,2-i,2))
            self.swapFours((0,1,i),(3,i,1),(4,1,2-i),(1,2-i,1))

        self.rotateSurface(2, False)

    #d moves

    def moveD(self):
        for i in range(3):
            self.swapFours((2,2,i),(3,2,i),(5,0,2-i),(1,2,i))

        self.rotateSurface(4, False)

    def moved(self):
        for i in range(3):
            self.swapFours((2,2,i),(3,2,i),(5,0,2-i),(1,2,i))
            self.swapFours((2,1,i),(3,1,i),(5,1,2-i),(1,1,i))

        self.rotateSurface(4, False)


    #l moves

    def moveL(self):
        for i in range(3):
            self.swapFours((0,i,0),(2,i,0),(4,i,0),(5,i,0))

        self.rotateSurface(1, False)

    def movel(self):
        for i in range(3):
            self.swapFours((0,i,0),(2,i,0),(4,i,0),(5,i,0))
            self.swapFours((0,i,1),(2,i,1),(4,i,1),(5,i,1))

        self.rotateSurface(1, False)


    #________________Graphic_______________


    def draw(self, quadric):
        for surface in range(6):
            for row in range(3):
                for col in range(3):
                    self.surfaces[surface][row][col].draw(quadric)



