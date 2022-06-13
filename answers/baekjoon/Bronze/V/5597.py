a = list(range(1, 31))

for _ in range(28):
    a.remove(int(input()))

a.sort()

for i in a:
    print(i)