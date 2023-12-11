def solution(n, lost, reserve):
    std = {i: 1 for i in range(1, n + 1)}
    for l in lost:
        std[l] = 0
    for r in reserve:
        std[r] += 1

    for i in range(1, n + 1):
        if std[i] == 0:
            if i - 1 > 0 and std[i - 1] == 2:
                std[i - 1] -= 1
                std[i] += 1
            elif i + 1 <= n and std[i + 1] == 2:
                std[i + 1] -= 1
                std[i] += 1
    return n - list(std.values()).count(0)                        
                            