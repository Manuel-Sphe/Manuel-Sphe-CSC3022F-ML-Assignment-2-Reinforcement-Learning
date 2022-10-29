import numpy
import random

from matplotlib import pyplot, colors

 
class FourRooms:

    # Action Constants
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    # Cell Type Constants
    BORDER = -1
    EMPTY = 0
    RED = 1
    BLUE = 2
    GREEN = 3

    custom_cmap = colors.LinearSegmentedColormap.from_list('', ['black', 'white', 'red', 'green', 'blue', 'pink',
                                                                'violet'])

    def __init__(self, scenario: str, stochastic: bool = False):

        if scenario in ['simple', 'multi', 'rgb']:
            self.scenario = scenario
        else:
            raise Exception('Invalid Scenario. Must be one of the following values: simple, multi or rgb')

        self.stochastic = stochastic

        # Create Four Rooms Domain
        self.__environment = numpy.array(
            [
                # 0   1   2   3   4   5   6   7   8   9  10  11  12 States
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],  # 0  actions
                [-1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1],  # 1
                [-1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1],  # 2
                [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],  # 3
                [-1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1],  # 4
                [-1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1],  # 5
                [-1, -1,  0, -1, -1, -1, -1,  0,  0,  0,  0,  0, -1],  # 6
                [-1,  0,  0,  0,  0,  0, -1, -1, -1,  0, -1, -1, -1],  # 7
                [-1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1],  # 8
                [-1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1],  # 9
                [-1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0, -1],  # 10
                [-1,  0,  0,  0,  0,  0, -1,  0,  0,  0,  0,  0, -1],  # 11
                [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]   # 12
            ], dtype=numpy.float32
        )
        
        

        # Generate Packages
        self.__start_num_packages = 1 if self.scenario == 'simple' else 3
        self.__current_num_packages = self.__start_num_packages

        self.__package_locations = []

        for i in range(self.__start_num_packages):
            randX, randY = random.randint(1, 11), random.randint(1, 11)
            while self.__environment[randY][randX] != 0:
                randX, randY = random.randint(1, 11), random.randint(1, 11)

            self.__environment[randY][randX] = (i + 1)
            self.__package_locations.append((randX, randY))

        # Generate Agent Start Pos
        randX, randY = random.randint(1, 11), random.randint(1, 11)
        while self.__environment[randY][randX] != 0:
            randX, randY = random.randint(1, 11), random.randint(1, 11)

        self.__start_pos = (randX, randY)
        self.__current_pos = (randX, randY)

        self.__is_terminal = False
        self.__pathRecords = [[]]

    def takeAction(self, action: int) -> (int, (int, int), int, bool):

        if self.__is_terminal:
            raise Exception('Tried to Take Action while Simulation was in a Terminal State.')

        if self.stochastic and random.random() < 0.2:
            action = random.choice([a for a in range(4) if a != action])

        newX, newY = self.__current_pos

        if action == FourRooms.UP and self.__environment[newY - 1][newX] != -1:
            newY -= 1
        elif action == FourRooms.DOWN and self.__environment[newY + 1][newX] != -1:
            newY += 1
        elif action == FourRooms.LEFT and self.__environment[newY][newX - 1] != -1:
            newX -= 1
        elif action == FourRooms.RIGHT and self.__environment[newY][newX + 1] != -1:
            newX += 1

        self.__current_pos = (newX, newY)

        grid_cell = int(self.__environment[newY][newX])
        self.__environment[newY][newX] = 0
        self.__pathRecords[-1].append((newX, newY))

        if grid_cell > 0:  # Found Package
            if self.scenario == 'rgb' and (newX, newY) != self.__package_locations[3 - self.__current_num_packages]:
                self.__is_terminal = True

            self.__current_num_packages -= 1

        if self.__current_num_packages == 0:
            self.__is_terminal = True
            
     

        return grid_cell, self.__current_pos, self.__current_num_packages, self.__is_terminal

    def getPosition(self):
        return self.__current_pos

    def getPackagesRemaining(self):
        return self.__current_num_packages

    def isTerminal(self):
        return self.__is_terminal

    def newEpoch(self):
        self.__pathRecords.append([])
        self.__current_pos = (self.__start_pos[0], self.__start_pos[1])
        self.__current_num_packages = self.__start_num_packages

        for i, loc in enumerate(self.__package_locations):
            self.__environment[loc[1]][loc[0]] = i + 1

        self.__is_terminal = False

    def showPath(self, index: int, savefig: str = None):

        # Environment
        pixels = self.__environment.copy()

        # Path
        for loc in self.__pathRecords[index]:
            pixels[loc[1]][loc[0]] = 4

        # Start Pos
        pixels[self.__start_pos[1]][self.__start_pos[0]] = 5

        # Package Locations
        for i, loc in enumerate(self.__package_locations):
            pixels[loc[1]][loc[0]] = i + 1

        # Create plot
        pyplot.imshow(pixels, cmap=FourRooms.custom_cmap, interpolation='nearest')

        if savefig is None:
            pyplot.show()
        else:
            pyplot.savefig(savefig, format='png')
