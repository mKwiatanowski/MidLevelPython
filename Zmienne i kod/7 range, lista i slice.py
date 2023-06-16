
# range(x) oznacza, że będzie coś liczone od 0 do x pamiętając że wartość wyświetlana będzie x - 1
# range(x,y) oznacza, że możemy podać zakres liczbowy od x do y z uwzględnieniem że wyświetlona wartośc y będzie y - 1
# range(x,y,z) z oznacza jak obliczać kolejną wartość. Standardowo wartośc rośnie +1 jesnak można to zmienić za pomocą parametru z np +2, jednak będzie się to działo
# o obrębie zbioru x,y
# range może być także malejący
#for i in range(10):
#for i in range(1,11):
#for i in range(1, 11, 2):
for i in range(10, 0, -1):
    print(i)

# zmienna przyjmuje typ range od range(x)
# list = range(10)

# konwersja range na liste, lista przyjmuje wartości range
list = list(range(10))
print("List: ",list, type(list),id(list))
# przypominając listy w tym zapisie wskazują to samo miejsce w pamięci, a żeby zrobić skuteczną kopie listy należy użyć funkcji copy()
list2 = list
list3 = list.copy()
print("List: ",list2, type(list2),id(list2))
print("List: ",list3, type(list3),id(list3))
# sztuczki w przypadku pracy z listami, w postaci wyciagania z nich elementow w okreslonej kolejnosci - slice

# wywołując liste w [x:y] w x traktuje za początek od kiedy ma zostać wyświetlona lista, za y traktuje gdzie ma skończyć wyswietlanie listy
# z uwzględnieniem że wyświetlana pozycja będzie y - 1.
# [:y] wyswietlenie wszystkiego od początku do y-1
# [x:] wyświetlenie wszystkiego od x do końca
# [:-1] wyświetlenie wszystkiego od początku do przedostatniego elementu listy ( ostatna pozycja zostanie niewidoczna ) wartość ujemna może się sięgać dowolnie głeboko
# [-1::-1] odwrócenie listy
print(list[5:7])
print(list[:7])
print(list[5:])
print(list[:-1])
print(list[5:-1])
print(list[-1::-1])




