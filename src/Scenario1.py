from optparse import Option
import random
from shutil import move
from FourRooms import FourRooms
import numpy as np

 # 12  x 12 is the size of the enviroment and we have 4 possible actions per state 
global R, directions
Q_table = np.zeros((144,4),dtype=float)
R = np.zeros((144,4),dtype=int)
epochs = 100
gamma = 0.8 
epsilon = 1
fourRoomsObj = FourRooms('simple')
visits = np.zeros(144)

decay = 1
epsilon_decay = epochs // 2

directions = np.array([[0,-1],[0,1],[-1,0],[1,0]]) # UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3 



def Eploration():
    
    pass
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
    
    
def Populate_R() -> np.array([[int]]) :
    
    # for populating the R table 
    
    for state in range(121):
        x,y = state%12 , state//12
        
        # Punishing the agent when it's taking an invalid move
        # This if for the states near the outer boarders 
        
        actSeq =[
            
        (x,y-1 if (y-1>=0 and  y-1< 12) else -1), # UP 
            (x, y+1 if( y+1>=0 and y+1 < 12) else -1), # DOWN
            (x-1 if (x-1>=0 and x-1<12) else -1,y), # LEFT 
            (x+1 if(x+1>=0 and x+1<12) else -1 ,y), # RIGHT
        ]
                
        for i,val in enumerate(actSeq):
            if val[0]<0 or val[1]<0:
                R[state,i] = -1
    return R
    
    
def inner_walls_R(old_state:int,new_state:int, action:int,grid_cell:int)->int:
    if old_state == new_state: # if hits the inner wall 
        R[new_state,action] = -1 # punish the agent
        return R[old_state,action]
    else:
        R[old_state,action] = grid_cell
        return R[old_state,action] + 1 # reward with 1
    
def Learning_Q(visits:np.array([[int]]),discout:int = 0.89):
        x,y = fourRoomsObj.getPosition()
        #print(x,y)
      
        state = y*12 + x # convert to 1D state 
       # print(f'state {state}')
        done = False
        
        while not done :
            visits[state] += 1
            alpha = 1/visits[state]
            state_action = Possible_Move(state)
            
            if random.random() < epsilon:
                action = state_action[np.random.randint(0, len(state_action))]
            else:
                action = np.max(Q_table[state])
               
            #print('action',action)
            #next_state = Move(state,action)
            
            gridCell, current_pos , gType, isTerminal = fourRoomsObj.takeAction(action)
            
            inner_walls_R(state,current_pos[1]*12 + current_pos[0],action,gridCell)
            next_state  = current_pos[1]*12 + current_pos[0]
            #print(f'state {state} and next_state {next_state}')
            #Q_table[state,action] += alpha *(gridCell + discout*(np.max(Q_table[next_state]) - Q_table[state,action]))   
            
            old_value = Q_table[state, action]
            next_max = np.max(Q_table[next_state])
        
            new_value = (1 - alpha) * old_value + alpha * (gridCell + gamma * next_max)
            Q_table[state, action] = new_value

            done = isTerminal         
            state = current_pos[1]*12 + current_pos[0]
      
        
         
def Exploit():
    
    x,y = fourRoomsObj.getPosition()
    done  =  False 
    state = y*11 + x
    
    while not done:
        action = np.argmax(Q_table[state])
        
        gridCell,current_poss,_,isTerminal = fourRoomsObj.takeAction(action)

        state = current_poss[1]*12 + current_poss[0]
        done = isTerminal
    
    fourRoomsObj.showPath(-1)
        
           

                
def main():
    # Create FourRooms Object
    R = Populate_R()
    for _ in range(1,epochs):
        Learning_Q(visits)
        fourRoomsObj.newEpoch()
    
    for _ in range(epochs):
        Exploit()
        fourRoomsObj.newEpoch()
        
    

    
    #fourRoomsObj.showPath(-1)
    
    # Explole 

if __name__ == "__main__":
    main()
