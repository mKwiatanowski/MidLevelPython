

import math

argument_list = []

# pętla która do puste listy doda 100 kolejnych pozycji, każda większa od poprzedniej o 0,1
for i in range(100):
    argument_list.append(i/10)

# użytkownik wprowadza wzór do obliczeń
formula = input("Please enter a formula, use 'x' as the argument: ")

# iteruje po liście z poprzedniej pętli
for x in argument_list:
    # ładuje wynik do słownika, gdzie pierwszy argument to x z listy argument_list a drugi to eval(wzór wprowadzony przez użytkownika)
    print("{0:3.1f} {1:6.2f}".format(x, eval(formula)))



