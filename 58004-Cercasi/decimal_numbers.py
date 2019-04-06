def decimal_to_roman(decimal_number):
    roman_number=''
    unidad=''
    centena=''
    decena=''
    valores = {1000: 'M',900:'CM',500:'D', 
    400:'CD', 100:'C',90:'XC', 50:'L',40:'XC',10: 'X',9:'IX',5: 'V',4:'IV',1:'I'}
    ant=''
    decimal= str(decimal_number) [::-1]
    cantidad=len(decimal)

    

    if decimal[0] =="0":
        unidad=unidad + ''

    if decimal[0] =='1':
        unidad=unidad + "I"

    if decimal[0]=='2':
        unidad=unidad+ "II"

    if decimal[0]=='3':
        unidad=unidad + "III"

    if decimal[0]=='4':
        unidad=unidad + "IV"

    if decimal[0]=='5':
        unidad=unidad + "V"

    if decimal[0]=='6':
        unidad=unidad + "VI"
        
    if decimal[0]=='7':
        unidad=unidad + "VII"
        
    if decimal[0]=='8':
        unidad=unidad + "VIII"

    if decimal[0]=='9':
        unidad=unidad + "IX"

    if cantidad>=2:

        if decimal[1]=='0':
            decena= decena + ''
        
        if decimal[1]=='1':
            decena=decena + "X"

        if decimal[1]=='2':
            decena= decena + "XX"

        if decimal[1]=='3':
            decena= decena + "XXX"

        if decimal[1]=='4':
            decena=decena + "XL"

        if decimal[1]=='5':
            decena=decena + "L"

        if decimal[1]=='6':
            decena=decena + "LX"
        
        if decimal[1]=='7':
            decena=decena + "LXX"
        
        if decimal[1]=='8':
            decena=decena + "LXXX"
    

    
        roman_number= decena+unidad
   
        
        

             
     
      
    return roman_number