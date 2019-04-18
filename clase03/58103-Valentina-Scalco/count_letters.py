def count_letters(palabra):
    diccionario= {}
    for letter in palabra:
        if letter in diccionario:
            diccionario[letter] += 1
        else:
            diccionario[letter] = 1
    return diccionario