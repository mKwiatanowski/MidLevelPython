
def double(x):
    return x * 2


x = 10
x = double(x)
print(x)


x = 10
# powyższy zapis wymaga kilku linijek, za pomocą lambda można to skrócić
# do zmiennej przyposuje lambda po czym nazwa parametru i : następnie wpisuje wartość tego wyrażenia
f = lambda x: x * 2
# wywołuje zmienna f z parametrem lambda
print(f(x))


def power(x,y):
    return x ** y

x = 5
y = 3
print(power(x,y))

f = lambda x,y: x ** y # funkcja anonimowa przypisane do zmiennej f
print(f(x,y))


list_numbers = [1,2,3,4,11,14,15,20,21]





def is_odd(x):
    # % dzielenie modulo != sprawdzenie czy reszta dzielenia jest różna od 0
    return x % 2 != 0

print(is_odd(7), is_odd(4))

# filter(funkcja warunek sprawdzający, miejsce w którym ma być to sprawdzane np lista)
filtered_list = list(filter(is_odd, list_numbers))
print(filtered_list)


# lambda
filtered_list = list(filter(lambda x: x % 2 != 0, list_numbers))
print(filtered_list)



print(list(filter(lambda  x: x % 2 != 0, list_numbers)))


def generate_multiply_function(n):
    return lambda x: n * x

mul_2 = generate_multiply_function(2)
mul_3 = generate_multiply_function(3)

print(mul_2(13), mul_3(8))





