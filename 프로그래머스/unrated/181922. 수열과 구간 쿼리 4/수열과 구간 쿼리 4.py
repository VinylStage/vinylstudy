def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i % k == 0:  # 인덱스 i가 k배수일때
                arr[i] += 1
    return arr