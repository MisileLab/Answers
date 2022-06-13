a = list(map(int, input().split(" ")))

print(abs((lambda a: a[0] - a[1] if (a[0] - a[1])>=0 else a[0] - a[1])(a)))