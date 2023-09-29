class Crop:
    def __init__(self, nombre):
        self.nombre = nombre
        self.crecimiento_actual = 0
        self.estado = "Brote"
    #regar
    def regar(self):
        self.crecimiento_actual += 20
        if self.crecimiento_actual <= 40:
            self.estado = "Brote"
        elif 40 < self.crecimiento_actual < 100:
            self.estado = "Crecimiento"
        elif self.crecimiento_actual >= 100:
            self.estado = "Maduración"
    #fertilizar
    def fertilizar(self):
        self.crecimiento_actual += 50
        if self.crecimiento_actual <= 40:
            self.estado = "Brote"
        elif 40 < self.crecimiento_actual < 100:
            self.estado = "Crecimiento"
        elif self.crecimiento_actual >= 100:
            self.estado = "Maduración"
    #cosechar
    def cosechar(self):
        if self.crecimiento_actual >= 100:
            self.estado = "Cosechado"
            return True
        else:
            self.estado = "Aún no está listo para cosechar"
            return False
   
class Suelo:
    def __init__(self):
        self.cultivos = []
    #plantarSuelo    
    def plantar(self, cultivo):
        self.cultivos.append(cultivo)
    #regarSuelo    
    def regarC(self, posicion):
        self.cultivos[posicion].regar()
    #fertilizarSuelo
    def fertilizarC(self, posicion):
        self.cultivos[posicion].fertilizar()    
    #cosecharSuelo    
    def cosecharC(self, posicion):
        return self.cultivos[posicion].cosechar()

class Menu:
    def __init__(self):
        self.suelo = Suelo()
        
    def tipo_cultivo(self):
        print("///Tipos de cultivos///")
        print("1. Manzana") #Apple
        print("2. Sandía") #Watermelon
        print("3. Zanahoria") #Carrot
        print("4. Trigo") #Wheat
        print("5. Maíz") #Corn    

    def menu(self):
        print("///MENÚ///")
        print("Bienvenido al sistema de cultivo.")
        print("1. Plantar un nuevo cultivo")
        print("2. Regar un cultivo")
        print("3. Fertilizar un cultivo")
        print("4. Cosechar un cultivo")
        print("5. Mostrar estado de cultivos")
        print("6. Salir")
        opcion = int(input("Ingrese su opción: "))
        while opcion != 4:
            if opcion == 1:
                self.tipo_cultivo()
                tipo = int(input("Ingrese el número del tipo de cultivo que desea sembrar: "))
                if 1 <= tipo <= 5:
                    if tipo == 1:
                        nombre_cultivo = "Manzana"
                        cultivo = Crop(nombre_cultivo)
                        self.suelo.plantar(cultivo)
                        print("Has plantado un/una", cultivo.nombre)
                    elif tipo == 2:
                        nombre_cultivo = "Sandía"
                        cultivo = Crop(nombre_cultivo)
                        self.suelo.plantar(cultivo)
                        print("Has plantado un/una", cultivo.nombre)
                    elif tipo == 3:
                        nombre_cultivo = "Zanahoria"
                        cultivo = Crop(nombre_cultivo)
                        self.suelo.plantar(cultivo)
                        print("Has plantado un/una", cultivo.nombre)
                    elif tipo == 4:
                        nombre_cultivo = "Trigo"
                        cultivo = Crop(nombre_cultivo)
                        self.suelo.plantar(cultivo)
                        print("Has plantado un/una", cultivo.nombre)
                    elif tipo == 5:
                        nombre_cultivo = "Maíz"
                        cultivo = Crop(nombre_cultivo)
                        self.suelo.plantar(cultivo)
                        print("Has plantado un/una", cultivo.nombre)
                else:
                    print("Opción no válida.")
            elif opcion == 2:
                posicion = int(input("Introduce la posición del cultivo que quieres regar: "))
        
            elif opcion == 3:
                posicion = int(input("Introduce la posición del cultivo que quieres cosechar: "))

            else:
                print("Opción no válida")
            print("///MENÚ///")
            print("Bienvenido al sistema de cultivo. Por favor, selecciona una opción:")
            print("1. Plantar un nuevo cultivo")
            print("2. Regar un cultivo")
            print("3. Cosechar un cultivo")
            print("4. Salir")
            opcion = int(input("Ingrese su opción: "))

        print("Saliendo del programa")
        
    
menu1 = Menu()
menu1.menu()