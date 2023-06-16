'''
W tym zadaniu sprawdzimy, jak zachowują się zmienne podczas modyfikowania ich wartości
'''

# ad 1
a = b = c = 10
print(a,b,c,"\n", id(a), id(b), id(c))

a = 20
print(a,b,c,"\n", id(a), id(b), id(c))

# ad 2
a = b = c = [1,2,3]
a.append(4)

print(a,b,c, "\n", id(a), id(b), id(c))

# ad 3


x = 10
y = 10
print(x,y, id(x), id(y))

#4

y = y + 1 - 1
print(x,y, id(x), id(y))

#5

y = y + 1234567890 - 1234567890
print(x,y, id(x), id(y))