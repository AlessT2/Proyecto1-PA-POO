import time
import threading
inventory_1 = [0, "Compuesto para Vaca"];inventory_2 = [0, "Compuesto para Oveja"];inventory_3 = [0, "Compuesto para Cerdo"];inventory_4 = [0, "Antiplagas"] #INICIA*****ALLAN
inventory_5 = [0, "Vacas"];inventory_6 = [0, "Ovejas"];inventory_7 = [0, "Cerdos"];inventory_8 = [0, "Fertilizantes"];inventory_9 = [0, "Semillas de Manzanas"];inventory_10 = [0, "Semillas deSandías"]
inventory_11 = [0, "Semillas de zanahora"];inventory_12 = [0, "Trigo"];inventory_13 = [0, "Maíz"]; inventory_5_1 = [0, "Leche de vaca"]; inventory_5_2 = [0, "Carne de vaca"]; inventory_5_3 = [0, "Piel de vaca"]; inventory_5_4 = [0, "Cuernos de vaca"]
inventory_6_1 = [0, "Leche de oveja"]; inventory_6_2 = [0, "Carne de oveja"]; inventory_6_3 = [0, "Lana de oveja"];inventory_7_1 = [0, "Leche de cerdo"]; inventory_7_2 = [0, "Carne de cerdo"]; inventory_7_3 = [0, "Piel de cerdo"]
inventory_14 = [0, "Manzanas"]; inventory_15 = [0, "Sandías"]; inventory_16 = [0, "Zanahorias"]; inventory_17 = [0, "Trigo"]; inventory_18 = [0, "Maíz"]
BARN = [inventory_1, inventory_2, inventory_3, inventory_5, inventory_6, inventory_7, inventory_4,inventory_8,inventory_9,inventory_10, inventory_11, inventory_12, inventory_13, inventory_14, inventory_15, inventory_16, inventory_17, inventory_18, inventory_5_1, inventory_5_2, inventory_5_3, inventory_5_4, inventory_6_1, inventory_6_2, inventory_6_3, inventory_7_1, inventory_7_2, inventory_7_3]
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
class Buy(Coin):
    def __init__(self, cost, total, buy, price, name, turned, coin):
        Coin.__init__(self, coin)
        self.cost = cost
        self.buy = "\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m"
        self.price = price
        self.total = "\033[1;38;2;233;255;12m                  ¿Qué cantidad desea comprar? \033[0;m"
        self.name = name
        self.turned = turned

    def Result(self):
        while True:
            global WALLET
            print(f"\033[1;38;2;255;170;0m{self.name} \033[0m" + "\033[1;38;2;243;255;0mCuesta $\033[0;m", self.cost)
            b = input(self.buy)
            if b == "s" or b == "S":
                global f
                t = int(input(self.total))
                f = t
                self.price = t * self.cost
                if WALLET >= self.price:
                    WALLET -= self.price
                    self.turned = print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", WALLET, "Monedas")
                    break
                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
                break
            print("Regresando")
            break


