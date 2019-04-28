def Convert(numbers):

    if numbers < 0:
        return (0)
    elif numbers <= 9:
        return (numbers)
    else:
        List = ''
        j = 1
        div = int(numbers / 16)
        while div != 0:
            div = int(div / 16)
            j = j + 1

        for i in range(1):
            rest = (numbers % 16)
            if rest < 10:
                List = List + str(rest)
            if rest == 10:
                List = List + str('A')
            if rest == 11:
                List = List + str('B')
            if rest == 12:
                List = List + str('C')
            if rest == 13:
                List = List + str('D')
            if rest == 14:
                List = List + str('E')
            if rest == 15:
                List = List + str('F')

        for i in range(j - 1):
            numbers = int(numbers / 16)
            rest = (numbers % 16)
            if rest < 10:
                List = List + str(rest)
            if rest == 10:
                List = List + str('A')
            if rest == 11:
                List = List + str('B')
            if rest == 12:
                List = List + str('C')
            if rest == 13:
                List = List + str('D')
            if rest == 14:
                List = List + str('E')
            if rest == 15:
                List = List + str('F')
        invert = List[::-1]

        return (invert)