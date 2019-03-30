def decimal_a_romano(decimal):
    romano =''


    for letter in decimal:
        if letter == '1':
            romano = 'I'
        if letter == '2':
            romano = 'II'
        if letter == '3':
            romano = 'III'
        if letter == '4':
            romano = 'IV'
        if letter == '5':
            romano = 'V'
    
    return romano