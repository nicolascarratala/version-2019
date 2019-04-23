def count_letters(world):
    dic = {}
    for x in world:
        if x in dic:
            dic[x] += 1
        else:
            dic[x] = 1
    return dic