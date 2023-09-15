non = [int(input()) for i in range(28)]
non.sort()
lst = []
count = 0
for i, j in enumerate(non):
    count += 1
    if count != j:
        non.insert(i, count)
        lst.append(count)
if len(non) != 30:
    non.append(30)
    lst.append(30)
lst.sort()
for s in lst:
    print(s)