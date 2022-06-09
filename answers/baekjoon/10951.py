a = []

while True:
    try:
        n1, n2 = map(int, input().split(" "))
    except EOFError:
        break

    a.append(n1 + n2)

for i in a:
    print(i)