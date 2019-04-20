def count_letters(palabra):
    dict_mio={}
    for letter in palabra:
        if letter in dict_mio:
            dict_mio[letter]+=1
        else:
            dict_mio[letter]=1
    return dict_mio
