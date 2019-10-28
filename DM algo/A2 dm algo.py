def calcN(code7):
    N=0
    m=8 #Coefficient de formule
    for i in range(7):
        N=N+m*int(code7[i])
        m=m-1
    return N

#Programme Principal


code7=str(input("Tapez les 7 chiffres :"))
print(calcN(code7))

