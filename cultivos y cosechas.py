class Crop:
    def __init__(self, name):
        self.name = name
        self.current_growth = 0
        self.state = "Brote"

    # Regar (Water)
    def water(self):
        self.current_growth += 20
        if self.current_growth <= 40:
            self.state = "Brote"
        elif 40 < self.current_growth < 100:
            self.state = "Crecimiento"
        elif self.current_growth >= 100:
            self.state = "Maduración"

    # Fertilizar (Fertilize)
    def fertilize(self):
        self.current_growth += 50
        if self.current_growth <= 40:
            self.state = "Brote"
        elif 40 < self.current_growth < 100:
            self.state = "Crecimiento"
        elif self.current_growth >= 100:
            self.state = "Maduración"

    # Cosechar (Harvest)
    def harvest(self):
        if self.current_growth >= 100:
            self.state = "Cosechado"
            return True
        else:
            self.state = "Aún no está listo para cosechar"
            return False

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
        self.crops.append(crop)

    # Regar en suelo (Water in soil)
    def water_crop(self, position):
        self.crops[position].water()

    # Fertilizar en suelo (Fertilize in soil)
    def fertilize_crop(self, position):
        self.crops[position].fertilize()

    # Cosechar en suelo (Harvest in soil)
    def harvest_crop(self, position):
        return self.crops[position].harvest()

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
            print("cultivos en el suelo:")
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
        print("6. Salir")
        option = int(input("Ingrese su opción: "))
        while option != 6:

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
                    print("Has plantado un/una", crop.name)
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
                        print("Ha regado el cultivo en la posición ", position)
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
                        print("Ha fertilizado el cultivo en la posición ", position)
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
                            print("Ha cosechado el cultivo en la posición", position)
                            del self.soil.crops[position]
                        else:
                            print("El cultivo no está listo para cosechar.")
                    else:
                        print("Posición no válida.")

            elif option == 5:
                self.show_crops()

            else:
                print("Opción no válida")
            print("///MENÚ///")
            print("Bienvenido al sistema de cultivo.")
            print("1. Plantar un nuevo cultivo")
            print("2. Regar un cultivo")
            print("3. Fertilizar un cultivo")
            print("4. Cosechar un cultivo")
            print("5. Mostrar estado de cultivos")
            print("6. Salir")
            option = int(input("Ingrese su opción: "))

        print("Saliendo del programa")

menu1 = Menu()
menu1.menu()