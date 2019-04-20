from factorial import factorial

def main():
    palabra = input("input: ")
    print(interfaz(palabra))

def interfaz(p):

    try:
        n = int(p)
        return factorial(n)

    except:
        return "error"

main()
        

