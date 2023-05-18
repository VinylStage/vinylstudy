"""
https://school.programmers.co.kr/learn/courses/30/lessons/181836
그림 확대

문제 설명
직사각형 형태의 그림 파일이 있고, 
이 그림 파일은 1 × 1 크기의 정사각형 크기의 픽셀로 이루어져 있습니다. 
이 그림 파일을 나타낸 문자열 배열 picture과 정수 k가 매개변수로 주어질 때, 
이 그림 파일을 가로 세로로 k배 늘린 그림 파일을 나타내도록 
문자열 배열을 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ picture의 길이 ≤ 20 ❤️
1 ≤ picture의 원소의 길이 ≤ 20
모든 picture의 원소의 길이는 같습니다.
picture의 원소는 '.'과 'x'로 이루어져 있습니다.
1 ≤ k ≤ 10
"""

pictures = [
    ".xx...xx.",
    "x..x.x..x",
    "x...x...x",
    ".x.....x.",
    "..x...x..",
    "...x.x...",
    "....x....",
]
k = 5

# result[
#     "..xxxx......xxxx..",
#     "..xxxx......xxxx..",
#     "xx....xx..xx....xx",
#     "xx....xx..xx....xx",
#     "xx......xx......xx",
#     "xx......xx......xx",
#     "..xx..........xx..",
#     "..xx..........xx..",
#     "....xx......xx....",
#     "....xx......xx....",
#     "......xx..xx......",
#     "......xx..xx......",
#     "........xx........",
#     "........xx........",
# ]

# [
#     "..xxxx......xxxx..",
#     "xx....xx..xx....xx",
#     "xx......xx......xx",
#     "..xx..........xx..",
#     "....xx......xx....",
#     "......xx..xx......",
#     "........xx........",
# ]

# pictures = ["x.x", ".x.", "x.x"]
# k = 3

# result
# [
#     "xxx...xxx",
#     "xxx...xxx",
#     "xxx...xxx",
#     "...xxx...",
#     "...xxx...",
#     "...xxx...",
#     "xxx...xxx",
#     "xxx...xxx",
#     "xxx...xxx",
# ]


"""elisa"""
answer = []

# for i in pictures:
#     answer.append(i.replace(".", "." * k).replace("x", "x" * k))


# for i,j in picture:
#     answer.append(i.replace(".", "."*k))
#     answer.append(j.replace("x", "x"*k))
# # ValueError: too many values to unpack (expected 2)

# for i in picture:
#     answer.append(i.replace({".":"."*k, "x":"x"*k}))
# TypeError: replace expected at least 2 arguments, got 1

# for i in picture:
#     answer.append(i.replace([".", "x"], ["."*k, "x"*k]))
# TypeError: replace() argument 1 must be str, not list

# for i in picture:
#     answer.append(i.replace(".", "."*k).replace("x", "x"*k))
# 결과값 몇개 다름


for j in pictures:
    for i in range(k):
        answer.append(j.replace(".", "." * k).replace("x", "x" * k))

print(answer)


"""vin"""

# pic = []
# ans = ""
# wer = []
# ans = "".join(pictures)
# for i in ans:
#     for j in range(k):
#         wer.append(i * k)

# print([wer[i : i + len(pictures[0])] for i in range(0, len(wer), len(pictures[0]))])

