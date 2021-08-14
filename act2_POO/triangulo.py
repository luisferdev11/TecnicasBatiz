from figura_geometrica import *

class Triangulo(FigGeo):

    def __init__(self, lado1, lado2, lado3):
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def calc_per(self):
        return self.__lado1 + self.__lado2 + self.__lado3

#Esta es una fórmula para cualcular el área de un triangulo cualquiera, sin tener que especificar la base
    def calc_area(self):
        p = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return math.sqrt(p*(p-self.__lado1)*(p-self.__lado2)*(p-self.__lado3))