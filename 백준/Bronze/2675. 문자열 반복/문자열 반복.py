t = int(input())
qr = []
for _ in range(t):
    r, s = input().split()
    qr.append([i*int(r) for i in s])
for i in qr:
    print(''.join(i))