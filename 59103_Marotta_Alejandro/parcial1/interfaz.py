from decimal_hexa import decimal_hexadecimal

class ValorAlto(Exception): #creo mi propia excepcion
    pass


def interfaz_hexadecimal(decimal):
    try:
        decimal = int(decimal) #trata de convertir el valor del string a entero, si no puede salta error
        if decimal > 4095: #si el numero es mayor a 4095 largo un error
            raise ValorAlto
        else:
            result = decimal_hexadecimal(decimal) #si todo esta bien realizo la operacion
            return result
    except ValueError as ex:
        print ("---------ERROR----------")
        print ("Disculpe,solo acepto numeros enteros")
        print (ex)
        return False #devuelvo valores booleanos para poder compararlos en el test
    except ValorAlto:
        print ("---------ERROR----------")
        print ('El valor no puede superar al 4095')
        return False
    
    




def main():
    decimal = input("Dame el numero decimal entero que quieras pasar a Hexadecimal: ") #por teclado entra string
    hexadecimal = interfaz_hexadecimal(decimal) #largo la funcion con el string que entra por teclado
    if hexadecimal != False : #si el valor que me devolvio la funcion es False que no escriba esta linea
        print ("EL valor en hexadecimal es:",hexadecimal)

main()
