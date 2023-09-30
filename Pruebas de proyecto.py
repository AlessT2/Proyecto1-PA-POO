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
        return self.healt, self.happiness, self.hunger,self.breeding, self.milk, self.meat, self.fur

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
    def __init__(self, number, healt=50, happiness=50, hunger=50, breeding=0, milk=0, meat=0, fur=0,horns=0):
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
        return "vida:",self.healt, "Felicidad",self.happiness, "Hambre:",self.hunger, "Crías",self.breeding, "Leche:",self.milk, "Carne:",self.meat, "Pelage:",self.fur, "Cuernos:",self.horns
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
        return self.healt, self.happiness, self.hunger,self.breeding, self.milk, self.meat, self.fur
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
            i.healt -= 5  # Ejemplo: la vida disminuye con el tiempo
        time.sleep(2)  # Esperar 2 segundos entre actualizaciones

print("\033[1;38;2;255;164;6mAnimales  :)\033[0m")
print("\033[1;38;2;255;210;27m1. Ingreso de animales\033[0m")
print("\033[1;38;2;6;255;255m2. Interactuar con animales\033[0m")
act_entry = int(input("\033[1;38;2;6;255;119mIngrese que desea realizar: \033[0m"))
tiempo_thread1 = threading.Thread(target=pasar_tiempo,args=(COW,))
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
            print("Usted tiene:",number_pig,"cerdos")
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
                    print("Tienes",number_pig)
                    pigNumber_get = int(input("Ingrese el número del animal que desea alimentar: "))
                    for x in PIG:
                        if x.number == pigNumber_get:
                            print(f"Atributos del cerdo {pigNumber_get}")
                            print(x.data_entry_return())
                            x.feed()
                            break
                elif act == 2:
                    print("Tienes",number_pig)
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
                    print("Tienes", number_cow,"vacas")
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
                    print("Tienes", number_cow,"vacas")
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