from random import randint, uniform,random



def tres_nums_random():
    numA= randint(0,9)
    numB= randint(0,9)
    numC= randint(0,9)
    total=str(numA)+str(numB)+str(numC)
    return int(total)

def es_este_numero_correcto(num,numRandomPc):
    noEcontrado=True
    a=False
    b=False
    c=False
    while(noEcontrado):
        if num[0]==numRandomPc[0]:
            a=True
            if num[1]==numRandomPc[1]:
                b=True
                if num[2]==numRandomPc[2]:
                    c=True
                    noEcontrado=False
                else:
                    pass
            else:
                pass
        else:
            pass

    if noEncontrado==True:
        print('Winner')
    else:
        print('Loser')