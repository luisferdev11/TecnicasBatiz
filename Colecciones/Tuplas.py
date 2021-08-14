lista = [69.7, 88.9, 104.3]
mitupla = ("id", "nombre", "puesto", 1, 1, (2.5, 35), ["lista1", "lista2"])
tupla2 = (1539, "Armando Alvarez", "docente", 22500)
tupladelista = ()
print(f"la tupla {mitupla}")

# convertir una lista en tupla
tupladelista = tuple(lista)
print(f"la lista convertida en tupla es {tupladelista}")

# obtener el numero de elementos de la tupla
print(f"la tupla consta de {len(mitupla)} elementos")

# para saber el numero de veces que aparece un valor
print(f"el valor aparece  {mitupla.count(1)} veces en la tupla")

# para saber la posición que tiene un elemento en la tupla
print(f"la posición en la que está el valor que buscas es {mitupla.index('puesto')}")

# pasando toda una lista a variables
folio, nombre, puesto, sueldo = tupla2
print(f"variable folio {folio}")
print(f"variable nombre {nombre}")
print(f"variable puesto {puesto}")
print(f"variable sueldo {sueldo}")

print(tuple("python"))