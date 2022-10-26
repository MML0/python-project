def EX1_5(a) :
    '''
    (Float) => str
    '''
    if a<=1:
        return('infant')
    elif a<13:
        return('child')
    elif a<20:
        return('teenager')
    else:
        return('adult')
