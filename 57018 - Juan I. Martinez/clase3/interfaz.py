from factorial import factorial

def main():
   while True:
      x = input("Ingrese un numero: ")
      y = interfaz_factorial(x)
      if type(y) == int:      #Si no se ingresa un numero no sale del loop
         print("El factorial del numero ingresado es: ", y)
         break


def interfaz_factorial(val):
    try:
       nro = int(val)
       return factorial(nro)
    except ValueError:
       return "Error"

        

#main()  

'''
borrar el comentario de arriba si se quiere probar la funcion main,
se comento para que no interfiera con el test

'''
