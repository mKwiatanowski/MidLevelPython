
class Car:


    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMachanicOk, accessories):
        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMachanicOk = isMachanicOk
        self.accessories = accessories


    def GetInfo(self):
        print('{} {}'.format(self.brand, self.model).upper())
        print('Air Bag  - ok -      {}'.format(self.isAirBagOk))
        print('Painting - ok -      {}'.format(self.isPaintingOk))
        print('Machanic - ok -      {}'.format(self.isMachanicOk))
        print('Accessories          {}'.format(self.accessories))
        print('-'*30)

    # operator __iadd__ odpowiada za znak += to znaczy, że jeżeli wezmę obiekt i dodam do niego jakieś nowe akcesoria to wynikiem będzie zupełnie nowy samochód
    # który będzie wyposażony w to wszystko co było do tej pory oryginalny samochód plus dodatkowo coś jeszcze
    # ten oryginalny samochód przekazywany jest przez mienna self a to coś jeszcze przez other
    def __iadd__(self, other):

        # zmodyfikowana metoda aby pojeduńczy napis nie był traktowany jako lista dodaje if elif
        if type(other) is list:
            # do zmiennej przypisuje dokładnie to co w tej chwoli dany samochód posiada
            accessories = self.accessories
            # extand() następnie poszerzam tą listę o nowe akcesoria
            # extand() służy do poszerzenie listy
            accessories.extend(other)
            # ponieważ mam zwrócić zupełnie nowy samochód plus dodatkowe akcesoria, tworzę nowy samochód Car do którego przekazuje parametry
            return Car(self.brand, self.model, self.isAirBagOk, self.isPaintingOk, self.isMachanicOk, self.accessories)


        elif type(other) is str:
            accessories = self.accessories
            accessories.append(other)
            return Car(self.brand, self.model, self.isAirBagOk, self.isPaintingOk, self.isMachanicOk, self.accessories)

        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))

    # __add__ (self, other) argument self to w tej chwili istniejący samochód do którego chcemy dodać coś innego i najlepiej jeśli to drugie też jest samochodem
    def __add__(self, other):
        # sprawdzenie czy typ tego drugiego obiektu to Car
        if type(other) is Car:
            # jeśli tak zwracam listę, aktualny samochód, i ten drugi samochód
            return [self,other]
        else:
            # return Exception oznacza zwrócenie wyjątku jeśli prawidłowe założenie nie zostanie zrealizowane
            return Exception('Adding type {} to Car is not implemented'.format(type(other)))


    # Tworzenie tekstowej prezentacji dla obiektu
    def __str__(self):
        return 'Brand: {}, Model: {}'.format(self.brand, self.model)


car_01 = Car('Seat','Ibiza', True, True, True, ['winter tires'])
car_01.GetInfo()

car_01 += ['navigation system', 'roof rack']
car_01.GetInfo()

# próbując dodać jeden element nie oznaczony jako lista [] wówczas zostanie to potraktowane jako lista literek i każda literka zostanie osobna zinterpretowana
# teraz po dodaniu w klasie operatora __iadd__ i zmodyfikowaniu jej akcesoria tekstowe dodają się prawidłowo w liscie, dzięki temu, że gdy mamy tekst to używamy polecenia append
car_01 += 'loudspeeker system'
car_01.GetInfo()


car_02 = Car('Opel','Corsa', True, False, True, [])

# próba dodania do siebie 2 samochodów
car_pack = car_01 + car_02
print('car_01 + car_02 = ', car_pack[0].brand, car_pack[1].brand)
print(car_pack)

# wywołanie skonwertowanego obiektu do napisu za pomocą __str__
print(car_01)


