
# dodanie na końcu argumentu *args (zmienna może mieć dowolną nazwę istotne jest to żeby przed nazwą zmiennej znajdowała się *)
# spowoduje to, że wywołując funkcję będzie można dodać dowolną ilośc argumentów
# **kwargs jest to argument poprzedzony słowem kluczowym i mamy tu doczynienia ze słownikiem
def BuyMe(prefix='Please bue me', what='something nice', *args, **kwargs):
    print(prefix, what)
    print(args)
    print(kwargs)

# Takie wywołanie spowoduje utworzenie tupleta z dodatkowych argumentów, które będzie można dodatkowo przetważać
# wywołując **kwargs należy poprzedzić wywołanie kluczem klucz = wartość, wówczas utwoży się z tego słownik
BuyMe('Please buy me', 'a new car','a cat','a dog', 'a dragon',shop = 'market', color = 'any')


product = ['milk','bread','flakes']
parameters = {'prince':'low', 'time':'now'}

# wywołując w ten sposób otrzymamy listę z tupletem o dwóch argumentach, jednym argumentem będzie lista product, a drugim argumentem będzie słownik parameters
BuyMe('Buy me','news paper', product, parameters)

# jeśli przed zmienną ustawie * to ta zmienna zostanie zaczytana jako args, jeśli użyje ** to ta zmienna zostanie potraktowana jako kwargs
BuyMe('Buy me','news paper', *product, **parameters)





