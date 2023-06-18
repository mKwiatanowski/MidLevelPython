
def calculate_paint(efficency_ltr_per_m2, *args):

    total_area = sum(args)
    calculate = efficency_ltr_per_m2 * total_area
    return calculate

print('You need total lts: ' , calculate_paint(1.2,22,14,69,10,15,64,48))

rooms = [22, 15, 156, 15.2, 43.4, 1.9]

print('You need total lts: ', calculate_paint(2.17 , *rooms))


def log_it(*args):
    path = r'c:\temp\log_it.txt'
    # otworzenie pliku i jego natomiast 'a' jest trybem apped
    with open(path,'a') as f:

        # pętla będzie wykonywać się tak długo jak dużo jest jest wprowadzonych wartości w args
        for line in args:
            # wpisanie lini do plku
            f.write(line)
            # wpisanie spacji do pliku
            f.write(' ')
        # na końcu wpisanie entera
        f.write('\n')



log_it('Starting processing forecasting')
log_it('ERROR', 'Not enough data', 'invoices', '2020')
