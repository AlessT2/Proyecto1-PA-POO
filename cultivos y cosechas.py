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

class Manzana(Crop):
    def __init__(self):
        super().__init__("Manzana")

class Sandia(Crop):
    def __init__(self):
        super().__init__("Sandía")

class Zanahoria(Crop):
    def __init__(self):
        super().__init__("Zanahoria")

class Trigo(Crop):
    def __init__(self):
        super().__init__("Trigo")

class Maiz(Crop):
    def __init__(self):
        super().__init__("Maíz")
   
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

    def mostrar_cultivos(self):
        if len(self.suelo.cultivos) == 0:
            print("No hay cultivos en el suelo.")
        else:
            print("Cultivos en el suelo:")
            posicion = 0
            for cultivo in self.suelo.cultivos:
                print(posicion, ".", cultivo.nombre, "- Estado:", cultivo.estado)
                posicion += 1

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
        while opcion != 6:
            
            if opcion == 1:
                self.tipo_cultivo()
                tipo = int(input("Ingrese el número del tipo de cultivo que desea sembrar: "))
                if 1 <= tipo <= 5:
                    if tipo == 1:
                        cultivo = Manzana()
                    elif tipo == 2:
                        cultivo = Sandia()
                    elif tipo == 3:
                        cultivo = Zanahoria()
                    elif tipo == 4:
                        cultivo = Trigo()
                    elif tipo == 5:
                        cultivo = Maiz()
                    
                    self.suelo.plantar(cultivo)
                    print("Has plantado un/una", cultivo.nombre)
                else:
                    print("Opción no válida.")
                    
            elif opcion == 2:
                if len(self.suelo.cultivos) == 0:
                    print("No hay cultivos para regar.")
                else:
                    self.mostrar_cultivos()
                    posicion = int(input("Ingrese la posición del cultivo que desea regar: "))
                    if 0 <= posicion < len(self.suelo.cultivos):
                        self.suelo.regarC(posicion)
                        print("Ha regado el cultivo en la posición ", posicion)
                    else:
                        print("Posición no válida.")
        
            elif opcion == 3:
                if len(self.suelo.cultivos) == 0:
                    print("No hay cultivos para fertilizar.")
                else:
                    self.mostrar_cultivos()
                    posicion = int(input("Ingrese la posición del cultivo que desea fertilizar: "))
                    if 0 <= posicion < len(self.suelo.cultivos):
                        self.suelo.fertilizarC(posicion)
                        print("Ha fertilizado el cultivo en la posición ", posicion)
                    else:
                        print("Posición no válida.")
                        
            elif opcion == 4:
                if len(self.suelo.cultivos) == 0:
                    print("No hay cultivos para cosechar.")
                else:
                    self.mostrar_cultivos()
                    posicion = int(input("Ingrese la posición del cultivo que desea cosechar: "))
                    if 0 <= posicion < len(self.suelo.cultivos):
                        if self.suelo.cosecharC(posicion):
                            print("Ha cosechado el cultivo en la posición", posicion)
                            del self.suelo.cultivos[posicion]
                        else:
                            print("El cultivo no está listo para cosechar.")
                    else:
                        print("Posición no válida.")
                        
            elif opcion == 5:
                self.mostrar_cultivos()

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
            opcion = int(input("Ingrese su opción: "))

        print("Saliendo del programa")
        
    
menu1 = Menu()
menu1.menu()