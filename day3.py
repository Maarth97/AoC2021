from typing import List
import numpy as np

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        return [x.replace("\n", "") for x in f]


# Puzzle 1
def f1(data : List[str]) -> int:
    N = len(data[0])
    counter = np.array([0 for _ in data[0]])
    
    for ele in data:
        counter += np.array([int(i) for i in ele])
        
    # Determine Gamma = Most Common bit
    gamma = sum([2**(N - idx) for idx, ele in enumerate(counter, start = 1) if ele >= len(data)/2])
    epsilon = sum([2**(N - idx) for idx, ele in enumerate(counter, start = 1) if ele < len(data)/2])
   # return gamma * ( 2**(N-1) ^ gamma)
    return gamma * epsilon
    
    
# Puzzle 2
def f2(data : List[str]) -> int:
    N = len(data[0])
    
    data_ox = [ele for ele in data]
    data_co2 = [ele for ele in data]
    
    for pos in range(N):
        # Determine Most Common bit
        MCB = 1 if sum([int(ele[pos]) for ele in data_ox ]) >= len(data_ox)/2 else 0
        LCB = 1 if sum([int(ele[pos]) for ele in data_co2 ]) < len(data_co2)/2 else 0
        
        # Reduce Search Room
        if len(data_ox) > 1:
            data_ox = [ele for ele in data_ox if int(ele[pos]) == MCB]
        if len(data_co2) > 1:
            data_co2 = [ele for ele in data_co2 if int(ele[pos]) == LCB]
        
    #ox = sum([2**(N - idx) for idx, ele in enumerate(data_ox[0], start = 1) if ele == "1"])
    #co2 = sum([2**(N - idx) for idx, ele in enumerate(data_co2[0], start = 1)if ele == "1"])
    
    return int(data_ox[0],2) * int(data_co2[0],2)   # ox * co2
        
        
 # MAIN       
def main():
        
    data = read_data("Data\\data3.txt")
    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()