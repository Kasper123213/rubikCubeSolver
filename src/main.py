import time as Time
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
    if key == GLFW_KEY_L and action == GLFW_PRESS:#todo usunąć
        cube.readFromFile("example.txt")
    if key == GLFW_KEY_ENTER and action == GLFW_PRESS:#todo usunąć
        findSolution()
        
    if key == GLFW_KEY_SPACE and action == GLFW_PRESS:#todo usunąć
        global solvingMoveIndex, translatedSolution, showingSolution, startRotationTime
        if len(translatedSolution) != 0 :

            if solvingMoveIndex >= len(translatedSolution):
                solvingMoveIndex = 0
                translatedSolution = []
            else:
                translatedSolution[solvingMoveIndex](cube)
                cube.loadParameters()
                solvingMoveIndex += 1
                showingSolution = True
                startRotationTime = glfwGetTime()







    if (key == GLFW_KEY_RIGHT or key == GLFW_KEY_LEFT) and action == GLFW_RELEASE:
        viewerMoveVector[0] = 0
    if (key == GLFW_KEY_UP or key == GLFW_KEY_DOWN) and action == GLFW_RELEASE:
        viewerMoveVector[1] = 0

def findSolution(): #todo do sth with it
    global translatedSolution, showingSolution, startRotationTime

    if cube.isSolved():
        print("solved")
        return

    translator = {
        "U" : [Cube.moveW],
        "U'": [Cube.moveW, Cube.moveW, Cube.moveW],
        "U2": [Cube.moveW, Cube.moveW],

        "D" : [Cube.moveY],
        "D'": [Cube.moveY, Cube.moveY, Cube.moveY],
        "D2": [Cube.moveY, Cube.moveY],

        "L" : [Cube.moveO],
        "L'": [Cube.moveO, Cube.moveO, Cube.moveO],
        "L2": [Cube.moveO, Cube.moveO],

        "R" : [Cube.moveR],
        "R'": [Cube.moveR, Cube.moveR, Cube.moveR],
        "R2": [Cube.moveR, Cube.moveR],

        "F" : [Cube.moveG],
        "F'": [Cube.moveG, Cube.moveG, Cube.moveG],
        "F2": [Cube.moveG, Cube.moveG],

        "B" : [Cube.moveB],
        "B'": [Cube.moveB, Cube.moveB, Cube.moveB],
        "B2": [Cube.moveB, Cube.moveB]
    }

    state = cube.getSurfaces()

    solution = kociemba.solve(state)
    solution = solution.split()


    for move in solution:
        move = translator.get(move)
        translatedSolution += move

    showingSolution = True


    # for move in translatedSolution:
    #     move(cube)
    #     cube.loadParameters()
    #     render()
    #     # time.sleep(1)



    # print(translatedSolution)


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
    global startRotationTime, showingSolution
    # time = glfwGetTime()
    # print(time)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(viewer[0], viewer[1], viewer[2], .0, .0, .0, .0, 1.0, .0)


    axes()




    if startRotationTime != -1 and showingSolution:
        deltaTime = time - startRotationTime
        angle = 90 - (90 * deltaTime / rotationTime)
        cube.draw(angle)
        Time.sleep(0.1)
        if deltaTime >= rotationTime:
            startRotationTime = -1
            showingSolution = False
    else:
        cube.draw()





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
    # cube.readFromFile()


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
solution = [] #todo delete

solvingMoveIndex = 0
translatedSolution = []

showingSolution = False
startRotationTime = -1
rotationTime = 1

if __name__ == "__main__":
    main()
    # main2()