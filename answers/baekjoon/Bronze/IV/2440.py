a = int(input())
b = ""

for i in range(1, a+1):
    b = b + ("*" * (a - (a - i)))
    if i != a:
        b = b + "\n"

print(b[::-1])