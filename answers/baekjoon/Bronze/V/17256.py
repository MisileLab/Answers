a = list(map(int, input().split(" ")))
b = []
c = list(map(int, input().split(" ")))

b.append(str(c[0] - a[2]))
b.append(str(c[1] // a[1]))
b.append(str(c[2] - a[0]))

print(" ".join(b))