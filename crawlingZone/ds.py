lista = [1,2,3,4,5]
lista.append(6) # agregar al final
lista.remove(3) # elimina primer elemento con valor 3

tupla = (1,2,3,4,5)

conjunto = {1,2,3,4,5}
conjunto.add(6)
conjunto.discard(3) # elimina elemento sin error si no existe

diccionario = {"nombre": "Alice", "edad": 25}
diccionario["nombre"] = "Marta" # modifica valor asociado a la clase

#funciones
def saludar(nombre):
    return f"hola, {nombre}!"
print (saludar("francisco"))

# funciones lambda
                # defino lambda con parametros x,y y su cuerpo es x*y
multiplicar = lambda x, y : x*y
print(multiplicar(3,4))

def aplicar(fun,x,y):
    return fun(x,y)
print( aplicar(lambda x,y: x-y, 10, 3))