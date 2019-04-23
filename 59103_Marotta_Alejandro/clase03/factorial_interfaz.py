from factorial import factorial

def factorial_interfaz(number): 

    try:
        number = int(number)
        result = factorial(number) 
        print (result)
        return result
        
    except Exception as ex:
        print ("Valor no valido")
        print (ex)
        return ("Valor no valido")

            


def main():    
    number1 = input("Ingrese un numero para calcular su factorial: ")
    factorial_interfaz(number1)

main()
