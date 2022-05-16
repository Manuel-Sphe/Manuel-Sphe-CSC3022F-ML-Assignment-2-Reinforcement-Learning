
from telnetlib import EC
from FourRooms import FourRooms
import random
import numpy as np

 # 12  x 12 is the size of the enviroment and we have 4 possible actions per state 
global R, directions
Q_table = np.zeros((3,144,4),dtype=float)
R = np.zeros((3,144,4),dtype=int)
epochs = 100
gamma = 0.8 
epsilon = 0.8
fourRoomsObj = FourRooms('multi')
visits = np.zeros((3,144)) # 


directions = np.array([[0,-1],[0,1],[-1,0],[1,0]]) # UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3 

def Possible_3D_Moves(package_type:int,state:int)->[int]:
    actSeq = [] 
    for action,val in enumerate(R[package_type,state]):
        
        if val != -1:
            actSeq.append(action)
    return actSeq

def Populate_3D() -> np.array([[[int]]]) : # Returns a 3D R matrix 
    
    # for populating the R table 
        
    for state in range(144):
        x,y = state%12 , state//12
            
        # Punishing the agent when it's taking an invalid move
        # This if for the states near the outer boarders 
            
        #contains the coordinates (x,y)
        actSeq =[
                
            (x,y-1 if (y-1>=0 and  y-1< 12) else -1), # UP 
            (x, y+1 if( y+1>=0 and y+1 < 12) else -1), # DOWN
            (x-1 if (x-1>=0 and x-1<12) else -1,y), # LEFT 
            (x+1 if(x+1>=0 and x+1<12) else -1 ,y), # RIGHT
        ]
        
        for a_package in range(3):        # a package  
            for i,val in enumerate(actSeq):
                if val[0]<0 or val[1]<0:
                    R[a_package,state,i] = -1
    return R

def reward(current_state:int,next_state:int,action:int,package:int,grid_Cell:int)->float:
    #hitting a wall
    if current_state == next_state:
        R[package,current_state,action]  = -1
        return -5.
        
    else:
        
        R[package,current_state,action] = grid_Cell
        return 10
    
def Learning_Q_3D(epoches,visits:np.array([[int]])):
   
    #print(x,y)
    fourRoomsObj.newEpoch()
    x,y  = fourRoomsObj.getPosition()
    global epsilon
    state = y*12 + x # convert to 1D state 
   # print(f'state {state}')
    
    
    package_num = 3 - fourRoomsObj.getPackagesRemaining()
    
    done = False
    while package_num != 3 and not done :
        
        visits[package_num,state] += 1
        alpha = 1/(1+ visits[package_num,state])
        
        state_action = Possible_3D_Moves(package_num,state)
    
        
        if random.uniform(0,1) < epsilon:
            action = state_action[np.random.randint(0, len(state_action))]
        else:
            action = np.argmax(Q_table[package_num,state])
               
            
        gridCell, current_pos , c_num_of_packages, isTerminal = fourRoomsObj.takeAction(action)
        
        
        
        r = reward(state,current_pos[1]*12 + current_pos[0],action,package_num,gridCell)
        next_state  = current_pos[1]*12 + current_pos[0]
        
        
        # Update the Q_table      
        old_value = Q_table[package_num,state, action]
        next_max = np.max(Q_table[package_num,next_state])
        
        new_value = (1 - alpha) * old_value + alpha * (r + gamma * next_max)
        Q_table[package_num,state, action] = new_value

        
        state = current_pos[1]*12 + current_pos[0]
        
        package_num= 3 - c_num_of_packages
        done = isTerminal

        

       # print('left to collect',fourRoomsObj.getPackagesRemaining(), 'package',package_num)
       
def Exploit():
    fourRoomsObj.newEpoch()
    X,Y = fourRoomsObj.getPosition()
    state = Y*11 + X  
    dest = 0  
    package_num = 0 
    done = False
    while package_num != 3 and not done :
        
        
        action=np.argmax(Q_table[package_num,state])

        gridCell, current_pos , c_num_of_packages, isTerminal = fourRoomsObj.takeAction(action)
                            
        state = current_pos[1]*12 + current_pos[0]
        
        if c_num_of_packages == 0 and dest == 2:
            dest = 3
            fourRoomsObj.showPath(-1)
            print("package 1")

        elif c_num_of_packages == 1 and dest == 1:
            dest = 2
            fourRoomsObj.showPath(-1)
            print("package 2")

        elif c_num_of_packages == 2 and dest == 0:
            dest = 1
            fourRoomsObj.showPath(-1)
            print("package 3")

        fourRoomsObj.showPath(-1)
                
        package_num= 3 - c_num_of_packages
        done =isTerminal
        

                  
def main():
    for i in range(1,epochs):
        Learning_Q_3D(i,visits)
    
    print(Q_table[0])
    
    Exploit()
 
    
    
    
   


if __name__ == "__main__":
    main()
