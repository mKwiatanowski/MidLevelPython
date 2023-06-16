
# funkcja, do której zwacam liste i n elementów
def GetListOfColors (colors, n):
    # funkcja będzie zwraca liste od początku do n elementu
    return colors[:n]


colors = ["red", "orange", "green", "violet", "blue", "yellow"]

# pętla będzie się wykonywać do momentu gdy c będzie się równać len(dlugość) listy, dodatkowo otoczone jest to range (1 do długośc listy +1 )
# ponieważ lista jaka będzie zwracana przez funkcje bedzie sie musiala rozpoczynac od 1 elementu wiec trzeba tez powiekszyc dlugosc listy o +1
for c in range(1,len(colors)+1):

    new_colors = GetListOfColors(colors,c)
    print(new_colors)





definition = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli. '


print(definition[definition.index('(')+1:definition.index(')')])



