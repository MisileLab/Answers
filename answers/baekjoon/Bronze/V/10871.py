_, a = map(int, input().split(" "))
b = list(map(int, input().split(" ")))
c = []

for i in b:
    if i < a:
        c.append(str(i))

print(" ".join(c))