def fib(n):
    a, b =0, 1
    for i in range(n):
        if a>100:
         break
        
        print(a)
        a, b=b, a+b

        
fib(100000)
