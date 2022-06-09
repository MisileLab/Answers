a = []

while True:
    try:
        a.append(input())
    except EOFError:
        break

for i in a:
    print(i)