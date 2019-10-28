def calcCle(N):
    r=N%11
    if(r>0):
        key=11-r
    elif(r==10):
        key='X'
    else:
        key=0
    return key


#Programme Principal

N=int(input("Entrez le nombre N :"))
print(calcCle(N))
