import math

def solution(array):
    array.sort()
    a = math.ceil(len(array)/2)
    return array[a-1]