

text_list = ['x','xxx','xxxxx','xxxxxxx','']


f = lambda x: len(x)
# Funkcja map() jest funkcją, która wykonuje określoną operację dla każdego elementu
# podanej sekwencji (w tym przypadku listy text_list) i zwraca wynik w postaci nowej listy

print(list(map(f, text_list)))

print(f('jakiś dowolny tekst'))

print(list(map(lambda x: len(x),text_list)))




