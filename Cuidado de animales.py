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

    def feed(self):
        print("Alimentos disponibles para animales: ")
        print("1. Manzana")
        print("2. Sandía")
        print("3. Zanahoría")
        print("4. Trigo")
        print("5. Maíz")
        feed_animal = int(input("Ingrese con que desea alimentar a su animal: "))
        if feed_animal >= 1 and feed_animal <= 5:
            self.hunger =+ 30
            print("El hambre de su animal ahora es: ",self.hunger)
        else:
            print("El hambre de su animal es: ",self.hunger)

    def clean(self):
        animal_clean = 50
        animal_clean2 = input("Presione la tecla 'C' si quiere limpiar a su animal: ").upper()
        if animal_clean2 == "C":
            animal_clean += 35
            print("El porcentaje de limpieza de su animal es: ",animal_clean)
        else:
            print("El procentaje de limpieza de su animal es: ",animal_clean)

    def strock(self):
        happ = input("Ingrese la tecla 'R' para limpiar: ").upper()
        if happ == "R":
            self.happiness += 20
            print("Ahora la felicidad de su animal se encuentra en: ", self.happiness)
        else:
            print("la felicidad de su animal es: ",self.happiness)

class Pigs(AnimalCare):
    def __init__(self, healt=50, happiness=50, hunger=50, breeding=0, milk=0, meat=0, fur=0):
        super().__init__(healt, happiness, hunger, breeding, milk)
        self.meat = meat
        self.fur = fur

    def data_entry(self):
        print("La salud de su cerdo es: ",self.healt)
        print("la felicidad de su cerdo es: ",self.happiness)
        print("El hambre de su cerdo es: ", self.hunger)
        self.breeding = int(input("Ingrese cuantas crias ha tenido su cerdo: "))
        self.milk = int(input("Ingrese cuantos litros de leche ha producido su cerdo: "))
        self.meat = int(input("Ingrese cuantas libras de carne puede generar su cerdo: "))
        self.fur = int(input("Ingrese cuantas m^2 de piel puede generar su cerdo: "))

    def collect_resources(self):
        print("Recursos disponibles: ")
        print("1. Su animal tiene ",self.breeding," crias")
        print("2. Su animal ha producido ",self.milk," litros de leche")
        print("3. Su animal puede generar ",self.meat," libras de carne")
        print("4. Su animal puede gener",self.fur," metros^2 de piel")
        collect = int(input("Ingrese que desea recoger: "))
        if collect == 1:
            collet_breeding = int(input("Ingrese cuantas crias desea recoger: "))
            self.breeding -= collet_breeding
            print("Ahora tiene ",self.breeding," crias")
        elif collect == 2:
            collect_milk = int(input("Ingrese cuantos litros de leche desea recoger: "))
            self.milk -= collect_milk
            print("Ahora tiene ",self.milk," litros de leche disponibles")
        elif collect == 3:
            collect_meat = int(input("Ingrese cuentas libras de carne desea recoger: "))
            self.meat -= collect_meat
            print("Ahora tiene ",self.meat," libras de carne disponibles")
        elif collect == 4:
            collect_fur = int(input("Ingrese cuantos metros^2 de piel desea recoger: "))
            self.fur -= collect_fur
            print("Ahora tiene ",self.fur," metros^2 de piel disponibles")

class Cows(AnimalCare):
    def __init__(self, healt=50, happiness=50, hunger=50, breeding=0, milk=0, meat=0, fur=0, horns=0):
        super().__init__(healt, happiness, hunger, breeding, milk)
        self.meat = meat
        self.fur = fur
        self.horns = horns

    def data_entry(self):
        print("La salud de su vaca es: ",self.healt)
        print("la felicidad de su vaca es: ",self.happiness)
        print("El hambre de su vaca es: ", self.hunger)
        self.breeding = int(input("Ingrese cuantas crias ha tenido su vaca: "))
        self.milk = int(input("Ingrese cuantos litros de leche ha producido su vaca: "))
        self.meat = int(input("Ingrese cuantas libras de carne puede generar su vaca: "))
        self.fur = int(input("Ingrese cuantas m^2 de piel puede generar su vaca: "))
        self.horns = int(input("Ingrese cuantos cuernos de vaca tiene: "))

    def collect_resources(self):
        print("Recursos disponibles: ")
        print("1. Su animal tiene ",self.breeding," crias")
        print("2. Su animal ha producido ",self.milk," litros de leche")
        print("3. Su animal puede generar ",self.meat," libras de carne")
        print("4. Su animal puede gener",self.fur," metros^2 de piel")
        print("5. Tiene en posecion ",self.horns," cuernos")
        collect = int(input("Ingrese que desea recoger: "))
        if collect == 1:
            collet_breeding = int(input("Ingrese cuantas crias desea recoger: "))
            self.breeding -= collet_breeding
            print("Ahora tiene ",self.breeding," crias")
        elif collect == 2:
            collect_milk = int(input("Ingrese cuantos litros de leche desea recoger: "))
            self.milk -= collect_milk
            print("Ahora tiene ",self.milk," litros de leche disponibles")
        elif collect == 3:
            collect_meat = int(input("Ingrese cuentas libras de carne desea recoger: "))
            self.meat -= collect_meat
            print("Ahora tiene ",self.meat," libras de carne disponibles")
        elif collect == 4:
            collect_fur = int(input("Ingrese cuantos metros^2 de piel desea recoger: "))
            self.fur -= collect_fur
            print("Ahora tiene ",self.fur," metros^2 de piel disponivles ")
        elif collect == 5:
            collect_horns = int(input("Ingrese cuantos cuernos desea recoger: "))
            self.horns -= collect_horns
            print("Ahora tiene ",self.horns," cuenros a disposicion")

