

import os
# r przed '' oznacza ze napis w '' trzeba potraktować surowo jeśli by tego r nie było to trzeba pamiętać, ze w scieżce trzeba użyć podwójny znak \\
path = r'c:\temp\mydata.txt'

# usunięcie pliku
os.remove(path)

# os.path.isfile() sprawdzenie czy wskazana sciezka prowadzi do istniejącego pliku
if os.path.isfile(path):
    print("File %s exists" % path)
else:
    print("Creating a file %s" % path)
    # open() otwiera / tworzenie nowego pliku 'x' oznacza, jeśli taki plik istnieje to ma być zwrócony błąd
    # close zamkniecie pliku
    open(path, 'x').close()
    print("File %s created" % path)


# warunek locziny w zmiennej. Najpierw sprawdzamy czy plik istnieje, python oszacował wartość 1 składnika na false.
# Następnie or (lub) jest sprawdzana druga częśc wyrażenia logicznego, wywołał polecenie open które otworzyła plik i zamknęło
# python widząc takie wyrazenie uważa to za alternatywe, więc jeśli 1 wartośc będzie true to drugiej strony już sprawdzać nie będzie

# jeśli mamy sytacje, że chcemy sprawdzić czy plik istnieje, a jeśli istnieje to go utworzyć, to zamiast pisać kilka linijek if else
# można zapisać wyrażenie logiczne jak niżej, którego działanie będzie takie samo.
result = os.path.isfile(path) or open(path,'x').close()
print(result)


# gdy użyjemy w takim wyrażeniu and to nie jest już alternatywa tylko koniunkcja, a koniunkcja jest prawdziwa wtedy gdy wszystkie jej składniki są prawdziwe
# gdy 1 część jest false to nie python nie bedzie sprawdzał drugiej części ponieważ gdy już jedna wartość jest false to nie ma sensu sprawdzać dalej
# ponieważ i tak nie zmieni to wyniku na true
'''
result = os.path.isfile(path) and open(path,'x').close()
print(result)
'''

'''
Podsumowując, jeśli mamy wyrażenie alternatywy or to jeśli 1 część jest true to python nie będzie sprawdzał 2 części, po prostu ją zignoruje.
Gdy 1 cześć będzie jednak o wartości false to wówczas dopiero python sprawdzi drugą część tego wyrażenia i je wykona. 
'''








