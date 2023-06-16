
dayType = 3

weekend = 1
workday = 2
holiday = 3

# tworzy się jakiś warunek, szkielet to zamiast wprowadzać jakiś skłądnie, w celu weryfikowania choćby prosty print można użyć dużo prostrze rozwiązanie
# funkcja pass to funkcja ktora nie robic apsolutnie nic, ale dzięki niej można łatwo przetestować np taki warunek
# jest to takie dobre zaznaczenie miejsca gdzie trzeba cos jeszcze napisac
if dayType == 1:
    pass
elif dayType == 2:
    pass
else:
    pass

# forma skrócona if, jeśli jest jakieś proste podstawienie prosty warunek bez wiekszego rozbudowywania, wystarczy zrobić skrócony if jak niżej
dayDescription = 'weekend' if dayType == 1 else '?'
print(dayDescription)

# skróconą formę if można zaknieżdzać
dayDescription = 'weekend' if dayType == 1 else 'weekend' if dayType == 2 else 'holiday'
print(dayDescription)

'''
Kiedy używamy skróconej adnotacji if, podczas przetważania danych są takie sytuacji gdy w danych oryginalnie znajduje się jakaś wartość która należy skonwertować, podstawić,
zamienić na inna wartość. W takich prostych sytuacjach taki prosty if będzie lepszym rozwiązaniem jak klasyczny if
'''










