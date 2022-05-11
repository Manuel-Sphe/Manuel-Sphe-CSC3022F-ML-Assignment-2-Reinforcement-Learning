import numpy as np
from FourRooms import FourRooms
import random


# returns a list of possible coordinates you can locate to 
def Possible_Move(state):
    moves =[]
    x_axis = [-1,1,0,0]
    y_axis = [0,0,-1,1]
    x, y =state
    for i in range(4):
        if x+x_axis[i]<12 and y+y_axis[i]<12:
            moves.append((x+x_axis[i],y+y_axis[i]))
            
    return moves     

# given possible states to go, get a Array of moves eg. [LEFT, RIGHT, UP, DOWN]
def Moves(state,actions):
        
    acts = []
    first  = np.array(state)
        
        
    for action in actions:
        sec = np.array(action)
            
        res = first - sec
            
        if (res == np.array([1,0])).all():
            acts.append(1) # DOWN
        elif (res == np.array([-1,0])).all():
            acts.append(0) # UP
        elif (res == np.array([0,1])).all():
            acts.append(3) # RIGHT
        elif (res == np.array([0,-1])).all():
            acts.append(2) # LEFT
    
    
    return acts


def main():

    # Create FourRooms Object
    fourRoomsObj = FourRooms('simple')

    # This will try to draw a zero
    actSeq = [FourRooms.LEFT, FourRooms.LEFT, FourRooms.LEFT,
              FourRooms.UP, FourRooms.UP, FourRooms.UP,
              FourRooms.RIGHT, FourRooms.RIGHT, FourRooms.RIGHT,
              FourRooms.DOWN, FourRooms.DOWN, FourRooms.DOWN]

    aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']
    
    initial = fourRoomsObj.getPosition()
    
    pos_moves = Possible_Move(initial)
    
    actSeletions = Moves(initial,pos_moves)
    
    
    print('Agent starts at: {0}'.format(initial))
    
    Possible_Move(fourRoomsObj.getPosition())
    
    
    # select the random action from the actions (Exploration) 
    
    
    
    for i in range(1,10001):
        pass
    

    for act in actSeq:
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(act)

        print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[act], newPos, gTypes[gridType]))
        
       

        if isTerminal:
            break

    # Don't forget to call newEpoch when you start a new simulation run

    # Show Path
    fourRoomsObj.showPath(-1)


if __name__ == "__main__":
    main()


