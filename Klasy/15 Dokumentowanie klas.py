
# dobra praktyki do prowadzenia dokumentacji

brandOnSale = 'Opel'

class Car:
    '''
    Car - class operating on cars available in the dealer
    '''


    def __init__(self, brand, model, isAirBagOk, isPaintingOk, isMachanicOk, isOnSale):
        # opis parametry za co odpowiadają
        '''
        init: arguments accapted
        :param brand: the brand of the car is Fiat
        :param model: the modle of the car is Multipla
        :param isAirBagOk: is the AirBag nod used
        :param isPaintingOk: is the car paint original/no corrections
        :param isMachanicOk: is the car free of any mechanics failure
        :param isOnSale: is the car covered by extra promotion (some additional conditions apply)
        '''

        self.brand = brand
        self.model = model
        self.isAirBagOk = isAirBagOk
        self.isPaintingOk = isPaintingOk
        self.isMachanicOk = isMachanicOk
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)



    @property
    def IsOnSale(self):
        '''
        IsOnSale - the car is on extra promotion that is limited in time (only selected cars may by "on sale"
        '''
        return self.__isOnSale


    @IsOnSale.setter
    def IsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Chaning status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))

        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))



# dzięki funkcj help można wyciągnąć informacje jakie zostały zawarte przez programiste w danym obiekcie
help(Car)
help(Car.IsOnSale)

# zaznaczając Car() i kombinacja ctrl + q można uzyskać dymek z informacjami o danym obiekcie
new_car = Car()
