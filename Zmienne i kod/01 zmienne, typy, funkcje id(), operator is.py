
myvar = 'Hello PyCHarm'
myvar2 = myvar+'!!'
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print('Is value the same? ', myvar == myvar2)
# W Pythonie, operator is jest używany do porównywania tożsamości obiektów. To oznacza, że is sprawdza, czy dwa zmienne odnoszą się do tego samego obiektu,
# a nie tylko, czy są one równe pod względem wartości.
print('Are the viriables the same? ', myvar is myvar2)
# id() jest to adres w pamieci gdzie sa przechowywane wartosci dla zmiennej
print(id(myvar), id(myvar2))
myvar2 = myvar2[:-2]
print(myvar, myvar2)
print(type(myvar), type(myvar2))
print('Is value the same? ', myvar == myvar2)
# W Pythonie, operator is jest używany do porównywania tożsamości obiektów. To oznacza, że is sprawdza, czy dwa zmienne odnoszą się do tego samego obiektu,
# a nie tylko, czy są one równe pod względem wartości.
print('Are the viriables the same? ', myvar is myvar2)
# id() jest to adres w pamieci gdzie sa przechowywane wartosci dla zmiennej
print(id(myvar), id(myvar2))







