
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

    # funkcja udostępnia ukryty atrybut __isonsale
    def __GetIsOnSale(self):
        return self.__isOnSale

    # zmiana wartości atrybutu który został ukryty
    def __SetIsOnSale(self, newIsOnSaleStatus):
        # jeżeli marka jest równa marce ze zmiennej do promocji, to się wykona operacja zmiany statusu na podany w zmiennej wywoływanej z metody
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Chaning status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))

        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    # dzięki zmiennej o funkcji property() można zmieniać ukrytą zmienną w głównym kodzie,w prosty sposób za pomocą przypisania do zmiennej nowej wartości
    # (funkcja pobierajaca, funkcja zmieniająca, funkcja usuwająca, komunikat)
    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'If set to true, the car is available in sale/promo')



car_01 = Car('Seat','Ibiza', True, True, True, False)
car_02 = Car('Opel','Corsa', True, False, True, True)

# zeby zmienić ukrytą właściwość. Mały problem dotyczy tylko notacji, żeby zmienić wartośc jednego atrybutu trzeba wywołać metodę i to metodę z przekazaniem parametru
# troche nieładnie to wygląda i źle się pisze.

# tak nie robimy
print('Status of cars:', car_01._Car__GetIsOnSale(), car_02._Car__GetIsOnSale())

'''car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print('Status of cars:', car_01.GetIsOnSale(), car_02.GetIsOnSale())'''

# wywołując property wskazuję nazwę zmiennej jaka została użyta w klasie i po = przypisunje nową wartość
car_01.IsOnSale = True
car_02.IsOnSale = True
print('Status of cars:', car_01.IsOnSale, car_02.IsOnSale)














'''
car_02.__isOnSale = False

car_02._Car__isOnSale = False

car_02.YearOfProduction = 2005
del car_02.YearOfProduction

setattr(car_02,'TAXI',False)
delattr(car_02,'TAXI')
print(hasattr(car_02,'TAXI'))
'''



car_02.GetInfo()
# teraz sprawdzając za pomoca vars mamy wynik '_Car__isOnSale': True, '__isOnSale': False} pokazały się 2 nowe atrybuty, pierwszy atrybut
# który był ukrywany w klasie na zewnątrz tej klasy nie jest dostępny już pod tą samą nazwą, a nazwa sięzmieniła w ten sposób że z przodu doklejona jest nazwa klasy
# próbując oszukać jak wyżej, do klasy została dodana zupełnie nowa właściwość
print(vars(car_02))










