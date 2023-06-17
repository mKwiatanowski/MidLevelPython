
listA = (range(6))
listB = (range(6))

print(listA,listB)


product = []

for a in listA:
    for b in listB:
        # do listy product dodawanie elementu tuple składającego się z iteracji a i b
        product.append((a,b))

print(product)

# rozwiązanie tego samego ale w jednej lini kodu
product = [(a,b) for a in listA for b in listB]
print(product)

# to samo tylko z dodatkowym if
# w przypadku listy używamy tupleta ()
product = [(a,b) for a in listA for b in listB if a % 2 == 1 and b % 2 == 0]
print(product)

# w przypadku słownika używamy klucza i wartośći a:b
# jednak tu gdy klucz był 1 to dla niego wygenerowało 1:0 następnie 1:2 następnie 1:4 czyli za 1 iterazcja stworzyło słównik i każda kolejna iteracja nadpisała tą
# pozycję słownika w efekcie każdy klucz kończy się ostatnim wynikiem iteracji wartości i w tym wypadku będzie 1:4 3:4 5:4
product = {a:b for a in listA for b in listB if a % 2 == 1 and b % 2 == 0}
print(product)