# def solution(picture, k):
#     answer = []
#     return answer
# [
#     "..xxxx......xxxx..",
#     "xx....xx..xx....xx",
#     "xx......xx......xx",
#     "..xx..........xx..",
#     "....xx......xx....",
#     "......xx..xx......",
#     "........xx........",
#     "..xxxx......xxxx..",
#     "xx....xx..xx....xx",
#     "xx......xx......xx",
#     "..xx..........xx..",
#     "....xx......xx....",
#     "......xx..xx......",
#     "........xx........",
# ]
# [
#     "..xxxx......xxxx..",
#     "..xxxx......xxxx..",
#     "xx....xx..xx....xx",
#     "xx....xx..xx....xx",
#     "xx......xx......xx",
#     "xx......xx......xx",
#     "..xx..........xx..",
#     "..xx..........xx..",
#     "....xx......xx....",
#     "....xx......xx....",
#     "......xx..xx......",
#     "......xx..xx......",
#     "........xx........",
#     "........xx........",
# ]
# [
#     ".....xxxxxxxxxx...............xxxxxxxxxx.....",
#     ".....xxxxxxxxxx...............xxxxxxxxxx.....",
#     ".....xxxxxxxxxx...............xxxxxxxxxx.....",
#     ".....xxxxxxxxxx...............xxxxxxxxxx.....",
#     ".....xxxxxxxxxx...............xxxxxxxxxx.....",
#     "xxxxx..........xxxxx.....xxxxx..........xxxxx",
#     "xxxxx..........xxxxx.....xxxxx..........xxxxx",
#     "xxxxx..........xxxxx.....xxxxx..........xxxxx",
#     "xxxxx..........xxxxx.....xxxxx..........xxxxx",
#     "xxxxx..........xxxxx.....xxxxx..........xxxxx",
#     "xxxxx...............xxxxx...............xxxxx",
#     "xxxxx...............xxxxx...............xxxxx",
#     "xxxxx...............xxxxx...............xxxxx",
#     "xxxxx...............xxxxx...............xxxxx",
#     "xxxxx...............xxxxx...............xxxxx",
#     ".....xxxxx.........................xxxxx.....",
#     ".....xxxxx.........................xxxxx.....",
#     ".....xxxxx.........................xxxxx.....",
#     ".....xxxxx.........................xxxxx.....",
#     ".....xxxxx.........................xxxxx.....",
#     "..........xxxxx...............xxxxx..........",
#     "..........xxxxx...............xxxxx..........",
#     "..........xxxxx...............xxxxx..........",
#     "..........xxxxx...............xxxxx..........",
#     "..........xxxxx...............xxxxx..........",
#     "...............xxxxx.....xxxxx...............",
#     "...............xxxxx.....xxxxx...............",
#     "...............xxxxx.....xxxxx...............",
#     "...............xxxxx.....xxxxx...............",
#     "...............xxxxx.....xxxxx...............",
#     "....................xxxxx....................",
#     "....................xxxxx....................",
#     "....................xxxxx....................",
#     "....................xxxxx....................",
#     "....................xxxxx....................",
# ]
# [
#     ".....xxxxxxxxxx...............xxxxxxxxxx.....",
#     "xxxxx..........xxxxx.....xxxxx..........xxxxx",
#     "xxxxx...............xxxxx...............xxxxx",
#     ".....xxxxx.........................xxxxx.....",
#     "..........xxxxx...............xxxxx..........",
#     "...............xxxxx.....xxxxx...............",
#     "....................xxxxx....................",
#     ".....xxxxxxxxxx...............xxxxxxxxxx.....",
#     "xxxxx..........xxxxx.....xxxxx..........xxxxx",
#     "xxxxx...............xxxxx...............xxxxx",
#     ".....xxxxx.........................xxxxx.....",
#     "..........xxxxx...............xxxxx..........",
#     "...............xxxxx.....xxxxx...............",
#     "....................xxxxx....................",
#     ".....xxxxxxxxxx...............xxxxxxxxxx.....",
#     "xxxxx..........xxxxx.....xxxxx..........xxxxx",
#     "xxxxx...............xxxxx...............xxxxx",
#     ".....xxxxx.........................xxxxx.....",
#     "..........xxxxx...............xxxxx..........",
#     "...............xxxxx.....xxxxx...............",
#     "....................xxxxx....................",
#     ".....xxxxxxxxxx...............xxxxxxxxxx.....",
#     "xxxxx..........xxxxx.....xxxxx..........xxxxx",
#     "xxxxx...............xxxxx...............xxxxx",
#     ".....xxxxx.........................xxxxx.....",
#     "..........xxxxx...............xxxxx..........",
#     "...............xxxxx.....xxxxx...............",
#     "....................xxxxx....................",
#     ".....xxxxxxxxxx...............xxxxxxxxxx.....",
#     "xxxxx..........xxxxx.....xxxxx..........xxxxx",
#     "xxxxx...............xxxxx...............xxxxx",
#     ".....xxxxx.........................xxxxx.....",
#     "..........xxxxx...............xxxxx..........",
#     "...............xxxxx.....xxxxx...............",
#     "....................xxxxx....................",
# ]
