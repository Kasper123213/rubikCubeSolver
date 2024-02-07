from cube import Cube

def main():
    cube = Cube()
    cube.printCube()

    print("\n"*3)

    cube.bMove()
    cube.printCube()

    print("\n"*3)

    cube.rotateSurface(1, True)
    cube.printCube()

    print("\n"*3)

    cube.rotateSurface(1, False)
    cube.printCube()


if __name__ == "__main__":
    main()