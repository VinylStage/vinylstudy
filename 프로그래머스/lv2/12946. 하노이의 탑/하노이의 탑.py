def solution(n):
    return hanoi(n, 1, 3, [])

def hanoi(n, x, y, answer):
    """원반 n개를 x기둥에서 y기둥으로 옮김

    Args:
        n (int): 원반의 갯수
        x (int): 시작 기둥의 번호
        y (int): 목표 기둥의 번호
        answer (list): 이동한 내용

    Returns:
        list: 이동한 내용
    """
    if n == 0:
        return
    hanoi(n - 1, x, 6 - (x + y), answer)
    answer.append([x, y])
    hanoi(n - 1, 6 - (x + y), y, answer)

    return answer