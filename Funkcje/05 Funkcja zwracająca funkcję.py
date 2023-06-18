

def Calculate(kind='+',*args):
    result = 0
    if kind == '+':
        for a in args:
          result += a
    elif kind == '-':
        for a in args:
            result -= a
    return result

print(Calculate('+'),1,2,3)
print(Calculate('-'),1-2-3)

# tworzenie funkcji, która przekazuje tylko 1 zmienną ze znakiem, następnie wewnątrz tej funkcji tworzymy zmienną, która tworzy nową funkcję
# funkcja ta przyjmuje argumenty.Następnie pętlą przechodzimy po wszystkich tych argumentach i w {} będzie poprzez polecenie format wstyrzkiwany znak
# który zostanie zadeklarowany w nadrzętnej funkcji. Następnie exec uruchamia stworzony tekst jako część programu i tworzy nową funkcę a global()
# jest potrzebny ponieważ żeby zwrócić wynik działania tego kodu należy uruchomić to globalnie. Na koniec w funkcji nadrzętnej zwracany jest wynik działania funkcji podrzednej
def CreateFunction(kind = '+'):
    source = '''
def f(*args):
    result = 0
    for a in args:
        result {}= a
    return result
'''.format(kind)
    exec(source,globals())

    return f

# do zmiennej zapisana jest funkcja nadrzędna, a podczas wywoływania tej nowej funkcji w jej parametrze () wskazywane są argumenty, które zostaną przekazane do
# funkcji podrzednej f, która z kolei przekaże 'znak', który był przekazany w tej zmiennej.
f_add = CreateFunction('+')
print(f_add(1,2,3,4))
f_subs = CreateFunction('-')
print(f_subs(10,20,30))


