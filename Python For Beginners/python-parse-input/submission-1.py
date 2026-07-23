from typing import List

def read_integers() -> List[int]:
    box = input()
    box1 = [int(x) for x in box.split(',')]
    return box1

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
