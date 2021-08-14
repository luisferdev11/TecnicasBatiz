# www.w3schools.com como apoyo, ta más
lista_variada = ["primero", "segundo", "xd", [2.2, 2.3, 2.5, 2.6], 2, 3, 4, 5, 5, True, False]
lista_num = [5, 10, 15, 20, 25]
lista_nueva = [] # Esta lista la podríamos declarar hasta el momento de utilizarla pero se hace así por buenas prácticas
tupla = ("datos", "llaves", 1, 2)

print(f"El numero de elementos en la lista variada es: {len(lista_variada)}")

# Así obtenemos los elementos de la sublista
for subelemento in lista_variada:
    if isinstance(subelemento, list):
        print(f"Son elementos de la sublista{subelemento}")

# concatenar 2 listas se puede hacer de las siguientes maneras
lista_nueva = lista_variada + lista_num
print(f"Lista concatendada: {lista_nueva}")

# podemos contar la cantidad de veces que se puede llegar a encontrar algún elemento dentro de una lista
print(f"El número de veces que aparece el 5 en la lista nueva es: {lista_nueva.count(5)}")

# Agregar elementos a las listas
lista_num.append(35)
print(f"Se agregó un elemento a la lista de números y quedó de la sig forma: {lista_num}")

# Agregar más de un elemento a la lista

lista_num.extend(lista_variada)
print(f"Tras agregar la lista variada a la lista de números: {lista_num}")

# borrar elementos
del lista_num[6:12]
print(f"la lista despues de haber borrado todos los elementos queda de la sig forma: {lista_num}")

# Verificar si un número se encuentra dentro de la lista
print("xd" in lista_nueva)

# Ordenar la lista ascendentemente
lista_num.sort()
print(f"La lista ordenada ascendentemente es: {lista_num}")

# Ordenar descendentemente
lista_num.sort(reverse=True)
print(f"La lista ordenada descendentemente es: {lista_num}")

# Convertir una tupla en lista
lista_variada = list(tupla)

print (f"conversión de tupla  a lista {lista_variada}")
print (list("python"))