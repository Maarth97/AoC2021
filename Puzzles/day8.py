from typing import List
import os

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        return [x.replace("\n", "") for x in f]

   
# Puzzle 1
def f1(data : List[List[int]]) -> int:

    cnt = 0
    for idx, line in enumerate(data):
        L = line.split("|")
        before = L[0].strip().split(" ")
        after = L[1].strip().split(" ")
        
        cnt += sum([1 for ele in after if len(ele) in [2,3,4,7]])

    return cnt
    
    
    
def sort_string(s : str):
    return "".join(sorted(s))

def contain_all(s1, s2):
    return all([True if ele in s2 else False for ele in s1])

def update(ele, num, RMAP, MAP, Vec = None):
    RMAP[num], MAP[ele] = ele, num
    if Vec: Vec.remove(ele)

    
# Puzzle 2
def f2(data : List[List[int]]) -> int:
    HT = {2: 1, 4:4, 3:7, 7:8}
    S = 0
    
    for idx, line in enumerate(data):
        
        MAP = dict()
        RMAP = dict()
    
        L = line.split("|")
        after = [sort_string(ele) for ele in L[1].strip().split(" ")]
        before = [sort_string(ele) for ele in L[0].strip().split(" ")]
        
        # Check 1, 4, 7, 8 ===================================================
        for ele in before:
            if len(ele) in HT:
                MAP[ele] = HT[len(ele)]
                RMAP[HT[len(ele)]] = ele        
       
        before = [ele for ele in before if len(ele) not in [2,7,4,3]]
                     
        assert len(before) == 6
        
        #check 3:    
        for ele in before:
            if contain_all(RMAP[1], ele) and len(ele) == 5:
                update(ele, 3, RMAP, MAP, before);break
        assert len(before) == 5
        
        #Check 9:    
        for ele in before:
            if contain_all(RMAP[3], ele) and len(ele) == 6:
                update(ele, 9, RMAP, MAP, before); break      
        assert len(before) == 4    
        
        #Check 0:    
        for ele in before:
            if contain_all(RMAP[1], ele) and len(ele) == 6:
                update(ele, 0, RMAP, MAP, before); break   
        assert len(before) == 3
        
        #check 6:       
        for ele in before:
            if len(ele) == 6:
                update(ele, 6, RMAP, MAP, before); break
        assert len(before) == 2
        
        #check 5:   
        for ele in before: 
            if contain_all(ele, RMAP[6]) and len(ele) == 5: 
                update(ele, 5, RMAP, MAP, before); break
        assert len(before) == 1
        
        # check 2
        for ele in before: 
            update(ele, 2, RMAP, MAP, before); break
        assert len(before) == 0

            
        # Decoder
        S += int("".join([str(MAP[ele]) for ele in after]))

    
    return S
        
        
 # MAIN       
def main(): 
    cwd = os.getcwd()
    os.chdir(cwd.replace("Puzzles",""))
    
    data = read_data("Data\\data8.txt")
    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()