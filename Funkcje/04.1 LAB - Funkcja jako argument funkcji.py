def double(x):
    return 2 * x


def square(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2

# funkcja, która jako activity będzie zwracać inną funkcję, a parametr x_table będzie zwracać wartość do innej funkcji
def generate_values(activity,x_table):
    # pusta lista w której będą przechowywane wyniki
    value = []

    # pętla, która będzie iterować po liście x_table
    for x in x_table:
        # dodawanie wyniku do listy value, w którym activity jest zwracana inna unkcja, a x przekazywany jest do tej funkcji na podstawie listy x_table
        value.append(activity(x))
    # zwrócenie wyniku funkcji będzie lista zapisanych wyników działanie pętli for
    return value

x_table = list(range(11))

print(generate_values(double, x_table))
print(generate_values(square, x_table))
print(generate_values(negative, x_table))
print(generate_values(div2, x_table))

