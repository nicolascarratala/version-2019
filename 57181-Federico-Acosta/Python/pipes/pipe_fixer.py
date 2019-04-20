def pipe_fix(pipe):
    x = max(pipe)
    q = min(pipe)
    result = []
    result.append(q)
    while q < x:
        q = q + 1
        result.append(q)        
    return result