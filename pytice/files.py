class Persona:
    def __init__(self, id,nombre,email):
        self.id=id
        self.nombre=nombre
        self.email=email
    def __str__(self) -> str :
        return f"persona con id: {self.id}, nombre: {self.nombre} email:{self.email}"
    def __repr__(self) -> str:
        return self.__str__() 
archivo= open("./fecha.csv", "r") # write lo crea y pisa
"""
    r+ leer y escribir, solo se abre, cada vez que lo abrimos lo sobreescribimos
    a añadir
    r leer
"""
#archivo.write("id,nombre,email\n")
#archivo.write("1,fran,fran@email.com\n")
#archivo.write("2,guada,guada@email.com\n")
#archivo.write("3,ellie,ellie@email.com\n")
#print(archivo.read())
personas=[]
#print(archivo.readlines()); lista de lineas
next(archivo) # salteo la primera linea
for line in archivo:
    datos= line.strip().split(",") #strip elimina espacios, split divide por parametro
    print(f"datos: {datos}" )
    if len(datos) ==3 :
        id,nombre,email=datos
        personas.append(Persona(id,nombre,email))
print(personas)
archivo.close()
