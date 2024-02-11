def caching_fibonacci():
    cache ={0: 0, 1: 1}
    def fibonacci(n):       
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibonacci(n-1) + fibonacci(n-2)
            return cache[n]
    return fibonacci 

fib = caching_fibonacci()

print(fib(10))
print(fib(15)) 