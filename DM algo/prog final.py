def calcN(code7):
    N=0
    m=8 #Coefficient de formule
    for i in range(7):
        N=N+m*int(code7[i])
        m=m-1
    return N

def calcCle(N):
    r=N%11
    if(r>0):
        key=11-r
    elif(r==10):
        key='X'
    else:
        key=0
    return key

def ISSNok(code8):
    N=0
    m=8
    for i in range (7):
        N=N+m*int(code8[i])
        m=m-1
    r=N%11
    key=0
    if(r==0):
        key=0
    elif(r==10):
        key='X'
    else:
        key=11-r
    if(key==int(code8[7])):
       return True
    else:
       return False


#Programme Principal :
code7=str(input("Tapez les 7 chiffres :"))
print("Clé de contrôle:",calcCle(calcN(code7)))
print("ISSN complet : ",code7,calcCle(calcN(code7)))
code8=str(input("Entrez les 8 chiffres ISSN:"))
if (ISSNok(code8)==True):
    print("ISSN valide")
else:
    print("ISSN non valide")




    




