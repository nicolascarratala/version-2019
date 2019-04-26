def cifrar_v(frase,clave):
    frase=frase.lower()
    clave=clave.lower()
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    text=''
    i=0
    for letra in frase:
        suma=alphabet.index(letra) + alphabet.index(clave[i % len(clave)])
        modulo=int(suma) % len(alphabet)
        text=text + str(alphabet[modulo])
        i=i+1
    return text.upper()

