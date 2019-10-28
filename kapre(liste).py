def kapre(liste):

    
    

    return[nb1,nb2,nb3]

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




#Programme principal


nb1 = int(input("Tapez un premier chiffre : "))
nb2 = int(input("Tapez un 2éme chiffre : "))
nb3 = int(input("Tapez un 3éme chiffre : "))


    
