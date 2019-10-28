from math import * 


n= int (input("Tapez un nombre : "))
nb_restant=n
liste=[]
while nb_restant >0 :
    chiffre = nb_restant%10
    liste.append(chiffre)
    nb_restant=(nb_restant-chiffre)//10
print(n," devient",liste)
