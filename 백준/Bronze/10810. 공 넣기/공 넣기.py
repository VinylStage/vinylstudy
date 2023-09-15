n, m = map(int, input().split())

lst = [[] for _ in range(n)]

while m > 0:
    i, j, k = map(int, input().split())
    m -= 1
    for p in range(i - 1, j):
        lst[p].append(k)
        if len(lst[p]) >= 2:
            lst[p].pop(0)
for q, _ in enumerate(lst):
    if len(lst[q]) == 0:
        lst[q].append(0)
new_lst = [i for s in lst for i in s]
print(" ".join(map(str, new_lst)))