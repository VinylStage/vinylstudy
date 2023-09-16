n, m = map(int, input().split())

lst = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j = map(int, input().split())
    arr = lst[i - 1 : j]
    arr.reverse()
    lst[i - 1 : j] = arr

print(" ".join(map(str, lst)))