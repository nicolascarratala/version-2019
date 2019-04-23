def codigo(clave,frase):

    abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    clave2=''
    
    cifrado=''

    if len(clave)<len(frase):
        for vuelta in range(int(len(frase)/len(clave))):
            clave2=clave2+clave

        clave2=clave2 + clave [:len(clave)%len(frase)]
    
    elif len(frase)<len(clave):	# Si la longitud del mensaje es menor que la de la clave...
	    clave2 = clave[:len(frase)]	# Se trunca la clave para que tenga la misma longitud que el mensaje #

    elif len(frase)==len(clave):	# Si la longitud del mensaje es igual que la de la clave... #
        clave2 = clave 

    for vuelta2 in range(len(frase)):
        x = abc.find(frase[vuelta2])	# Se guarda la posición del caracter del mensaje en el abecedario
        y= abc.find(clave2[vuelta2])	# Se guarda la posición del caracter de la clave en el abecedario
        suma = x+y	# Se calcula la suma de ambas posiciones
        modulo = suma%len(abc)	# Se calcula el módulo de la suma respecto a la longitud del abecedario
        cifrado= cifrado+abc[modulo] 
    
    return cifrado

    print ('Mensaje cifrado: ' + cifrado)   

