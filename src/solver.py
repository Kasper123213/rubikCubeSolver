import time
import random
from copy import deepcopy
from src.cube import Cube


class Solver:
    moves = []
    possibleMoves = [Cube.moveW, Cube.moveG, Cube.moveR,
                     Cube.moveB, Cube.moveY, Cube.moveO]

    correctCube =[
                                                        [['W'for _ in range(3)]for _ in range(3)],
           [['G'for _ in range(3)]for _ in range(3)],   [['R'for _ in range(3)]for _ in range(3)],    [['B'for _ in range(3)]for _ in range(3)],
                                                        [['Y'for _ in range(3)]for _ in range(3)],
                                                        [['O'for _ in range(3)]for _ in range(3)]
           ]

    #algorithm parameters
    searchingTime = 2 #seconds
    mutationPoss = 0.1
    crossingPoss = 0.9
    populationSize = 30
    tournamentSize = int(populationSize * 0.2)
    numberOfParents = int(populationSize * 0.5)

    bestSolution = []
    bestValue = 0

    def __init__(self, cube):
        self.beginCube = Cube()
        self.beginCube.cube = deepcopy(cube.cube)


        # print("Na pocaątku")
        # cube.printCube()

#mnożenie - wzięcie od lepszego osobnika losowe n pierwszych ruchów
#mutacja - dodanie ruchu w losowe miejsce
#fitnesse - w zalezniosci od pol na swoich miejscach. kolejne poziomy mają wiecej punktow. wziąć też pod uwage dlugosc
#i/lub ilosc wystąpien ruchow aby uniknąć pętli

    #genetic algorithm
    def solve(self):
        startTime = int(time.time())

        population = self.setPopulation()

        while int(time.time()) - startTime < self.searchingTime:

            self.findBest(population)

            parents = self.findParents(population)

            children = []
            for i in range(0,len(population), 2):
                if self.crossingPoss > random.random():
                    children.append(cross(parents[i], parents[i+1]))    #todo

            for child in children:
                if self.crossingPoss > random.random():
                    mutate(child)   #todo

            population += children

    def setPopulation(self):
        population = []

        for i in range(self.populationSize):
            population.append(random.choice(self.moves))

        return population

    def findBest(self, population):
        newPopulation = []

        while len(newPopulation) != self.populationSize:
            bestChromosom = max(population, key=fitness)    #todo
            newPopulation.append(bestChromosom)
            population.remove(bestChromosom)

        bestValue = fitness(newPopulation[0])   #todo
        if bestValue > self.bestValue:
            self.bestValue = bestValue
            self.bestSolution = newPopulation[0]

        population = newPopulation


    def findParents(self, population):
        parents = []

        for i in range(self.tournamentSize):
            tournamentPopulation = []
            for i in range(self.numberOfParents):
                tournamentPopulation.append(random.choice(population))

            parents.append(max(tournamentPopulation, key=fitness))    #todo

        return parents