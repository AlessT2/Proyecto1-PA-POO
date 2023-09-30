import time
import threading
inventory_1 = [0, "Compuesto para Vaca"];inventory_2 = [0, "Compuesto para Oveja"];inventory_3 = [0, "Compuesto para Cerdo"];inventory_4 = [0, "Antiplagas"] #INICIA*****ALLAN
inventory_5 = [0, "Vacas"];inventory_6 = [0, "Ovejas"];inventory_7 = [0, "Cerdos"];inventory_8 = [0, "Fertilizantes"];inventory_9 = [0, "Semillas de Manzanas"];inventory_10 = [0, "Semillas deSandías"]
inventory_11 = [0, "Semillas de zanahora"];inventory_12 = [0, "Trigo"];inventory_13 = [0, "Maíz"]
BARN = [inventory_1, inventory_2, inventory_3, inventory_5, inventory_6, inventory_7, inventory_4,inventory_8,inventory_9,inventory_10, inventory_11, inventory_12, inventory_13]
GET_COW_FOOD = 0;GET_FOOD_SHEEP = 0;GET_PIG_FOOD = 0;GET_ANTI_PEST = 0;GET_COW = 0;GET_PIG = 0;GET_SHEEP = 0;GET_FERTILIZER = 0; GET_APPLE = 0; GET_MELON = 0; GET_CARROT = 0; GET_WHEAT = 0; GET_CORN = 0
class Coin:
    def __init__(self, coin):
        self.coin = coin
    def show(self):
        return self.coin
