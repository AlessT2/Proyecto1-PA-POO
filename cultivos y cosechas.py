class Crop:
    def __init__(self):
        self.crecimiento_actual = 0
    def tipo_cultivo(self):
        print("///Tipos de cultivos///")
        print("1. Manzana") #Apple
        print("2. Sandía") #Watermelon
        print("3. Zanahoria") #Carrot
        print("4. Trigo") #Wheat
        print("5. Maíz") #Corn
        self.nombre = input("Ingrese el tipo de cultivo que quiere sembrar: ")
    #regar   
    def regar(self):
        self.crecimiento_actual + 20
    #etapas    
    def etapas(self):
        if 0 <= self.crecimiento_actual >= 40:
            print("Brote")
            
        elif 40 < self.crecimiento_actual > 100:
            print("Crecimiento")
        
        elif self.crecimiento_actual >= 100:
            print("Maduración")
    #fertilizacion        
    def fertilizacion(self):
        self.crecimiento_actual + 50
    #cosechar    
    def cosechar(self):
        if self.crecimiento_actual >= 100:
            print("Cosechado")
        else:
            return print("Aún no está listo para cosechar")
            
class Suelo:
    def __init__(self):
        self.cultivos = []
    #plantarSuelo    
    def plantar(self, cultivo):
        self.cultivos.append(cultivo)
    #regarSuelo    
    def regarC(self, posicion):
        self.cultivos[posicion].regar()
    #cosecharSuelo    
    def cosecharC(self, posicion):
        self.cultivos[posicion].cosechar()
suelo = Suelo()

class Menu:
    def __init__(self):
        self.inventario = []
        
    def menu(self):
        print("///MENÚ///")
        print("Bienvenido al sistema de cultivo. Por favor, selecciona una opción:")
        print("1. Plantar un nuevo cultivo")
        print("2. Regar un cultivo")
        print("3. Cosechar un cultivo")
        print("4. Salir")
        opcion = int(input("Ingrese su opción: "))
        while opcion != 4:
            if opcion == 1:
                self.crear_cultivo()

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
        
    def crear_cultivo(self):
        crop1 = Crop()
        crop1.tipo_cultivo()
    
    
menu1 = Menu()
menu1.menu()