def fibonnaci(a: int) -> int:
    if a <= 1:
        return a
    else:
        return fibonnaci(a-1) + fibonnaci(a-2)

print(fibonnaci(int(input())))