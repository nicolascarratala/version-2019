from Decimal_to_Ex import Convert

def main():
    number=input("Ingrese un numero decimal: ")
    print(decimal(number))

def decimal(n):
    try:
        t=int(n)
        return Convert(t)
    except:
        return "Disculpe,solo acepto numeros"

main()
