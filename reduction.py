age =int(input("Age : "))
abo =str(input("Abonnement ?(Oui/Non):"))
km = int(input("Nbre de kms parcourus : "))




if (abo=="Non" and age<25) or (abo=="Oui" and hm>=15 ):
    print("Vous bénéficier de la réduction de 25%")
else :
    print ("Vous ne bénéficiez pas de la réduction de 25 %")
tranche=km/5

if km%5>0:
    tranche=tranche+1

if abo="non":
    tarif=100
    tarif2=50+tranche*0.5
    tarif3=tranche*2

    


