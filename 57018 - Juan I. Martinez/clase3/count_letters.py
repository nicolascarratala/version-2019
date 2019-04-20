def count_letters(frase):
    diccionario = {}

    for letra in frase:
        diccionario.setdefault(letra, 0)
        diccionario[letra] += 1

    return diccionario

#De esta forma se puede hacer sin la funcion

def count_letters2(frase):
    diccionario = {}

    for letra in frase:
        if not letra in diccionario: 
            diccionario[letra] = 1
        else:
            diccionario[letra] += 1

    return diccionario

#print(count_letters2('Hola'))
#Sacar el comentario anterior para probar la version sin setdefault()
#Si se quiere correr la otra funcion en el test, invertir los nombre(agregar 2 en la 1ra, borrarlo en la otra)