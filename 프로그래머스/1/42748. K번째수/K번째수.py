def solution(array, commands):
    answer = []
    # [i-1:j], 정렬하고 [k-1]
    for a in commands:
        answer.append(sorted(array[a[0]-1:a[1]])[a[2]-1])
    return answer