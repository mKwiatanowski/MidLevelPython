
class NoDuplicates:

    def __init__(self):
        self.list = []

    def __call__(self, new_item):
        # pętla która będzie iterować po wszystkich nowych argumentach
        for i in new_item:
            # każdy argument zostanie porównany z listą czy nie występuje
            if not i in self.list:
                # jeśli nie występuje to dodanie do listy
                self.list.append(i)


my_no_drop_list = NoDuplicates()
print(my_no_drop_list.list)

my_no_drop_list(['keybors', 'mouse'])
print(my_no_drop_list.list)

my_no_drop_list(['keybors', 'mouse','pendrive'])
print(my_no_drop_list.list)

my_no_drop_list(['charger','pendrive'])
print(my_no_drop_list.list)






