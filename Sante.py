poids = int (input("tapez votre poids:"))
taille = float (input("tapez votre taille:"))
imc = poids/(taille*taille)
if imc <=16.5 :
    print ("famine !");
elif imc <= 18.5 :
    print ("maigreur");
elif imc <= 25 :
    print ("normal");
elif imc <= 30 :
    print ("surpoids");
elif imc <= 35 :
    print ("obésité modéré");
elif imc <= 40 :
    print ("obésité sévére")
else :
     print ("t'es enorme....")
                
                
                
                
        
