conjunto = set()
conjunto2 = set()
print(conjunto)
conjunto = {1, 2, 3, 1, 2, 3}
print(f"los conjuntos no puede repetir valores {conjunto}")

# convertir una tupla en conjunto
tupla = ("one", "two", "tree", "one")
conjunto2 = set(tupla)
print(conjunto2)

# adiccionar un elemento al conjunto, esto lo hace al azar al ordenarlo
conjunto.add(5)
print(f"nuevo valor introducido al {conjunto}")

# eliminar un elemento al conjunto,
conjunto.discard(1)
print(f"conjunto quitando elemento {conjunto}")
'''operaciones con 
    conjutos'''
a = {1, 2, 3}
b = {3, 4, 5}
c = {6, 7, 8}
d = {1, 2, 3, 4, 5, 6, 7, 8}

# union
print(f"union de conjuntos a | b {a.union(b)}")
# intersección
print(f"intersección de conjuntos a & b {a.intersection(b)}")
# resta de conjunto
print(f"resta de conjuntos a - b {a.difference(b)}")
print(f"resta de conjuntos b - a {b.difference(a)}")
# resta simétrica
print(f"la resta simétrica de a ^ b {a.symmetric_difference(b)} ")

# verificar si no tienen relación
print(f"No tienen elemento en comun: {a.isdisjoint(c)}")

# verificar si es un sobconjunto
print(f"a es subconjunto de d: {a.issubset(d)}")
print(f"b es subconjunto de d: {b.issubset(d)}")
print(f"c es subconjunto de d: {c.issubset(d)}")
print(f"a es subconjunto de b: {a.issubset(b)}")

settest1 = set("esto es un ejemplo")
listax = [4, 5, 6, 7, 8, 99, 0, 1, 5, 0, 5]
settest2 = {"e", "s", "t", "e", "e", "s", "o", "t", "r", "o", "s", "e", "t"}
settest3 = set(listax)
print("conjunto settest1", settest1)
print("conjunto settest2", settest2)
print("conjunto settest3", settest3)
cjto = set([1, 2, 3])
print(cjto)