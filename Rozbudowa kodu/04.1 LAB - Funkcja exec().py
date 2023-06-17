

import os

files_to_process = [
    r"C:\temp\python\math_sin_square.py",
    r"C:\temp\python\math_square_root.py"
    ]


for file in files_to_process:

    # otwarcie pliku 'r' otwarcie i zamknięcie i zapisanie tego do zmiennej f
    with open(file,'r') as f:
        # os.path.basename(file) przeczytanie nazwy pliku
        print("Open file: {} ".format(os.path.basename(file)))
        # przeczytanie zawartości pliku zapisanego w zmiennej f
        source = f.read()
        # wywołanie kodu jaki znajduje się w przeczytanym pliku
        # funkcja exec() wywołuje kod jako fragment programu  python. Oznacza to, że kod z pliku jest interpretowany i wykonany
        exec(source)








