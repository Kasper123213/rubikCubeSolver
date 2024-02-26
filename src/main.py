import time
from math import pi, sin, cos
from PIL import Image
from glfw.GLFW import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL import *
from OpenGL.GLU import *
from cube import Cube
import kociemba

from surface import Surface


def keyboard_key_callback(window, key, scancode, action, mods):
    if (key == GLFW_KEY_ESCAPE or key == GLFW_KEY_P or key == GLFW_KEY_Q) and action == GLFW_PRESS:
        glfwSetWindowShouldClose(window, GLFW_TRUE)


    if key == GLFW_KEY_RIGHT and action == GLFW_PRESS:
        viewerMoveVector[0] = 1
    if key == GLFW_KEY_LEFT and action == GLFW_PRESS:
        viewerMoveVector[0] = -1
    if key == GLFW_KEY_UP and action == GLFW_PRESS:
        viewerMoveVector[1] = -1
    if key == GLFW_KEY_DOWN and action == GLFW_PRESS:
        viewerMoveVector[1] = 1

    if key == GLFW_KEY_W and action == GLFW_PRESS:#todo usunąć
        cube.moveW()
        cube.loadParameters()
    if key == GLFW_KEY_G and action == GLFW_PRESS:#todo usunąć
        cube.moveG()
        cube.loadParameters()
    if key == GLFW_KEY_R and action == GLFW_PRESS:#todo usunąć
        cube.moveR()
        cube.loadParameters()
    if key == GLFW_KEY_B and action == GLFW_PRESS:#todo usunąć
        cube.moveB()
        cube.loadParameters()
    if key == GLFW_KEY_Y and action == GLFW_PRESS:#todo usunąć
        cube.moveY()
        cube.loadParameters()
    if key == GLFW_KEY_O and action == GLFW_PRESS:#todo usunąć
        cube.moveO()
        cube.loadParameters()
    if key == GLFW_KEY_X and action == GLFW_PRESS:#todo usunąć
        cube.fullRotateX()
        cube.loadParameters()
    if key == GLFW_KEY_Z and action == GLFW_PRESS:#todo usunąć
        cube.fullRotateY()
        cube.loadParameters()
    if key == GLFW_KEY_S and action == GLFW_PRESS:#todo usunąć
        cube.saveCube("example.txt")
    if key == GLFW_KEY_ENTER and action == GLFW_PRESS:#todo usunąć
        findSolution()


    if (key == GLFW_KEY_RIGHT or key == GLFW_KEY_LEFT) and action == GLFW_RELEASE:
        viewerMoveVector[0] = 0
    if (key == GLFW_KEY_UP or key == GLFW_KEY_DOWN) and action == GLFW_RELEASE:
        viewerMoveVector[1] = 0

def findSolution():
    state = cube.getSurfaces()
    print(state)
    solution = kociemba.solve(state)
    print(solution)




def update_viewport(window, width, height):
    if width == 0:
        width = 1
    if height == 0:
        height = 1
    aspect_ratio = width / height

    glMatrixMode(GL_PROJECTION)
    glViewport(0, 0, width, height)
    glLoadIdentity()

    if width <= height:
        glOrtho(-7.5, 7.5, -7.5 / aspect_ratio, 7.5 / aspect_ratio, 20.5, -10.5)
    else:
        glOrtho(-7.5 * aspect_ratio, 7.5 * aspect_ratio, -7.5, 7.5, 20.5, -10.5)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()



def setup():
    global window, cube

    if not glfwInit():
        exit(-1)

    window = glfwCreateWindow(display[0], display[1], __file__, None, None)
    if not window:
        glfwTerminate()
        exit(-1)

    glfwMakeContextCurrent(window)
    glfwSetFramebufferSizeCallback(window, update_viewport)
    glfwSetKeyCallback(window, keyboard_key_callback)
    glfwSwapInterval(1)

    update_viewport(None, display[0], display[1])
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    cube = Cube()

    cube.createSurfaces()
    cube.loadParameters()



def axes():
    glBegin(GL_LINES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-5.0, 0.0, 0.0)
    glVertex3f(5.0, 0.0, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, -5.0, 0.0)
    glVertex3f(0.0, 5.0, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.0, -5.0)
    glVertex3f(0.0, 0.0, 5.0)
    glEnd()


def calcPose(object, angles):
    object[0] = angles[2] * cos(angles[1]) * cos(angles[0])
    object[1] = angles[2] * sin(angles[1])
    object[2] = angles[2] * sin(angles[0]) * cos(angles[1])



def render(time):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2], .0, .0, .0, .0, 1.0, .0)


    axes()





    # cube.draw(gluNewQuadric())
    cube.draw()
    # surface = Surface('Y')
    # surface.draw(quadric)
    #
    # surface = Surface('O')
    # surface.draw(quadric)

    # # Przód
    # glColor3f(1, 1, 0.0)  # Czerwony
    # glTranslatef(0, 0, 0.5)
    # gluDisk(quadric, 0, 0.5, 4, 32)





    glFlush()

    if viewerMoveVector[0] != 0:
        viewerAngles[0] += viewerMoveVector[0] * viewerSpeed
        calcPose(viewer, viewerAngles)
    if viewerMoveVector[1] != 0:
        viewerAngles[1] += viewerMoveVector[1] * viewerSpeed
        if viewerAngles[1]<= -1.5:
            viewerAngles[1] = -1.49
        if viewerAngles[1] >= 1.5:
            viewerAngles[1] = 1.49
        calcPose(viewer, viewerAngles)





def main():
    cube.readFromFile()


    setup()

    while not glfwWindowShouldClose(window):
        render(glfwGetTime())
        glfwSwapBuffers(window)
        glfwPollEvents()


    glfwTerminate()







display = (1000, 800)

# parametru kamery
viewerAngles = [pi / 180 * 90, 0, 3]
viewer = [0.0, 0.0, 3.0]
viewerMoveVector = [0, 0, 1]  # x, y, zoom
viewerSpeed = pi / 180 * 0.5

cube = Cube()
solution = []


if __name__ == "__main__":
    main()
    # main2()