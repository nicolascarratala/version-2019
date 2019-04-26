def pipe_fix(pipe):
    lis=[]
    t=pipe[0]-1
    for i in range(max(pipe)-min(pipe)+1):
        t=t+1
        lis.append(t)
    return lis