a = []

for _ in range(2):
    a.append(int(input()))

b = a[1]
a = a[0]

if a >= 0:
    if b >= 0:
        print("1")
    else:
        print("4")
else:
    if b >= 0:
        print("2")
    else:
        print("3")