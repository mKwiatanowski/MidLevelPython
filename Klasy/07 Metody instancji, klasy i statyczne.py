


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

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Chaning status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))

        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'If set to true, the car is available in sale/promo')

    # metoda, która ma działać na poziomie klasy musi być oznaczona dekoratorem classmethod
    # metoda klasy w żaden sposób nie dotykała istniejącej instancji. Ta metoda utworzyła w sobie utworzyła zupełnie nową instancje i ją zwróciła. Ale nie wykorzystała
    # do tego żadnej metod, które miały w sobie self
    @classmethod
    # cls to skrót od class
    def ReadFromText(cls,aText):
        # aText.split(':') spowoduje utworzenie listy, a : posłuzy za podzielnik. Jednak ja nie chce utworzyć listy i do tego potrzebna jest * i dzieki temu
        # będzie mozna przekazac oddzielne wartości
        aNewCar = cls(*aText.split(':'))
        return aNewCar


    # @staticmethod metoda statyczna jest ciekawsza jak metoda klasy bo nie musi mieć żadnego związku z klasą. Generalnie mogła by byc utworzona gdziekolwiek ale z punktu widzenia
    # logicznego powiązania funkcjonalności wykonywanej przez funkcje wstawiamy ją wówczas w określonej klasie
    # przykładowo metoda przeliczająca  konie mechaniczne na klikovaty
    @staticmethod
    def Convert_KM_KW(KM):
        return KM * 0.735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW * 1.36


lineOfText = 'Renault:Megane:True:True:False:False'

# dzięki rozdzieleniu wartości przez : i użyciu * przekaże do zmiennej car_03 osobne obiekty z nazwy lineOfText
car_03 = Car.ReadFromText(lineOfText)
car_03.GetInfo()


print('converting 120 KM to KW', Car.Convert_KM_KW(120))
print('converting 90 KW to KM', Car.Convert_KW_KM(90))

# pokazanie dlaczego nie można wywołac metody instancji na rzecz klasy. Metoda GetInfo() oczekuje dla 1 argumentu self. Niestety ten parametr nie został podstawiony
# bo próbowałem wywołać tą metodę na rzecz klasy, a na poziomie klasy nie ma jeszcze obiektu self, dlatego też pojawił się błąd.
# print(Car.GetInfo())



# warto też wiedzieć, że zarówno metody klasy jak i metody statyczne można wywoływać na rzecz instancji. Instancje mają dostęp do klasy dlatego też to nie
# spododowało błedu
print(car_03.ReadFromText(lineOfText))
# tak samo jak na rzecz klasy wywołam metodę statyczną, metoda ta w żaden sposób nie musi dotykać tej instancji to jednak instancja ma dostęp do każdej
# metody statycznej zdefiniowanej w klasie
print(car_03.Convert_KW_KM(50))

























