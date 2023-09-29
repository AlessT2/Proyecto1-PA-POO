inventory_1 = [0, "Compuesto para Vaca"];inventory_2 = [0, "Compuesto para Oveja"];inventory_3 = [0, "Compuesto para Cerdo"];inventory_4 = [0, "Antiplagas"] #INICIA*****ALLAN
inventory_5 = [0, "Vacas"];inventory_6 = [0, "Ovejas"];inventory_7 = [0, "Cerdos"];inventory_8 = [0, "Fertilizantes"]
BARN = [inventory_1, inventory_2, inventory_3, inventory_5, inventory_6, inventory_7, inventory_4,inventory_8]
GET_COW_FOOD = 0;GET_FOOD_SHEEP = 0;GET_PIG_FOOD = 0;GET_ANTI_PEST = 0;GET_COW = 0;GET_PIG = 0;GET_SHEEP = 0;GET_FERTILIZER = 0
class Coin:
    def __init__(self, coin):
        self.coin = coin
    def show(self):
        return self.coin
BASE_COIN = Coin(50)
WALLET = BASE_COIN.show() #Termina******Allan
while True:
    menu = input("*****Nombre del Juego*****\n"+"A. Opción A\n"
                 "B. Opción B\n"+"C. Opción C\n"+"D. Opción D\n"+"\033[1;38;2;255;54;0mE. Ti\033[1;0m" + "en" + "\033[1;38;2;255;54;0mda\033[0m\n"
                 "Elija su opción: ")
    while menu == "A" or menu == "a":
        if menu == "A" or menu == "a":
            opcionA = input("*****Opcion A*****\n"+"A. Opción A\n"
                 "B. Opción B\n"+"C. Opción C\n"+"D. Opción D\n"+"E. Opción E\n"+"Elija su opción: ")
            while opcionA == "A" or opcionA == "a":
                if opcionA == "A" or opcionA == "a":
                    print("")
                break
            while opcionA == "B" or opcionA == "b":
                if opcionA == "B" or opcionA == "b":
                    print("")
                break
            while opcionA == "C" or opcionA == "c":
                if opcionA == "C" or opcionA == "c":
                    print("")
                break
            while opcionA == "D" or opcionA == "d":
                if opcionA == "D" or opcionA == "d":
                    print("")
                break
            while opcionA == "E" or opcionA == "e":
                if opcionA == "E" or opcionA == "e":
                    print("")
                break
            Continuar = input("¿Desea continuar con el programa?" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
            if Continuar == "n" or Continuar == "N":
                print("Regresando...")
                break
            opcionA = "A"
    while menu == "B" or menu == "b":
        if menu == "B" or menu == "b":
            opcionB = input("*****Opción B*****\n"+"A. Opción A\n"+"B. Opción B\n"
            "C. Opción C\n"+"D. Opción D\n"+"E. Opción E\n"+"Elija su opción: ")
            while opcionB == "A" or opcionB == "a":
                if opcionB == "A" or opcionB == "a":
                    print("")
                break
            while opcionB == "B" or opcionB == "b":
                if opcionB == "B" or opcionB == "b":
                    print("")
                break
            while opcionB == "C" or opcionB == "c":
                if opcionB == "C" or opcionB == "c":
                    print("")
                break
            while opcionB == "D" or opcionB == "d":
                if opcionB == "D" or opcionB == "d":
                    print("")
                break
            while opcionB == "E" or opcionB == "e":
                if opcionB == "E" or opcionB == "e":
                    print("")
                break
        Continuar = input("¿Desea continuar con el programa?" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
        if Continuar == "n" or Continuar == "N":
            print("Regresando...")
            break
        opcionB = "B"
    while menu == "C" or menu == "c":
        if menu == "C" or menu == "c":
            opcionC = input("*****Opción C*****\n"+"A. Opción A\n"+"B. Opción B\n"
            "C. Opción C\n"+"D. Opción D\n"+"E. Opción E\n"+"Elija su opción: ")
            while opcionC == "A" or opcionC == "a":
                if opcionC == "A" or opcionC == "a":
                    print("")
                break
            while opcionC == "B" or opcionC == "b":
                if opcionC == "B" or opcionC == "b":
                    print("")
                break
            while opcionC == "C" or opcionC == "c":
                if opcionC == "C" or opcionC == "c":
                    print("")
                break
            while opcionC == "D" or opcionC == "d":
                if opcionC == "D" or opcionC == "d":
                    print("")
                break
            while opcionC == "E" or opcionC == "e":
                if opcionC == "E" or opcionC == "e":
                    print("")
                break
        Continuar = input("¿Desea continuar con el programa?" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
        if Continuar == "n" or Continuar == "N":
            print("Regresando...")
            break
        opcionC = "C"
    while menu == "D" or menu == "d":
        if menu == "D" or menu == "d":
            opcionD = input("*****Opción D*****\n"+"A. Opción A\n"+"B. Opción B\n"
            "C. Opción C\n"+"D. Opción D\n"+"E. Opción E\n"+"Elija su opción: ")
            while opcionD == "A" or opcionD == "a":
                if opcionD == "A" or opcionD == "a":
                    print("")
                break
            while opcionD == "B" or opcionD == "b":
                if opcionD == "B" or opcionD == "b":
                    print("")
                break
            while opcionD == "C" or opcionD == "c":
                if opcionD == "C" or opcionD == "c":
                    print("")
                break
            while opcionD == "D" or opcionD == "d":
                if opcionD == "D" or opcionD == "d":
                    print("")
                break
            while opcionD == "E" or opcionD == "e":
                if opcionD == "E" or opcionD == "e":
                    print("")
                break
        Continuar = input("¿Desea continuar con el programa?" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
        if Continuar == "n" or Continuar == "N":
            print("Regresando...")
            break
        opcionD = "D" or "d"
    while menu == "E" or menu == "e": #**********Allan**********
        if menu == "E" or menu == "e":
            optionE = input("\033[1;38;2;255;54;0mTi\033[1;0m" + "en" + "\033[1;38;2;255;54;0mda:\033[0m\n"+"\033[1;38;2;178;250;0mA. Comprar\033[0;m\n"+"B. Vender\n"+"Elija su opción: ")
            while optionE == "A" or optionE == "a":
                if optionE == "A" or optionE == "a":
                    print("\033[1;38;2;255;54;0mTi\033[1;0m" + "en" + "\033[1;38;2;255;54;0mda:\033[0m")
                    while True:
                        print("\033[1;38;2;23;252;248mActualmente tienes:\033[0m", WALLET, "Monedas")
                        menu = input("\033[1;38;2;255;54;0mProductos \033[1;38;2;255;165;00m" + "disponibles:\033[0m\n"+"\033[1;38;2;255;240;1mA. Compuesto para Vaca\033[0m\n"
                        "\033[1;38;2;51;214;243mB. Compuesto para Oveja \033[0;m\n"+"\033[1;38;2;209;0;255mC. Compuesto para Cerdo\033[0;m\n" + "\033[1;38;2;244;155;0mD. Vaca\033[0m\n"
                        "\033[1;38;2;255;224;0mE. Oveja \033[0;m\n" + "\033[1;38;2;227;10;96mF. Cerdo\033[0;m\n"+"\033[1;38;2;180;255;71mG. Fertilizante\033[0;m\n" + "\033[1;38;2;255;185;71mH. Antiplagas\033[0;m\n"
                        "\033[1;38;2;25;238;187mI. Granero\033[0;m\n" + "\033[1;38;2;215;0;0mJ. Salir de la tienda\033[0;m\n"+"\033[1;38;2;50;205;50mElija su opción: \033[0;m")
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
