"""
def factorial (number):
    T=1
    for n in range(number):
        T=T*(n+1)
    return T 
"""

def factorial(n):

    if n==1:
        return 1

    else:
        return (n* factorial (n-1))  #recursion, llama a la funcion -factorial(n)-
