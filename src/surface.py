from OpenGL.GL import *
from OpenGL.GLU import *

class Surface:
    pos = (0,0,1)
    angle = (90, 0, 1, 0)
    side = 1
    def __init__(self, colorName):
        self.colorName = colorName
        color_map = {'W': (1, 1, 1), 'G': (0, 1, 0), 'R': (1, 0, 0), 'B': (0, 0, 1), 'Y': (1, 1, 0), 'O': (1, .5, 0)}
        self.color = color_map.get(colorName, (0, 0, 0))

    def draw(self, quadric):
        glColor3f(*self.color)

        glTranslatef(*self.pos)
        glRotatef(*self.angle)

        gluDisk(quadric, 0, self.side, 4, 5)

        glRotatef(-self.angle[0], self.angle[1], self.angle[2], self.angle[3])
        glTranslatef(-self.pos[0], -self.pos[1], -self.pos[2])

