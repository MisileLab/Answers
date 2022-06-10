from datetime import date, timedelta

a = []

for _ in range(int(input())):
    y, m = map(int, input().split(" "))
    a.append(date(y, m, m) - timedelta(days=m))

for i in a:
    print(f"{i.year} {i.month} {i.day}")