

import pickle
import glob

''' glob
jeśli znamy ścieżkę dostępu do katalogu i  w tym katalogu znajdują się pliki z rozszerzeniem bakery, 
to chcielibyśmy mieć funkcję , która zwróci listę takich plików. Odpowiednią do tego prawie gotową funkcję znajdziesz w module glob:
'''
'''
Jeśli f to uchwyt do pliku, a obj to jakiś obiekt, to możesz go zapisać na dysku poleceniem:
    pickle.dump(obj, f)
A jeśli potem ten obiekt chcesz odczytać, to możesz to zrobić tak:
    new_obj = pickle.load(f)
'''


class Cake:

    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel' ,'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free,text):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))


    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:    {}".format(self.kind))
        print("Taste:   {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling: {}".format(self.filling))
        print('Is there gluten? {}'.format(self.__gluten_free))
        if len(self.__text) > 0:
            print('Text:     {}'.format(self.__text))
        print('- ' *20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)


    def __get_text(self):
        return self.__text

    def __set_text(self,new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on the cake')

    def save_to_file(self, path):
        # wb otwarcie pliku w formacie binarnym
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        # rb odczyt w trybie binarnym
        with open(path, 'rb') as r:
            new_cake = pickle.load(r)

        # przypisanie do listy bakery_offer informacji z pliku binarnego
        cls.bakery_offer.append(new_cake)
        # zwrócenie na zewnątrz informacji z pliku
        return new_cake

    @staticmethod
    def get_bakery_files(catalog):
        return glob.glob(catalog+'/*.bakery')




cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, 'Good luck!')

print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

cake01.Text = 'Happy birthday!'
cake02.Text = '18'

for c in Cake.bakery_offer:
    c.show_info()



cake01.save_to_file('c:/temp/cake01.bakery')
cake02.save_to_file('c:/temp/cake02.bakery')


cake05 = Cake.read_from_file('c:/temp/cake01.bakery')
cake05.show_info()


print(Cake.get_bakery_files('c:/temp'))































