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