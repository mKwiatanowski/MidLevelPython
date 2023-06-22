# biblioteka requests To pozwoli Ci na dokonywanie żądań HTTP, takich jak wysyłanie żądań GET lub POST do serwera sieciowego i obsługę odpowiedzi.
# Moduł requests nie jest modułem wbudowanym i musi zostać zainstalowany. Możesz go zainstalować za pomocą narzędzia pip, uruchamiając następującą komendę w terminalu:
# pip install requests
import requests
import os
import functools


def save_url_file(url, dir, file, msg):
    print(msg.format(file))

    r = requests.get(url, stream=True)
    file_path = os.path.join(dir, file)

    with open(file_path, "wb") as f:
        f.write(r.content)


'''
msg = "Please wait - the file {} will be downloaded"

url = 'http://mobilo24.eu/spis'
dir = 'c:/temp/'
file = 'spis.html'
save_url_file(url, dir, file, msg)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
dir = 'c:/temp/'
file = 'logo.png'
save_url_file(url, dir, file, msg)
'''



save_url_to_dir = functools.partial(save_url_file, dir = r'c:\temp' , msg = 'Please wait: {}')


url = 'http://mobilo24.eu/spis'
file = 'spis.html'
save_url_to_dir(url = url ,file = file)

url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
file = 'logo.png'
save_url_to_dir(url = url,file = file)


