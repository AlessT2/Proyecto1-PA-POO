print("\033[1;38;2;255;54;0mTi\033[1;0m"+"en"+"\033[1;38;2;255;54;0mda:\033[0m")
inventario1 = {}
inventario2 = {}
inventario3 = {}
Inventory = [inventario1, inventario2, inventario3]
class Moneda:
    def __init__(self,moneda):
        self.moneda = moneda
    def show(self):
        return self.moneda
class Tienda:
    def __init__(self,compuestoVaca, compuestoPollo, compuestoCerdo):
        self.compuestoVaca = compuestoVaca
        self.compuestoPollo = compuestoPollo
        self.compuestoCerdo = compuestoCerdo
moneda_base = Moneda(10)
billetera = moneda_base.show()
while True:
    print("\033[1;38;2;23;252;248mActualmente tienes:\033[0m",billetera, "Monedas")
    menu = input("\033[1;38;2;255;54;0mObjetos \033[1;38;2;255;165;00m"+"disponibles:\033[0m\n"
                 "\033[1;38;2;216;98;55mA. Compuesto para Vaca\033[0m\n"
                 "\033[1;38;2;255;224;0mB. Compuesto para Oveja \033[0;m\n"
                 "\033[1;38;2;255;0;255mC. Compuesto para Cerdo\033[0;m\n"
                 "\033[1;38;2;0;255;228mD. Inventario\033[0;m\n"
                 "\033[1;38;2;50;205;50m"+"Elija su opción: "+"\033[0;m")
    while menu == "A" or menu == "a":
        if menu == "A" or menu == "a":
            precio = 5
            print("\033[1;38;2;216;98;55mCompuesto para Vaca; \033[0m"+"\033[1;38;2;254;214;90mCuesta $\033[0;m",precio)
            Comprar = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
            if Comprar == "s" or Comprar == "S":
                cantidad = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                costo = cantidad * precio
                if billetera >= costo:
                    billetera = billetera - costo
                    print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m",billetera,"Monedas")
                    obtieneCompuestoVaca = 1 * cantidad
                    inventario1[obtieneCompuestoVaca] = "Compuesto para Vaca"
                    break
                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
        break
    while menu == "B" or menu == "b":
        if menu == "B" or menu == "b":
            precio = 3
            print("\033[1;38;2;255;224;0mCompuesto para Oveja; \033[0m"+"\033[1;38;2;254;214;90mCuesta $\033[0;m", precio)
            Comprar = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
            if Comprar == "s" or Comprar == "S":
                cantidad = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                costo = cantidad * precio
                if billetera >= costo:
                    billetera = billetera - costo
                    print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", billetera,"Monedas")
                    obtieneCompuestoPollo = 1 * cantidad
                    inventario2[obtieneCompuestoPollo] = "Compuesto para Oveja"
                    break
                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
        break
    while menu == "C" or menu == "c":
        if menu == "C" or menu == "c":
            precio = 4
            print("\033[1;38;2;255;0;255mCompuesto para Cerdo; \033[0m"+"\033[1;38;2;254;214;90mCuesta $\033[0;m", precio)
            Comprar = input("\033[1;38;2;166;255;12m¿Desea comprarlo?\033[0;m\n" + "\033[1;32m" + "S" + "\033[0;m" + "/" + "\033[1;31m" + "N: " + "\033[0;m")
            if Comprar == "s" or Comprar == "S":
                cantidad = int(input("\033[1;38;2;233;255;12m¿Qué cantidad desea comprar? \033[0;m"))
                costo = cantidad * precio
                if billetera >= costo:
                    billetera = billetera - costo
                    print("\033[1;38;2;0;178;255mSu vuelto es de:\033[0m", billetera,"Monedas")
                    obtieneCompuestoCerdo = 1 * cantidad
                    inventario3[obtieneCompuestoCerdo] = "Compuesto para Cerdo"
                    break
                print("\033[1;38;2;203;68;0mDinero insuficiente, vuelva cuando tenga el dinero necesario\033[0m")
        break
    while menu == "D" or menu == "d":
        if menu == "D" or menu == "d":
            print(Inventory)
        break
    while menu == "E" or menu == "e":
        if menu == "E" or menu == "e":
            print("")
        break