def count_letters(letters):
    diccionarie={}
    for letter in letters:
        if letter in diccionarie:
            diccionarie[letter]+=1
        else:
            diccionarie[letter]=1
    return diccionarie