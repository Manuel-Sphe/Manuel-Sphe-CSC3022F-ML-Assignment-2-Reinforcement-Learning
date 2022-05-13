from FourRooms import FourRooms
import numpy as np


# 12  x 12 is the size of the enviroment and we have 4 possible actions per state 

Q_table = np.zeros((144,4),dtype=float)
R = np.zeros((144,4),dtype=int)


directions = np.array([[0,-1],[0,1],[-1,0],[1,0]]) # UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3 

# for getting a listf of possible moves given a state 
def Possible_Move(state: int) -> [int] :
    """
    given a state get all the possible actions you can take on that state 
    to transition to a new state , a state can have a minimum of 2 to a muximum of 4 possible actions 
    returns a list of actions
    """
    
    actSeq = []
    for i,value in enumerate(R[state]):
        if value !=-1 :
            actSeq.append(i)
    return actSeq

# for moving from one state to a new state given (state,action)
def Move(state:int ,action: int) -> int:
    
    x,y = state%12, state//12 # get the coordinates given a state 
    
    new_state = [x,y] + directions[action]
    
    new_state = np.array(new_state) # make this a numpy array
    
    return new_state[1]*12 + new_state[0] # the new state s'
    
    
def Reward() -> np.array([[int]]) :
    
    
    
    
    pass
def main():

    # Create FourRooms Object
    fourRoomsObj = FourRooms('simple')

    # This will try to draw a zero

    """
    actSeq = [FourRooms.LEFT, FourRooms.LEFT, FourRooms.LEFT,
            FourRooms.UP, FourRooms.UP, FourRooms.UP,
            FourRooms.RIGHT, FourRooms.RIGHT, FourRooms.RIGHT,
            FourRooms.DOWN, FourRooms.DOWN, FourRooms.DOWN]



    aTypes = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    gTypes = ['EMPTY', 'RED', 'GREEN', 'BLUE']

    print('Agent starts at: {0}'.format(fourRoomsObj.getPosition()))

    for act in actSeq:
        gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(act)

        print("Agent took {0} action and moved to {1} of type {2}".format (aTypes[act], newPos, gTypes[gridType]))
        
       

        if isTerminal:
            break

    # Don't forget to call newEpoch when you start a new simulation run


    # Show Path
    fourRoomsObj.showPath(-1)
    """
  


if __name__ == "__main__":
    main()
