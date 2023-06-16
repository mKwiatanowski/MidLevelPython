
workDays = [19,21,22,21,20,22]
months = ['I', "II", 'III', 'IV', 'V', 'VI']

# dict() konwersja na słownik
monthDays = dict(zip(months,workDays))
print(monthDays)

# taka konstrukcja zwróci błąd
#for key, value in monthDays:
# w słowniku trzeba iterować po klucz, a następnie jeszcze raz wywolać słownik jednak wtedy w [klucz]
for key in monthDays:
    print('Key is ', key, 'value is', monthDays[key])


for value in monthDays.values():
    print('the value is: ',value)



