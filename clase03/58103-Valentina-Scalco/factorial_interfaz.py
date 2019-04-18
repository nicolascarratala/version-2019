from factorial import factorial
def factorial_interfaz(number):
    try:
        result = int(number)
        return result
    except:
        return 'Error'
def main():
    palabra = ''
    result = factorial_interfaz (palabra)
    print (result)
main()