def solution(code):
    mode = False
    ret = ''
    for i, j in enumerate(code):
        if mode:
            if j != "1":
                if i % 2:
                    ret += j
            else:
                mode = False
        else:
            if j != "1":
                if i % 2 == 0:
                    ret += j
            else:
                mode = True
    if not ret:
        return "EMPTY"
    return ret