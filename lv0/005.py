"""
없는 숫자 더하기

https://school.programmers.co.kr/learn/courses/30/lessons/86051


1 ≤ numbers의 길이 ≤ 9
0 ≤ numbers의 모든 원소 ≤ 9
numbers의 모든 원소는 서로 다릅니다.

"""

# numbers = [1, 2, 3, 4, 6, 7, 8, 0]
# result 14
numbers = [5, 8, 4, 0, 6, 7, 9]
# result 6


# dict
def solution(numbers):
    arr = list(range(10))
    for i in numbers:
        arr.remove(i)
    return sum(arr)


# print(solution(numbers))

# print(tuple(i for i in numbers))
# print(map(lambda x: arr.remove(x), numbers))

# print(solution(numbers))
