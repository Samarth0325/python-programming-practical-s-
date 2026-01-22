import time
def timer(fun):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = fun(*args,**kwargs)
        print(f"Timer:{time.time() - start}")
        return result
    return wrapper

@timer
def my_function():
    time.sleep(1)
my_function()