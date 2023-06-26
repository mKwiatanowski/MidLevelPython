
# poduł pozwala importować dane do pliku csv
import csv
import types

# funkcja exportująca do pliku csv ma 3 parametry, path- scieżkę dostępu, header-lista nagłówków znajdujących sie w pliku csv, data-lista wartości które mają
# mają być umieszczone w tym pliku
def exportToFile_Static(path, header, data):
    # otwarcie pliku do zapisu "w"
    with open(path, "w") as file:
        # tworzymy obiekt writer, ten obiekt deklaruje jak pracować z plikiem csv. Po 1 jest skojarzony z plikiem, który własnie otworzyłem, następnie wskazuje
        # że poszczególne wartości będa oddzielone przecinkiem za to odpowiada parametr delimiter, jeżeli by były jakieś dane, które zawierają w sobie przecinek to wtedy dodatkowo mają być
        # zamknięte w cudzysłowiu " za to odpowiada parametr quotechar, quoting określa jak mocno mają być cytowane wszystkie wartości
        # QUOTE_MINIMAL - oznacza, że umeiścimy w " tylko te wartości, które gdzieś w środku zawierały przecinek, natomiast te wartości, które nie zawierały przecinka
        # będziemy umieszczać bez cudzysłowia
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # mając taki obiekt, zapisujemy do niego tylko 2 linijki danych, najpierw z parametrem header czyli nazwy kolumn, następnie data czyli co ma się znaleźć w
        # danych zapisywanych do tego pliku
        writer.writerow(header)
        writer.writerow(data)
    # za pomocą tego sprawdzam czy metoda jest wywoływana
    print('>>> This is function exportToFile - static method')



# zmodyfikowana funkcja dzięki, której będzie można zrzucić hurtowa dane do pliku csv
# funkcja ta tworzona jest na poziomie klasy dzięki cls, nie jest już ona funkcją statyczna
def exportToFile_Class(cls, path):
    with open(path, "w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # pierwsza zmiana to tu są wbudowane wartości jakie mają być zwrócone jako nagłówek
        writer.writerow(['brand','model','IsOnSale'])

        # następnie ze zmiennej zdefiniowanej na poziomie klasy, zostaną pobrane wszystkie instancje które w tej chwili istnieją i dla każdej z instancji
        # do pliku csv zostanie wysłany osobny wiersz
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    print('>>> This is function exportToFile - class method')


def exportToFile_Instance(self, path):
    with open(path, "w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand','model','IsOnSale'])
        writer.writerow([self.brand, self.model, self.IsOnSale])
    print('>>> This is function exportToFile - instance method')


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



car_01 = Car('Seat','Ibiza', True, True, True, False)
car_02 = Car('Opel','Corsa', True, False, True, True)



print('-'*10, 'STATIC', '-'*10)

# aby przekazać funkcję do klasy to po 1, podać nazwę klasy Car po . wprowadzić nazwę nowo utworzonej funkcji pod jaką ta funkcja powinna być widonczna w klasie
# następnie przypisuje do wartości nazwę zdefiniowanej zewnętrznej funkcji
Car.ExportToFile_Static = exportToFile_Static
#exportToFile_Static(r'c:\temp\export_static.csv', ['Brand','Model','IsOnSale'],[car_01.brand, car_01.model, car_01.IsOnSale])

# zmiana sposobu wowyłania, po pierwsze trzeba poprzedzić nazwę funkcji nazwą klasy. Następnie przekaże wszystkie parametry.
Car.ExportToFile_Static(r'c:\temp\export_static.csv', ['Brand','Model','IsOnSale'],[car_01.brand, car_01.model, car_01.IsOnSale])
print(dir(Car))



print('-'*10, 'Class', '-'*10)
# komentuje poinże bo się nie sprawdziło
# Car.ExportToFile_Class = exportToFile_Class

# kiedy zewnętrzą funkcje chcesz przypisać jak funkcje klasy to należy zrobić to przy użyciu odpowiedniej metody znajdującej sie w module types
# funkcja types.MethodType(funkcja zewnętrzna, klasa) oczekuje 2 argumenty 1 to nazwa zewnętrznej funkcji, która ma być przybindowana do klasy a 2 to nazwa klasy
Car.ExportToFile_Class = types.MethodType(exportToFile_Class,Car)
Car.ExportToFile_Class(path = r'c:\temp\export_class.csv')
print(dir(Car))
()
print('-'*10, 'Instance', '-'*10)
# tak samo jak wyżej jest błąd brakuj jednego argumentu
#Car.ExportToFile_Instance = exportToFile_Instance()

# w tym wypadku jako że jest to instacja jako drugi argument będzie przypisanie co zmiennej z danymi a nie do klasy
# druga różnica, nie jest to już wywoływany z poziomu klasy Car. tylko z poziomu instancji car_01
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
car_01.ExportToFile_Instance(path = r'c:\temp\export_instance.csv')
print(dir(car_01))

print('-'*10, 'Ceck function', '-'*10)
# sprawdzanie czy istnieje funkcja
# hasattr(zmienna, atrybut) sprawdzenie czy istnieje atrybut ( sprawdza to czy taka nazwa jest rozpoznawalna w klasie ) jednak nie oznacza to ze coś takiego jest w klasie
# bo to niekoniecznie może być funkcja. Dlatego drugi test sprawdza czy tą nazwę da się uruchomić jako funkcje callable(zmienna.funkcja do sprawdzenia)
if hasattr(car_01, 'ExportToFile_Static') and callable(car_01.ExportToFile_Static):
    print('The object has method ExportToFile_Static')
if hasattr(car_01, 'ExportToFile_Class') and callable(car_01.ExportToFile_Class):
    print('The object has method ExportToFile_Class')
if hasattr(car_01, 'ExportToFile_Instance') and callable(car_01.ExportToFile_Instance):
    print('The object has method ExportToFile_Instance')
# sprawdzenie czegoś nieistniejącego
if hasattr(car_01, 'ExportToFile_InstanceXXX') and callable(car_01.ExportToFile_InstanceXXX):
    print('The object has method ExportToFile_Instance')
else:
    print('no such mathod!!')
# jako że IsOnSale nie można wywołać to zwróciło else
if hasattr(car_01, 'IsOnSale') and callable(car_01.IsOnSale):
    print('The object has method ExportToFile_Instance')
else:
    print('no such mathod!!')