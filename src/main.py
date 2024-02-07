from cube import Cube

def main():
    cube = Cube()
    cube.printCube()

    print("\n"*3)

    cube.moveB()
    cube.moveb()
    cube.moveF()
    cube.movef()
    cube.moveD()
    cube.moved()
    cube.moveL()
    cube.movel()
    cube.printCube()





if __name__ == "__main__":
    main()