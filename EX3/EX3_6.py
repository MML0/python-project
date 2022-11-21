def EX3_6(n) :
    if len(n):
        s = max(n)-min(n)
    else :
        return ':/'
    try:
        n.index(s)
        return ":)"
    except:
        return ':('
