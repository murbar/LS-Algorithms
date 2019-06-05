# import time
from timeit import default_timer as timer

# def timeit(fn):
#     def wrapper(*args):
#         start = time.time()
#         result = fn(*args)
#         end = time.time()
#         print(f"Time: {(end - start) * 1000} ms")
#         return result
#     return wrapper


def naive_fib(n):
    if n < 2:
        return n

    return naive_fib(n-1) + naive_fib(n-2)


def cached_fib(n):
    cache = {}

    def fib(n):
        if n < 2:
            return n

        cached = cache.get(n, None)
        if cached:
            return cached

        cache[n] = fib(n-1) + fib(n-2)
        return cache[n]

    return fib(n)


def iterative_fib(n):
    answer = 0
    n1, n2 = 1, 0
    for i in range(n-1):
        answer = n1 + n2
        n1, n2 = answer, n1
    return answer


t1 = timer()
print(iterative_fib(3000))
t2 = timer()
print(f"Took {(t2 - t1)/1000} S")
print(cached_fib(30))
print(naive_fib(30))
