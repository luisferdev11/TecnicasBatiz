from figura_geometrica import *

class PoligonoN(FigGeo):
    def __init__(self, numero_lados, lado):
        self.numero_lados = numero_lados
        self.__lado = lado

    def calc_per(self):
        global perimetro
        perimetro = self.numero_lados * self.__lado
        return perimetro

    def calc_area(self):
        angulo = 360 / (2* self.numero_lados)
        apotema = self.__lado / (2* math.tan((angulo*math.pi)/180))
        return (perimetro * apotema) / 2

