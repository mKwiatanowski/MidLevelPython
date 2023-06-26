
class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling


    def show(self):
        print('{}'.format(self.name).upper())
        print('Kind is  {}'.format(self.kind))
        print('Taste is {}'.format(self.taste))

        if len(self.additives):
            print('Additives is ')
            for a in self.additives:
                print('\t{}'.format(a))

        if len(self.filling) > 0:
            print('Filling is {}'.format(self.filling))
        print('-'*50)

    def set_filling(self,fillgin):
        self.filling = fillgin
        print('-' * 30)


    def add_additives(self, additives):
        # extend() przyjmuje jako argument inną sekwencję i dodaje jej elementy na koniec listy, na której jest wywoływana.
        # Nie tworzy nowej listy, lecz modyfikuje oryginalną listę.
        self.additives.extend(additives)



cake1 = Cake('Szarlotka','placek','jabłkowy',['jabłka','mąka','drożdże'],'krem')
cake2 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake3 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')
print(cake1.name, cake1.kind, cake1.taste, cake1.additives, cake1.filling)


cake1.show()
cake2.show()
cake3.show()

cake1.set_filling('vanillia cream')
cake2.set_filling('cake')
cake3.set_filling('chocolate')

cake1.add_additives('cream')
cake2.add_additives(['cacoa powder','coconuts'])



bakery_office = []
bakery_office.append(cake1)
bakery_office.append(cake2)
bakery_office.append(cake3)

print("Today in our offer:")
for b in bakery_office:
    print('{} - {} main taske: {} with additives of {}, filled with {}'.format(b.name, b.kind, b.taste, b.additives, b.filling))









