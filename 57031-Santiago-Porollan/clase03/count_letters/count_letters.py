
def count_letters(word):
    dictionary = {}
    for letter in word:
        if letter in dictionary:
            dictionary[letter]=dictionary[letter]+1
        else:
            dictionary[letter] = 1
    return dictionary

