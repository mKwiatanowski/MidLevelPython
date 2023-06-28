
class MemoryClass:

    def __init__(self,list):
        self.list_of_items = list

    # __call__() umożliwia tworzenie obiektów tej klasy, które można traktować jako funkcje. W tym wypadku będziemy dodawać nowe pozycje do listy
    def __call__(self, item):
        self.list_of_items.append(item)


# tworzenie obiektu klasy
mem = MemoryClass([])
print('List of items in memory', mem.list_of_items)

mem.list_of_items.append('buy suger')
print('List of items in memory', mem.list_of_items)

print('This class is callable:', callable(MemoryClass))
# callable() służy do sprawdzania, czy obiekt jest wywoływalny, czyli czy można go wywołać jak funkcję i tu mem nie jest calllable więc nie można jej wywołać jak by była
# zmienna funkcji
print('This class is callable:', callable(mem))

# dzięki zdefiniowanej w klasie funkcji __call__ teraz wystarczy napisać zmienna i w nawiasie wskazać wartośc do dodania na liście
mem('buy milk')
print('List of items in memory', mem.list_of_items)
mem('buy coffy')
print('List of items in memory', mem.list_of_items)

# teraz gdy w klasie jest zdefiniowana funkcja __call__ to zmienna mem jest callable czyli jest wywoływana przez klasę
print('This class is callable:', callable(MemoryClass))
print('This class is callable:', callable(mem))