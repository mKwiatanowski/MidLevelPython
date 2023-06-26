

class Car:
    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMachanicOk):        # self.dany argument = chodzi o właściwość w tym momencie instancji, a po prawej stronie nie poprzedzony self oznacza podany argument
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMachanicOk = isMachanicOk

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


car_01 = Car('Seat','Ibiza', True, True, True)
car_02 = Car('Opel','Corsa', True, False, True)


car_01.GetInfo()
car_02.GetInfo()


# wywołując funkcje z wnętrza klasy nie podaje się do niej zmiennej, python automatycznie przypisuje zmienna self
print(car_01.brand, car_01.model,car_01.IsDamaged())
print(car_02.brand, car_02.model,car_02.IsDamaged())

print(car_01.brand, car_01.model, car_01.isAirBagOk, car_01.isPaintingOk,car_01.isMachanicOk)
print(car_02.brand, car_02.model, car_02.isAirBagOk, car_02.isPaintingOk,car_02.isMachanicOk)



