def solution(arr, queries):
    for i, j in enumerate(queries):
        arr[j[0]], arr[j[1]] = arr[j[1]], arr[j[0]]
    return arr