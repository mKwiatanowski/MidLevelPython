
class Cake:
    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        # .copy() jest dodane dlatego, żeby utworzyć kopię listy wprowadzanej w zmiennej ponieważ, gdyby tego nie była to modyfikacje na liście wpłynęły by
        # na tą pierwotną listę
        self.additives = additives.copy()
        self.filling = filling



cake1 = Cake('Szarlotka','placek','jabłkowy',['jabłka','mąka','drożdże'],'krem')
cake2 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '')
cake3 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '')
print(cake1.name, cake1.kind, cake1.taste, cake1.additives, cake1.filling)


bakery_office = []
bakery_office.append(cake1)
bakery_office.append(cake2)
bakery_office.append(cake3)

print("Today in our offer:")
for b in bakery_office:
    print('{} - {} main taske: {} with additives of {}, filled with {}'.format(b.name, b.kind, b.taste, b.additives, b.filling))




