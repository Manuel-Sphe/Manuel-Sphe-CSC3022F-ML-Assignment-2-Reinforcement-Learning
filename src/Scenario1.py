from multiprocessing.spawn import old_main_modules
from operator import ne
from FourRooms import FourRooms
import numpy as np


# 11  x 11 is the size of the enviroment and we have 4 possible actions per state 

Q_table = np.zeros([121,4],dtype=float)
R = np.zeros([121,4],dtype=int)


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
    
    x,y = state%11, state//11 # get the coordinates given a state 
    
    new_state = [x,y] + directions[action]
    
    new_state = np.array(new_state) # make this a numpy array
    
    return new_state[1]*11 + new_state[0] # the new state s'
    
    
def Populate_R() -> np.array([[int]]) :
    
    # for populating the R table 
    
    for state in range(121):
        x,y = state%11 , state//11
        
        # Punishing the agent when it's taking an invalid move
        # This if for the states near the outer boarders 
        
        actSeq =[
            
            [x,y-1 if (y-1>=0 and  y-1< 11) else -1], # UP 
            [x, y+1 if( y+1>=0 and y+1 < 11) else -1], # DOWN
            [x-1 if (x-1>=0 and x-1<11) else -1,y], # LEFT 
            [x+1 if(x+1>=0 and x+1<11) else -1 ,y], # RIGHT
        ]
                
        for i,val in enumerate(actSeq):
            if val[0]<0 or val[1]<0:
                R[state,i] = -1
    return R
    
    
def inner_walls_R(old_state:int,new_state:int, action:int,grid_cell:int)->int:
    res = None
    if old_state == new_state: # if hits the inner wall 
        R[new_state,action] = -1 # punish the agent
        res = R[old_state,action]
    else:
        R[old_state,action] = grid_cell
        res = R[old_state,action] + 1 # reward with 1
    
    return res
        
def main():

    # Create FourRooms Object
    fourRoomsObj = FourRooms('simple')
    
    #print(Populate_R())

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
