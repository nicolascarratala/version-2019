from cifrador import cifrador

def interfaz_cifrador(x, y):
    try:
        result = cifrador(x, y)
        return result

    except TypeError:
        return "Una variable es INT Type Error"
    except ValueError:
        return "Hay numeros en las variables Value Error"