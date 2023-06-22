
import time
import functools

@functools.lru_cache(maxsize=100)
def fib(n):

    time.sleep(0.1)
    if n < 2:
        result = n
    else:
        result = fib( n -1) + fib( n -2)

    return result


start1 = time.time()

for i in range(1,11):
    start = time.time()
    print('n - {} result {}'.format(i, fib(i)))
    stop = time.time()
    print('Executed n {} time is {}'.format(i, stop - start))

stop1 = time.time()
print('Executed tima ', stop1 - start1)
print(fib.cache_info())
