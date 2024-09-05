suma = 0;
for i in range(5):
    print(i) #imprime del 0 al 4
    suma+= i
print(suma)
i=1
while(suma > 0):
    print(i)
    suma-=i
    i*=2
print(suma)
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]