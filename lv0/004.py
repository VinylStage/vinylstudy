"""
https://school.programmers.co.kr/learn/courses/30/lessons/120866

안전지대

다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 
위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.


지뢰는 2차원 배열 board에 1로 표시되어 있고 
board에는 지뢰가 매설 된 지역 1과, 
지뢰가 없는 지역 0만 존재합니다.
지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 
안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

board는 n * n 배열입니다.
1 ≤ n ≤ 100
지뢰는 1로 표시되어 있습니다.
board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.
"""

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
]
# result 16


board2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
]


"""elisa"""


def solution(board):
    answer = 0
    return answer


"""vinyl"""


# answer = 0
# for i, j in enumerate(board):
#     for k, l in enumerate(j):
#         try:
#             if l == 1:
#                 if j[k - 1] == 1 and j[k + 1] == 1:
#                     pass
#                 elif
#             else:
#                 print(i, k, "no")
#         except IndexError:
#             pass
