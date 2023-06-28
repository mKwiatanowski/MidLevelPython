
brandOnSale = 'Opel'

# za nazwą klasy w ()  można się odwołać do klasy rodzicielskiej object, jeśli nic tam wcześniej nie było to jest nią generyczna klasa object
class Car(object):

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

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Chaning status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))

        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'If set to true, the car is available in sale/promo')


# tworzenie klasy dla cieżarówki, z dziedziczeniem od klasy car
class Truck(Car):

    # tworzenie __init__ ze zmiennymi od car oraz z dodatkową zmienną
    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale, capacityKg):
        # zapamiętanie wartości przekazanych przez init dzięki dziedziczeniu można zasotsować uproszczenie dzięki funkcji super()
        # która odwołuje się do klasy rodzicielskiej czyli do klasy Car, trzeba przekazać wszystkie parametry jakie się znajdują w niej.
        super().__init__(brand,model,isAirBagOk,isPaintingOk,isMechanicOk,isOnSale)

        # jest to inny sposób wywołania w () przekazuje nazwę klasy dla której należy poszukać rodzica a potem przekazać instancje tej klasy
        # przekazywanie tych parametrów nie jest wymagane,ponieważ kiedy wywołuje super to domyślnie zostanie podstawiona domyślna nazwa klasy na której pracuje a za instancje self
        #super(Truck, self).__init__(brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale)

        # dostęp do rodzicielskich metod można również uzyskać w następujący sposób Klasa.__init_(instancje klasy), ten sposób będzie przydatny np wtedy gdy moja klasa
        # odziedziczy z kilku innych klas
        #Car.__init__(self, brand, model, isAirBagOk, isPaintingOk, isMechanicOk, isOnSale)
        self.capacityKg = capacityKg

    # utworzenie nowej metody GetInfo, która ma za zadanie wyświetlić informacje o capacity
    def GetInfo(self):
        # aby były widoczne jeszcze informacje zawarte w GetInfo z klasy car dodaje init w klasie Truck odwołujący się do GetInfo z klasy Car
        super().GetInfo()
        print('CapacityKG           {}'.format(self.capacityKg))



truck_01 = Truck('Ford','Transit',True,False,True,False,1600)
truck_02 = Truck('Reanult','Traffic',True,True,True,True,1200)

print('Calling properties:')
print(truck_01.brand, truck_02.capacityKg, truck_01.IsOnSale, truck_02.brand, truck_02.capacityKg, truck_02.IsOnSale)

# wywołanie metody GetInfo dla klasy Truck z klasy Car. Jest tu jednak pewna wada, do klasy Truck dodane zostało capacity jednak w klasie Car i metodzie GetInfo nie jest to zdefiniowane
# co za tym idzie tak wywołując tego nie zobaczymy
# po modyfikacje w klasie Truck i dodaniu do niej GetInfo, teraz wyświetlają się informacje tylko zawarte w drugiej metodzie czyli capacity
truck_01.GetInfo()
truck_02.GetInfo()




car_01 = Car('Seat','Ibiza', True, True, True, False)
car_02 = Car('Opel','Corsa', True, False, True, True)
