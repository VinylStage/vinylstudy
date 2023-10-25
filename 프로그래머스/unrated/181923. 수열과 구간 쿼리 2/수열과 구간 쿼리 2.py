def solution(arr, queries):
    answer = []
    for i, j in enumerate(queries):
        s = j[0]
        e = j[1]
        k = j[2]
        f = list(filter(lambda x: x > k, arr[s:e+1]))
        if f:
            answer.append(min(f))
        else:
            answer.append(-1)
    return answer