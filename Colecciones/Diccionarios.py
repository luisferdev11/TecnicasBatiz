diccionario = {"Armando": ["altura 1.80 cm", "peso 93 kg"], "Sergio": ["altura 1.92 cm", "peso 91 kg"]}
equipo = {10: "Messi", 9: "Suárez", 8: "Griezman"}
print(diccionario)

# introducir un nuevo elemento
diccionario["Erika"] = ["altura 1.60 cm", "peso 60 kg"]
print("el peso de Armando es ", diccionario["Armando"][1])
# obtener el valor de un elemento en particular
print(diccionario.keys())
for i in diccionario:
    print(diccionario[i])
# función obtener datos del diccionario
for i in range(5, 11, 1):
    print(equipo.get(i, "No se tiene registrado ese jugador con el número en el dorsal"))
# función que devuelve los valores del diccionario como tuplas
var = equipo.items()
print(var)
print(dict([[1, "java"], [2, "python"], [3, "c"]]))