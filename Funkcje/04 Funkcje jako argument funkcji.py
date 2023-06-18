
def Bake(what):
    print('Baking {}'.format(what))


def Add(what):
    print('Baking {}'.format(what))

def Mix(what):
    print('Baking {}'.format(what))


# można przekazać funkcję do zmiennej, można także przekazać funkcję do funkcji wówczać funkcja by się stała argumentem w funkcji

cookbook = [(Add, 'milk'), (Add, 'eggs'),(Add, 'flour'),(Add, 'suger'),(Mix, 'ingradients'),(Bake, 'cookies'),]

# dla każdej czynności i każdego składnika który znajdują się na liście złożónej z tupletów
for activity,obj in cookbook:
    # wywołanie czynności z obiektem jako składnik
    activity(obj)

print('-'*30)

# można to samo co wyżej zrobić w inny sposób

def Cook(activity, obj):
    activity(obj)

Cook(Bake,'brownies')

# można w ten sposób ułatwić wywołanie szeregu jakiś funkcji, bo nie trzeba się martwić o przechowywanie jakiś wyników poszczególnych funkcji
# Można więc połączyć ze sobą funkcję aby wzajemnie przekazały sobie odpowiednie dane. Skróci to koncowy kod.
for activity,obj in cookbook:
    Cook(activity, obj)




