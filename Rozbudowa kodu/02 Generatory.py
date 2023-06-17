
listA = (range(6))
listB = (range(6))

print(listA,listB)


product = []

for a in listA:
    for b in listB:
        product.append((a,b))

print(product)

product = [(a,b) for a in listA for b in listB]
print(product)

product = [(a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]
print(product)

product = {a:b for a in listA for b in listB if a % 2 == 1 and b % 2 == 0}
print(product)


# w celu utworzenia generatora należy użyć nawiasów ()
# generator jest typu generator
# generator będzie przydatny tam, gdzie danych będzie masakrycznie dużo, dlatego gdybym chciał do tego wykorzystać listę to by trzeba było na to poświęcić maskakrycznie dużo
# pamięci i w pamięci przechowywać wszystkie kombinacje listy a i b, które mają po kilka tysięcy rekordów
gen = ((a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)
print(gen)

# w celu wyświetlenia zawartości generatora należy użyć funkcji next() i tym sposobem zostanie zwrócona pierwsza wartość jaka znajduje się w tym generatorze
print(next(gen))
# kolejna wartośc do wyświetlenia to kolejny raz użyta funkcja next()
print(next(gen))

# ponieważ ja użyłem już 2x next() to pętla wyświetliła tylko pozostałe 7 wolnych kombinacji
print('-'*30)
for x in gen:
    print(x)

print('-'*30)
# drugie polecenie for nie pokazuje już żadnych wyników z generatora
for x in gen:
    print(x)()

# aby użyć ponownie generator należy go ponownie wywołać ( nie ma polecenia która by czyściła generator )
gen = ((a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0)

# aby pobierać dane z generatora ręcznie użyjemy do tego pętli while która będzie się wykonywać w nieskończoność
while True:
    # gdy skończy się zakres generatora to zakończy się to błędem dlatego pakujemy to w try except
    try:
        print(next(gen))
    # gdy pokaże się bład informuje o pobraniu wszystkich wartości i break kończe działanie pętli
    except StopIteration:
        print('All value have been generated')
        break
