def solution(sides):
    # sides중 하나가 가장 긴 변일경우 A
        # other이 가장 작은 변일경우 A-1
        # a = max(sides)
        # min(sides) + other > a
        # range(min(sides), a+1
    # 나머지 하나가 가장 긴 변일 경우 B
        # len(range(max(sides), sum(sides) + 1))
    # A + B
    a = [i for i in range(max(sides) - min(sides)+1, max(sides)+1)]
    b = [i for i in range(max(sides)+1, sum(sides))]
    return len(a)+len(b)