def EX3_3(n):
    x=0
    y=0
    dx = {'n':1 , 's':-1 }
    dy = {'e':1 , 'w':-1 }
    for i in n:
        x+= dx.get(i,0)
        y+= dy.get(i,0)
    if ( x == 2 and y == 3) or ( x == 3 and y == -4):
        return True
    return False
