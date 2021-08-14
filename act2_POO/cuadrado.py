from figura_geometrica import *

class Cuadrado(FigGeo):

    def __init__(self, base, altura):
        self.__base = base
        self.__altura = altura

    def calc_per(self):
        return 2*(self.__base + self.__altura)

    def calc_area(self):
        return self.__base * self.__altura