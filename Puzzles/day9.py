from typing import List
import os

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
       # return [x.replace("\n", "") for x in f]
        return [int(x) for x in f]

   
# Puzzle 1
def f1(data : List[List[int]]) -> int:
    pass
    
    
    
# Puzzle 2
def f2(data : List[List[int]]) -> int:
    pass
        
        
 # MAIN       
def main(): 
    cwd = os.getcwd()
    os.chdir(cwd.replace("Puzzles",""))
    
    data = read_data("Data\\data9.txt")
    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()