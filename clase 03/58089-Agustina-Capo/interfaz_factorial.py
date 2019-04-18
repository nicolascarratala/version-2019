from factorial import factorial
def interfaz_factorial (number):
    try:
        result = int(number)
        return factorial (result)
    except:
        return 'error'
def main ():
    palabra = ''
    result = interfaz_factorial (palabra)
    print (result)
main ()