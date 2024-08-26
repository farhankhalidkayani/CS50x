from cs50 import get_int  # type: ignore

n = get_int("Enter Height:")
while n < 1 or n > 8:
    n = get_int("Enter Height")
for i in range(1, n + 1):
    for j in range(n):
        if j < n - i:
            print(" ", end="")
        else:
            print("#", end="")
    print("\n", end="")
