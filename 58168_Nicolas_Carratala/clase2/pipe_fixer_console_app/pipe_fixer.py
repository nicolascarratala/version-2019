def pipe_fix(tuberiaRota):
    
    largo=len(tuberiaRota)
    primerNum=tuberiaRota[0]
    elUltimo=tuberiaRota[largo-1]
    nuevaTuberia=[]

    print('Tuberia rota:')
    print(tuberiaRota)

    for x in range(primerNum,elUltimo+1):
        nuevaTuberia.append(x)
      
    print('Tuberia arreglada')
    print(nuevaTuberia)
    print('----------')
    
    return nuevaTuberia
   
    



    

    
