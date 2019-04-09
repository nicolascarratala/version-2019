def pipe_fix(broken_pipe):
        first=broken_pipe[0]
        last=broken_pipe[-1]
        fixed_pipe=[]
        while first <= last:
            fixed_pipe.append(first)
            first += 1
        return fixed_pipe