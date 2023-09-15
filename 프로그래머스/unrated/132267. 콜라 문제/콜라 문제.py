def solution(a, b, n):
    c = 0
    while n >= a:
        n -= a
        n += b
        c += b
    return c