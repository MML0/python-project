def EX3_2(n):
    a=[]
    for i in range (len(n)-1):
        a+=[n[i]*n[i+1]]
    return max(a)
