def count_letters(word):
    dictionarie={}
    for letter in word:
        if letter in dictionarie:
            dictionarie[letter]+=1
        else:
            dictionarie[letter]=1
    return dictionarie