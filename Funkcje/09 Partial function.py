

import smtplib
import functools



def SentInfoEmail(user,password,mailFrom,mailTo,mailSubject,mailBody):

    message = '''From: {}
    Sumject: {}
    
    {}
    '''.format(mailFrom,mailSubject,mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user,password)
        server.sendmail(user,mailTo,message)
        server.close()
        print('Mail sent')
        return True

    except:
        print('Error sending mail')
        return False







mailFrom = 'Your automation system'
mailTo = ['mateusz.kwiatanowski@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = ''' Hello

This mail confirm that processing has finished without problems,

hova a nice day!
'''

user = 'dodgewrclw@gmail.com'
password = '123'

# funkcja partial ma możliwość wyeliminowanie podawania na późniejszym etapie użytkownika i hasło ponieważ on go zna. Jako parametr podajemy najpierw
# nazwę funkcji, następnie wpisujemy zmienne które ta funkcja ma znać. Jeszce tu jest jedno ważne zmienne które mają być zapamiętane muszą rozpoczynać się od początku
# jednak jest sposób żeby to obejść jeśli np chcemy na sztywno wpisywać adres maila ( któryś z kolei parametr ) więc przyjmuje tutaj, że parametry powinien przyjąść wartość
SentInfoEmailFromGmail = functools.partial(SentInfoEmail,user,password, mailSubject = 'Execution alert' )

# po takim zmodyfikowaniu i ponownym wywołaniu funkcji w parametrach używamy już tylko tych pozostałych zmiennych, a zmienne które ta funkcja miała zapamiętać pomijamy
# jednak po zmodyfikowaniu funkcji partial i dodaniu dodatkowego parametru na sztywno, to w momencie wywołania funkcji i usunięciu tego parametru będzie błąd
# aby ten bład naprawić, należy każdy parametr przekazywać przez nazwę
SentInfoEmailFromGmail(mailFrom = mailFrom, mailTo = mailTo, mailBody = mailBody)

# funkcja partial pozwala utworzyć nową funkcję gdzie wykorzysytwać będzie starą funkcję ale będzie ją wywoływać z predefiniowanymi parametrami jeżeli te argumenty znajdują się
# na początku listy argumentów to wystarczy wymieniać je przez pozycje. Jednak gdy będzie trzeba użyć argumentu znajdującego się gdzieś dalej, to wywołując funkcję partial
# trzeba będzie wywoływać argumenty po nazwie


#SentInfoEmail(user,password,mailFrom,mailTo,mailSubject,mailBody)

