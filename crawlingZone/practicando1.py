import random

intentos = 0
maxIntentos = 32
numero_secreto = random.randint(1,10)

while( intentos <maxIntentos):
    intento = int(input("Introduce un numero:"))
    intentos+=1
    if(intento == numero_secreto):
        print("Encontrado ! felicidades ganaste!")
        break
    elif intento < numero_secreto:
        print("ups! el numero es más grande que ese!")
    else:   
        print("ups! el numero es mas chico que ese!")
if intentos == maxIntentos:
    print("lo siento! suerte para la proxima!")      