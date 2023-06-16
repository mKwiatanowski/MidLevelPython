
# próba konwertowania tekstu, listy na typ bool ma pewny haczyk. Jeśli będzie wprowadzona jakakolwiek wartość to python będzie traktować to jako True,
# natomiast jeśli wartość będzie pusta potraktuje to jako False, 0 też jest konwertowany do Fałsz
isOk = True
print("Variable isOk: ", isOk,type(isOk))

if isOk:
    print('True')


listOfErrors = [100,101,102]
print('Variable listOferrors: ', listOfErrors, type(listOfErrors))

# jest to mniej intuicyjne jak to rozwiązanie niżej
# if listOfErrors:
#    print('True')
# jest tp lepsze o bardziej logiczne rozwiązanie sprawdzenia czy lista jest niepusta
if len(listOfErrors) > 0:
    print("True")
