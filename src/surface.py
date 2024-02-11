from OpenGL.GL import *
from OpenGL.GLU import *
from math import sqrt

class Surface:
    pos = [0,0,0]
    angle = (0, 0, 1, 0)
    side = sqrt(2) - 0.01
    def __init__(self, colorName):
        self.setColor(colorName)

    def draw(self, quadric):
        glColor3f(*self.color)

        glTranslatef(*self.pos)
        glRotatef(*self.angle)
        glRotatef(45, 0, 0, 1)

        gluDisk(quadric, 0, self.side, 4, 5)

        glRotatef(45, 0, 0, -1)
        glRotatef(-self.angle[0], self.angle[1], self.angle[2], self.angle[3])
        glTranslatef(-self.pos[0], -self.pos[1], -self.pos[2])

    def setColor(self, colorName):
        self.colorName = colorName
        color_map = {'W': (1, 1, 1), 'G': (0, 1, 0), 'R': (1, 0, 0), 'B': (0, 0, 1), 'Y': (1, 1, 0), 'O': (1, .5, 0)}
        self.color = color_map.get(colorName, (0, 0, 0))

    def setPos(self, surface, row, col):
        self.pos = [0,0,0]

        if surface == 0:
            self.setZ(row)
            self.setX(col)
            self.pos[1] = 3
        if surface == 1:
            self.setZ(col)
            self.setY(row)
            self.pos[0] = -3
        elif surface == 2:
            self.setY(row)
            self.setX(col)
            self.pos[2] = -3
        elif surface == 3:
            self.setZ(col)
            self.pos[2] *= -1
            self.setY(row)
            self.pos[0] = 3
        elif surface == 4:
            self.setZ(row)
            self.pos[2] *= -1
            self.setX(col)
            self.pos[1] = -3
        elif surface == 5:
            self.setY(row)
            self.pos[1] *= -1
            self.setX(col)
            self.pos[2] = 3

    def setX(self, col):
        if col == 0:
            self.pos[0] = -2
        elif col == 2:
            self.pos[0] = 2

    def setY(self, row):
        if row == 0:
            self.pos[1] = 2
        elif row == 2:
            self.pos[1] = -2
        else: return

    def setZ(self, row):
        if row == 0:
            self.pos[2] = 2
        elif row == 2:
            self.pos[2] = -2
        else: return