from factorial import factorial_num

def main():
    a=input('Ingrese un numero para factorizar:')
    factorial_interface(minor_to_zero(a))

def minor_to_zero(data):
    if data<0:
        print('Se necesita un numero mayor a 0')
        return 'ERROR'
    else:
        return data 

def factorial_interface(data):
    try:
        a=int(data)
        return factorial_num(data)
    except:
        return 'ERROR'   

"""run
main()"""