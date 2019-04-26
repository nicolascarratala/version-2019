from cifrado_vigenere import cifrar_v

def main():
    frase=input("ingrese la frase")
    clave=input("ingrese la clave")
    print(word(frase,clave))

def word(data,data1):
    try:
        n=str(data)
        n1=str(data1)
        return cifrar_v(n, n1)
    except:
        return "ERROR no se ingresaron letras"

main()