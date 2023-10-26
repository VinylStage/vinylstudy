def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if not set(str(i)) - {'0','5'}: # 차집합
            answer.append(i)
    if not answer:
        answer.append(-1)
    return answer