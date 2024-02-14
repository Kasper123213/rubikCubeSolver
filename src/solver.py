import sys
import time
import random
from copy import deepcopy
from src.cube import Cube


class Solver:
    moves = [Cube.moveW, Cube.moveG, Cube.moveR,
                     Cube.moveB, Cube.moveY, Cube.moveO]

    correctCube =[
                                                        [['W'for _ in range(3)]for _ in range(3)],
           [['G'for _ in range(3)]for _ in range(3)],   [['R'for _ in range(3)]for _ in range(3)],    [['B'for _ in range(3)]for _ in range(3)],
                                                        [['Y'for _ in range(3)]for _ in range(3)],
                                                        [['O'for _ in range(3)]for _ in range(3)]
           ]

    #algorithm parameters
    searchingTime =  10000#seconds
    mutationPoss = 0.7
    crossingPoss = 0.0
    populationSize = 50
    tournamentSize = int(populationSize * 0.2)
    numberOfParents = int(populationSize * 0.3)

    bestSolution = []
    bestValue = 0#sys.maxsize

    def __init__(self, cube):
        self.beginCube = Cube()
        self.beginCube.cube = deepcopy(cube.cube)


        # print("Na pocaątku")
        # cube.printCube()

#mnożenie - wzięcie od lepszego osobnika losowe n pierwszych ruchów
#mutacja - dodanie ruchu w losowe miejsce
#fitnesse - w zalezniosci od pol na swoich miejscach. kolejne poziomy mają mniej punktow. wziąć też pod uwage dlugosc
#i/lub ilosc wystąpien ruchow aby uniknąć pętli

    #genetic algorithm
    def solve(self):
        startTime = int(time.time())

        population = self.setPopulation()
        while int(time.time()) - startTime < self.searchingTime:
            self.findBest(population)

            parents = self.findParents(population)

            children = []
            for i in range(0,len(parents), 2):
                if True:
                    # if self.crossingPoss > random.random():
                    child1, child2 = self.cross(parents[i], parents[i+1])
                    children.append(child1)
                    children.append(child2)

            population += children

            for chromosom in population:
                if self.mutationPoss > random.random():
                    population.append(self.mutate(deepcopy(chromosom)))



        return self.bestSolution

    def setPopulation(self):
        population = []
        chromosom = []
        for i in range(self.populationSize):
            population.append([random.choice(self.moves)])

        return population

    def findBest(self, population):
        oldPopulation = deepcopy(population)
        population.clear()

        while len(population) != self.populationSize:
            bestChromosom = max(oldPopulation, key=self.fitness)
            population.append(bestChromosom)
            oldPopulation.remove(bestChromosom)

        bestValue = self.fitness(population[0])
        if bestValue > self.bestValue:
            self.bestValue = bestValue
            self.bestSolution = population[0]
            print("**")
            print("Walju=",bestValue)
            # print("Walju=",int(bestValue * len(self.bestSolution)))
            print(self.bestSolution)
            print("**")




    def findParents(self, population):
        parents = []

        for i in range(self.tournamentSize):
            tournamentPopulation = []
            for j in range(self.numberOfParents):
                tournamentPopulation.append(random.choice(population))

            parents.append(max(tournamentPopulation, key=self.fitness))    #todo

        return parents

    def cross(self, parent1, parent2):
        minLen = min(len(parent2), len(parent1))
        index = int(random.random() * minLen)
        child1 = deepcopy(parent1[:index]) + deepcopy(parent2[index:])
        child2 = deepcopy(parent2[:index]) + deepcopy(parent1[index:])
        return child1, child2

    def mutate(self, chromosom):
        r = random.random()

        if r>0.4:
            newChromosom = self.addMutauion(chromosom)
        elif r>0.3:
            newChromosom = self.deleteMutation(chromosom)
        else:
            newChromosom = self.changeMutation(chromosom)


        return newChromosom


    def addMutauion(self, chromosom):
        # index = int(random.random() * (len(chromosom) + 1))
        # move = random.choice(self.moves)
        # chromosom.insert(index, move)
        move = random.choice(self.moves)
        chromosom.append(move)
        return chromosom

    def deleteMutation(self, chromosom):
        if len(chromosom)==1: return self.mutate(chromosom)
        index = int(random.random() * len(chromosom))
        chromosom.pop(index)
        return chromosom

    def changeMutation(self, chromosom):
        index = int(random.random() * len(chromosom))
        move = random.choice(self.moves)
        chromosom[index] = move
        return chromosom

    # def fitness(self, chromosom):
    #     points = [{'W':0, 'G':1, 'R':1, 'B':1, 'Y':2, 'O':1},
    #               {'W':1, 'G':0, 'R':1, 'B':2, 'Y':1, 'O':1},
    #               {'W':1, 'G':1, 'R':0, 'B':1, 'Y':1, 'O':2},
    #               {'W':1, 'G':2, 'R':1, 'B':0, 'Y':1, 'O':1},
    #               {'W':2, 'G':1, 'R':1, 'B':1, 'Y':0, 'O':1},
    #               {'W':1, 'G':1, 'R':2, 'B':1, 'Y':1, 'O':0}]
    #
    #     testCube = Cube()
    #     for move in self.moves:
    #         move(testCube)
    #
    #     score = 0
    #     for surface in range(6):
    #         for row in range(3):
    #             for col in range(3):
    #                 score += points[surface].get(testCube.cube[surface][row][col])
    #
    #     return score

    def fitness(self, chromosom):
        score = 0

        testCube = Cube()
        testCube.cube = deepcopy(self.beginCube.cube)

        for move in chromosom:
            move(testCube)


        colors = ['W', 'G', 'R', 'B', 'Y', 'O']

        for surface in range(len(testCube.cube)):
            pointsOnSurface = 0
            for row in testCube.cube[surface]:
                for color in row:
                    if color == colors[surface]:
                        score += 1
                        pointsOnSurface += 1
            if pointsOnSurface == 9:
                score += 9


        # for row in testCube.cube[0]:
        #     for color in row:
        #         if color == colors[0]:
        #             score += 1
        # score -= 0.001*len(chromosom)

        return score