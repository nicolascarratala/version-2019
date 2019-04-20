#Juan I. Martinez, Legajo 57018
def pipe_fix(lista):
    primero = lista[0]     
    new_value = []
    new_value.append(primero)
    for valor in range (lista[0], lista[-1]):
        primero += 1
        new_value.append(primero)
    return new_value