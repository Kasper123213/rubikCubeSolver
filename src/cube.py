import time
from copy import deepcopy
from surface import Surface
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.raw.GLU import gluCylinder, gluDisk, gluQuadricTexture

class Cube:

    #colors
    cube =[
                                                        [['W'for _ in range(3)]for _ in range(3)],
           [['G'for _ in range(3)]for _ in range(3)],   [['R'for _ in range(3)]for _ in range(3)],    [['B'for _ in range(3)]for _ in range(3)],
                                                        [['Y'for _ in range(3)]for _ in range(3)],
                                                        [['O'for _ in range(3)]for _ in range(3)]
           ]

    quadric = gluNewQuadric()
    # def setCube(self):
    #     colorsMap = {0:'W', 1:'G', 2:'R', 3:'B', 4:'Y', 5:'O'}
    #     for surface in range(6):
    #         row = []
    #         for r in range(3):
    #             col = []
    #             for c in range(3):
    #                 col.append(Surface(colorsMap.get(surface)))
    #             row.append(col)
    #         self.surfaces.append(row)




    def createSurfaces(self):
        self.surfaces = [
            [[Surface('W') for _ in range(3)] for _ in range(3)],
            [[Surface('G') for _ in range(3)] for _ in range(3)], [[Surface('R') for _ in range(3)] for _ in range(3)],
            [[Surface('B') for _ in range(3)] for _ in range(3)],
            [[Surface('Y') for _ in range(3)] for _ in range(3)],
            [[Surface('O') for _ in range(3)] for _ in range(3)],
        ]
    def setSurface(self, colors):
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
    # #b moves
    # def moveB(self):
    #     for i in range(3):
    #         self.swapFours((0,0,i),(1,2-i,0),(4,2,2-i),(3,i,2))
    #
    #     self.rotateSurface(5, True)
    #
    #
    # def moveb(self):
    #     for i in range(3):
    #         self.swapFours((0,0,i),(1,2-i,0),(4,2,2-i),(3,i,2))
    #         self.swapFours((0,1,i),(1,2-i,1),(4,1,2-i),(3,i,1))
    #
    #     self.rotateSurface(5, True)
    #
    #
    # #f moves
    #
    # def moveF(self):
    #     for i in range(3):
    #         self.swapFours((0,2,i),(3,i,0),(4,0,2-i),(1,2-i,2))
    #
    #     self.rotateSurface(2, False)
    #
    # def movef(self):
    #     for i in range(3):
    #         self.swapFours((0,2,i),(3,i,0),(4,0,2-i),(1,2-i,2))
    #         self.swapFours((0,1,i),(3,i,1),(4,1,2-i),(1,2-i,1))
    #
    #     self.rotateSurface(2, False)
    #
    # #d moves
    #
    # def moveD(self):
    #     for i in range(3):
    #         self.swapFours((2,2,i),(3,2,i),(5,0,2-i),(1,2,i))
    #
    #     self.rotateSurface(4, False)
    #
    # def moved(self):
    #     for i in range(3):
    #         self.swapFours((2,2,i),(3,2,i),(5,0,2-i),(1,2,i))
    #         self.swapFours((2,1,i),(3,1,i),(5,1,2-i),(1,1,i))
    #
    #     self.rotateSurface(4, False)
    #
    #
    # #l moves
    #
    # def moveL(self):
    #     for i in range(3):
    #         self.swapFours((0,i,0),(2,i,0),(4,i,0),(5,i,0))
    #
    #     self.rotateSurface(1, False)
    #
    # def movel(self):
    #     for i in range(3):
    #         self.swapFours((0,i,0),(2,i,0),(4,i,0),(5,i,0))
    #         self.swapFours((0,i,1),(2,i,1),(4,i,1),(5,i,1))
    #
    #     self.rotateSurface(1, False)

    #rotate around white center
    def moveW(self):
        for i in range(3):
            self.swapFours((5,2,i),(3,0,i),(2,0,2-i),(1,0,2-i))
        self.rotateSurface(0, False)


    #rotate around green center
    def moveG(self):
        for i in range(3):
            self.swapFours((0,i,0),(2,i,0),(4,i,0),(5,i,0))
        self.rotateSurface(1, False)


    #rotate around red center
    def moveR(self):
        for i in range(3):
            self.swapFours((0,2,i),(3,i,0),(4,0,2-i),(1,2-i,2))
        self.rotateSurface(2, False)


    # rotate around blue center
    def moveB(self):
        for i in range(3):
            self.swapFours((0,2-i,2),(5,2-i,2),(4,2-i,2),(2,2-i,2))
        self.rotateSurface(3, False)


    #rotate around yellow center
    def moveY(self):
        for i in range(3):
            self.swapFours((2,2,i),(3,2,i),(5,0,2-i),(1,2,i))
        self.rotateSurface(4, False)


    # rotate around orange center
    def moveO(self):
        for i in range(3):
            self.swapFours((0,0,i),(1,2-i,0),(4,2,2-i),(3,i,2))

        self.rotateSurface(5, False)





    def fullRotateY(self):
        surface = deepcopy(self.cube[1])
        self.cube[1] = deepcopy(self.cube[2])
        self.cube[2] = deepcopy(self.cube[3])

        for i in range(3):
            self.cube[3][i] = deepcopy(self.cube[5][2-i][::-1])

        for i in range(3):
            self.cube[5][i] = surface[2-i][::-1]

        self.rotateSurface(0, False)
        self.rotateSurface(4, True)

    def fullRotateX(self):
        surface = deepcopy(self.cube[0])
        self.cube[0] = deepcopy(self.cube[2])
        self.cube[2] = deepcopy(self.cube[4])
        self.cube[4] = deepcopy(self.cube[5])
        self.cube[5] = surface

        self.rotateSurface(1, True)
        self.rotateSurface(3, False)



    #________________Graphic_______________


    def draw(self):
        for surface in range(6):
            for row in range(3):
                for col in range(3):
                    self.surfaces[surface][row][col].draw(self.quadric)


    def loadParameters(self):
        anglesMap = {0:(90, 1, 0, 0), 1:(90, 0, 1, 0), 2:(0, 0, 1, 0), 3:(90, 0, 1, 0), 4:(90, 1, 0, 0), 5:(0, 0, 1, 0),}
        # self.surfaces[0][0][0].
        # self.surfaces[0][0][0].setPos(0, 0, 0)
        # self.surfaces[1][0][0].setPos(1, 0, 0)

        for surface in range(6):
            for row in range(3):
                for col in range(3):
                    self.surfaces[surface][row][col].setColor(self.cube[surface][row][col])
                    self.surfaces[surface][row][col].angle = anglesMap.get(surface)
                    self.surfaces[surface][row][col].setPos(surface, row, col)
