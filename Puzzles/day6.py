from typing import List

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        return [x.replace("\n", "") for x in f]


   
# Puzzle 1
def f1(data : List[int]) -> int:
    pass
    
    
    
# Puzzle 2
def f2(data : List[int]) -> int:
    pass
        
        
 # MAIN       
def main(): 
    data = read_data("Data\\data6.txt")
    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()