from typing import List, Tuple
from collections import Counter

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        return [x.replace("\n", "") for x in f]


def get_sequence(x1:int,y1:int,x2:int,y2:int, diag:bool=False)->Tuple[int,int]:
    """
    Args:
        x1 (int): x-Position von Punkt 1
        y1 (int): y-Position von Punkt 1
        x2 (int): x-Position von Punkt 2
        y2 (int): y-Position von Punkt 2
        diag (bool, optional): True: Berücksichtigt auch Diagonale im +/-45° Winkel. Defaults to False.

    Yields:
        Iterator[Tuple[int,int]]: Iteriert über alle Punkte zwischen [x1,y1] und [x2,y2]
    """
    
    # Waagerecht  
    if x1==x2:
        for y in range(min(y1,y2), max(y1,y2) +1):
            yield x1, y
            
    # Senkrecht
    elif y1 == y2:
        for x in range(min(x1,x2), max(x1,x2) +1):
            yield x, y1

    # Positive Steigung   
    elif diag and (x1-x2)/(y1-y2) > 0:
        for x,y in zip( range(min(x1,x2), max(x1,x2) +1), range(min(y1,y2), max(y1,y2) +1)): 
            yield x,y
            
    # Negative Steigung        
    elif diag and (x1-x2)/(y1-y2) < 0:
        for x,y in zip( range(min(x1,x2), max(x1,x2) +1), range(max(y1,y2), min(y1,y2) -1, -1)):
            yield x,y


            
    
   
# Puzzle 1
def f1(data : List[str]) -> int:
    count = Counter()
    for line in data:
        (x1,y1),(x2,y2) = [(int(x), int(y)) for x,y in [ele.split(",") for ele in line.split(" -> ")]]
        count.update(get_sequence(x1,y1,x2,y2, diag=False))
    return sum([1 for ele in count if count[ele] > 1])
     
            
# Puzzle 2
def f2(data : List[str]) -> int:
    count = Counter()
    for line in data:
        (x1,y1),(x2,y2) = [(int(x), int(y)) for x,y in [ele.split(",") for ele in line.split(" -> ")]]
        count.update(get_sequence(x1,y1,x2,y2, diag=True))
    return sum([1 for ele in count if count[ele] > 1])
        
        
 # MAIN       
def main(): 
               
    data = read_data("Data\\data5.txt")
    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")  # 21305

if __name__ == "__main__":
    main()