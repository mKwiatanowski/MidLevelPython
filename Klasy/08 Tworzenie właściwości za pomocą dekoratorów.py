
brandOnSale = 'Opel'


class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMachanicOk, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMachanicOk = isMachanicOk
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)


    def IsDamaged(self):
        return not (self.isAirBagOk and self.isPaintingOk and self.isMachanicOk)

    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -      {}'.format(self.isAirBagOk))
        print('Painting - ok -      {}'.format(self.isPaintingOk))
        print('Machanic - ok -      {}'.format(self.isMachanicOk))
        print('IS ON SALE           {}'.format(self.__isOnSale))
        print('-'*30)




    @property
    def IsOnSale(self):
        return self.__isOnSale


    @IsOnSale.setter
    # nazwa musi być  teraz taka sama jak przy property
    def IsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Chaning status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))

        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))


    # zeby mieć możliwość usunięcia trzeba stworzyć dekorator z .deleter i obsłużyć możliwość wyzerowania danych. Wówczas zabieg kasowania się powiedzie
    # w przeciwnym wypadku takiej możliwości nie ma
    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None


    # właściwość, która zapisze nazwę samochodu w ładniejszy sposób, że pierwsza litera słowa będzie z dużej litery
    @property
    def CarTitle(self):
        return "Brank: {}, Model: {}".format(self.brand, self.model).title()







car_01 = Car('Seat', 'Ibiza', True, True, True, False)

print(car_01.IsOnSale)
car_01.IsOnSale = True
# teraz pokazałą się ciekawa właściwość nie można usunąć takiego atrybutu, ponieważ brakuje metody która by się nazywała deleter
del car_01.IsOnSale
print(car_01.IsOnSale)


print(car_01.CarTitle)

