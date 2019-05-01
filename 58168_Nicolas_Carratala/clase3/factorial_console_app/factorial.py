def factorial_num(n):
        if n==1:
            return 1
        else:
            return n*factorial_num(n-1)