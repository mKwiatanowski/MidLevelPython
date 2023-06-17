
# funkcja eval pozwala wykonać jedynie wyrażenia i jest to coś co może być póxniej przypisane do zmiennej.
# W wyrażeniu nie można samodzielnie czegoś przypisywać nie można budować pętli ani żadnych skomplikowanych poleceń
var_x = 10

#source = 'var_x = 4'

# exec przyjmie zmienna, która może mieć więcej linijek kodu. Można np napisać pętle
source = '''
new_var = 1
for i in range(var_x):
    print('-' * i) 
    new_var += 1
'''



# wywołując resultat exec zawsze otrzymamy none
result = exec(source)
print(result)

# jednak gdy wywołamy zmienna wprowadzoną ręcznie to okaże się że zmienna została zmodyfikowana
# tu jeszcze bardziej trzeba uważać ponieważ użytkownik będzie mógł wpływać na wynik krytycznych zmiennych zawartych w programie
print(var_x)
print(new_var)

# exec jest bardziej niebezpieczną funkcją dającą znacznie większe możliwości ponieważ pozwalamy na uruchomienie dowolnego kodu przez użytkownika

source = input("Enter your expression: " )
print(eval(source))

