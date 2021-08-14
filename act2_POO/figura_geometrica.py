import math

#Clase padre
class FigGeo:
    def __init__(self, numero_lados):
        self._numero_lados = numero_lados


    def __str__(self):
        return f"Has seleccionado una fig de {self._numero_lados} lados"


    def calc_per(self):
        pass


    def calc_area(self):
        pass
