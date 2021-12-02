from typing import List

# Get Data Input
def read_data(filename : str) -> List[int]:
    with open(filename) as f:
        return [x for x in f]


# Puzzle 1
def f1(data : List[str]) -> int:
    hor, depth = 0,0
    
    for idx, ele in enumerate(data):
        command, num = ele.split(" ")
        hor += int(command == "forward") * int(num)
        depth += int(command == "down") * int(num)
        depth -= int(command == "up") * int(num)
        
    return hor*depth
# Puzzle 2
def f2(data : List[str]) -> int:
    hor, depth, aim = 0,0,0
    
    for idx, ele in enumerate(data):
        command, num = ele.split(" ")
        hor += int(command == "forward") * int(num)
        depth += int(command == "forward") * int(num)*aim
        aim += int(command == "down") * int(num)
        aim -= int(command == "up") * int(num)
        
    return hor*depth
        
 # MAIN       
def main():
    data = read_data("Data\\data2.txt")
    print(f"Puzzle 1: {f1(data)}")
    print(f"Puzzle 2: {f2(data)}")

if __name__ == "__main__":
    main()