class Sheep(AnimalCare):
    def __init__(self, healt=50, happiness=50, hunger=50, breeding=0, milk=0, meat=0, wool=0):
        super().__init__(healt, happiness, hunger, breeding, milk)
        self.meat = meat
        self.wool = wool

    def data_entry(self):
        print("La salud de su oveja es: ",self.healt)
        print("la felicidad de su oveja es: ",self.happiness)
        print("El hambre de su oveja es: ", self.hunger)
        self.breeding = int(input("Ingrese cuantas crias ha tenido su oveja: "))
        self.milk = int(input("Ingrese cuantos litros de leche ha producido su oveja: "))
        self.meat = int(input("Ingrese cuantas libras de carne puede generar su oveja: "))
        self.fur = int(input("Ingrese la cantidad de libras de lana que puede generar su oveja "))

    def collect_resources(self):
        print("Recursos disponibles: ")
        print("1. Su animal tiene ",self.breeding," crias")
        print("2. Su animal ha producido ",self.milk," litros de leche")
        print("3. Su animal puede generar ",self.meat," libras de carne")
        print("4. Su animal puede gener",self.fur," metros^2 de piel")
        print("5. Tiene en posecion ",self.wool," libras de lana")
        collect = int(input("Ingrese que desea recoger: "))
        if collect == 1:
            collet_breeding = int(input("Ingrese cuantas crias desea recoger: "))
            self.breeding -= collet_breeding
            print("Ahora tiene ",self.breeding," crias")
        elif collect == 2:
            collect_milk = int(input("Ingrese cuantos litros de leche desea recoger: "))
            self.milk -= collect_milk
            print("Ahora tiene ",self.milk," litros de leche disponibles")
        elif collect == 3:
            collect_meat = int(input("Ingrese cuentas libras de carne desea recoger: "))
            self.meat -= collect_meat
            print("Ahora tiene ",self.meat," libras de carne disponibles")
        elif collect == 4:
            collect_fur = int(input("Ingrese cuantos metros^2 de piel desea recoger: "))
            self.fur -= collect_fur
            print("Ahora tiene ",self.fur," metros^2 de piel disponivles ")
        elif collect == 5:
            collect_wool = int(input("Ingrese cuantas libras de lana desea recoger: "))
            self.wool -= collect_wool
            print("Ahora tiene ",self.wool," libras de lana disponibles")

print("Animales  :)")
print("1. Ingreso de animales")
print("2. Interactuar con animales")
act_entry = int(input("Ingrese que desea realizar: "))

while act_entry >= 1 and act_entry <= 2:
    if act_entry == 1:
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

    elif act_entry == 2:
        print("1. Interactuar con animales")
        print("2. Recolección de Recursos")
        select = int(input("Ingrese que acción desea realizar: "))

        if select == 1:
            print("1. Cerdos")
            print("2. Vacas")
            print("3. Ovejas")
            select_animal = int(input("Ingrese con que animal desea interactuar: "))
            if select_animal == 1:
                print("Acciones: ")
                print("1. Alimentar")
                print("2. Acariciar")
                print("3. Limpiar")
                act = int(input("Ingrese que acción desea realizar: "))
                if act == 1:
                    pig1.feed()
                elif act == 2:
                    pig1.strock()
                elif act == 3:
                    pig1.clean()
            if select_animal == 2:
                print("Acciones: ")
                print("1. Alimentar")
                print("2. Acariciar")
                print("3. Limpiar")
                act = int(input("Ingrese que acción desea realizar: "))
                if act == 1:
                    cow1.feed()
                elif act == 2:
                    cow1.strock()
                elif act == 3:
                    cow1.clean()
            if select_animal == 3:
                print("Acciones: ")
                print("1. Alimentar")
                print("2. Acariciar")
                print("3. Limpiar")
                act = int(input("Ingrese que acción desea realizar: "))
                if act == 1:
                    sheep1.feed()
                elif act == 2:
                    sheep1.strock()
                elif act == 3:
                    sheep1.clean()
        elif select == 2:
            print("Animales a disposicion: ")
            print("1. Cerdos")
            print("2. Vacas")
            print("3. Ovejas")
            animal = int(input("Ingrese de que animal desea recolectar recursos: "))
            if animal == 1:
                pig1.collect_resources()
            if animal == 2:
                cow1.collect_resources()
            if animal == 3:
                sheep1.collect_resources()
