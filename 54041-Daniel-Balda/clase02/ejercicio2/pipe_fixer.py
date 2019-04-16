def pipe_fix(pipe):
    lower = pipe[0] #Primera Posicion de la lista
    upper = pipe[-1] #Ultima posicion "   "   "
    pipe_inc = [] #Nueva Lista
    while lower <= upper: #Mientras lower sea menor o igual que upper 
        pipe_inc.append(lower) #append = Agrega elementos
        lower += 1
    return pipe_inc