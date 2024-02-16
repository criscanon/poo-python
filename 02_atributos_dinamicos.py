class Computador:
    #This is the constructor and this is a function or method that run automatically every call. (constructor method or function)
    def __init__(self, marca, modelo, ram):
        #Here we define the attributes
        self.marca = marca
        self.modelo = modelo
        self.ram = ram

computador1 = Computador("Lenovo", "G4080", "16GB")

print(computador1.marca)