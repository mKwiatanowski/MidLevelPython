

class Car:


    def __init__(self, brand, model, isOnSale):
        print('>> Class car __init__ - starting <<')
        self.brand = brand
        self.model = model
        self.isOnSale = isOnSale
        self.name = '{} {}'.format(brand,model)
        print('>> Class car __init__ - finishing <<')


    def GetInfo(self):
        print('>> Class car GetInfo - starting <<')
        # Klasa Car ma tu instrukcję super() wywołującą również GetInfo() na rzecz obiektu zwróconego przez super więc ten zapis powoduje wywołanie metody GetInfo z klasy
        # Specialist. Dlatego też wywołując mamy informacje, że w tej chwili startuje GetInfo z klasy Specialist. Zostały wyświetlone informacje z GetInfo klasy Specialist
        # czyli imie i nazwisko.
        super().GetInfo()
        # teraz zakończyło się wywołanie GetInfo z klasy Specialist i wystartowała reszta instrukcji znajdującej się w GetInfo ale z klasy Car.
        print('{} {}'.format(self.brand, self.model))
        print('IS ON SALE           {}'.format(self.isOnSale))
        print('>> Class car GetInfo - finishing <<')


# tworzenie drugiej klasy, która będzie miała z pierwszą klasą wspólne parametry, które spowodują konflikt
class Specialist:

    def __init__(self, firstname, lastname, brand):
        print('>> Class Specialist __init__ - starting <<')
        self.firstname = firstname
        self.lastname = lastname
        self.name = '{} {}'.format(firstname,lastname)
        self.brand = brand
        print('>> Class Specialist __init__ - finishing <<')


    def GetInfo(self):
        print('>> Class Specialist GetInfo - starting <<')
        print('{} {} - ({})'.format(self.firstname, self.lastname, self.brand))
        print('>> Class Specialist GetInfo - finishing <<')



# tworzę nową klasę, w której jako parametr będzą przekazywane klasy rodzicielskie. Klasa ta będzie łączyć w sobie będzie informacje z klasy 1 i 2
class CarSpecialist(Car, Specialist):
    def __init__(self, brand, model, isOnSale, firstname, lastname):
        print('>> Class CarSpecialist __init__ - starting <<')
        # niestosuje tutaj super() ponieważ odwołał bym się do pierwszej z lewej czyli do klasy Car, a nie także do Specialist. Dlatego też wywołuje odwołanie
        # do klasy rodzicielskiej do init dla klasy Car i Specialist
        Car.__init__(self, brand, model, isOnSale)
        # aby pokazać który brand został użyty w jednym przypadku sformatuje jego wygląd do dużych liter
        Specialist.__init__(self, firstname, lastname, brand.upper())
        print('>> Class CarSpecialist __init__ - finishing <<')


    def GetInfo(self):
        print('>> Class CarSpecialist GetInfo - starting <<')
        # teraz nie określam, żadnej konkretnej kolejności w jakiem jaką się wywoływać GetInfo w klasach rodzicielskich. Czyli za pomocą super mówie, wyświetl to co ma być
        # wyświetlone przez rodzica.
        super().GetInfo()
        print('>> Class CarSpecialist GetInfo - finishing <<')

tom = CarSpecialist('Toyota', 'Corolla', True, 'Tom', 'Smith')
# widać, że ta druga metoda z klasy Specialist nadpisała zmienną brand z pierwszej metody, ponieważ zapis jest dużymi literami
# zarówno w klasie Car jak i Specialist była utworzona zmienna name. W 1 klasie jest to złączona nazwa marki i modelu natomiast w 2 jest to połaczenie imienia i nazwiska
# Jako, że metoda init z klasy Specialist była wywołana jako druga to nadpisała wywołanie tego z klasy Car. Dlatego nie mamy zapisanej nazwy marka i model, a imie i nazwisko
print(vars(tom))

# w jaki sposób jest ustalana kolejnośc wywoływania rodzica. CarSpecialist(Car, Specialist) jeśli jest zdefiniowane więcej jak 1 to w pierwszej kolejności idziemy od lewej
# i następnie do prawej.
print('-' * 30, '\n')
tom.GetInfo()



# Method Resolution Order
# można sprawdzić dzięki __mro_ kolejność wywoływania poszczególnych metod
print(CarSpecialist.__mro__)





