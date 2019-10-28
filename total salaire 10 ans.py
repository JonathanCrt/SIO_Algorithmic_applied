salaire=float(input("Saissisez votre salaire S.V.P:"))
#sdouble=salaire*2
#augmentation =salaire*0.046
annee=0
total=0
for loop in range(10):
    salaire=salaire+salaire*0.046
    annee=annee+1
    total=total+salaire*12
    print(salaire)
   # print("le salaire a double au bout de",annee,"annees")
print("le salarie touchera au total en 10 ans :",total,"euros")
    

