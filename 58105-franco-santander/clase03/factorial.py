def factorial(numero):

    """
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -=1
    return factorial """

    if numero == 1:
        return 1
    else:
        return numero * factorial (numero - 1)



