facturas = {1: 3, 2: 45}
cd = 0

def contar_deuda(contador_deuda = cd):
    for i in facturas:
        contador_deuda += facturas[i]
    return contador_deuda

print(contar_deuda(cd))

facturas = {1: 3, 2: 45, 3: 6}
print(contar_deuda(cd))