
# cache będzie przechowywał w pamięci wyniki wcześniejszych uruchomień danej funkcji, dzięki czemu jeśli użytkownik wywoła poraz kolejny tą samą funkcję
# to wynik będzie gotowy natychmiast bez wykonywania funkcji.

import time
import functools

# dekorator @functools.lru_cache() dzięki zastosowaniu lru_cache() można zapisać wynik działania w pamięci, i jeśli to samo działanie by miało być wykonane ponownie,
# wówczas python pobierze z pamięci komputera już wcześniej obliczoną wartość gdy pierwszy raz było użyte dane wyrażenie.
@functools.lru_cache()
def Factorial(n):

    # sleep(czas w sekundach) pozwala na opóźnienie wykonania dalszej części kodu o wartośc parametru podanego w sekundach
    time.sleep(0.1)
    if n == 1:
        return n
    else:
        return n * Factorial(n-1)

start = time.time()
for i in range(1,11):
    print('{}! = {} '.format(i, Factorial(i)))
stop = time.time()

print('Execution time',stop - start)

print(Factorial.cache_info())

'''
start = time.time()
for i in range(1,11):
    print('{}! = {} '.format(i, Factorial(i)))
stop = time.time()

print('Execution time',stop - start)
'''









