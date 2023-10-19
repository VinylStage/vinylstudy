def solution(citations):
    answer = 0
    citations.sort()
    for i, j in enumerate(citations):
        hIndex = len(citations)-i
        if j >= hIndex:
            answer = hIndex
            break
    return answer