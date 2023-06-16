

number = 10
print('Variable number: ', number, id(number))

number += 2
print('Variable number: ', number, id(number))

# zmienna typu int jest niezmienna
# w pythonie w odroznieniu do innych j. programowania, nie jest zapisywana w pamieci zmienna bez wzgledu na jej wartosc
# w pytjonie jest zapisana wartosc tej zmiennej bez wzgledu jak ta zmienna sie nazywa

# tutaj tak samo jak wyzej zmienna jest niezmienna ( immutable = niezmienny )
text = 'Africa'
print('Variable text: ', text, id(text))
text += ' is not'
print('Variable text: ', text, id(text))


# zmienna która jest zmienna mówimy:
# mutable = zmienny
# zmienna która jest niezmienna mówimy:
# immutable = niezmienny

# zmienna lista jest zmienna mutable
list = [1,2,3]
print('Variable list: ', list, id(list))
list.append(4)
print('Variable list: ', list, id(list))


# zmienne które są mutable mogą spowodować pewną niespodziankę
# mimo ze do list2 został dodany element 5 to także do list został dodany element 5 ponieważ list i list2 wskazywalo na ten sam obszar w pamięci bo jest to jedna i ta sama zmienna
list2 = list
print('Variable list2: ', list2, id(list2))
list2.append(5)
print('Variable list: ', list, id(list))
print('Variable list2: ', list2, id(list2))

# trzeba pamiętać jeśli tworzę kopię listy, w celu np sprawdzenia działania programu, należy zrobić kopię listy po przez funkcję copy(), ponieważ stworzy to nową listę
# w nowej lokalizacji i dziłania na tej nowej liście nie będą miały wpływu na pierwotną listę.
# Gdyby natomiast kopię zrobić poprzez lista = lista2 to działania na list2 będą miały wpływ na list
list3 = list.copy()
print('Variable list: ', list, id(list))
print('Variable list3: ', list3, id(list3))
list.append(6)
print('Variable list: ', list, id(list))
print('Variable list3: ', list3, id(list3))






