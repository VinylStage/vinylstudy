def solution(num_list):
    even = ''
    odd = ''
    for i in num_list:
        if not (i) % 2:
            even+=str(i)
        else:
            odd+=str(i)
    return sum(map(int, [even, odd]))