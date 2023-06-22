
import smtplib

mailFrom = 'Your automation system'
mailTo = ['mateusz.kwiatanowski@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = ''' Hello

This mail confirm that processing has finished without problems,

hova a nice day!
'''

message = '''From: {}
Sumject: {}

{}
'''.format(mailFrom,mailSubject,mailBody)

user = 'dodgewrclw@gmail.com'
password = '123'

# przy wysyłaniu maila może pójść coś nie tak więc trzeba obsłużyć ewentualne błędu

try:
    # SMTP_SSL() dlatego że gmail oczekuje właśnie takiego klienta, łącząc się do innych serwerów pocztowych może być tak, że wymagane będzie np .SMTP()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # ehlo() przedstawienie się kim jesteśmy, na tym etapie przekazywane są dane komputera z jakiego dochodzi do połączenia z serwerem pocztowym
    server.ehlo()
    # lgoin(user,password) logowanie do serwera, która oczekuje 2 parametrów użytkownika i hasło
    server.login(user,password)
    # sendmail(user,mailTo,massage) wysyłanie maila, przyjmuje minimum 3 parametry: od kogo jest wysyłany mail, do kogo jest wysyłany mail, odpowienie sformatowana
    # treść maila
    server.sendmail(user,mailTo,message)
    # close() zamknięcie połączenia
    server.close()
    # wyświetlenie komunikatu że mail został wysłany
    print('Mail sent')

except:
    print('Error sending mail')






