import NumerosSecretos

def humano_vs_pc():
    numRandomPc = NumerosSecretos.tres_nums_random()
    numA=input("Escriba num A")
    numB=input("Escriba num B")
    numC=input("Escriba num C")
    numHumano=numA+numB+numC
    NumerosSecretos.es_este_numero_correcto(numHumano,numRandomPc)
    