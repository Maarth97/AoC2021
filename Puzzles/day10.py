from typing import List
import os

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        return [x.replace("\n", "") for x in f]


def corrupted(line)->str:
    Stack = []
    
    for idx, char in enumerate(line):
        if char in ["<", "[", "{","("]: 
            Stack.append(char)
        elif Stack[-1]  + char in ["<>","()","[]","{}"]:
            Stack.pop()
        else:
            return False, char
    return True, Stack
            
            
    
    
# Puzzle 1
def f1(data : List[List[int]]) -> int:
    Awards = {")":3,"]":57, "}":1197,">":25137}
    failure = 0
    
    for line in data:
        succ, char = corrupted(line)
        failure = failure + Awards[char] if not succ else failure
        
    return failure


# Puzzle 2
def f2(data : List[List[int]]) -> int:
    Awards = {"(":1,"[":2, "{":3,"<":4}
    score = []
    
    for idx, line in enumerate(data):
        succ, char = corrupted(line)
        if succ:
            score.append(0)
            for ele in reversed("".join(char)):
                score[-1] = score[-1] * 5 + Awards[ele]
       
    return sorted(score)[int(len(score)/2)]
        
        
 # MAIN       
def main(): 
    cwd = os.getcwd()
    os.chdir(cwd.replace("Puzzles",""))
    
    data = read_data("Data\\data10.txt")
    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()