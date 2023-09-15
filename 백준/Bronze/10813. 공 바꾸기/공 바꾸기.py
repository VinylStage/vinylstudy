n, m = map(int, input().split())

lst = [i + 1 for i in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    a = lst[i - 1]
    lst[i - 1] = lst[j - 1]
    lst[j - 1] = a
print(" ".join(map(str, lst)))