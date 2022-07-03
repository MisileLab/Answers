a = list(map(int, input().split(" ")))
b = 0

if a[0] == a[1] and a[1] == a[2]:
    b = 10000 + a[0] * 1000
elif a[0] == a[1] or a[1] == a[2]:
    b = 1000 + a[1] * 100
elif a[0] == a[2]:
    b = 1000 + a[2] * 100
else:
    b = max(a) * 100

print(b)