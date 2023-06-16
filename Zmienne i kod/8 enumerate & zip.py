
workDays = [19,21,22,21,20,22]

print(workDays)

# enumerate() numeracja
enumerateDays = list(enumerate(workDays))
# po skonwertowaniu całości na liste, wynik to tuplet [(0,19) itp]
print(enumerateDays)

# pętla for ma możliwośc iteraci przez więcej jak 1 wartośc która przechodzi prez dany obiekt
for pos, value in enumerateDays:
    print('Position', pos, 'value', value)



months = ['I', "II", 'III', 'IV', 'V', 'VI']

# funkcja zip służy do połączenia ze sobą dwóch różnych list, które w tuplecie będą ze sobą połączone
# jednak nie można wyświetlić bezpośrednio wyniku funkcji zip(l1, l2) ponieważ wynikiem będą dane binarne.
# trzeba to dodatkowo skonwertować do listy
monthsDays = list(zip(months,workDays))
print(monthsDays)


# m - określa teraz w tuplecie pierwszą wartość czyli numer miesiąca a d - określa drugą wartość czyli ilość dni roboczych w miesiącu
for m, d in monthsDays:
    print("Month", m, 'days', d)

# pos jest wywoływane przez funkcje enumerate jako kolejna pozycja jaka została zliczona
# 2 zmienna w (m,d) jest wywoływana przez zip(m,d)
for pos, (m,d) in enumerate(zip(months, workDays)):
    print('Position', pos, 'month', m, 'days', d)





















