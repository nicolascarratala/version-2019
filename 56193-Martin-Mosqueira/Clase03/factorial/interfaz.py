from factorial import factorial

def main():
    palabra=input("ingrese un numero: ")
    print(isnumber(palabra))

def isnumber(data):
    try:
        n=int(data)
        return factorial(n)
    except:
        return "ERROR"

main()
