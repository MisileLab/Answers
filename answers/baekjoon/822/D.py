a = int(input())
b = "".join(input().split(" "))
c = []

for _ in range(a):
    c.append(b)

print("".join(c))