def interfaz_factorial (palabra):
   from factorial import factorial
   try:
    n=int(palabra)
    return factorial(n)

   except:
         return 'Error' 