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
visits = np.zeros(3,144) # 

decay = 1
epsilon_decay = epochs // 2

directions = np.array([[0,-1],[0,1],[-1,0],[1,0]]) # UP = 0, DOWN = 1, LEFT = 2, RIGHT = 3 

def Move_3D(package_type:int,state:int)->[int]:
    actSeq = [] 
    for action,val in enumerate(R[package_type,state]):
        
        if val != -1:
            actSeq.append(action)
    return actSeq
        
    
def main():

    # Create FourRooms Object
    fourRoomsObj = FourRooms('multi')
    print(R.shape)
   


if __name__ == "__main__":
    main()
