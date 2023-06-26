
class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMachanicOk, isOnSale):        # self.dany argument = chodzi o właściwość w tym momencie instancji, a po prawej stronie nie poprzedzony self oznacza podany argument
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMachanicOk = isMachanicOk
        # sztuczka pozwala zasymulować ukrywania pewnych właściwości wystarczy po self.__nazwa dać dwa znaki __ przed nazwą
        # __ oznacza definiowanie czegoś co jest wewnętrzne, schowane, systemowe
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
        # w funkcji też trzeba dokonwać modyfikacji i dodać __
        print('IS ON SALE           {}'.format(self.__isOnSale))
        print('-'*30)
print('Class level variables BEFORE creating instances:', Car.numberOfCars,Car.listOfCars)

car_01 = Car('Seat','Ibiza', True, True, True, False)
car_02 = Car('Opel','Corsa', True, False, True, True)

# minusem pythona jest to, że można zmienić wartość w klasie
# teraz po dokonaniu ukrycia w klasie za pomocą __ próbując wywołać tą zmienna nie znajdize się na liście dostępnych zmiennych
# próbując nawet na sztywno wpisać zmienna z dodanym __ spowodowało, że wywołanie funkcji getinfo nie zmieniło wartości na false
car_02.__isOnSale = False

# jednak jak ktoś będzie upary i zmieni na zapis to wówczas wynik w klasie już ulegnie zmianie na false
car_02._Car__isOnSale = False

# jeśli bym chciał dodać do jakiegoś samochodu właściwość jakiej nie posiadają inne auta i pojawił się jeszcze jeden atrybut w klasie
car_02.YearOfProduction = 2005
# del aby usunąć taki dodany atrybut
del car_02.YearOfProduction
# w innych językach raz definiowana klasa jest święta w pythonie klase można modyfikować na bieżąco, są dedykowane metody które pozwalają w locie modyfikować atrybuty klasy

# setattr(obiekt do modyfikacji, 'Nazwa nowo utworzonego atrybutu', wartość tego atrybutu) dodanie nowej właściwości
setattr(car_02,'TAXI',False)
# inny sposób na usunięcie atrybutu
delattr(car_02,'TAXI')
# hasattr(obiekt,'jego nazwa') sprawdzenie czy obiekt posiada atrybut o wskazanej nazwie
print(hasattr(car_02,'TAXI'))




car_02.GetInfo()
# teraz sprawdzając za pomoca vars mamy wynik '_Car__isOnSale': True, '__isOnSale': False} pokazały się 2 nowe atrybuty, pierwszy atrybut
# który był ukrywany w klasie na zewnątrz tej klasy nie jest dostępny już pod tą samą nazwą, a nazwa sięzmieniła w ten sposób że z przodu doklejona jest nazwa klasy
# próbując oszukać jak wyżej, do klasy została dodana zupełnie nowa właściwość
print(vars(car_02))







