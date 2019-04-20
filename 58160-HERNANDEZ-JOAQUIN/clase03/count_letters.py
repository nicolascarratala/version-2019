def count_letters(palabra):
    dict_d = {}
    for letter in palabra:
        if letter in dict_d:
            dict_d[letter] += 1
        else:
            dict_d[letter] = 1
    return dict_d
    
            

    