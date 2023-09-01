import math

def solution(numer1, denom1, numer2, denom2):
    num_lcm = (denom1 * denom2) // math.gcd(denom1, denom2)
    a = int(num_lcm / denom1 * numer1)
    b = int(num_lcm / denom2 * numer2)
    c = a+b
    d = math.gcd(c, num_lcm)
    return [c/d, num_lcm/d]