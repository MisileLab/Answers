a = int(input())
b = []
c = []

for _ in range(a):
    input()
    b.append(list(map(int, input().split(" "))))

for i in b:
    n = len(i)
    temp = []
    for i2 in i:
        temp.append(n - i2 + 1)
    if sum(temp) == sum(i):
        c.append("YES")
    else:
        c.append("NO")

for i in c:
    print(i)