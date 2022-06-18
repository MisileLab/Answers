a = []
b = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
while True:
    temp = input()
    temp2 = 0

    if temp == "#":
        break

    for i in b:
        temp2 = temp2 + temp.count(i)

    a.append(temp2)

for i in a:
    print(i)