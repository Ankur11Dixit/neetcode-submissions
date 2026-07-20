from typing import List

def contains_duplicate(words: List[str]) -> bool:
    seen = set()
    for element in words:
        if element in seen:
            return True
        else:
            seen.add(element)
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))