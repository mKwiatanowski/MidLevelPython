

import datetime
import functools

# zmienna przekazująca ściezkę do pliku nie jest już potrzebna dlatego że będzie ona przekazywana do funkcji za pomocą wrappera
# logFilePath = r'c:\temp\function_log.txt'


# druga różnica jest taka, że funkcja tworząca wrappera nie będzie już samoistną funkcją ale stanie się funkcją zdefiniowaną we wnętrzu innej funkcji
'''def CreateFunctionWithWrapper(func):
    def func_with_wrapper(*args, **kwargs):
        # otwarcie pliku z typem 'a' czyli jeśli plik istenie to należy do niego dpisać dane
        file = open(logFilePath,'a')
        file.write('-'* 20 + '\n')
        # zamiana print na file.write( to co było w print )
        file.write('Function "{}" staret at {}\n'.format(func.__name__,datetime.datetime.now().isoformat()))
        file.write('Following arguments were used: \n')
        # w szczególny sposób zostały potraktowane paramektry, które zapisujemy do pliku parametr jest listą a parametr file.write oczekuje przekazania napisu
        # dlatego dla napisu będącego " " spacja wywołuje metodę join która ma połączyć wartości które są argumentem funkcji join. Tu dzieje się małe czary mary
        # w "" a wnim {}. format od (x) powstanie napis którego treśią będzie 'x' napis ten pwstanie niezależnie od tego jakiego typu jest x ( jeśli jest liczba zostanie
        # zamieniony na tekst ) a x jest kolejnymi wartościami w zmiennej args
        file.write(" ".join("{}".format(x) for x in args))
        file.write('\n')
        # tu ta sama sztuczka co wyżej. join będzie łączyć ze sobą wszystkie argumenty spacją i będą one zapisane w formie napis = napis {} = {}. W miejsce nawiasów klamrowych
        # zostaną włożone wartości k i v key i value k i v to kolejne wartości znajdujące się w tablicy kwargs.items()
        file.write(" ".join("{}={}".format(k,v) for (k,v) in kwargs.items()))
        file.write('\n')
        # wywołanie oryginalnej funkcji, która jest obudowywana wrapperem i następnie zapisuje go do pliku
        result = func(*args, **kwargs)
        file.write('Function returned {}\n'.format(result))
        # zamknięcie pliku
        file.close()
        return result

    return func_with_wrapper'''

# tutaj nic się nie zmieniło

# pierwsza funkcja przyjmuje jako parametr ścieżkę dostępu do pliku,
def CreateFunctionWithWrapper_LogToFile(logFilePath):
    # zadaniem tej funkcji jest utworzenie wrappera, która będzie pisałą do właściwego pliku
    def CreateFunctionWithWrapper(func):
        # wewnątrz funkcji CreateFunctionWithWrapper dzieje się następująca rzecz:
        # zdefiniowaliśmy funkcje, która może przyjąć jakiekolwiek parametry, następnie zalogowaliśmy uruchomienie funkcji w pliku i zapisaliśmy tam te informacje
        # na końcu wywołaliśmy oryginalną funkcję "result" przekazując do niej właściwe parametry, finalnie zamkniemy plik i zwrócimy wynik
        def func_with_wrapper(*args, **kwargs):
            file = open(logFilePath, 'a')
            file.write('-' * 20 + '\n')
            file.write('Function "{}" staret at {}\n'.format(func.__name__, datetime.datetime.now().isoformat()))
            file.write('Following arguments were used: \n')
            file.write(" ".join("{}".format(x) for x in args))
            file.write('\n')
            file.write(" ".join("{}={}".format(k, v) for (k, v) in kwargs.items()))
            file.write('\n')
            result = func(*args, **kwargs)
            file.write('Function returned {}\n'.format(result))
            file.close()
            return result
        return func_with_wrapper
    # dlatego na końcu znajduje się wywołanie CreateFunctionWithWrapper
    return CreateFunctionWithWrapper





    print('CHANGING SALARY FOR {} TO {} AS BONUS = {}'.format(emp_name,new_salary,is_bonus))
    return new_salary

@CreateFunctionWithWrapper_LogToFile(r'c:\temp\change_salary_log.txt')
def ChangerSalary(emp_name, new_salary, is_bonus = False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS = {}'.format(emp_name,new_salary,is_bonus))
    return new_salary

@CreateFunctionWithWrapper_LogToFile(r'c:\temp\change_position_log.txt')
def ChangePosition(emp_name, new_salary, is_bonus = False):
    print('CHANGING SALARY FOR {} TO {} AS BONUS = {}'.format(emp_name,new_salary,is_bonus))
    return new_salary



print(ChangerSalary('Johnson', 20000, True))
#ChangeSalary = CreateFunctionWithWrapper(ChangerSalary)
print(ChangerSalary('Johnson', 20000, is_bonus = True))

print(ChangePosition('Michael','Salasman'))
print(ChangePosition('Anke','Manager'))

