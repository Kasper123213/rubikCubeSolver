import time
from copy import deepcopy
from surface import Surface
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.raw.GLU import gluCylinder, gluDisk, gluQuadricTexture

class Cube:
    currentSet = None

    currentRotation = None
    rotatedSurfaces = []
    rotationDic = { #1,0,0 w gore 0,1,0 w lewo 0,0,1 przeciwnie do rucchu wskazowek
        'W':[-1, 0, 1, 0],
        'G':[1, 1, 0, 0],
        'R':[1, 0, 0, 1],
        'B':[-1, 1, 0, 0],
        'Y':[1, 0, 1, 0],
        'O':[-1, 0, 0, 1]
    }

    #colors
    cube =[
        [['W'for _ in range(3)]for _ in range(3)],
        [['G'for _ in range(3)]for _ in range(3)],   [['R'for _ in range(3)]for _ in range(3)],    [['B'for _ in range(3)]for _ in range(3)],
        [['Y'for _ in range(3)]for _ in range(3)],
        [['O'for _ in range(3)]for _ in range(3)]
    ]

    quadric = gluNewQuadric()

    def createSurfaces(self):
        self.surfaces = [
            [[Surface('W') for _ in range(3)] for _ in range(3)],
            [[Surface('G') for _ in range(3)] for _ in range(3)], [[Surface('R') for _ in range(3)] for _ in range(3)],
            [[Surface('B') for _ in range(3)] for _ in range(3)],
            [[Surface('Y') for _ in range(3)] for _ in range(3)],
            [[Surface('O') for _ in range(3)] for _ in range(3)],
        ]
    def setSurfaces(self, colors):
        index = 0
        for surface in range(6):
            for row in range(3):
                for col in range(3):
                    self.cube[surface][row][col] = colors[index]
                    index += 1



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
                    self.rotatedSurfaces += [(surfaceIndex, i, j)]
        else:
            for i in range(3):
                for j in range(3):
                    self.cube[surfaceIndex][j][2-i] = surface[i][j]
                    self.rotatedSurfaces += [(surfaceIndex, i, j)]




    #####################_moves_#############################


    #rotate around white center
    def moveW(self):
        for i in range(3):
            self.swapFours((5,2,i),(3,0,2-i),(2,0,2-i),(1,0,2-i))
            self.rotatedSurfaces += [(5,2,i),(3,0,2-i),(2,0,2-i),(1,0,2-i)]
        self.rotateSurface(0, False)

        self.currentRotation = 'W'

    #rotate around green center
    def moveG(self):
        for i in range(3):
            self.swapFours((0,i,0),(2,i,0),(4,i,0),(5,i,0))
            self.rotatedSurfaces += [(0,i,0),(2,i,0),(4,i,0),(5,i,0)]
        self.rotateSurface(1, False)

        self.currentRotation = 'G'


    #rotate around red center
    def moveR(self):
        for i in range(3):
            self.swapFours((0,2,i),(3,i,0),(4,0,2-i),(1,2-i,2))
            self.rotatedSurfaces += [(0,2,i),(3,i,0),(4,0,2-i),(1,2-i,2)]
        self.rotateSurface(2, False)

        self.currentRotation = 'R'


    # rotate around blue center
    def moveB(self):
        for i in range(3):
            self.swapFours((0,2-i,2),(5,2-i,2),(4,2-i,2),(2,2-i,2))
            self.rotatedSurfaces += [(0,2-i,2),(5,2-i,2),(4,2-i,2),(2,2-i,2)]
        self.rotateSurface(3, False)

        self.currentRotation = 'B'


    #rotate around yellow center
    def moveY(self):
        for i in range(3):
            self.swapFours((2,2,i),(3,2,i),(5,0,2-i),(1,2,i))
            self.rotatedSurfaces += [(2,2,i),(3,2,i),(5,0,2-i),(1,2,i)]
        self.rotateSurface(4, False)

        self.currentRotation = 'Y'


    # rotate around orange center
    def moveO(self):
        for i in range(3):
            self.swapFours((0,0,i),(1,2-i,0),(4,2,2-i),(3,i,2))
            self.rotatedSurfaces += [(0,0,i),(1,2-i,0),(4,2,2-i),(3,i,2)]

        self.rotateSurface(5, False)

        self.currentRotation = 'O'





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


    def draw(self, angle = 0):
        for surface in range(6):
            for row in range(3):
                for col in range(3):

                    if (surface, row, col) in self.rotatedSurfaces and self.currentRotation is not None:
                        angleVector = deepcopy(self.rotationDic.get(self.currentRotation))
                        angleVector[0] *= angle
                        self.surfaces[surface][row][col].draw(self.quadric, angleVector)
                    else:
                        self.surfaces[surface][row][col].draw(self.quadric)


        if angle == 0:
            self.rotatedSurfaces = []


    def loadParameters(self):
        anglesMap = {0:(90, 1, 0, 0), 1:(90, 0, 1, 0), 2:(0, 0, 1, 0), 3:(90, 0, 1, 0), 4:(90, 1, 0, 0), 5:(0, 0, 1, 0),}


        for surface in range(6):
            for row in range(3):
                for col in range(3):
                    self.surfaces[surface][row][col].setColor(self.cube[surface][row][col])
                    self.surfaces[surface][row][col].angle = anglesMap.get(surface)
                    self.surfaces[surface][row][col].setPos(surface, row, col)


    def saveCube(self, filename = "example.txt"):
        with open(filename, "w") as file:
            text = ""
            for s in range(6):
                for r in range(3):
                    for c in range(3):
                        text += self.cube[s][r][c]
                        text += "\n"



            file.write(text)

    def readFromFile(self, filename = "example.txt"):
        surfaces = []
        with open(filename, "r") as file:
            for line in file:
                surfaces.append(line.strip())

        self.setSurfaces(surfaces)
        self.loadParameters()


    def getSurfaces(self):
        notations = {
            'G': 'F',
            'W': 'U',
            'B': 'B',
            'R': 'R',
            'O': 'L',
            'Y': 'D'
        }

        state = ""
        for surface in (0, 2, 1, 4, 5, 3):
            for row in range(3):
                for col in range(3):
                    if surface == 4:
                        state += notations.get(self.cube[surface][2-col][row])
                    elif surface == 5:
                        state += notations.get(self.cube[surface][2-row][2-col])
                    elif surface == 0:
                        state += notations.get(self.cube[surface][col][2-row])
                    else:
                        state += notations.get(self.cube[surface][row][col])
        return state

    def isSolved(self):
        colors = {0:'W', 1:'G', 2:'R', 3:'B', 4:'Y', 5:'O'}

        for surface in range(6):
            for row in range(3):
                for col in range(3):
                    if self.cube[surface][row][col] != colors.get(surface):
                        return False
        return True

    def reset(self):
        for surface in range(6):
            for row in range(3):
                for col in range(3):
                    self.cube[surface][row][col] = 'X'

        self.cube[0][0][0] = 'S'
        self.loadParameters()

        self.currentSet = [0, 0, 0]

    def setNext(self, color):
        self.cube[self.currentSet[0]][self.currentSet[1]][self.currentSet[2]] = color


        self.currentSet[2]+=1

        if self.currentSet[2]>2:
            self.currentSet[2] = 0
            self.currentSet[1] += 1
            if self.currentSet[1]>2:
                self.currentSet[1] = 0
                self.currentSet[0] += 1
                if self.currentSet[0] > 5:
                    self.currentSet = None
                    return
        self.cube[self.currentSet[0]][self.currentSet[1]][self.currentSet[2]] = 'S'

        self.loadParameters()


    def isSet(self):
        if self.currentSet is None:
            return True
        else:
            return False

    def setPos(self):
        if self.cube[0][1][1] != 'W':
            if self.cube[1][1][1] == 'W':
                self.fullRotateY()
                self.fullRotateX()
                self.fullRotateX()
                self.fullRotateX()
            elif self.cube[2][1][1] == 'W':
                self.fullRotateX()
            elif self.cube[3][1][1] == 'W':
                self.fullRotateY()
                self.fullRotateX()
            elif self.cube[4][1][1] == 'W':
                self.fullRotateX()
                self.fullRotateX()
            else:
                self.fullRotateX()
                self.fullRotateX()
                self.fullRotateX()


        if self.cube[1][1][1] != 'G':
            if self.cube[0][1][1] == 'G':
                self.fullRotateX()
                self.fullRotateY()
                self.fullRotateY()
                self.fullRotateY()
            elif self.cube[2][1][1] == 'G':
                self.fullRotateY()
            elif self.cube[3][1][1] == 'G':
                self.fullRotateY()
                self.fullRotateY()
            elif self.cube[4][1][1] == 'G':
                self.fullRotateX()
                self.fullRotateY()
            else:
                self.fullRotateY()
                self.fullRotateY()
                self.fullRotateY()

        self.loadParameters()
