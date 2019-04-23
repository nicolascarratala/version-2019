#Sin recurcion
"""def factorial(number):
    result=1
    for n in range(1,number+1):
        result*= n
    return result
"""
#Con recurcion
def factorial(number):
    if number == 1: #condiciion de corte
        return 1
    else:
        return number * factorial(number -1)