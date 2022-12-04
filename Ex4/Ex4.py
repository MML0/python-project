
l= {'H':8,'G':7 ,
'F':6 ,'E':5 ,
'D':4 ,'C':3,
'B':2,'A':1}

num = [1,2,3,4,5,6,7,8]

xk = l.get(input('xk h').upper(),'er')
yk = int(input('yk v'))
xb = l.get(input('xb h').upper(),'er')
yb = int(input('yb v'))

rang = [-1,1]
flag = False
flag2 = True

if xk == 'er' or xb == 'er' or yk not in num or yb not in num  :
    print('h k,b er')
    flag2= False
elif xk == xb and yk == yb :
    print("They can't be in the same square")
    flag2= False
elif abs(xk-xb) == abs(yk-yb):
    print("Bishop can attack knight")
    flag2= False
else:
    for i in rang:
        for j in rang:
            if xb+2*i == xk and yb+j == yk:
                flag = True
            if xb+1*i == xk and yb+2*j == yk:
                flag = True
if flag:
    print("knight can attack bishop")
    flag2= False
if flag2:
    print("Neither of them can attack each other")

