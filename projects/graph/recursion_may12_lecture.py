def f(n):
    if n == 0:
        return 3490
    print(n)
    return f(n-1)

print(f(10))

print(f(10000))