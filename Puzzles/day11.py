from typing import List
import os
from itertools import product
import numpy as np

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        return [[int(y) for y in x.replace("\n","")] for x  in f]


def adjustant_increase(MAP, M, N):
    boolMap = dict()
    
    while True:
        cnt = 0
        for row, col in product(range(1, M+1), range(1, N+1)):     
            if MAP[row,col] > 9 and (row, col) not in boolMap:
                for offR, offC in [(-1,-1), (-1,0),(-1,1), (0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    MAP[row+offR, col+offC] += 1
                    boolMap[row, col] = 1
                    cnt += 1
        if cnt == 0:
            return MAP
        
                
    
# Puzzle 1
def f1(data : List[List[int]], TIME = 100) -> int:
    M,N = len(data), len(data[0])
    MAP = np.pad(np.array(data),1, constant_values=-np.inf)
    cnt = 0
    
    
    for t in range(TIME):
        # Increase everything by 1
        MAP = MAP + 1
        # Increase adjustant if bigger than 9
        MAP = adjustant_increase(MAP, M,N)
        # Reset to 0
        cnt += len(MAP[MAP > 9])
        MAP[MAP > 9] = 0
        
    return cnt
            
            
    


# Puzzle 2
def f2(data : List[List[int]], MAX_TIME = 100000) -> int:
    M,N = len(data), len(data[0])
    MAP = np.pad(np.array(data),1, constant_values=-np.inf)
    cnt = 0
    
    
    for t in range(1, MAX_TIME):
        # Increase everything by 1
        MAP = MAP + 1
        # Increase adjustant if bigger than 9
        MAP = adjustant_increase(MAP, M,N)
        # Reset to 0
        MAP[MAP > 9] = 0
        
        if len(MAP[MAP == 0]) >= M*N:
            return t
        
        
    return -1
        
        
 # MAIN       
def main(): 
    cwd = os.getcwd()
    os.chdir(cwd.replace("Puzzles",""))
    
    data = read_data("Data\\data11.txt")
    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()