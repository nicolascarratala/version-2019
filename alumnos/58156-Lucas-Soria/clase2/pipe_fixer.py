def pipe_fix(pipe):
    if not pipe: return None
    else:
        pipe_fixed = [i for i in range(pipe[0], pipe[-1] + 1)]
        return pipe_fixed