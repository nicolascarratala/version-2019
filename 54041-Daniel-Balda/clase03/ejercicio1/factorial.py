#Sin Recursividad
"""
def factorial(number):
    result=1
    for n in range(1,number+1):
        result*=n
    return result
"""
#Con Recursividad

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)