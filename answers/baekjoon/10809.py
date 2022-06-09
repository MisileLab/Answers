import string

a = list(input())
b = string.ascii_lowercase

for i in b:
    try:
        print(a.index(i))
    except ValueError:
        print(-1)