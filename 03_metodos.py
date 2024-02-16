class Computer:
    #This is the constructor and this is a function or method that run automatically every call. (constructor method or function)
    def __init__(self, marca, modelo, ram):
        #Here we define the attributes
        self.marca = marca
        self.modelo = modelo
        self.ram = ram

    def restart(self):
        print(f'Restarting computer: {self.marca}')

    def consultRamMemory(self):
        print(f'Ram memory of your computer {self.marca} is {self.ram}')


computer1 = Computer("Lenovo", "G4080", "16GB")

computer1.restart()

computer1.consultRamMemory()
