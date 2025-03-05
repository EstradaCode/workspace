class Celu:
    #atributo de clase, compartido para todas las instancias
    tipo_dispositivo= "movil"
    #constructor
    def __init__(self, marca, precio): ## self == this, se lleva la palabra this como parametro siempre
        self.marca=marca
        self.precio=precio
    #metodos
    def llamar(self, numero_tel):
        print(f"{self.marca} está llamando a {numero_tel}")
    def __str__(self) -> str: ## to string equivalente
        return f"marca {self.marca} precio {self.precio} dispositivo {self.tipo_dispositivo}"
    
iphone= Celu("Iphone 7 plus", 300000)
samsung= Celu("Samsung S20", 140000)
print(iphone.marca)
samsung.llamar("11275")  
print(samsung)
print(iphone)