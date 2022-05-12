import numpy as np
from FourRooms import FourRooms
import random


def getMove(state:(int))->int:
    
    poss_Mov = Possible_Move(state)
    actS = Moves(state,poss_Mov)
    print(f'possible actions {poss_Mov}')
    index = random.randint(0,len(actS)-1)
    
    
    
    
    return actS[index]
    

# returns a list of possible coordinates you can locate to 
def Possible_Move(state):
    moves =[]
    
    wall1 = [(6,i) for i in range(1,12) if (i!=3 and i != 10)] # vertical wall with 2 doors 

    wall2 = [(i,6) for i in range(1,6) if i!=2] # left-innner horinontal wall

    wall3 = [(i,7) for i in range(7,12) if i!=9] # right inner horizontal wall 

    wall = wall1 + wall2 + wall3
    
    x_axis = [-1,1,0,0]
    y_axis = [0,0,-1,1]
    x, y =state
    for i in range(4):
        if (x+x_axis[i]<12 and y+y_axis[i]<12) and (x+x_axis[i]>0 and y+y_axis[i]>0) and (x+x_axis[i],y+y_axis[i]) not in wall:
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
    
    
    print('Agent starts at: {0}'.format(initial))
    
    Possible_Move(fourRoomsObj.getPosition())
    
    
    # select the random action from the actions (Exploration) 
    action = getMove(initial)
   
    print(f'start {initial}')
    
    gridType, newPos, packagesRemaining, isTerminal = fourRoomsObj.takeAction(action)
    
    print(f'new {newPos}')
    
    
   # while is not isTerminal:
        
        
  
        
    
    

    

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


