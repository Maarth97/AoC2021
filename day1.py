from typing import List

def read_data(filename : str) -> List[int]:
    data = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            data.append(int(line))
    return data


# Puzzle 1
def count_increase(data : List[int]) -> int:
    # Count how many times the data increases
    
    cnt, prev = 0, data[0]
    
    for ele in data:
        cnt = cnt + 1 if ele > prev else cnt
        prev = ele
    
    return cnt


# Puzzle 2
def count_increase_triples(data : List[int]) -> int:
    # Count how many times triples of data increases
    
    cnt, prevSum = 0, sum(data[0:3])
    
    for idx, ele in enumerate(data):
        windowSum = sum(data[idx: idx+3])
        cnt = cnt + 1 if windowSum > prevSum else cnt
        prevSum = windowSum
        
    return cnt
        
        
        
    

def main():
    data = read_data("data1.txt")
    print(f"Puzzle 1: {count_increase(data)}")
    print(f"Puzzle 2: {count_increase_triples(data)}")
    
    
    
    
if __name__ == "__main__":
    main()