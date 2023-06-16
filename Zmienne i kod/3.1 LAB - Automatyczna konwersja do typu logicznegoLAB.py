

# Napisz skrypt, który będzie wyświetlał użytkownikowi zestaw opcji do wyboru:


def DisplayOptions(options):
    # pętla która iteruje tak długo jak jest długość listy options oraz range który tworzy sekwencje liczb od 0
    for i in range(len(options)):
        # tworzenie słownika, gdzie 1 wartość jest liczbą iteracji + 1, a 2 wartość to pobrana i pozycja z listy
        print("{} - {}".format(i+1 , options[i]))

    # użytkownik wprowadza numer
    choice = input('Select option above or press enter to exit: ')
    # funkcja ma zwrócić numer wpisany przez użytkownika
    return choice


options = ['load data', 'export data', 'analyze & predict']
choice = 'x'


# pętla wykonuje się tak długo jak długo zmienna choise jest niepusta
while choice:
    # wywołanie funkcji z parametrem listy
    choice = DisplayOptions(options)

    # dopuki lista jest niepusta wykonuje działania
    if choice != '':

        try:
            # konwersja liczby wprowadzonej przez uzyt. na format int. -1 dlatego, że użytkownik wpisuje wartosci 1-3 natomiast współżędne na liscie rozpoczynają się od 0
            choice_num = int(choice)-1

            if choice_num >= 0 and choice_num < len(options):
                print("you have selected {} - {}", format(choice_num+1, options[choice_num]))

            else:
                print("Your choice is wrong, pleas try again and press enter!")
        except:
            print("You need to enter a number")

    else:
        print("The end")




