def count_letters(frase):

    dic_mio = {}

    for letter in frase:
        if letter in dic_mio:
            dic_mio[letter] += 1
        else:
            dic_mio[letter] = 1

    return dic_mio

