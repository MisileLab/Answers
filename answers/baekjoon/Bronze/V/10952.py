a = []

while True:
    n1, n2 = map(int, input().split(" "))

    if n1 == 0 and n2 == 0:
        break
    else:
        a.append(n1 + n2)

for i in a:
    print(i)