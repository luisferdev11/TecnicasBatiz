
from abc import abstractmethod
import math


class Fig_geo:
    def __init__(self, lados, figura):
        self.lados = lados
        self.figura = figura

    @abstractmethod
    def perimetro():
        """Devuelve el perimetro"""
    @abstractmethod
    def area():
        """Devuelve el area"""

    def __str__(self) -> str:
        return f"Soy una figura de {self.lados} lados"


class circulo(Fig_geo):
    def __init__(self, lados, radio, figura="circulo"):
        super().__init__(lados, figura)
        self.radio = radio

    def perimetro(self):
        return 2 * self.radio * math.pi

    def area(self):
        return (math.pi * self.radio) ** 2


class triangulo(Fig_geo):
    def __init__(self, lados, lado1, lado2, lado3, figura="triangulo"):
        super().__init__(lados, figura)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def perimetro(self):
        return self.__lado1 + self.__lado2 + self.__lado3

    def area(self):
        p = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return math.sqrt(p*(p-self.__lado1)*(p-self.__lado2)*(p-self.__lado3))


class rectangulo(Fig_geo):
    def __init__(self, lados, lado1, lado2, figura="rectangulo"):
        super().__init__(lados, figura)
        self.__lado1 = lado1
        self.__lado2 = lado2

    def perimetro(self):
        return 2*(self.__lado1 + self.__lado2)

    def area(self):
        return self.__lado1 * self.__lado2
