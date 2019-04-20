def pipe_fix(pipe):
    if not pipe:
        return None
    
    fixed_pipe= list (range(pipe[0], pipe[-1]+1))

    return fixed_pipe

 