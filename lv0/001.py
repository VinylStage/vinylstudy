"""
https://school.programmers.co.kr/learn/courses/30/lessons/181905
문자열 뒤집기
문자열 my_string과 정수 s, e가 매개변수로 주어질 때, 
my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.

my_string은 숫자와 알파벳으로만 이루어져 있습니다.
1 ≤ my_string의 길이 ≤ 1,000
0 ≤ s ≤ e < my_string의 길이

입출력 예 #1

예제 1번의 my_string에서 인덱스 6부터 인덱스 12까지를 뒤집은 문자열은 
"ProgrammerS123"이므로 "ProgrammerS123"를 return 합니다.
입출력 예 #2

예제 2번의 my_string에서 인덱스 4부터 인덱스 10까지를 뒤집으면 원래 문자열과 같은 "Stanley1yelnatS"이므로 "Stanley1yelnatS"를 return 합니다.
"""

my_string = "Progra21Sremm3"
s = 6
e = 12
# result "ProgrammerS123"
# my_string = "Stanley1yelnatS"
# s = 4
# e = 10
# result "Stanley1yelnatS"

"""elisa"""

# 쨌다가
# 접합수술

# new_string = []
# # new_string.append(__object)
# new_string.append(my_string[: s - 1])
# new_string.append(reversed(my_string[s:e]))
# new_string.append(my_string[e + 1 :])
# print(new_string)


# reversed_str = list(reversed(my_string[s:e]))
# print("".join(reversed_str))


def solution(my_string, s, e):
    a = my_string[:s]
    b = "".join(reversed(my_string[s : e + 1]))
    c = my_string[e + 1 :]

    answer = a + b + c
    return answer


"""vin"""

# def solution(my_string, s, e):
#     return my_string.replace(my_string[s : e + 1], "".join(reversed(my_string[s : e + 1])))
