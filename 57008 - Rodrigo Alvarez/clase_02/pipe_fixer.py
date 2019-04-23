#Rodrigo Alvarez, 57008
def pipe_fix(lista):
    primero = lista[0]     
    new_value = []
    new_value.append(primero)
    for value in range (lista[0], lista[-1]):
        primero += 1
        new_value.append(primero)
    return new_value