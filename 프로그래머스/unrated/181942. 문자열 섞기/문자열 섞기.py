def solution(str1, str2):
    answer = []
    for i in str1:
        answer.append(i)
    for i, j in enumerate(str2):
        answer[i] += j
    answer = "".join(answer)
    return answer