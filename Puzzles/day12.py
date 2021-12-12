from typing import List
import os
import copy

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        return [x.replace("\n", "").split("-") for x in f]


def find_moves(node, MAP, visitedList = None, visitTwice = False , once=False):
    # Return 1 if End found
    if node == "end": return 1
    
    # Return 0 if start was reached again
    if node == "start" and visitedList: return 0
    
    # Create VisitedList for the First Run
    if visitedList == None: visitedList = {node:0 for node in MAP if node != node.upper()}
        
    if node in visitedList: # Check for Bigger Caves
    
        # Puzzle 1: Cave visited more than once -> Return
        if  (not  visitTwice) and  visitedList[node] >= 1:
            return 0
        # Puzzle 2: Two Caves visited more than once
        elif visitTwice and visitedList[node] >= 1 and once:
            return 0
        
        visitedList[node] += 1
        once = True if  visitedList[node] >= 2 else once
    
    cnt = 0
    for next_node in MAP[node]:
        # Perform find_moves for the next node and deep copy the visitedList
        cnt += find_moves(next_node, MAP, copy.deepcopy(visitedList), visitTwice, once)
        
    return cnt
   
def create_map(data):
    MAP = dict()
    
    for node1,node2 in data:
        if node1 not in MAP: MAP[node1] = []
        if node2 not in MAP: MAP[node2] = []
        MAP[node1].append(node2)
        MAP[node2].append(node1)
        
    return MAP
        
# Puzzle 1
def f1(data : List[List[int]]) -> int:
    MAP = create_map(data)
    return find_moves("start", MAP)
    
    
# Puzzle 2
def f2(data : List[List[int]]) -> int:
    MAP = create_map(data)
    return find_moves("start", MAP, visitTwice=True)
  
        
 # MAIN       
def main(): 
    cwd = os.getcwd()
    os.chdir(cwd.replace("Puzzles",""))
    
    data = read_data("Data\\data12.txt")
    
    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()