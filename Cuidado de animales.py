#snake_case para variables, funciones y métodos
#PascalCase para clases
#SCREAMING_SNAKE_CASE para constantes

class CuidadoAnimales:
    def __init__(self, salud, hambre, felicidad, crias):
        self.salud = salud
        self.hambre = hambre
        self.felicidad = felicidad
        self.crias = crias

class Cerdos(CuidadoAnimales):
    def __init__(self, salud, hambre, felicidad, crias, leche, carne, piel):
        super().__init__(salud, hambre, felicidad, crias)
        self.leche = leche
        self.carne = carne
        self.piel = piel

class Vacas(CuidadoAnimales):
    def __init__(self, salud, hambre, felicidad, crias, leche, carne, piel, cuernos):
        super().__init__(salud, hambre, felicidad, crias)
        self.leche = leche
        self.carne = carne
        self.piel = piel
        self.hueso = cuernos

class Ovejas(CuidadoAnimales):
    def __init__(self, salud, hambre, felicidad, crias, leche, carne, lana):
        super().__init__(salud, hambre, felicidad, crias)
        self.leche = leche
        self.carne = carne
        self.lana = lana