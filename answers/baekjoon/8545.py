a = list(input())
b = ""
a.sort(reverse=True)

for i in a:
    b = b + i

print(b)