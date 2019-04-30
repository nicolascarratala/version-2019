#Juan I. Martinez, Legajo 57018

from hexa_a_dec import conversor

def main():
    print("A continuación podrá ingresar tantos números hexadecimales como desee y convertirlos a decimal")
    print("Para salir, escriba 'SALIR' ")
    while True:
      x = input("\nIngrese un numero: ")
      if x.upper() == "SALIR":     
         break
      else:
         y = interfaz(x)
         print("El numero ingresado en su forma decimal es:", y)


def interfaz(num):
    return conversor(num)


#main() 
#quitar comentario anterior para probar interfaz