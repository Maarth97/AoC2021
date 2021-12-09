from typing import List
import os
import numpy as np
from itertools import product

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
       # return [x.replace("\n", "") for x in f]
        return [[int(y) for y in x.replace("\n","")] for x in f]
        

def find_lowest(MAP, M, N):
    return  [(row,col) for row, col in product(range(1, M-1), range(1, N-1)) if MAP[row,col] < min(MAP[row, col-1], MAP[row,col+1], MAP[row+1,col], MAP[row-1,col])]
    
              
                                                   
            

# Puzzle 1
def f1(data : List[List[int]]) -> int:
    M,N = len(data)+2, len(data[0])+2
    MAP = np.pad(np.array(data),1, constant_values=10)     # Pad Data with 10 at the border
    lowest = find_lowest(MAP, M,N)

    return sum([MAP[x,y] for x,y in lowest]) + len(lowest)
    
def append_to_basin(MAP, row, col, basinList = None):
    if basinList == None: basinList = [(row,col)]
    for x,y in [(row, col-1), (row,col+1), (row-1,col), (row+1, col)]:
        if (x,y) not in basinList and MAP[x,y] < 9 and MAP[x,y] > MAP[row,col]:
            basinList.append((x,y))
            append_to_basin(MAP, x, y, basinList)
    return basinList
            
    
# Puzzle 2
def f2(data : List[List[int]]) -> int:
    M,N = len(data)+2, len(data[0])+2
    HT = dict()
    MAP = np.pad(np.array(data),1, constant_values=10)     # Pad Data with 10 at the border
    lowest = find_lowest(MAP, M,N)

    for ele in lowest:
        HT[ele] = append_to_basin(MAP, ele[0], ele[1])

    res = sorted([len([MAP[x,y] for x,y in HT[key]]) for key in HT],reverse=True)   
    return res[0] * res[1] * res[2]

 # MAIN       
def main(): 
    cwd = os.getcwd()
    os.chdir(cwd.replace("Puzzles",""))
    
    data = read_data("Data\\data9.txt")
    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()