

import os
import urllib.request

data_dir = r'c:\temp'
pages =[ { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
         { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
         { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]

# pętla iteruje po każdej lini słownika
for i in pages:

   try:
        # tworzenie nazwy pliku {}.format(klucz) oznacza, że do {wartosc} ma zostać wczytawa wartość z słownika dla wskazanego klucza
        file_name = '{}.html'.format(i['name'])
        # łączenie ścieżki i nazwy
        path = os.path.join(data_dir, file_name)

        print('Procesing {} to {}...'.format(i['url'],file_name))
        urllib.request.urlretrieve(i['url'],path)
        print('Done')
   # Gdy wystąpi błąd w bloku try to wyświetlamy komunikat i przerywamy pętle
   except:
       print("Something is wrong! Failure processing web page {} ".format(i['name']))
       print('Stopping the process!')
       break

# gdy pętla nie zostanie przerwana to ma się wyśietlić komunikat
else:
    print('Done')




