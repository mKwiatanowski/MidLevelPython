'''
Piszesz program, który będzie obsługiwał wpłatomat. To będzie super nowoczesny wpłatomat,
do którego można też wpłacać monety. Ilekroć ktoś wpłaca pieniądze należy policzyć ile
banknotów lub monet danego nominału znajduje się w kasie.
'''

banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]

dict_denominations = {}

# pętla do słownika dict_deniminations przypisuje dla każdego klucza z listy banknotes_coins wartość 0
for d in banknotes_coins:
    dict_denominations[d] = 0

# mamy słownik gdzie wywołany [klucz] zmienia wartość += o x
dict_denominations[100] += 1
dict_denominations[20] += 1
dict_denominations[5] += 1
dict_denominations[0.5] += 1

dict_denominations[50] += 1
dict_denominations[20] += 2
dict_denominations[5] += 1
dict_denominations[2] += 2

dict_denominations[100] += 1
dict_denominations[50] += 1
dict_denominations[2] += 1

# pętla iteruje przes posortowany słownik po kluczu
for k in sorted(dict_denominations.keys()):
    # Wywołanie słownika, gdzie pokolei jest iterowany klucz i dla tego klucza jest pobierany wynik z powyższego dodawania ilosci wystapien dla poszczególnego klucza
    print("Denominate: {0:6.2f} - amount {1:5}".format(k, dict_denominations[k]))