BASE_COIN = Coin(50)
WALLET = BASE_COIN.show() #Termina******Allan
PIG = []
COW = []
SHEEP = []
while True:
    menu = input("\033[1;38;2;202;255;6mFarm Family Programadors\033[1;0m\n"+"\033[1;38;2;223;174;52mA. Animales :)\033[1;0m\n" #Animales, encargado por Alessandro
                 "\033[1;38;2;104;255;6mB. Cultivos\033[1;0m\n" #Cultivos encargado por Lesther
                "\033[1;38;2;255;54;0mC. Ti\033[1;0m" + "en" + "\033[1;38;2;255;54;0mda\033[0m\n" #Tienda encargado por Allan
                 "\033[1;38;2;6;164;255mElija su opción: \033[1;0m\n")
    while menu == "A" or menu == "a":
        if menu == "A" or menu == "a":
            # snake_case para variables, funciones y métodos
            # PascalCase para clases
            # SCREAMING_SNAKE_CASE para constantes
            class AnimalCare:
                def __init__(self, tim, healt=0, happiness=0, hunger=100, breeding=0, milk=0):
                    self.healt = healt
                    self.happiness = happiness
                    self.hunger = hunger
                    self.breeding = breeding
                    self.milk = milk
                    self.milk = tim

                def feed(self):
                    print("Alimentos disponibles para animales: ")
                    print("1. Manzana")
                    print("2. Sandía")
                    print("3. Zanahoría")
                    print("4. Trigo")
                    print("5. Maíz")
                    feed_animal = int(input("Ingrese con que desea alimentar a su animal: "))
                    if feed_animal >= 1 and feed_animal <= 5:
                        self.hunger -= 30
                        print(f"El hambre de su animal {self.number} ahora es: ", self.hunger)
                    else:
                        print(f"El hambre de su animal {self.number} es: ", self.hunger)

                def clean(self):
                    animal_clean = 50
                    animal_clean2 = input("Presione la tecla 'C' si quiere limpiar a su animal: ").upper()
                    if animal_clean2 == "C":
                        animal_clean += 35
                        print("El porcentaje de limpieza de su animal es: ", animal_clean)
                    else:
                        print("El procentaje de limpieza de su animal es: ", animal_clean)

                def strock(self):
                    happ = input("Ingrese la tecla 'R' para acariciar: ").upper()
                    if happ == "R":
                        self.happiness += 20
                        print("Ahora la felicidad de su animal se encuentra en: ", self.happiness)
                    else:
                        print("la felicidad de su animal es: ", self.happiness)


            class Pigs(AnimalCare):
                def __init__(self, number, healt=50, happiness=50, hunger=50, breeding=0, milk=0, meat=0, fur=0):
                    super().__init__(healt, happiness, hunger, breeding, milk)
                    self.meat = meat
                    self.fur = fur
                    self.number = number

                def data_entry(self):
                    print(f"La salud de su cerdo {self.number} es: ", self.healt)
                    print(f"la felicidad de su cerdo {self.number} es: ", self.happiness)
                    print(f"El hambre de su cerdo {self.number} es: ", self.hunger)
                    self.breeding = int(input("Ingrese cuantas crias ha tenido su cerdo: "))
                    self.milk = int(input(f"Ingrese cuantos litros de leche ha producido su cerdo: "))
                    self.meat = int(input(f"Ingrese cuantas libras de carne puede generar su cerdo: "))
                    self.fur = int(input(f"Ingrese cuantas m^2 de piel puede generar su cerdo: "))

                def data_entry_return(self):
                    return self.healt, self.happiness, self.hunger, self.breeding, self.milk, self.meat, self.fur

                def collect_resources(self):
                    print("Recursos disponibles: ")
                    print("1. Su animal tiene ", self.breeding, " crias")
                    print("2. Su animal ha producido ", self.milk, " litros de leche")
                    print("3. Su animal puede generar ", self.meat, " libras de carne")
                    print("4. Su animal puede gener", self.fur, " metros^2 de piel")
                    collect = int(input("Ingrese que desea recoger: "))
                    if collect == 1:
                        collet_breeding = int(input("Ingrese cuantas crias desea recoger: "))
                        self.breeding -= collet_breeding
                        print("Ahora tiene ", self.breeding, " crias")
                    elif collect == 2:
                        collect_milk = int(input("Ingrese cuantos litros de leche desea recoger: "))
                        self.milk -= collect_milk
                        print("Ahora tiene ", self.milk, " litros de leche disponibles")
                    elif collect == 3:
                        collect_meat = int(input("Ingrese cuentas libras de carne desea recoger: "))
                        self.meat -= collect_meat
                        print("Ahora tiene ", self.meat, " libras de carne disponibles")
                    elif collect == 4:
                        collect_fur = int(input("Ingrese cuantos metros^2 de piel desea recoger: "))
                        self.fur -= collect_fur
                        print("Ahora tiene ", self.fur, " metros^2 de piel disponibles")


            class Cows(AnimalCare):
                def __init__(self, number, healt=50, happiness=50, hunger=50, breeding=0, milk=0, meat=0, fur=0,
                             horns=0):
                    super().__init__(healt, happiness, hunger, breeding, milk)
                    self.meat = meat
                    self.fur = fur
                    self.horns = horns
                    self.number = number

                def data_entry(self):
                    print(f"La salud de su vaca {self.number} es: ", self.healt)
                    print(f"la felicidad de su vaca {self.number} es: ", self.happiness)
                    print(f"El hambre de su vaca {self.number} es: ", self.hunger)
                    self.breeding = int(input("Ingrese cuantas crias ha tenido su vaca: "))
                    self.milk = int(input("Ingrese cuantos litros de leche ha producido su vaca: "))
                    self.meat = int(input("Ingrese cuantas libras de carne puede generar su vaca: "))
                    self.fur = int(input("Ingrese cuantas m^2 de piel puede generar su vaca: "))
                    self.horns = int(input("Ingrese cuantos cuernos de vaca tiene: "))

                def data_entry_return(self):
                    return "vida:", self.healt, "Felicidad", self.happiness, "Hambre:", self.hunger, "Crías", self.breeding, "Leche:", self.milk, "Carne:", self.meat, "Pelage:", self.fur, "Cuernos:", self.horns

                def collect_resources(self):
                    print("Recursos disponibles: ")
                    print("1. Su animal tiene ", self.breeding, " crias")
                    print("2. Su animal ha producido ", self.milk, " litros de leche")
                    print("3. Su animal puede generar ", self.meat, " libras de carne")
                    print("4. Su animal puede gener", self.fur, " metros^2 de piel")
                    print("5. Tiene en posecion ", self.horns, " cuernos")
                    collect = int(input("Ingrese que desea recoger: "))
                    if collect == 1:
                        collet_breeding = int(input("Ingrese cuantas crias desea recoger: "))
                        self.breeding -= collet_breeding
                        print("Ahora tiene ", self.breeding, " crias")
                    elif collect == 2:
                        collect_milk = int(input("Ingrese cuantos litros de leche desea recoger: "))
                        self.milk -= collect_milk
                        print("Ahora tiene ", self.milk, " litros de leche disponibles")
                    elif collect == 3:
                        collect_meat = int(input("Ingrese cuentas libras de carne desea recoger: "))
                        self.meat -= collect_meat
                        print("Ahora tiene ", self.meat, " libras de carne disponibles")
                    elif collect == 4:
                        collect_fur = int(input("Ingrese cuantos metros^2 de piel desea recoger: "))
                        self.fur -= collect_fur
                        print("Ahora tiene ", self.fur, " metros^2 de piel disponibles ")
                    elif collect == 5:
                        collect_horns = int(input("Ingrese cuantos cuernos desea recoger: "))
                        self.horns -= collect_horns
                        print("Ahora tiene ", self.horns, " cuenros a disposicion")


            class Sheep(AnimalCare):
                def __init__(self, number, healt=50, happiness=50, hunger=50, breeding=0, milk=0, meat=0, wool=0):
                    super().__init__(healt, happiness, hunger, breeding, milk)
                    self.meat = meat
                    self.wool = wool
                    self.number = number

                def data_entry(self):
                    print(f"La salud de su {self.number} oveja es: ", self.healt)
                    print(f"la felicidad de su {self.number} oveja es: ", self.happiness)
                    print(f"El hambre de su {self.number} oveja es: ", self.hunger)
                    self.breeding = int(input("Ingrese cuantas crias ha tenido su oveja: "))
                    self.milk = int(input("Ingrese cuantos litros de leche ha producido su oveja: "))
                    self.meat = int(input("Ingrese cuantas libras de carne puede generar su oveja: "))
                    self.fur = int(input("Ingrese la cantidad de libras de lana que puede generar su oveja "))

                def data_entry_return(self):
                    return self.healt, self.happiness, self.hunger, self.breeding, self.milk, self.meat, self.fur

                def collect_resources(self):
                    print("Recursos disponibles: ")
                    print("1. Su animal tiene ", self.breeding, " crias")
                    print("2. Su animal ha producido ", self.milk, " litros de leche")
                    print("3. Su animal puede generar ", self.meat, " libras de carne")
                    print("4. Su animal puede gener", self.fur, " metros^2 de piel")
                    print("5. Tiene en posecion ", self.wool, " libras de lana")
                    collect = int(input("Ingrese que desea recoger: "))
                    if collect == 1:
                        collet_breeding = int(input("Ingrese cuantas crias desea recoger: "))
                        self.breeding -= collet_breeding
                        print("Ahora tiene ", self.breeding, " crias")
                    elif collect == 2:
                        collect_milk = int(input("Ingrese cuantos litros de leche desea recoger: "))
                        self.milk -= collect_milk
                        print("Ahora tiene ", self.milk, " litros de leche disponibles")
                    elif collect == 3:
                        collect_meat = int(input("Ingrese cuantas libras de carne desea recoger: "))
                        self.meat -= collect_meat
                        print("Ahora tiene ", self.meat, " libras de carne disponibles")
                    elif collect == 4:
                        collect_fur = int(input("Ingrese cuantos metros^2 de piel desea recoger: "))
                        self.fur -= collect_fur
                        print("Ahora tiene ", self.fur, " metros^2 de piel disponivles ")
                    elif collect == 5:
                        collect_wool = int(input("Ingrese cuantas libras de lana desea recoger: "))
                        self.wool -= collect_wool
                        print("Ahora tiene ", self.wool, " libras de lana disponibles")


            def pasar_tiempo(y):
                while True:
                    for i in y:
                        i.hunger += 10
                        i.healt -= 5
                        i.happiness -=5
                    time.sleep(60)  # Esperar 2 segundos entre actualizaciones


            print("\033[1;38;2;255;164;6mAnimales  :)\033[0m")
            print("\033[1;38;2;255;210;27m1. Ingreso de animales\033[0m")
            print("\033[1;38;2;6;255;255m2. Interactuar con animales\033[0m")
            act_entry = int(input("\033[1;38;2;6;255;119mIngrese que desea realizar: \033[0m"))
            tiempo_thread1 = threading.Thread(target=pasar_tiempo, args=(COW,))
            tiempo_thread2 = threading.Thread(target=pasar_tiempo, args=(SHEEP,))
            tiempo_thread3 = threading.Thread(target=pasar_tiempo, args=(PIG,))
            tiempo_thread1.daemon = True
            tiempo_thread2.daemon = True
            tiempo_thread3.daemon = True
            tiempo_thread1.start()
            tiempo_thread2.start()
            tiempo_thread3.start()
            while act_entry >= 1 and act_entry <= 2:
                if act_entry == 1:
                    print("1. Cerdos")
                    print("2. Vacas")
                    print("3. Ovejas")
                    chosen_animal = int(input("Seleccione que animal desea ingresar: "))
                    if chosen_animal == 1:
                        number_pig = inventory_7[0]
                        n = 1
                        print("Usted tiene:", number_pig, "cerdos")
                        if number_pig > 0:
                            while n <= number_pig:
                                print(f"Cerdo número: {n}")
                                pig1 = Pigs(n)
                                pig1.data_entry()
                                PIG.append(pig1)
                                n += 1
                            break
                        print("No tiene cerdos actualmente")
                    elif chosen_animal == 2:
                        number_cow = inventory_5[0]
                        n = 1
                        print("Usted tiene:", number_cow, "vacas")
                        if number_cow > 0:
                            while n <= number_cow:
                                print(f"Vaca número: {n}")
                                cow1 = Cows(n)
                                cow1.data_entry()
                                COW.append(cow1)
                                n += 1
                            break
                        print("No tiene vacas actualmente")
                    elif chosen_animal == 3:
                        number_sheep = inventory_6[0]
                        n = 1
                        print("Usted tiene:", number_sheep, "ovejas")
                        if number_sheep > 0:
                            while n <= number_sheep:
                                print(f"Oveja número: {n}")
                                sheep1 = Sheep(n)
                                sheep1.data_entry()
                                SHEEP.append(sheep1)
                                n += 1
                            break
                        print("No tiene ovejas actualmente")
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
                                print("Tienes", number_pig)
                                pigNumber_get = int(input("Ingrese el número del animal que desea alimentar: "))
                                for x in PIG:
                                    if x.number == pigNumber_get:
                                        print(f"Atributos del cerdo {pigNumber_get}")
                                        print(x.data_entry_return())
                                        x.feed()
                                        break
                            elif act == 2:
                                print("Tienes", number_pig)
                                pigNumber_get = int(input("Ingrese el número del animal que desea acariciar: "))
                                for x in PIG:
                                    if x.number == pigNumber_get:
                                        print(f"Atributos del cerdo {pigNumber_get}")
                                        print(x.data_entry_return())
                                        x.strock()
                                        break
                            elif act == 3:
                                print("Tienes", number_pig)
                                pigNumber_get = int(input("Ingrese el número del animal que desea limpiar: "))
                                for x in PIG:
                                    if x.number == pigNumber_get:
                                        print(f"Atributos del cerdo {pigNumber_get}")
                                        print(x.data_entry_return())
                                        x.clean()
                                        break
                        if select_animal == 2:
                            print("Acciones: ")
                            print("1. Alimentar")
                            print("2. Acariciar")
                            print("3. Limpiar")
                            act = int(input("Ingrese que acción desea realizar: "))
                            if act == 1:
                                print("Tienes", number_cow, "vacas")
                                cowNumber_get = int(input("Ingrese el número del animal que desea alimentar: "))
                                for x in COW:
                                    if x.number == cowNumber_get:
                                        print(f"Atributos de la vaca {cowNumber_get}")
                                        print(x.data_entry_return())
                                        x.feed()
                                        break
                            elif act == 2:
                                print("Tienes", number_cow, "vacas")
                                cowNumber_get = int(input("Ingrese el número del animal que desea acariciar: "))
                                for x in COW:
                                    if x.number == cowNumber_get:
                                        print(f"Atributos de la vaca {cowNumber_get}")
                                        print(x.data_entry_return())
                                        x.strock()
                                        break
                            elif act == 3:
                                print("Tienes", number_cow, "vacas")
                                cowNumber_get = int(input("Ingrese el número del animal que desea limpiar: "))
                                for x in COW:
                                    if x.number == cowNumber_get:
                                        print(f"Atributos de la vaca {cowNumber_get}")
                                        print(x.data_entry_return())
                                        x.clean()
                                        break
                        if select_animal == 3:
                            print("Acciones: ")
                            print("1. Alimentar")
                            print("2. Acariciar")
                            print("3. Limpiar")
                            act = int(input("Ingrese que acción desea realizar: "))
                            if act == 1:
                                print("Tienes", number_sheep, "ovejas")
                                sheepNumber_get = int(input("Ingrese el número del animal que desea alimentar: "))
                                for x in SHEEP:
                                    if x.number == sheepNumber_get:
                                        print(f"Atributos de la oveja {sheepNumber_get}")
                                        print(x.data_entry_return())
                                        x.feed()
                                        break
                            elif act == 2:
                                print("Tienes", number_sheep, "ovejas")
                                sheepNumber_get = int(input("Ingrese el número del animal que desea acariciar: "))
                                for x in SHEEP:
                                    if x.number == sheepNumber_get:
                                        print(f"Atributos de la oveja {sheepNumber_get}")
                                        print(x.data_entry_return())
                                        x.strock()
                                        break
                            elif act == 3:
                                print("Tienes", number_sheep, "ovejas")
                                sheepNumber_get = int(input("Ingrese el número del animal que desea limpiar: "))
                                for x in SHEEP:
                                    if x.number == sheepNumber_get:
                                        print(f"Atributos de la oveja {sheepNumber_get}")
                                        print(x.data_entry_return())
                                        x.clean()
                                        break
                    elif select == 2:
                        print("Animales a disposicion: ")
                        print("1. Cerdos")
                        print("2. Vacas")
                        print("3. Ovejas")
                        animal = int(input("Ingrese de que animal desea recolectar recursos: "))
                        if animal == 1:
                            print("Tienes", number_pig, "cerdos")
                            pigNumber_get = int(input("Ingrese el número del animal que desea recolectar recursos: "))
                            for x in PIG:
                                if x.number == pigNumber_get:
                                    print(f"Atributos del cerdo {pigNumber_get}")
                                    print(x.data_entry_return())
                                    x.collect_resources()
                                    break
                        if animal == 2:
                            print("Tienes", number_cow, "vacas")
                            cowNumber_get = int(input("Ingrese el número del animal que desea recolectar recursos: "))
                            for x in COW:
                                if x.number == cowNumber_get:
                                    print(f"Atributos de la vaca {cowNumber_get}")
                                    print(x.data_entry_return())
                                    x.collect_resources()
                                    break
                        if animal == 3:
                            print("Tienes", number_sheep, "ovejas")
                            sheepNumber_get = int(input("Ingrese el número del animal que desea recolectar recursos: "))
                            for x in SHEEP:
                                if x.number == sheepNumber_get:
                                    print(f"Atributos del cerdo {sheepNumber_get}")
                                    print(x.data_entry_return())
                                    x.collect_resources()
                                    break
                break
            Continuar = input("¿Desea continuar con el programa?" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
            if Continuar == "n" or Continuar == "N":
                print("Regresando...")
                break
            opcionA = "A"
    while menu == "B" or menu == "b":
        if menu == "B" or menu == "b":
            import random
            class Crop:
                seeds_available = {
                    "Manzana": inventory_9[0],
                    "Sandía": inventory_10[0],
                    "Zanahoria": inventory_11[0],
                    "Trigo": inventory_12[0],
                    "Maíz": inventory_13[0]}
                fertilizers_available = {
                    "Manzana": inventory_8[0],
                    "Sandía": inventory_8[0],
                    "Zanahoria": inventory_8[0],
                    "Trigo": inventory_8[0],
                    "Maíz": inventory_8[0]}
                treatments_available = {
                    "Manzana": inventory_4[0],
                    "Sandía": inventory_4[0],
                    "Zanahoria": inventory_4[0],
                    "Trigo": inventory_4[0],
                    "Maíz": inventory_4[0]}

                def __init__(self, name):
                    self.name = name
                    self.current_growth = 0
                    self.state = "Brote"
                    self.plague_chance = 0.2
                    self.has_plague = "not plague"

                # Simular el efecto de las plagas
                def apply_plague(self):
                    if random.random() < self.plague_chance:
                        self.has_plague = "plague"

                # Regar (Water)
                def water(self):
                    self.current_growth += 20
                    if self.current_growth <= 40:
                        self.state = "Brote"
                    elif 40 < self.current_growth < 100:
                        self.state = "Crecimiento"
                    elif self.current_growth >= 100 and self.has_plague == "not plague":
                        self.state = "Maduración"
                    elif self.current_growth >= 100 and self.has_plague == "plague":
                        self.state = "Plagas"
                    self.apply_plague()

                # Fertilizar (Fertilize)
                def fertilize(self):
                    if self.fertilizers_available.get(self.name, 0) > 0:
                        self.current_growth += 50
                        self.fertilizers_available[self.name] -= 1
                        if self.current_growth <= 40:
                            self.state = "Brote"
                        elif 40 < self.current_growth < 100:
                            self.state = "Crecimiento"
                        elif self.current_growth >= 100 and self.has_plague == "not plague":
                            self.state = "Maduración"
                        elif self.current_growth >= 100 and self.has_plague == "plague":
                            self.state = "Plagas"
                        self.apply_plague()
                        print("Has fertilizado el cultivo de ",self.name)
                    else:
                        print("No quedan fertilizantes disponibles para el cultivo de ",self.name)

                # Cosechar (Harvest)
                def harvest(self):
                    if self.current_growth >= 100 and self.has_plague == "not plague":
                        self.state = "Cosechado"
                        return True
                    else:
                        if self.current_growth >= 100 and self.has_plague == "plague":
                            self.state = "Plagas"
                        else:
                            self.state = "Aún no está listo para cosechar"
                        self.apply_plague()
                        return False

                def plant_seed(cls, name):
                    # Verifica si hay semillas disponibles para el tipo de cultivo
                    if cls.seeds_available.get(name, 0) > 0:
                        cls.seeds_available[name] -= 1
                        return True
                    else:
                        return False

                # Curar las plagas
                def cure_plague(self):
                    if self.treatments_available.get(self.name, 0) > 0:
                        self.has_plague = "not plague"
                        if self.current_growth >= 100:
                            self.state = "Maduración"
                        self.treatments_available[self.name] -= 1
                        print("Has curado las plagas en el cultivo de",self.name)
                    else:
                        print("No quedan tratamientos disponibles para el cultivo de ",self.name)

            class Apple(Crop):
                def __init__(self):
                    super().__init__("Manzana")


            class Watermelon(Crop):
                def __init__(self):
                    super().__init__("Sandía")


            class Carrot(Crop):
                def __init__(self):
                    super().__init__("Zanahoria")


            class Wheat(Crop):
                def __init__(self):
                    super().__init__("Trigo")


            class Corn(Crop):
                def __init__(self):
                    super().__init__("Maíz")


            class Soil:
                def __init__(self):
                    self.crops = []

                # Plantar en suelo (Plant in soil)
                def plant(self, crop):
                    # Verifica si hay semillas disponibles antes de plantar
                    if crop.plant_seed(crop.name):
                        self.crops.append(crop)
                        print("Has plantado un/una", crop.name)
                    else:
                        print("No quedan semillas disponibles para", crop.name)

                # Regar en suelo (Water in soil)
                def water_crop(self, position):
                    self.crops[position].water()

                # Fertilizar en suelo (Fertilize in soil)
                def fertilize_crop(self, position):
                    self.crops[position].fertilize()

                # Cosechar en suelo (Harvest in soil)
                def harvest_crop(self, position):
                    return self.crops[position].harvest()

                # Curar un cultivo con plagas
                def cure_crop(self, position):
                    self.crops[position].cure_plague()


            class Menu:
                def __init__(self):
                    self.soil = Soil()

                def crop_type(self):
                    print("///Tipos de cultivos///")
                    print("1. Manzana")  # Apple
                    print("2. Sandía")  # Watermelon
                    print("3. Zanahoria")  # Carrot
                    print("4. Trigo")  # Wheat
                    print("5. Maíz")  # Corn

                def show_crops(self):
                    if len(self.soil.crops) == 0:
                        print("No hay cultivos en el suelo.")
                    else:
                        print("Cultivos en el suelo:")
                        position = 0
                        for crop in self.soil.crops:
                            print(position, ".", crop.name, "- Estado:", crop.state)
                            position += 1

                def menu(self):
                    print("///MENÚ///")
                    print("Bienvenido al sistema de cultivo.")
                    print("1. Plantar un nuevo cultivo")
                    print("2. Regar un cultivo")
                    print("3. Fertilizar un cultivo")
                    print("4. Cosechar un cultivo")
                    print("5. Mostrar estado de cultivos")
                    print("6. Curar plagas en un cultivo")
                    print("7. Salir")
                    option = int(input("Ingrese su opción: "))
                    while option != 7:

                        if option == 1:
                            self.crop_type()
                            type_choice = int(input("Ingrese el número del tipo de cultivo que desea sembrar: "))
                            if 1 <= type_choice <= 5:
                                if type_choice == 1:
                                    crop = Apple()
                                elif type_choice == 2:
                                    crop = Watermelon()
                                elif type_choice == 3:
                                    crop = Carrot()
                                elif type_choice == 4:
                                    crop = Wheat()
                                elif type_choice == 5:
                                    crop = Corn()

                                self.soil.plant(crop)
                            else:
                                print("Opción no válida.")

                        elif option == 2:
                            if len(self.soil.crops) == 0:
                                print("No hay cultivos para regar.")
                            else:
                                self.show_crops()
                                position = int(input("Ingrese la posición del cultivo que desea regar: "))
                                if 0 <= position < len(self.soil.crops):
                                    self.soil.water_crop(position)
                                    print("Has regado el cultivo en la posición ", position)
                                else:
                                    print("Posición no válida.")

                        elif option == 3:
                            if len(self.soil.crops) == 0:
                                print("No hay cultivos para fertilizar.")
                            else:
                                self.show_crops()
                                position = int(input("Ingrese la posición del cultivo que desea fertilizar: "))
                                if 0 <= position < len(self.soil.crops):
                                    self.soil.fertilize_crop(position)
                                else:
                                    print("Posición no válida.")

                        elif option == 4:
                            if len(self.soil.crops) == 0:
                                print("No hay cultivos para cosechar.")
                            else:
                                self.show_crops()
                                position = int(input("Ingrese la posición del cultivo que desea cosechar: "))
                                if 0 <= position < len(self.soil.crops):
                                    if self.soil.harvest_crop(position):
                                        print("Has cosechado el cultivo en la posición", position)
                                        del self.soil.crops[position]
                                    else:
                                        print("El cultivo no está listo para cosechar.")
                                else:
                                    print("Posición no válida.")

                        elif option == 5:
                            self.show_crops()

                        elif option == 6:
                            if len(self.soil.crops) == 0:
                                print("No hay cultivos para curar de plagas.")
                            else:
                                self.show_crops()
                                position = int(input("Ingrese la posición del cultivo que desea curar de plagas: "))
                                if 0 <= position < len(self.soil.crops):
                                    self.soil.cure_crop(position)
                                else:
                                    print("Posición no válida.")

                        else:
                            print("Opción no válida")
                        print("///MENÚ///")
                        print("Bienvenido al sistema de cultivo.")
                        print("1. Plantar un nuevo cultivo")
                        print("2. Regar un cultivo")
                        print("3. Fertilizar un cultivo")
                        print("4. Cosechar un cultivo")
                        print("5. Mostrar estado de cultivos")
                        print("6. Curar plagas en un cultivo")
                        print("7. Salir")
                        option = int(input("Ingrese su opción: "))

                    print("Saliendo del programa")


            menu1 = Menu()
            menu1.menu()
        Continuar = input("¿Desea continuar con el programa?" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
        if Continuar == "n" or Continuar == "N":
            print("Regresando...")
            break
        opcionB = "B"
    while menu == "C" or menu == "c": #**********Allan**********
        if menu == "C" or menu == "c":
            optionE = input("\033[1;38;2;255;54;0mTi\033[1;0m" + "en" + "\033[1;38;2;255;54;0mda:\033[0m\n"+"\033[1;38;2;178;250;0mA. Comprar\033[0;m\n"+"B. Vender\n"+"Elija su opción: ")
            while optionE == "A" or optionE == "a":
                if optionE == "A" or optionE == "a":
                    print("\033[1;38;2;255;54;0mTi\033[1;0m" + "en" + "\033[1;38;2;255;54;0mda:\033[0m")
                    while True:
                        print("\033[1;38;2;23;252;248mActualmente tienes:\033[0m", WALLET, "Monedas")
                        menu = input("\033[1;38;2;255;54;0mProductos \033[1;38;2;255;165;00m" + "disponibles:\033[0m\n"+"\033[1;38;2;255;240;1mA. Compuesto para Vaca\033[0m\n"
                        "\033[1;38;2;51;214;243mB. Compuesto para Oveja \033[0;m\n"+"\033[1;38;2;209;0;255mC. Compuesto para Cerdo\033[0;m\n" + "\033[1;38;2;244;155;0mD. Vaca\033[0m\n"
                        "\033[1;38;2;255;224;0mE. Oveja \033[0;m\n" + "\033[1;38;2;227;10;96mF. Cerdo\033[0;m\n"+"\033[1;38;2;180;255;71mG. Fertilizante\033[0;m\n" + "\033[1;38;2;255;185;71mH. Antiplagas\033[0;m\n"
                        "\033[1;38;2;25;238;187mI. Semillas de manzana\033[0;m\n" + "\033[1;38;2;25;238;187mJ. Semillas de sandía\033[0;m\n" + "\033[1;38;2;25;238;187mK. Semillas de zanahoria\033[0;m\n"
                        "\033[1;38;2;25;238;187mL. Trigo\033[0;m\n" + "\033[1;38;2;25;238;187mM. Maíz\033[0;m\n" +"\033[1;38;2;25;238;187mN. Granero\033[0;m\n"
                        "\033[1;38;2;215;0;0mO. Salir de la tienda\033[0;m\n"+"\033[1;38;2;50;205;50mElija su opción: \033[0;m")
                        while menu == "A" or menu == "a":
                            if menu == "A" or menu == "a":
                                COST = 5
                                print("\033[1;38;2;216;98;55mCompuesto para Vaca; \033[0m" + "\033[1;38;2;254;214;90mCuesta $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_COW_FOOD = GET_COW_FOOD + total
                                inventory_1[0] = GET_COW_FOOD
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "B" or menu == "b":
                            if menu == "B" or menu == "b":
                                COST = 3
                                print("\033[1;38;2;255;224;0mCompuesto para Oveja; \033[0m" + "\033[1;38;2;254;214;90mCuesta $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_FOOD_SHEEP = GET_FOOD_SHEEP + total
                                inventory_2[0] = GET_FOOD_SHEEP
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "C" or menu == "c":
                            if menu == "C" or menu == "c":
                                COST = 4
                                print("\033[1;38;2;255;0;255mCompuesto para Cerdo; \033[0m" + "\033[1;38;2;254;214;90mCuesta $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_PIG_FOOD = GET_PIG_FOOD + total
                                inventory_3[0] = GET_PIG_FOOD
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "D" or menu == "d":
                            if menu == "D" or menu == "d":
                                COST = 8
                                print("\033[1;38;2;255;0;255mVacas; \033[0m" + "\033[1;38;2;254;214;90mCuestan $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_COW = GET_COW + total
                                inventory_5[0] = GET_COW
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "E" or menu == "e":
                            if menu == "E" or menu == "e":
                                COST = 7
                                print("\033[1;38;2;255;0;255mOvejas; \033[0m" + "\033[1;38;2;254;214;90mCuestan $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_SHEEP = GET_SHEEP + total
                                inventory_6[0] = GET_SHEEP
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "F" or menu == "f":
                            if menu == "F" or menu == "f":
                                COST = 8
                                print("\033[1;38;2;255;0;255mCerdos; \033[0m" + "\033[1;38;2;254;214;90mCuestan $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_PIG = GET_PIG + total
                                inventory_7[0] = GET_PIG
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "G" or menu == "g":
                            if menu == "G" or menu == "g":
                                COST = 3
                                print("\033[1;38;2;255;0;255mFertilizante; \033[0m" + "\033[1;38;2;254;214;90mCuestan $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_FERTILIZER = GET_FERTILIZER + total
                                inventory_8[0] = GET_FERTILIZER
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "H" or menu == "h":
                            if menu == "H" or menu == "h":
                                COST = 2
                                print("\033[1;38;2;181;221;19mAntiplagas; \033[0m" + "\033[1;38;2;254;214;90mCuesta $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_ANTI_PEST = GET_ANTI_PEST + total
                                inventory_4[0] = GET_ANTI_PEST
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "I" or menu == "i":
                            if menu == "I" or menu == "i":
                                COST = 1
                                print("\033[1;38;2;181;221;19mManzanas; \033[0m" + "\033[1;38;2;254;214;90mCuesta $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_APPLE = GET_APPLE + total
                                inventory_9[0] = GET_APPLE
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "J" or menu == "j":
                            if menu == "J" or menu == "j":
                                COST = 3
                                print("\033[1;38;2;181;221;19mSandía; \033[0m" + "\033[1;38;2;254;214;90mCuesta $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_MELON = GET_MELON + total
                                inventory_10[0] = GET_MELON
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "K" or menu == "k":
                            if menu == "K" or menu == "k":
                                COST = 2
                                print("\033[1;38;2;181;221;19mZanahora; \033[0m" + "\033[1;38;2;254;214;90mCuesta $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_CARROT = GET_CARROT + total
                                inventory_11[0] = GET_CARROT
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "L" or menu == "l":
                            if menu == "L" or menu == "l":
                                COST = 3
                                print("\033[1;38;2;181;221;19mTrigo; \033[0m" + "\033[1;38;2;254;214;90mCuesta $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_WHEAT = GET_WHEAT + total
                                inventory_12[0] = GET_WHEAT
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "M" or menu == "m":
                            if menu == "M" or menu == "m":
                                COST = 1
                                print("\033[1;38;2;181;221;19mMaíz; \033[0m" + "\033[1;38;2;254;214;90mCuesta $\033[0;m",COST)
                                buy = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                                if buy == "s" or buy == "S":
                                    total = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                                    price = total * COST
                                    if WALLET >= price:
                                        WALLET = WALLET - price
                                        print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                                GET_CORN = GET_CORN + total
                                inventory_13[0] = GET_CORN
                                break
                                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                            break
                        while menu == "N" or menu == "n":
                            if menu == "N" or menu == "n":
                                print("\033[1;38;2;23;252;248mActualmente tienes:\033[0m", WALLET, "Monedas")
                                LINE = 4
                                for i, objects in enumerate(BARN):
                                    if i % LINE == 0 and i != 0:
                                        print()
                                    print(objects, end="\t")
                                print()
                            break
                        continue_end = input("\033[1;38;2;178;250;0m¿Desea seguir en la Tienda?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
                        if continue_end == "n" or continue_end == "N":
                            print("\033[1;38;2;255;54;0mSaliendo de la Tienda...\033[0m\n")
                            break
                break
            while optionE == "B" or optionE == "b":
                if optionE == "B" or optionE == "b":
                    print("")
                break
        continue_end = input("\033[1;38;2;218;206;35m¿Desea regresar al menú de inicio?\033[0;m\n" + "\033[1;32mS\033[0;m" + "/" + "\033[1;31mN: \033[0;m")
        if continue_end == "s" or continue_end == "S":
            print("\033[1;38;2;255;54;0mRegresando...\033[0m\n")
            break
        menu = "E"
