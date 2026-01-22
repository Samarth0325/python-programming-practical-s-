def fib_gen():
    a, b=0,1
    while True:
        yield a
        a,b=b,a+b
g = fib_gen()
print([next(g) for _ in range(5)])