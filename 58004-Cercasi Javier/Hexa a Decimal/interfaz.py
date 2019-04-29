def interfaz(palabra):
    from hexa_to_decimal import hexadecimal

    

    if not palabra:
        return ('Error1')
        print("No ingreso ninguna palabra")

    try:
        numero=str(palabra)
        return hexadecimal(numero)

    except:
        return('Error2')
        print("Disculpe, solo acepto numeros")
    
    

def main():
    palabra=input('Ingrese un numero: ')
    result=interfaz(palabra)
    print(result)
main()

    