from typing import List
import os
import numpy as np

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        data = [x.split(",") for x in f]
        return [int(x) for x in data[0]]


   
# Puzzle 1 - Schmal aber nicht Speicheroptimiert -> Für große Zeiten nicht zu gebrauchen
def f1(data : List[int], NUM_DAYS = 80) -> int:
    population = data
    
    for day in range(1, NUM_DAYS+1):
        population = [fish - 1  for fish in population]
        population = population + [8 for _ , fish in enumerate(filter(lambda x: x < 0, population))]
        population = [fish if fish >= 0 else 6 for fish in population]
        
        
        
    return len(population)
    
# Puzzle 2 - Speicheroptimierte Version mit Hashtable
def f2(data : List[int], NUM_DAYS = 80) -> int:
    population = {i:0 for i in range((9))}
    for ele in data: population[ele] += 1
    
    for day in range(1, NUM_DAYS+1):
        new_fish = population[0]
        for key in population:
            if key != 8: population[key] = population[key+1]
        population[8] = new_fish
        population[6] += new_fish
                 
    return sum([population[key] for key in population]) 
        
        
 # MAIN       
def main():
    cwd = os.getcwd()
    os.chdir(cwd.replace("Puzzles",""))
    
    data = read_data("Data\\data6.txt")

    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data, NUM_DAYS=256)}")

if __name__ == "__main__":
    main()