class errorvacio(Exception):
    pass
class errornolista(Exception):
    pass
class errornonumero(Exception):
    pass



def pipe_fix(pipe):
    if not isinstance(pipe, list):
        raise errornolista("no es lista")
    if len(pipe) < 1:
        raise errorvacio("esta vacio")
    for x in pipe:
        if isinstance(x, str):
            raise errornonumero("tiene letra")
    

    result = []
    for valor in range(pipe[0], pipe[-1]+1):
        result.append(valor)       
    return result