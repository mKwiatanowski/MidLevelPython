
# największym minusem klas w pythonie jest to, że nie chronią one w odpowiedni sposób swoich danych


class Car:

    # pozwala to przechowywać pewnych informacji nie na poziomie instancji ale na poziomie samej klasy
    numberOfCars = 0
    listOfCars = []

    # w klasie funkcje nazywamy metodami
    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMachanicOk):        # self.dany argument = chodzi o właściwość w tym momencie instancji, a po prawej stronie nie poprzedzony self oznacza podany argument
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMachanicOk = isMachanicOk
        # zwiększanie ilości liczącej ilośc danych
        Car.numberOfCars += 1
        # zapisywanie do listy wartości
        Car.listOfCars.append(self)


    def IsDamaged(self):
        # żeby odwołać się do atrybutów klasy nalezy poprzedzić to self.
        return not (self.isAirBagOk and self.isPaintingOk and self.isMachanicOk)

    def GetInfo(self):
        # upper() formatowanie do wielkich liter
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -      {}'.format(self.isAirBagOk))
        print('Painting - ok -      {}'.format(self.isPaintingOk))
        print('Machanic - ok -      {}'.format(self.isMachanicOk))
        print('-'*30)
# sprawdzenie listy obiektów przed utworzeniem instancji
print('Class level variables BEFORE creating instances:', Car.numberOfCars,Car.listOfCars)

car_01 = Car('Seat','Ibiza', True, True, True)
car_02 = Car('Opel','Corsa', True, False, True)

print('Class level variables AFTER creating instances:', Car.numberOfCars,Car.listOfCars)

print('Id of class is: ', id(Car))
print('Id of instatnces are: ', id(car_01), id(car_02))

# isinstance(instancja, klasa) sprawdzenie czy dana instancja pochodzi czy też należy do danej klasy zwraca true lub false
print('Check if object belongs to class: ', isinstance(car_01,Car))
# następny sposób na sprawdzenie czy obiekt należy do klasy true lub false
print('Chect if object belongs to class using type:', type(car_01) is Car)
# następny sposób na sprawdzenie czy instancja należy do klasy zwraca do jakiej klasy należy
print('Check class of an object using __class_-:', car_01.__class__)
# funkcja vars() pozwala na zobaczenie obiektu (instancji) od środka, wyświetlone zostana informacje o poszczególnych atrybutach tego obiektu w formie słownika

print('List of instance attributes with values:', vars(car_01))
# używając vars do klasy zostaną zwrócone informacje o tej klasie ale nie o instancjach tej klasy
print('List of instance attributes with values:', vars(Car))

# funkcja dir odkrywa ona wewnętrznie jeszcze inne metody, które są przed nami schowane
print('List of instance attributes with values:', dir(car_01))
# to samo co wyżej tylko dla klasy
print('List of instance attributes with values:', dir(Car))

# na sztywno można przekazać do klasy wartość zmiennej w klasie
Car.numberOfCars = 123


'''

car_01.GetInfo()
car_02.GetInfo()


print(car_01.brand, car_01.model,car_01.IsDamaged())
print(car_02.brand, car_02.model,car_02.IsDamaged())

print(car_01.brand, car_01.model, car_01.isAirBagOk, car_01.isPaintingOk,car_01.isMachanicOk)
print(car_02.brand, car_02.model, car_02.isAirBagOk, car_02.isPaintingOk,car_02.isMachanicOk)
'''


