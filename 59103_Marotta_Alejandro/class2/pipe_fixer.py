def pipe_fix(pipe):
    try:
        pipe_new = []
        for valor in range (pipe[0],pipe[-1]+1):
            pipe_new.append(valor)
        return pipe_new
    except TypeError as ex:
        print (ex)
        return ("Valor no valido")

