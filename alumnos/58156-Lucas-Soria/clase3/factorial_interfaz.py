from factorial import factorial



def factorial_interfaz(number): 

    try:
        result = int(number)   
        if abs(result) != result:
            result = "Error, el valor ingresado no es un numero entero positivo"
        return result
    except:
        return "Error, el valor ingresado no es un numero entero"
            


def main():    
    number = input("Ingrese un numero para calcular su factorial: ")
    result = factorial_interfaz(number)
    result = factorial(int(number))
    print(result)

main()
