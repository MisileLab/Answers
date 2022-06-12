a = input()
b = []

for i in a:
    i = int(i)
    b.append(i*i*i*i*i)

print(sum(b))