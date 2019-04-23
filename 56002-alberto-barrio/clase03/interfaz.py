from factorial import factorial
def main():
    palabra=input("Ingrese un numero: ")
    print(interfaz(palabra))

def interfaz(data):
    try:    
        n=int(data)
        return factorial(n)
    except:
        return 'ERROR'
