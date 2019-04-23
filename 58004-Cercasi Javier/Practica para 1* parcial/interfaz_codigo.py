
def interfaz_codigo(clave,simbolos):
    
    from codigo import codigo

    try:
        frase1=str(simbolos)
        resultado = codigo(clave,frase1)
        return resultado
    except:
        print('Error')

def main():
    clave=str(input('Ingrese la clave: '))
    clave=clave.replace(' ', '').upper() 
    simbolos=str(input('Ingrese la frase: '))
    simbolos=simbolos.replace(' ', '').upper() 
    resultado=interfaz_codigo(clave,simbolos)
    print(resultado)
main()
