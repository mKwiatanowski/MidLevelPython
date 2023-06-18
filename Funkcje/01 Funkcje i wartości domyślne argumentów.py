
# jeśli wprowadzimy wartośc domyślną dla 1 parametru, a dla drugiego nie to nie uda się skompilować tej funkcji
#def BuyMe(prefix='Please bue me', what):

def BuyMe(prefix='Please bue me', what='something nice'):
    print(prefix, what)

# w 1 przykładzie trzeba podawać kolejność zgodnie z zaprogramowaną kolejnością w funkcji
BuyMe('Please buy me', 'a new car')
# przy wywołaniu zmiennej kolejnośc ich nie ma znaczenia
BuyMe(prefix='Please buy me', what='a new car')
BuyMe(what='a bran new car', prefix='Please buy me')

# gdy w funkcji ustawi się wartość domyślną, to nie ma potrzeby w wywołaniu funkcji jej wpisywania, natomiast aby nadpisać domyślną wartość, wystarczy
# wprowadzić dla tego parametru wartość
BuyMe('Please')
BuyMe(what='something sweet')
