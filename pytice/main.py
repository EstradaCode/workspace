print("hola mundo!")
nombre= "francisco"
print(type(nombre))
edad=20
print(type(edad))
edad= "veinte"
print(type (edad))
### tipos de datos: str, list, int, float, bool 
# asignación en conjunto
numeros=[1,2,3,4,5]
nombre, edad= "fran", 22
print(edad)
print(nombre)
print(numeros)
#en python se suele utilizar snake case
variable_edad= 22
print(variable_edad)
#setear como strin para desarrolladores y saber que variable contiene
brand:str = "prada"
brand= 44
print(brand)
def hello() -> int: 
    return "hello"
print(hello())
# tipos de datos chequeados a runtime y no a compile time
"""
    dsadasdae como estas?
"""
# operadores
resultado = 1+2
print(resultado)
print(2**4) # 2 a la 4
print(4/2)
print(5%2)
print(10 > 5)
print( 10< 5)
print( 10>5)
print (10 !=5)
## operadores logicos para unir condiciones
print ( 10> 5 or 1<3 or "A" == "c")
# and
# not
#operadores de asignación = 
numero= 0
numero +=1 # numero = numero+1
numero /=2
numero*=200
numero**=0
numero-=1
if numero >0:
    print(f"{numero} es positivo")
elif numero == 0:
    print(f"numero {numero} es cero")
else:
    print(f"numero {numero} es negativo")
#operador ternario
mensaje= f"el numero {numero} es "
mensaje+= "positivo" if numero >10 else "0 o negativo"
print(mensaje) 
"""
estructuras de datos
"""
numeros= [1,2,3,4,-1,0] # lista -> similar a arraylist
# metodos de lista
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)
numeros.append(1000)
print(f"numeros {numeros} con longitud {len(numeros)}")
numeros.remove(1) # remueve la primer instancia coincidente que encuentra
numeros.pop()# remueve el elemento al tope de la ""pila"""
print(numeros) 
#del numeros[0:3] se puede eliminar de a varios, no se tiene en cuenta el 3, es hasta que sea 3
## sets el orden no está garantizado como en list y no hay duplicados
letrasA= {"a","b", "c", "d"}
letrasB={"a", "e","f"}
union= letrasA | letrasB #union
print(union)
interseccion= letrasA & letrasB
print(interseccion) # conjunto vacio
diferencia= letrasA - letrasB # se le resta al conjunto la interseccion del conjunto b y a 
print(diferencia)
## diccionario 
persona = {
    "nombre": "fran",
    "edad": "20", 
    "direccion": "calle falsa 123"
}
print(persona["direccion"])
print(persona.keys()) ## metodo para las claves
print(persona.values()) ## valores
## for loop
nombres= {"martin", "ludmi", "joaquin"}
for nombre in nombres:
    print(nombre)

for key in persona:
    print(f"clave: {key} valor: {persona[key]}")
for key, value in persona.items(): # items contiene un arreglo de pares clave valor
    print(f"clave: {key} valor: {value}")

numeros= [1,3,4,5,6,8,9,10]
suma=0
for numero in numeros:
    suma+= numero
print(suma)
##
numeros_n=0
while numeros_n<10:
    numeros_n+=1
print(numeros_n)

## funciones
def saludar(nombre, edad=-1):
    print(f"hola {nombre} como estas?")
    if edad >=0:
        print(f"essaaaa, tu edad es {edad}")
saludar("francisco")
saludar("guada", 21)
def es_adulto(edad):
    return edad >=18
print(es_adulto(21))
print(es_adulto(17))
# funciones built in utiles []. "".
import math # despues de importarlo se puede utilizar, sigue siendo una lectura secuencial
print(math.pi)
from math import pi # importar elemento que necesito, para no traer las funcionalidades enteras
pi
import calculadora as calcu
# importar modulo propio + apodo
print(calcu.suma(2,2))
print(calcu.division(3,9))
print(calcu.multiplicacion(3,3))
print(calcu.division(10,2))
