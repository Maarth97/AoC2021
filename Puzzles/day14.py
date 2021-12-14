from typing import List
import os
from collections import Counter, defaultdict

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        poly = f.readline().replace("\n","").strip()
        f.readline()
        data = [[a for a in x.replace("\n", "").split(" -> ")] for x in f]

    return poly, data



def step(rules, HT, count):
            
    newHT = defaultdict(int)
    
    for ele in HT:
        if ele in rules:
            newHT[ele[0]      + rules[ele]] += HT[ele]
            newHT[rules[ele]  + ele[1]]     += HT[ele]
            count[rules[ele]]               += HT[ele]

        else:
            newHT[ele] = HT[ele]
        
    return newHT, count


            
def count_poly(poly, rules, STEPS):
    HT = defaultdict(int)   # Contains Number of Pairs
    count = Counter(poly)   # Contains Number of Singles
    
    for val1, val2 in zip(poly[:-1], poly[1:]):
        HT[val1+val2] += 1
        
    for t in range(STEPS):
        HT, count = step(rules, HT, count)
        
    return count
        
    
   
# Puzzle 1
def f1(data : List[List[int]], STEPS : int = 10) -> int:

    poly, rules = data
    rules = {outer: middle for (outer,middle) in rules}
    c = count_poly(poly, rules, STEPS)

    maxV, minV = c.most_common()[0][1], c.most_common()[-1][1]
    return maxV - minV
    
    
# Puzzle 2
def f2(data : List[List[int]]) -> int:
    return f1(data, STEPS=40)
        
    
        
 # MAIN       
def main(): 
    cwd = os.getcwd()
    os.chdir(cwd.replace("Puzzles",""))
    
    data = read_data("Data\\data14.txt")

    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()