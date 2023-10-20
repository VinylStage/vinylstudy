import sys

def bubblesort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

input = sys.stdin.readline

N = int(input())
sorted_array = bubblesort([int(input()) for _ in range(N)])
for i in sorted_array:
    print(i)