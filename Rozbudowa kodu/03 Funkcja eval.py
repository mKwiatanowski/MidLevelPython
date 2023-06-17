

# funkcja eval pozwoli pobrać od użytkownika jakiś napis, który będzie prawdopodobnie fragmentem jakiegoś kodu i ten framgment kodu będzie można uruchomić samodzielnie
# w pythonie
# za pomocą tej funkcji, można pobrać z bazy danych zapisany kod np w formie raportu, a następnie wygenerować ten raport tak jakby tego chciał użytkownik
# to rozwiązanie ma tez pewne wady nie wiemy co się stani w tym kodzie wprowadzonym przez użytkownika tam mogą być błędy, które spowodują, że nasza aplikacja
# będzie mieć awarię albo też tam może być taki kod, który może się okazać dla nas szkodliwy.

var_x = 10
password = 'My super secret password'

# source = 'var_x + 2'
# source = 'password'
# sprytny użytkownik zaimportował sobie modół os i wywołał scieżkę do katalogu, mógłby teraz nawet usunąć pliki jeśli aplikacja by miała do tego prawa
source = '__import__("os").getcwd()'

# tworzenie kopii środowiska, następnie usuwam wrażliwą zmienną. Teraz gdy użytkownik by wprowadził odwołanie do password to zakończy się błędem
# jednak używając eval zawsze może się zdażyć zapomnieć usunąć wszystkie strategiczne zmienne i tu można stwożyć puste środowisko
# globals = globals().copy()
# del globals['password']


globals = {}


result = eval(source,globals)
print(result)

# globals to środowisko pythona, tu można wydobyć wszystkie zdefiniowane zmienne
#print(globals())

















