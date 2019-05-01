
def dictionary_creator(word):
    
    dic={}
    large=len(word)
    wList=[]

    for valor in word:
        wList.append(valor)

    for clave in range(0,large):
        dic[clave]=wList[clave]

    return dic
