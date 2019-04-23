def count_letters(n):
    resultado = {}
    for x in n:
        if resultado.get(x) == None:
            resultado[x] = 1
        else:
            resultado[x] = resultado[x] + 1
    return resultado
