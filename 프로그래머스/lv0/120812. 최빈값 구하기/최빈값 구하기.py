from collections import Counter

def solution(array):
    counter = Counter(array)
    mode_count = max(counter.values())
    mode = [k for k, v in counter.items() if v == mode_count]
    return mode[0] if len(mode) == 1 else -1
