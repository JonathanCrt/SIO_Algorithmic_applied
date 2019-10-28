def croiss(liste):
    n=len(liste)
    i=1
    while i <n :
        k=0
        while k<i:
            if liste[i]<liste[k]:
                liste[i],liste[k]=liste[k],liste[i]
            k=k+1
        i=i+1
    return liste 


