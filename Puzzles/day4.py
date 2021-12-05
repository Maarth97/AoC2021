from typing import List, Tuple
import os

# Get Data Input
def read_data(filename : str) -> Tuple[List[int], List[int]]:
    with open(filename) as f:
        data = [x.replace("\n", "") for x in f]

        nums = [int(x) for x in data[0].split(",")]
        fields = []
        field = []
        
        for idx, line in enumerate(data[2:]):
            if line == "":
                fields.append(field)
                field = []
            else:
                field = field + [int(num) for num in line.split(" ") if num != ""]
                
        return nums, fields



def check_field(field : List[int] , nums : List[int])->bool:

    for idx in range(5):
        # Check Row with idx: 5*idx : 5*idx + 5 --> All Elements for Row idx
        if all([True if elem in nums else False for elem in [ele for ele in field[5*idx : 5*idx+5]]]): return True
        # Check Cols with idx: idx2 % 5 == idx --> All Elements for Col idx
        if all([True if elem in nums else False for elem in [ele for idx2, ele in enumerate(field) if idx2 % 5 == idx ]]): return True
            
    return False
    
    
# Puzzle 1
def f1(data : List[List[int]]) -> int:
    nums, fields = data[0], data[1]
    
    for idx, lotto in enumerate(nums):
        if idx < 4: continue    # Performance
        
        for field in fields:
            if check_field(field, nums[:idx+1]):
                # Sum of unmarked elements in First Bingo * Last Element to Win the Bingo
                return sum([ele for ele in field if ele not in nums[:idx+1]]) * lotto
        
    
    
    
# Puzzle 2
def f2(data : List[List[int]]) -> int:
    nums, fields = data[0], data[1]
    
    for idx, lotto in enumerate(nums):
        if idx < 4: continue    # Performance
        
        for field in fields:
            if check_field(field, nums[:idx+1]):
                last_field = field
                lastNums = nums[:idx+1]
                fields.remove(field)
                
    # Sum of unmarked elements in Last Bingo * Last Element to Win the Bingo
    return sum([ele for ele in last_field if ele not in lastNums]) * lastNums[-1]
        
        
        
 # MAIN       
def main(): 
    cwd = os.getcwd()
    os.chdir(cwd.replace("Puzzles",""))
    
    data = read_data("Data\\data4.txt")
    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()