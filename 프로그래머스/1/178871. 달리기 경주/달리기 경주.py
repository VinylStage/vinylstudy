def solution(players, callings):
    player = {p:i for i, p in enumerate(players)}
    for j in callings:
        p = player[j] # 3
        player[players[p-1]] += 1
        player[j] -= 1
        players[p-1], players[p] = players[p], players[p-1]
    return players