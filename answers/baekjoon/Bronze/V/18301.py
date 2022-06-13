from math import floor

n, n2, n3 = map(int, input().split(" "))
print(floor((n + 1)*(n2 + 1)/(n3 + 1) - 1))