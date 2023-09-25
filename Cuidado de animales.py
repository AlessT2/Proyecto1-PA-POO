#snake_case para variables, funciones y métodos
#PascalCase para clases
#SCREAMING_SNAKE_CASE para constantes

class AnimalCare:
    def __init__(self, healt=0, happiness=0, hunger=100, breeding=0, milk=0):
        self.healt = healt
        self.happiness = happiness
        self.hunger = hunger
        self.breeding = breeding
        self.milk = milk

class Pigs(AnimalCare):
    def __init__(self, healt=0, happiness=0, hunger=100, breeding=0, milk=0, meat=0, fur=0):
        super().__init__(healt, happiness, hunger, breeding, milk)
        self.meat = meat
        self.fur = fur

    def data_entry(self):
        self.healt = int(input("Ingrese la salud del cerdo: "))
        self.happiness = int(input("Ingrese la felicidad del cerdo: "))
        print("El hambre de su cerdo es: ", self.hunger)
        self.breeding = int(input("Ingrese cuantas crias ha tenido su cerdo: "))
        self.milk = int(input("Ingrese cuantos litros de leche ha producido su cerdo: "))
        self.meat = int(input("Ingrese cuantas libras de carne puede generar su cerdo: "))
        self.fur = int(input("Ingrese cuantas m^2 de piel puede generar su cerdo: "))

class Cows(AnimalCare):
    def __init__(self, healt=0, happiness=0, hunger=100, breeding=0, milk=0, meat=0, fur=0, horns=0):
        super().__init__(healt, happiness, hunger, breeding, milk)
        self.meat = meat
        self.fur = fur
        self.horns = horns

    def data_entry(self):
        self.healt = int(input("Ingrese la salud de la vaca: "))
        self.happiness = int(input("Ingrese la felicidad de la vaca: "))
        print("El hambre de su vaca es: ", self.hunger)
        self.breeding = int(input("Ingrese cuantas crias ha tenido su vaca: "))
        self.milk = int(input("Ingrese cuantos litros de leche ha producido su vaca: "))
        self.meat = int(input("Ingrese cuantas libras de carne puede generar su vaca: "))
        self.fur = int(input("Ingrese cuantas m^2 de piel puede generar su vaca: "))

class Sheep(AnimalCare):
    def __init__(self, healt=0, happiness=0, hunger=100, breeding=0, milk=0, meat=0, wool=0):
        super().__init__(healt, happiness, hunger, breeding, milk)
        self.meat = meat
        self.wool = wool

    def data_entry(self):
        self.healt = int(input("Ingrese la salud de la oveja: "))
        self.happiness = int(input("Ingrese la felicidad de la oveja: "))
        print("El hambre de su oveja es: ", self.hunger)
        self.breeding = int(input("Ingrese cuantas crias ha tenido su oveja: "))
        self.milk = int(input("Ingrese cuantos litros de leche ha producido su oveja: "))
        self.meat = int(input("Ingrese cuantas libras de carne puede generar su oveja: "))
        self.fur = int(input("Ingrese en micras el grosor de la piel de la oveja: "))

care = 0

animal_entry = 0
while animal_entry >= 0 and animal_entry <= 3:
    print("1. Cerdos")
    print("2. Vacas")
    print("3. Ovejas")
    chosen_animal = int(input("Seleccione que animal desea ingresar: "))
    if chosen_animal == 1:
        pig1 = Pigs()
        pig1.data_entry()
    elif chosen_animal == 2:
        cow1 = Cows()
        cow1.data_entry()
    elif chosen_animal == 3:
        sheep1 = Sheep()
        sheep1.data_entry()

while care >= 0 and care <= 6:
    print("Acciones con animales")
    print("1. Interactuar con animales")
    print("2. Recolección de Recursos")
    select = int(input("Ingrese que acción desea realizar: "))

    if select == 1:
        print("Acciones: ")
        print("1. Alimentar")
        print("2. Acariciar")
        print("3. Limpiar")
        act = int(input("Ingrese que acción desea realizar: "))
        if act == 1:
            print("Seleccione con que lo desea alimentar: ")
            print()
        elif act == 2:
            print("La felicidad de su animal está en: ",self.happiness)
            print("Precione la tecla 'Y' para acariciar")
            print("Ahora la felicidad de su animal está en:",self.happiness)
        elif act == 3:
            print("Su animal se encuentra limpio")

    elif select == 2:
        print("Animales a disposicion: ")
        print("1. Cerdos")
        print("2. Vacas")
        print("3. Ovejas")
        animal = int(input("Ingrese de que animal desea recolectar recursos: "))
        if animal == 1:
            print("Recursos a recolectar de los cerdos: ")

