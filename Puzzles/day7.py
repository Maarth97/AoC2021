from typing import List
import os
import numpy as np
import matplotlib.pyplot as plt

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        data = [x.split(",") for x in f]
        return [int(x) for x in data[0]]


   
def f1(data : List[int]) -> int:
    
    data = np.array(data)
    min_fuel, best_pos = np.inf, 0
    
    return min([ sum(abs(data - pos)) for pos in range(data.max())])
            
    

def f2(data : List[int]) -> int:
    data = np.array(data)
    min_fuel, best_pos = np.inf, 0
    # Gauß Summe
    return int(min([ sum(abs(data - pos)  * (abs(data - pos) +1 )/2  )  for pos in range(data.max())]))

        
        
 # MAIN       
def main():
    cwd = os.getcwd()
    os.chdir(cwd.replace("Puzzles",""))
    
    data = read_data("Data\\data7.txt")

    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()