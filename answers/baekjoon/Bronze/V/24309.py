a = []
for _ in range(3):
    a.append(int(input()))

b = a[1]
c = a[2]
a = a[0]

print((b-c)//a)