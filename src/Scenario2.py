from FourRooms import FourRooms
import random
import numpy as np

 # 12  x 12 is the size of the enviroment and we have 4 possible actions per state 
global R, directions
Q_table = np.zeros((3,144,4),dtype=float)
R = np.zeros((3,144,4),dtype=int)
epochs = 100
gamma = 0.8 
epsilon = 1
fourRoomsObj = FourRooms('simple')
visits = np.zeros((3,144)) # 

decay = 1
epsilon_decay = epochs // 2

directions = np.array([[0,-1],[0,1],[-1,0],[1,0]]) # UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3 

def Move_3D(package_type:int,state:int)->[int]:
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
        return -1.
        
    else:
        
        R[package,current_state,action] = grid_Cell
        return 1.
    
    
def main():

    # Create FourRooms Object
    fourRoomsObj = FourRooms('multi')
   
   


if __name__ == "__main__":
    main()
