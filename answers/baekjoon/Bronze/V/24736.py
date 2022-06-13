a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

def get_point(a: list):
    return str(6*a[0]+3*a[1]+2*a[2]+1*a[3]+2*a[4])

print(f"{get_point(a)} {get_point(b)}")