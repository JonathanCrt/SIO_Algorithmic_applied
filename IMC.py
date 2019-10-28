poids = int (input("tapez votre poids:"))
taille = float (input("tapez votre taille:"))
imc = poids/(taille*taille)
if imc >=18.5 and imc <= 25 :
    print ("Votre poids est normal !")
else :
    print ("Votre poids est anormal !")
                
