from typing import List
import os
import numpy as np


# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        data = []
        folds = []
        for line in f:
            if "0"<=line[0] <= "9":
                data.append([int(a) for a in line.split(",")])
            elif line != "\n":
                tmp = line.replace("fold along","").strip().split("=")             
                folds.append([tmp[0], int(tmp[1])])

    return data, folds

def fold(data, dir, num):
    folded_data = []
    for ele in data:
        folded = [ele[0], ele[1]]
        folded[0] = 2 * num - ele[0] if  ele[0] > num and dir == "x" else folded[0]
        folded[1] = 2 * num - ele[1] if  ele[1] > num and dir == "y" else folded[1]
            
        if folded not in folded_data:
            folded_data.append(folded)

    return folded_data

def print_map(MAP):
    M,N = MAP.shape
    for i in range(M):
        for j in range(N):
            print(f"{'###' if MAP[i,j] == 1 else '   '}", end="")
        print("\n", end="")
                  


# Puzzle 1
def f1(data : List[List[int]]) -> int:
    data, folds = data 
    data = fold(data, folds[0][0], folds[0][1])
    
    return len(data)
    
# Puzzle 2
def f2(data : List[List[int]]) -> int:
    data, folds = data
    
    for dir, num in folds:
        data = fold(data, dir, num)
        
    #Create and print Map with the data
    xMax = max([ele[0] for ele in data])
    yMax = max([ele[1] for ele in data])

    MAP = np.zeros((yMax+1, xMax+1))
    for ele in data:
        MAP[ele[1],ele[0]] = 1
        
    print_map(MAP)
    
    return len(data)
        
        
 # MAIN       
def main(): 
    cwd = os.getcwd()
    os.chdir(cwd.replace("Puzzles",""))
    
    data = read_data("Data\\data13.txt")

    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()
    
    
