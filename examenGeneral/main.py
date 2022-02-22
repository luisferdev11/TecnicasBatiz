
from Figuras import rectangulo, triangulo, circulo
from bd import *
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt

my_rectangulo = rectangulo(4, 3, 4)
print(my_rectangulo.figura)
print(my_rectangulo.perimetro())

my_triangulo = triangulo(3, 3, 4, 5)
print(my_triangulo.area())

my_circulo = circulo(None, 4)
print(my_circulo.perimetro())


con("root", "Pillofon", "3306")

insert(my_rectangulo.figura, my_rectangulo.area(), my_rectangulo.perimetro())
print(select(my_rectangulo.figura))

if __name__ == "__main__":
    seguir = True
    while seguir:
        accion = input("Escribe la figura que quieres seleccionar: ").lower()
        if accion in ("triangulo", "t", "3"):
            lado1 = float(input("Escribe un lado"))
            lado2 = float(input("Escribe otro lado"))
            lado3 = float(input("Escribe otro lado"))
            figura = triangulo(3, lado1, lado2, lado3)
        elif accion in ("rectangulo", "r", "4", "2"):
            lado1 = float(input("Escribe un lado"))
            lado2 = float(input("Escribe otro lado"))
            figura = rectangulo(4, lado1, lado2)
        else:
            radio = float(input("Escribe el radio"))
            figura = circulo(None, radio)
        insert(figura.figura, figura.area(), figura.perimetro())
        if input("desea continuar??") not in ("si", "s", True):
            seguir = False

    triangulos = selectArea("triangulo")
    rectangulos = selectArea("rectangulo")
    circulos = selectArea("circulo")

    print(
        f"Media, moda y desviacion estandar triangulos (area): {np.mean(triangulos)}, {stat.mode(triangulos)}, {np.std(triangulos)}")

    print(
        f"Media, moda y desviacion estandar rectangulos (area): {np.mean(rectangulos)}, {stat.mode(rectangulos)}, {np.std(rectangulos)}")

    print(
        f"Media, moda y desviacion estandar circulos (area): {np.mean(circulos)}, {stat.mode(circulos)}, {np.std(circulos)}")

    # Declaramos valores para el eje x
    eje_x = ['triangulos', 'Rectangulos', 'circulos']

    # Declaramos valores para el eje y
    eje_y = [np.mean(triangulos), np.mean(rectangulos), np.mean(circulos)]

    # Creamos Gráfica
    plt.bar(eje_x, eje_y)

    # Legenda en el eje y
    plt.ylabel('Media de areas')

    # Legenda en el eje x
    plt.xlabel('Figuras')

    # Título de Gráfica
    plt.title('Areas de figuras')

    # Mostramos Gráfica
    plt.show()
