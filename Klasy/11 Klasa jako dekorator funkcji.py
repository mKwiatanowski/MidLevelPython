
import random

# definiuje klase, która będzie na poziomie klasy będzie przechowywać zmienną z markami, które już zostały wylosowane
class MemoryClass:

    list_of_already_selected_items = []

    def __init__(self, funct):
        print('>>> This is init of MemoryClass <<<')
        self.funct = funct

    # funkcja która wylosuje auto z listy, a następnie doda wynik do listy list_of_already_selected_items

    def __call__(self, list):
        print('>>> This is call of MemoryClass instance')
        # budowanie listy, w której nie będzie już elementów wcześniej wybranych.
        '''
        * i for i in list - Oznacza, że dla każdego elementu i w liście list będzie generowany nowy element.
        * if i not in MemoryClass.list_of_already_selected_items - Jest warunkiem filtrującym. Tylko te elementy i,
        które nie znajdują się w liście MemoryClass.list_of_already_selected_items, zostaną uwzględnione w nowej liście.       
        '''
        items_not_selected = [i for i in list if i not in MemoryClass.list_of_already_selected_items]
        print('+-- selecting only from a list of ', items_not_selected)
        # item jest zmienna określoną w funct i tu przekaże już okrojoną listę
        item = self.funct(items_not_selected)
        # zapamiętanie na poziomie klasy wylosowanej marki i zapisanie tego na liście list_of_already_selected_items
        MemoryClass.list_of_already_selected_items.append(item)
        # na koniec informacja o zwróceniu wylosowanej marki
        return item



cars = ['Opel','Toyota', 'Fiat', 'Ford', 'Renault', 'Mercedes', 'BMW', 'Peugeot', 'Porshe', 'Audi', 'VW', 'Mazda']

# losowanie auta, które dziś będzie w promocji
@MemoryClass
def SelectTodayPromotion(list_of_cars):
    return random.choice(list_of_cars)

# losowanie auta które będą wystawione na show
@MemoryClass
def SelectTodayShow(list_of_cars):
    return random.choice(list_of_cars)

# losowanie auta które będa dodawane darmowe akcesoria
@MemoryClass
def SelectFreeAccessories(list_of_cars):
    return random.choice(list_of_cars)

# wywołując powyższą funkcję, tak naprawdę wywoływała się klasa z metodą __call__
print('Promotion:', SelectTodayPromotion(cars))
print('Show:', SelectTodayShow(cars))
print('Free accessoriesL', SelectFreeAccessories(cars))


# po wyniku widać, że powstały 3 instancje dla klasy, co można rozumieć, że klasa została użyta 3 razy dla każdej z funkcji osobno
