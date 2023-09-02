n = int(input())
c = list(map(int, input().split()))
m = int(input())
d = list(map(int, input().split()))
temp = {}
for i in range(len(c)):
    temp[c[i]] = 0
print(*[+(d[k] in temp) for k in range(m)])