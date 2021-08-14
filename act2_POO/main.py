import figura_geometrica, triangulo, cuadrado , poligono_n, math

#Código elaborado por Rodríguez Domínguez Luis Fernando

#Hace las funciones principales
def menu():
    global opcion
    stop = False
    while stop == False:
        try:
            opcion = int(input("Seleccione el número de lados que tendrá su figura: "))
            miFigura = figura_geometrica.FigGeo(opcion)
            print(miFigura.__str__())
            if opcion == 3:
                print("Por lo tanto tu figura es un triángulo")
                area = float(0)
                while area <= 0:
                    lado1 = float(input("Escribe el primer lado: "))
                    lado2 = float(input("Escribe el segundo lado: "))
                    lado3 = float(input("Escribe el tercer lado: "))
                    miTriangulo = triangulo.Triangulo(lado1, lado2, lado3)
                    try:
                        area = miTriangulo.calc_area()
                        print(f"El perimetro es: {miTriangulo.calc_per()}")
                        print(f"El área es: {str(area)}")
                        stop = True
                    except ValueError:
                        print("No puede existir un triangulo de estas medidas en la vida real \n")
            elif opcion == 4:
                print("Por lo tanto tu figura es un cuadrado")
                base = float(input("Escribe la base: "))
                altura = float(input("Escriba la altura: "))
                miCuadrado = cuadrado.Cuadrado(base, altura)
                print(f"El perimetro es: {miCuadrado.calc_per()}")
                print(f"El área es: {miCuadrado.calc_area()}")
                stop = True
            elif opcion > 4:
                print(f"Bien, calcularemos un poligono regular de {opcion} lados")
                lado = float(input("Escriba la longitud del lado: "))
                miPoligono = poligono_n.PoligonoN(opcion, lado)
                print(f"El perimetro es: {miPoligono.calc_per()}")
                print(f"El área es: {miPoligono.calc_area()}")
                stop = True
            else:
                print("Una figura así no existe, vuelva a intentar \n")
        except ValueError:
            print("Valor no aceptado, vuelva a intentar")

#Ejecucion final
stop = False
while stop == False:
    menu()
    detener = input("Desea agregar otra figura??: ")
    if detener in ("Si", "si", "S", "s"):
        print("")
        stop = False
    elif detener in ("No", "no", "N", "n"):
        stop = True
    else:
        print("Comando incorrecto")