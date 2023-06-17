
import time

source = "reportLine += 1"

reportLine = 0
start = time.time()
for i in range(1000000):
    exec(source)
stop = time.time()
time_out_compitale = stop - start

# exec kompiluje fragment tekstu i to trwa trochę czasu ale jeśli raport by miał 1000 linijek to  wtedy proces dodatkowej kompilacji wiązał by się
# z 1000 krotnym kompilowaniem
exec(source)

# Funkcja compile() w Pythonie służy do kompilacji kodu źródłowego w postaci łańcucha znaków lub obiektu AST (Abstract Syntax Tree) w obiekt kodu Pythona.
# Wywołanie compile() zwraca obiekt kodu, który może być później wykonywany przy użyciu funkcji exec() lub eval()
# Parametry funkcji source - Kod źródłowy, który ma zostać skompilowany. Może to być łańcuch znaków zawierający kod
# filename - Opcjonalny parametr, który określa nazwę pliku, z którego pochodzi kod źródłowy. Jeśli kod pochodzi z pliku, wartość tego parametru powinna być nazwą pliku.
# W przypadku kodu wprowadzonego interaktywnie, można przekazać arbitralną nazwę
# mode - Tryb kompilacji. Może przyjąć jedną z trzech wartości: 'exec' (domyślnie), 'eval' lub 'single'. Tryb 'exec' jest używany, gdy kompilowany kod to cały moduł lub skrypt.
# Tryb 'eval' jest używany, gdy kompilowany kod to pojedyncze wyrażenie. Tryb 'single' jest używany, gdy kompilowany kod to pojedyncza instrukcja.
start = time.time()
sourceCompiled = compile(source,'Internal variable source', 'exec')
for i in range(1000000):
    exec(sourceCompiled)
stop = time.time()
time_compiled = stop - start


print(time_out_compitale)
print(time_compiled)
# różnica jest taka, że kod skompilowany zadziałała 33x szybciej od kodu nie skompilowanego
print(time_out_compitale / time_compiled)

print(reportLine)