class Product1(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_COW_FOOD
        self.name = "Compuesto para Vaca"
        self.cost = 5
        Buy.Result(self)
        GET_COW_FOOD += f
        inventory_1[0] = GET_COW_FOOD


class Product2(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_FOOD_SHEEP
        self.name = "Compuesto para Oveja"
        self.cost = 5
        Buy.Result(self)
        GET_FOOD_SHEEP += f
        inventory_2[0] = GET_FOOD_SHEEP


class Product3(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_PIG_FOOD
        self.name = "Compuesto para Cerdo"
        self.cost = 5
        Buy.Result(self)
        GET_PIG_FOOD += f
        inventory_3[0] = GET_PIG_FOOD


class Product4(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_ANTI_PEST
        self.name = "Antiplagas"
        self.cost = 6
        Buy.Result(self)
        GET_ANTI_PEST += f
        inventory_4[0] = GET_ANTI_PEST


class Product5(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_COW
        self.name = "Animal: Vaca"
        self.cost = 8
        Buy.Result(self)
        GET_COW += f
        inventory_5[0] = GET_COW


class Product6(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_SHEEP
        self.name = "Animal: Oveja"
        self.cost = 7
        Buy.Result(self)
        GET_SHEEP += f
        inventory_6[0] = GET_SHEEP


class Product7(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_PIG
        self.name = "Animal: Cerdo"
        self.cost = 5
        Buy.Result(self)
        GET_PIG += f
        inventory_7[0] = GET_PIG


class Product8(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_FERTILIZER
        self.name = "Fertilizantes"
        self.cost = 6
        Buy.Result(self)
        GET_FERTILIZER += f
        inventory_8[0] = GET_FERTILIZER


class Product9(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_APPLE
        self.name = "Semillas de Manzanas"
        self.cost = 2
        Buy.Result(self)
        GET_APPLE += f
        inventory_9[0] = GET_APPLE


class Product10(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_MELON
        self.name = "Semillas de Sandía"
        self.cost = 3
        Buy.Result(self)
        GET_MELON += f
        inventory_10[0] = GET_MELON


class Product11(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_CARROT
        self.name = "Semillas de Zanahoria"
        self.cost = 2
        Buy.Result(self)
        GET_CARROT += f
        inventory_11[0] = GET_CARROT


class Product12(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_WHEAT
        self.name = "Semillas para Trigo"
        self.cost = 2
        Buy.Result(self)
        GET_WHEAT += f
        inventory_12[0] = GET_WHEAT


class Product13(Buy):
    def __init__(self, cost, total, buy, price, name, turned, cash):
        Buy.__init__(self, cost, total, buy, price, name, turned, cash)

    def Result(self):
        global GET_CORN
        self.name = "Semillas para Maíz"
        self.cost = 1
        Buy.Result(self)
        GET_CORN += f
        inventory_13[0] = GET_CORN


class Sell(Buy):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Buy.__init__(self, cost, total, buy, price, name, turned, coin)
        self.sell = "\033[1;38;2;166;255;12m¿Desea venderlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m"
        self.totalsell = "\033[1;38;2;233;255;12m                  ¿Qué cantidad desea vender? \033[0;m"
        self.name = name
        self.turned = turned
        self.inventor = inventor
    def Result(self):
        while True:
            global WALLET
            print(f"\033[1;38;2;255;170;0m{self.name} \033[0m" + "\033[1;38;2;243;255;0mVale $\033[0;m", self.cost)
            v = input(self.sell)
            if v == "s" or v == "S":
                global fs
                ts = int(input(self.totalsell))
                if self.inventor > 0:
                    fs = ts
                    self.price = ts * self.cost
                    WALLET += self.price
                    print(f"Ha ganado: $. {self.price}")
                    self.turned = print("\033[1;38;2;0;178;255mUsted ahora tiene:\033[0m", WALLET, "Monedas")
                    break
                print(f"No tiene {self.name} en su inventario")
            print("Regresando")
            break
class Sell1(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)

    def Result(self):
        global GET_COW_FOOD
        self.name = "Compuesto para Vaca"
        self.cost = 7
        self.inventor = inventory_1[0]
        Sell.Result(self)
        GET_COW_FOOD -= fs
        inventory_1[0] = GET_COW_FOOD
class Sell2(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)

    def Result(self):
        global GET_FOOD_SHEEP
        self.name = "Compuesto para Oveja"
        self.cost = 7
        self.inventor = inventory_2[0]
        Sell.Result(self)
        GET_FOOD_SHEEP -= fs
        inventory_2[0] = GET_FOOD_SHEEP
class Sell3(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)
    def Result(self):
        global GET_PIG_FOOD
        self.name = "Compuesto para Cerdo"
        self.cost = 7
        self.inventor = inventory_3[0]
        Sell.Result(self)
        GET_PIG_FOOD -= fs
        inventory_3[0] = GET_PIG_FOOD
class Sell4(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)

    def Result(self):
        global GET_ANTI_PEST
        self.name = "Antiplagas"
        self.cost = 8
        self.inventor = inventory_4[0]
        Sell.Result(self)
        GET_ANTI_PEST-= fs
        inventory_4[0] = GET_ANTI_PEST
class Sell5(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)
    def Result(self):
        global GET_COW
        self.name = "Animal: Vaca"
        self.cost = 10
        self.inventor = inventory_5[0]
        Sell.Result(self)
        GET_COW -= fs
        inventory_5[0] = GET_COW
class Sell6(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)
    def Result(self):
        global GET_SHEEP
        self.name = "Animal: Oveja"
        self.cost = 9
        self.inventor = inventory_6[0]
        Sell.Result(self)
        GET_SHEEP -= fs
        inventory_6[0] = GET_SHEEP
class Sell7(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)
    def Result(self):
        global GET_PIG
        self.name = "Animal: Cerdo"
        self.cost = 7
        self.inventor = inventory_7[0]
        Sell.Result(self)
        GET_PIG -= fs
        inventory_7[0] = GET_PIG
class Sell8(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)
    def Result(self):
        global GET_FERTILIZER
        self.name = "Fertilizantes"
        self.cost = 8
        self.inventor = inventory_8[0]
        Sell.Result(self)
        GET_FERTILIZER -= fs
        inventory_8[0] = GET_FERTILIZER
class Sell9(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)
    def Result(self):
        global GET_APPLE
        self.name = "Semilla de Manzana"
        self.cost = 4
        self.inventor = inventory_9[0]
        Sell.Result(self)
        GET_APPLE -= fs
        inventory_9[0] = GET_APPLE
class Sell10(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)
    def Result(self):
        global GET_MELON
        self.name = "Semilla de Sandía"
        self.cost = 5
        self.inventor = inventory_10[0]
        Sell.Result(self)
        GET_MELON -= fs
        inventory_10[0] = GET_MELON
class Sell11(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)
    def Result(self):
        global GET_CARROT
        self.name = "Semillas de Zanahoria"
        self.cost = 4
        self.inventor = inventory_11[0]
        Sell.Result(self)
        GET_CARROT -= fs
        inventory_11[0] = GET_CARROT
class Sell12(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)
    def Result(self):
        global GET_WHEAT
        self.name = "Semillas para Trigo"
        self.cost = 4
        self.inventor = inventory_12[0]
        Sell.Result(self)
        GET_WHEAT -= fs
        inventory_12[0] = GET_WHEAT
class Sell13(Sell):
    def __init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor):
        Sell.__init__(self, cost, total, buy, price, name, turned, sell, totalsell, coin, inventor)
    def Result(self):
        global GET_CORN
        self.name = "Semilla de Maíz"
        self.cost = 3
        self.inventor = inventory_13[0]
        Sell.Result(self)
        GET_CORN -= fs
        inventory_13[0] = GET_CORN
TIMES = []
class TIEMPO:
    def __init__(self, clock=60):
        self.clock = clock
class MEDIR(TIEMPO):
    def __init__(self, clock=0):
        super().__init__(clock)
    def show(self):
        return self.clock
def pasar(y):
    while True:
        for i in y:
            i.clock += 10
            time.sleep(1)

tiempo_thread1 = threading.Thread(target=pasar, args=(TIMES,))
tiempo_thread1.daemon = True
tiempo_thread1.start()
tim1 = MEDIR()
tim1.show()
TIMES.append(tim1)
while True:
    print(tim1.show())
    menu = input("\033[1;38;2;202;255;6mFarm The Best\033[1;0m\n"+"\033[1;38;2;223;174;52mA. Animales :)\033[1;0m\n" #Animales, encargado por Alessandro
                 "\033[1;38;2;104;255;6mB. Cultivos\033[1;0m\n" #Cultivos encargado por Lesther
                "\033[1;38;2;255;54;0mC. Ti\033[1;0m" + "en" + "\033[1;38;2;255;54;0mda\033[0m\n" #Tienda encargado por Allan}
                "\033[1;38;2;6;244;255mI. Inventario\033[1;0m\n"+"\033[1;38;2;6;164;255mElija su opción: \033[1;0m")

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
                    print("\033[1;38;2;202;255;6mAlimentos disponibles para animales: \033[1;0m\n")
                    print("\033[1;38;2;255;23;0m1. Manzana: \033[1;0m\n")
                    print("\033[1;38;2;151;255;0m2. Sandía: \033[1;0m\n")
                    print("\033[1;38;2;255;120;0m3. Zanahoría: \033[1;0m\n")
                    print("\033[1;38;2;255;255;0m4. Trigo: \033[1;0m\n")
                    print("\033[1;38;2;97;255;0m5. Maíz: \033[1;0m\n")
                    feed_animal = int(input("\033[1;38;2;202;255;6mIngrese con que desea alimentar a su animal: \033[1;0m\n"))
                    if feed_animal >= 1 and feed_animal <= 5:
                        if feed_animal == 1:
                            if inventory_14[0] > 0:
                                self.hunger -= 30
                                print(f"El hambre de su animal {self.number} ahora es: ", self.hunger)
                            print("No tiene alimentos de manzana")
                        if feed_animal == 2:
                            if inventory_15[0] > 0:
                                self.hunger -= 30
                                print(f"El hambre de su animal {self.number} ahora es: ", self.hunger)
                            print("No tiene alimentos de sandía")
                        if feed_animal == 3:
                            if inventory_16[0] > 0:
                                self.hunger -= 30
                                print(f"El hambre de su animal {self.number} ahora es: ", self.hunger)
                            print("No tiene alimentos de zanahoria")
                        if feed_animal == 4:
                            if inventory_17[0] > 0:
                                self.hunger -= 30
                                print(f"El hambre de su animal {self.number} ahora es: ", self.hunger)
                            print("No tiene alimentos de Trigo")
                        if feed_animal == 5:
                            if inventory_18[0] > 0:
                                self.hunger -= 30
                                print(f"El hambre de su animal {self.number} ahora es: ", self.hunger)
                            print("No tiene alimentos de maíz")
                    else:
                        print(f"El hambre de su animal {self.number} es: ", self.hunger)

                def clean(self):
                    animal_clean = 50
                    animal_clean2 = input("\033[1;38;2;0;247;255mPresione la tecla 'C' si quiere limpiar a su animal:  \033[1;0m\n").upper()
                    if animal_clean2 == "C":
                        animal_clean += 35
                        print("El porcentaje de limpieza de su animal es: ", animal_clean)
                    else:
                        print("El procentaje de limpieza de su animal es: ", animal_clean)

                def strock(self):
                    happ = input("\033[1;38;2;255;205;0mIngrese la tecla 'R' para acariciar: \033[1;0m\n").upper()
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
                    print(f"\033[1;38;2;54;255;0mLa salud de su cerdo {self.number} es: \033[1;0m", self.healt)
                    print(f"\033[1;38;2;0;197;255mLa felicidad de su cerdo {self.number} es: \033[1;0m", self.happiness)
                    print(f"\033[1;38;2;255;162;0mEl hambre de su cerdo {self.number} es: \033[1;0m", self.hunger)
                    self.breeding = int(input(f"\033[1;38;2;243;255;0mIngrese cuantas crias ha tenido su cerdo {self.number}:  \033[1;0m"))
                    inventory_7[0] += self.breeding
                    self.milk = int(input(f"\033[1;38;2;255;0;135mIngrese cuantos litros de leche ha producido su cerdo {self.number}: \033[1;0m"))
                    inventory_7_1[0] += self.milk
                    self.meat = int(input(f"\033[1;38;2;0;209;255mIngrese cuantas libras de carne puede generar su cerdo {self.number}: \033[1;0m"))
                    inventory_7_2[0] += self.meat
                    self.fur = int(input(f"\033[1;38;2;0;201;255mIngrese cuantas m^2 de piel puede generar su cerdo {self.number}:   \033[1;0m"))
                    inventory_7_3[0] += self.meat

                def data_entry_return(self):
                    return "Vida:",self.healt, "Felicidad:",self.happiness, "Hambre:",self.hunger, "Crías:",self.breeding, "Leche",self.milk, "Carne",self.meat, "Piel",self.fur

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
                        inventory_7[0] -= self.breeding
                        print("Ahora tiene ", inventory_7[0], " crias")
                    elif collect == 2:
                        collect_milk = int(input("Ingrese cuantos litros de leche desea recoger: "))
                        self.milk -= collect_milk
                        inventory_7_1[0] -= self.milk
                        print("Ahora tiene ", self.milk, " litros de leche disponibles")
                    elif collect == 3:
                        collect_meat = int(input("Ingrese cuentas libras de carne desea recoger: "))
                        self.meat -= collect_meat
                        inventory_7_2[0] -= self.meat
                        print("Ahora tiene ", self.meat, " libras de carne disponibles")
                    elif collect == 4:
                        collect_fur = int(input("Ingrese cuantos metros^2 de piel desea recoger: "))
                        self.fur -= collect_fur
                        inventory_7_3[0] -= self.fur
                        print("Ahora tiene ", self.fur, " metros^2 de piel disponibles")


            class Cows(AnimalCare):
                def __init__(self, number, healt=50, happiness=50, hunger=50, breeding=0, milk=0, meat=0, fur=0,horns=0):
                    super().__init__(healt, happiness, hunger, breeding, milk)
                    self.meat = meat
                    self.fur = fur
                    self.horns = horns
                    self.number = number

                def data_entry(self):
                    print(f"\033[1;38;2;54;255;0mLa salud de su vaca {self.number} es: \033[1;0m", self.healt)
                    print(f"\033[1;38;2;0;197;255mLa felicidad de su vaca {self.number} es: \033[1;0m", self.happiness)
                    print(f"\033[1;38;2;255;162;0mEl hambre de su vaca {self.number} es: \033[1;0m", self.hunger)
                    self.breeding = int(input("\033[1;38;2;243;255;0mIngrese cuantas crias ha tenido su vaca:  \033[1;0m"))
                    inventory_5[0] += self.breeding
                    self.milk = int(input("\033[1;38;2;255;0;135mIngrese cuantos litros de leche ha producido su vaca: \033[1;0m"))
                    inventory_5_1[0] += self.milk
                    self.meat = int(input("\033[1;38;2;0;209;255mIngrese cuantas libras de carne puede generar su vaca: \033[1;0m"))
                    inventory_5_2[0] += self.meat
                    self.fur = int(input("\033[1;38;2;0;201;255mIngrese cuantas m^2 de piel puede generar su vaca:   \033[1;0m"))
                    inventory_5_3[0] += self.fur
                    self.horns = int(input("Ingrese cuantos cuernos de vaca tiene: "))
                    inventory_5_4[0] += self.horns

                def data_entry_return(self):
                    return "vida:", self.healt, "Felicidad:", self.happiness, "Hambre:", self.hunger, "Crías", self.breeding, "Leche:", self.milk, "Carne:", self.meat, "Pelage:", self.fur, "Cuernos:", self.horns

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
                        inventory_5[0] -= self.breeding
                        print("Ahora tiene ", inventory_5[0], " crias")
                    elif collect == 2:
                        collect_milk = int(input("Ingrese cuantos litros de leche desea recoger: "))
                        self.milk -= collect_milk
                        inventory_5_1[0] -= self.milk
                        print("Ahora tiene ", self.milk, " litros de leche disponibles")
                    elif collect == 3:
                        collect_meat = int(input("Ingrese cuentas libras de carne desea recoger: "))
                        self.meat -= collect_meat
                        inventory_5_1[0] -= self.meat
                        print("Ahora tiene ", self.meat, " libras de carne disponibles")
                    elif collect == 4:
                        collect_fur = int(input("Ingrese cuantos metros^2 de piel desea recoger: "))
                        self.fur -= collect_fur
                        inventory_5_1[0] -= self.fur
                        print("Ahora tiene ", self.fur, " metros^2 de piel disponibles ")
                    elif collect == 5:
                        collect_horns = int(input("Ingrese cuantos cuernos desea recoger: "))
                        self.horns -= collect_horns
                        inventory_5_1[0] -= self.horns
                        print("Ahora tiene ", self.horns, " cuenros a disposicion")


            class Sheep(AnimalCare):
                def __init__(self, number, healt=50, happiness=50, hunger=50, breeding=0, milk=0, meat=0, wool=0):
                    super().__init__(healt, happiness, hunger, breeding, milk)
                    self.meat = meat
                    self.wool = wool
                    self.number = number

                def data_entry(self):
                    print(f"\033[1;38;2;54;255;0mLa salud de su oveja {self.number} es: \033[1;0m", self.healt)
                    print(f"\033[1;38;2;0;197;255mLa felicidad de su oveja {self.number} es: \033[1;0m", self.happiness)
                    print(f"\033[1;38;2;255;162;0mEl hambre de su oveja {self.number} es: \033[1;0m", self.hunger)
                    self.breeding = int(input("\033[1;38;2;243;255;0mIngrese cuantas crias ha tenido su oveja:  \033[1;0m"))
                    inventory_6[0] += self.breeding
                    self.milk = int(input("\033[1;38;2;255;0;135mIngrese cuantos litros de leche ha producido su oveja: \033[1;0m"))
                    inventory_6_1[0] += self.milk
                    self.meat = int(input("\033[1;38;2;0;209;255mIngrese cuantas libras de carne puede generar su oveja: \033[1;0m"))
                    inventory_6_2[0] += self.meat
                    self.fur = int(input("\033[1;38;2;0;201;255mIngrese la cantidad m2 de carne que puede generar su oveja  \033[1;0m"))
                    inventory_6_3[0] += self.fur

                def data_entry_return(self):
                    return "Vida:",self.healt, "Felicidad:",self.happiness, "Hambre:",self.hunger, "Crías:",self.breeding, "Leche:",self.milk, "Carne",self.meat, "Piel",self.fur

                def collect_resources(self):
                    print("\033[1;38;2;202;255;6mRecursos disponibles \033[1;0m")
                    print("\033[1;38;2;243;255;0m1. Su animal tiene \033[1;0m", self.breeding, " crias")
                    print("\033[1;38;2;255;0;135m2. Su animal ha producido \033[1;0m", self.milk, " litros de leche")
                    print("\033[1;38;2;0;209;255m3. Su animal puede generar \033[1;0m", self.meat, " libras de carne")
                    print("\033[1;38;2;255;178;0m4. Su animal puede generar \033[1;0m", self.fur, " metros^2 de piel")
                    print("\033[1;38;2;0;201;255m5. Tiene en posecion  \033[1;0m", self.wool, " libras de lana")
                    collect = int(input("Ingrese que desea recoger: "))
                    if collect == 1:
                        collet_breeding = int(input("Ingrese cuantas crias desea recoger: "))
                        self.breeding -= collet_breeding
                        inventory_6[0] -= self.breeding
                        print("Ahora tiene ", inventory_6[0], " crias")
                    elif collect == 2:
                        collect_milk = int(input("Ingrese cuantos litros de leche desea recoger: "))
                        self.milk -= collect_milk
                        inventory_6_1[0] -= self.milk
                        print("Ahora tiene ", self.milk, " litros de leche disponibles")
                    elif collect == 3:
                        collect_meat = int(input("Ingrese cuantas libras de carne desea recoger: "))
                        self.meat -= collect_meat
                        inventory_6_2[0] -= self.meat
                        print("Ahora tiene ", self.meat, " libras de carne disponibles")
                    elif collect == 4:
                        collect_fur = int(input("Ingrese cuantos metros^2 de piel desea recoger: "))
                        self.fur -= collect_fur
                        inventory_6_3[0] -= self.fur
                        print("Ahora tiene ", self.fur, " metros^2 de piel disponibles ")

            def pasar_tiempo(y):
                while True:
                    for i in y:
                        i.hunger += 10
                        i.healt -= 5
                        i.happiness -=5
                    time.sleep(60)


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
                        print("Has fertilizado el cultivo de ", self.name)
                    else:
                        print("No quedan fertilizantes disponibles para el cultivo de ", self.name)

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
                        print("Has curado las plagas en el cultivo de", self.name)
                    else:
                        print("No quedan tratamientos disponibles para el cultivo de ", self.name)


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
                    self.ready_crops = []

                def crop_type(self):
                    print("\033[1;38;2;202;255;6m                   ///Tipos de cultivos///\033[1;0m")
                    print("\033[1;38;2;178;2;2m1. Manzana     \033[1;0m" + "\033[1;38;2;2;178;39m2. Sandía     \033[1;0m" +  # Apple # Watermelon
                    "\033[1;38;2;255;170;0m3. Zanahoria     \033[1;0m" + "\033[1;38;2;255;228;0m4. Trigo     \033[1;0m" +  # Carrot  # Wheat
                    "\033[1;38;2;209;255;0m5. Maíz     \033[1;0m")  # Corn

                def show_crops(self):
                    if len(self.soil.crops) == 0:
                        print("No hay cultivos en el suelo.")
                    else:
                        print("Cultivos en el suelo:")
                        position = 0
                        for crop in self.soil.crops:
                            print(position, ".", crop.name, "- Estado:", crop.state)
                            position += 1

                def show_harvested_crops(self):
                    if len(self.ready_crops) == 0:
                        print("No hay cultivos cosechados.")
                    else:
                        print("Cultivos cosechados:")
                        position = 0
                        for crop in self.ready_crops:
                            print(position, ".", crop.name, "- Estado:", crop.state)
                            position += 1

                def menu(self):
                    print("\033[1;38;2;202;255;6m                   ///MENÚ///\033[1;0m")
                    print("\033[1;38;2;255;220;0mBienvenido al sistema de cultivo:\033[1;0m")
                    print("\033[1;38;2;66;255;0m1. Plantar un nuevo cultivo     \033[1;0m"+"\033[1;38;2;0;255;247m2. Regar un cultivo       \033[1;0m"+"\033[1;38;2;255;0;104m3. Fertilizar un cultivo\033[1;0m")
                    print("\033[1;38;2;255;255;0m4. Cosechar un cultivo         \033[1;0m"+"\033[1;38;2;161;96;7m5. Mostrar estado de cultivos      \033[1;0m"+"\033[1;38;2;255;0;209m6. Curar plagas en un cultivo\033[1;0m")
                    print("\033[1;38;2;193;0;255m7. Salir\033[1;0m")
                    option = int(input("\033[1;38;2;202;255;6mIngrese su opción: \033[1;0m"))
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
                                        self.ready_crops.append(crop)
                                        del self.soil.crops[position]
                                    else:
                                        print("El cultivo no está listo para cosechar.")
                                else:
                                    print("Posición no válida.")

                        elif option == 5:
                            self.show_crops()
                            self.show_harvested_crops()

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
                        print("\033[1;38;2;202;255;6m                   ///MENÚ///\033[1;0m")
                        print("\033[1;38;2;255;220;0mBienvenido al sistema de cultivo:\033[1;0m")
                        print(
                            "\033[1;38;2;66;255;0m1. Plantar un nuevo cultivo     \033[1;0m" + "\033[1;38;2;0;255;247m2. Regar un cultivo       \033[1;0m" + "\033[1;38;2;255;0;104m3. Fertilizar un cultivo\033[1;0m")
                        print(
                            "\033[1;38;2;255;255;0m4. Cosechar un cultivo         \033[1;0m" + "\033[1;38;2;161;96;7m5. Mostrar estado de cultivos      \033[1;0m" + "\033[1;38;2;255;0;209m6. Curar plagas en un cultivo\033[1;0m")
                        print("\033[1;38;2;193;0;255m7. Salir\033[1;0m")
                        option = int(input("\033[1;38;2;202;255;6mIngrese su opción: \033[1;0m"))

                    print("\033[1;38;2;178;2;2mSaliendo del programa\033[1;0m")


            menu1 = Menu()
            menu1.menu()
            Continuar = input("\033[1;38;2;2;178;141m¿Desea continuar con el programa? \033[1;0m" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
            if Continuar == "n" or Continuar == "N":
                print("Regresando...")
                break
            opcionB = "B"
    while menu == "C" or menu == "c": #**********Allan**********
        if menu == "C" or menu == "c":
            optionE = input("\033[1;38;2;255;54;0mTi\033[1;0m" + "en" + "\033[1;38;2;255;54;0mda:\033[0m\n"+"\033[1;38;2;178;250;0mA. Comprar\033[0;m\n"+"\033[1;38;2;247;255;6mB. Vender: \033[1;0m\n"+"\033[1;38;2;6;164;255mElija su opción: \033[1;0m")
            while optionE == "A" or optionE == "a":
                if optionE == "A" or optionE == "a":
                    print("\033[1;38;2;255;54;0mTi\033[1;0m" + "en" + "\033[1;38;2;255;54;0mda:\033[0m")
                    while True:
                        print("\033[1;38;2;23;252;248mActualmente tienes:\033[0m", WALLET, "Monedas")
                        product = input("\033[1;38;2;255;54;0m                                                  Productos \033[1;38;2;255;165;00m" + "disponibles:\033[0m\n"
                            "\033[1;38;2;216;98;55mA. Compuesto para Vaca   \033[0m" + "\033[1;38;2;51;214;243mB. Compuesto para Oveja     \033[0;m" + "\033[1;38;2;209;0;255mC. Compuesto para Cerdo    \033[0;m" + "\033[1;38;2;244;155;0mD. Vaca    \033[0m"
                            "\033[1;38;2;255;224;0mE. Oveja     \033[0;m" + "\033[1;38;2;255;6;210mF. Cerdo\033[0;m\n" + "\033[1;38;2;180;255;71m           G. Fertilizante    \033[0;m" + "\033[1;38;2;255;185;71mH. Antiplagas   \033[0;m"
                            "\033[1;38;2;255;6;93mI. Semillas de manzana  \033[0;m" + "\033[1;38;2;25;238;187mJ. Semillas de sandía   \033[0;m" + "\033[1;38;2;153;6;255mK. Semillas de zanahoria\033[0;m\n"
                            "\033[1;38;2;6;157;255m                                                L. Trigo    \033[0;m" + "\033[1;38;2;78;255;6mM. Maíz     \033[0;m" + "\033[1;38;2;6;255;217mN. Granero\033[0;m\n"
                            "\033[1;38;2;215;0;0m                                 O. Salir de la tienda\033[0;m\n" + "\033[1;38;2;50;205;50m            Elija su opción: \033[0;m")
                        while product == "A" or product == "a":
                            if product == "A" or product == "a":
                                if __name__ == "__main__":
                                    get_product1 = Product1("", "", "", "", "", "", WALLET)
                                    get_product1.Result()
                            break
                        while product == "B" or product == "b":
                            if product == "B" or product == "b":
                                if __name__ == "__main__":
                                    get_product2 = Product2("", "", "", "", "", "", WALLET)
                                    get_product2.Result()
                            break
                        while product == "C" or product == "c":
                            if product == "C" or product == "c":
                                if __name__ == "__main__":
                                    get_product3 = Product3("", "", "", "", "", "", WALLET)
                                    get_product3.Result()
                            break
                        while product == "D" or product == "d":
                            if product == "D" or product == "d":
                                if __name__ == "__main__":
                                    get_product5 = Product5("", "", "", "", "", "", WALLET)
                                    get_product5.Result()
                            break
                        while product == "E" or product == "e":
                            if product == "E" or product == "e":
                                if __name__ == "__main__":
                                    get_product6 = Product6("", "", "", "", "", "", WALLET)
                                    get_product6.Result()
                            break
                        while product == "F" or product == "f":
                            if product == "F" or product == "f":
                                if __name__ == "__main__":
                                    get_product7 = Product7("", "", "", "", "", "", WALLET)
                                    get_product7.Result()
                            break
                        while product == "G" or product == "g":
                            if product == "G" or product == "g":
                                if __name__ == "__main__":
                                    get_product8 = Product8("", "", "", "", "", "", WALLET)
                                    get_product8.Result()
                            break
                        while product == "H" or product == "h":
                            if product == "H" or product == "h":
                                if __name__ == "__main__":
                                    get_product4 = Product4("", "", "", "", "", "", WALLET)
                                    get_product4.Result()
                            break
                        while product == "I" or product == "i":
                            if product == "I" or product == "i":
                                if __name__ == "__main__":
                                    get_product9 = Product9("", "", "", "", "", "", WALLET)
                                    get_product9.Result()
                            break
                        while product == "J" or product == "j":
                            if product == "J" or product == "j":
                                if __name__ == "__main__":
                                    get_product10 = Product10("", "", "", "", "", "", WALLET)
                                    get_product10.Result()
                            break
                        while product == "K" or product == "k":
                            if product == "K" or product == "k":
                                if __name__ == "__main__":
                                    get_product11 = Product11("", "", "", "", "", "", WALLET)
                                    get_product11.Result()
                            break
                        while product == "L" or product == "l":
                            if product == "L" or product == "l":
                                if __name__ == "__main__":
                                    get_product12 = Product12("", "", "", "", "", "", WALLET)
                                    get_product12.Result()
                            break
                        while product == "M" or product == "m":
                            if product == "M" or product == "m":
                                if __name__ == "__main__":
                                    get_product13 = Product13("", "", "", "", "", "", WALLET)
                                    get_product13.Result()
                            break
                        while product == "N" or product == "n":
                            if product == "N" or product == "n":
                                print("\033[1;38;2;23;252;248mActualmente tienes:\033[0m", WALLET, "Monedas")
                                LINE = 5
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
                    print("\033[1;38;2;247;255;6mVentas: \033[1;0m")
                    while True:
                        print("\033[1;38;2;23;252;248mActualmente tienes:\033[0m", WALLET, "Monedas")
                        productsell = input("\033[1;38;2;255;54;0m                                                  Productos \033[1;38;2;255;165;00m" + "disponibles:\033[0m\n"
                            "\033[1;38;2;216;98;55mA. Compuesto para Vaca   \033[0m" + "\033[1;38;2;51;214;243mB. Compuesto para Oveja     \033[0;m" + "\033[1;38;2;209;0;255mC. Compuesto para Cerdo    \033[0;m" + "\033[1;38;2;244;155;0mD. Vaca    \033[0m"
                            "\033[1;38;2;255;224;0mE. Oveja     \033[0;m" + "\033[1;38;2;255;6;210mF. Cerdo\033[0;m\n" + "\033[1;38;2;180;255;71m           G. Fertilizante    \033[0;m" + "\033[1;38;2;255;185;71mH. Antiplagas   \033[0;m"
                            "\033[1;38;2;255;6;93mI. Semillas de manzana  \033[0;m" + "\033[1;38;2;25;238;187mJ. Semillas de sandía   \033[0;m" + "\033[1;38;2;153;6;255mK. Semillas de zanahoria\033[0;m\n"
                            "\033[1;38;2;6;157;255m                                                L. Trigo    \033[0;m" + "\033[1;38;2;78;255;6mM. Maíz     \033[0;m" + "\033[1;38;2;6;255;217mN. Granero\033[0;m\n"
                            "\033[1;38;2;215;0;0m                                 O. Salir de la tienda\033[0;m\n" + "\033[1;38;2;50;205;50m            Elija su opción: \033[0;m")
                        while productsell == "A" or productsell == "a":
                            if productsell == "A" or productsell == "a":
                                if __name__ == "__main__":
                                    get_productsell1 = Sell1("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell1.Result()
                            break
                        while productsell == "B" or productsell == "b":
                            if productsell == "B" or productsell == "b":
                                if __name__ == "__main__":
                                    get_productsell2 = Sell2("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell2.Result()
                            break
                        while productsell == "C" or productsell == "c":
                            if productsell == "C" or productsell == "c":
                                if __name__ == "__main__":
                                    get_productsell3 = Sell3("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell3.Result()
                            break
                        while productsell == "D" or productsell == "d":
                            if productsell == "D" or productsell == "d":
                                if __name__ == "__main__":
                                    get_productsell5 = Sell5("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell5.Result()
                            break
                        while productsell == "E" or productsell == "e":
                            if productsell == "E" or productsell == "e":
                                if __name__ == "__main__":
                                    get_productsell6 = Sell6("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell6.Result()
                            break
                        while productsell == "F" or productsell == "f":
                            if productsell == "F" or productsell == "f":
                                if __name__ == "__main__":
                                    get_productsell7 = Sell7("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell7.Result()
                            break
                        while productsell == "G" or productsell == "g":
                            if productsell == "G" or productsell == "g":
                                if __name__ == "__main__":
                                    get_productsell8 = Sell8("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell8.Result()
                            break
                        while productsell == "H" or productsell == "h":
                            if productsell == "H" or productsell == "h":
                                if __name__ == "__main__":
                                    get_productsell4 = Sell4("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell4.Result()
                            break
                        while productsell == "I" or productsell == "i":
                            if productsell == "I" or productsell == "i":
                                if __name__ == "__main__":
                                    get_productsell9 = Sell9("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell9.Result()
                            break
                        while productsell == "J" or productsell == "j":
                            if productsell == "J" or productsell == "j":
                                if __name__ == "__main__":
                                    get_productsell10 = Sell10("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell10.Result()
                            break
                        while productsell == "K" or productsell == "k":
                            if productsell == "K" or productsell == "k":
                                if __name__ == "__main__":
                                    get_productsell11 = Sell11("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell11.Result()
                            break
                        while productsell == "L" or productsell == "l":
                            if productsell == "L" or productsell == "l":
                                if __name__ == "__main__":
                                    get_productsell12 = Sell12("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell12.Result()
                            break
                        while productsell == "M" or productsell == "m":
                            if productsell == "M" or productsell == "m":
                                if __name__ == "__main__":
                                    get_productsell13 = Sell13("", "", "", "", "", "", "", "", WALLET, "")
                                    get_productsell13.Result()
                            break
                        while productsell == "N" or productsell == "n":
                            if productsell == "N" or productsell == "n":
                                print("\033[1;38;2;23;252;248mActualmente tienes:\033[0m", WALLET, "Monedas")
                                LINE = 5
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
            continue_end = input("\033[1;38;2;218;206;35m¿Desea regresar al menú de inicio?\033[0;m\n" + "\033[1;32mS\033[0;m" + "/" + "\033[1;31mN: \033[0;m")
            if continue_end == "s" or continue_end == "S":
                print("\033[1;38;2;255;54;0mRegresando...\033[0m\n")
                break
            menu = "E"
            break
    while menu == "I" or menu == "i":
        if menu == "I" or menu == "i":
            print("\033[1;38;2;23;252;248mActualmente tienes:\033[0m", WALLET, "Monedas")
            LINE = 5
            for i, objects in enumerate(BARN):
                if i % LINE == 0 and i != 0:
                    print()
                print(objects, end="\t")
            print()
        break
