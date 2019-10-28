salaire=float(input("Saissisez votre salaire S.V.P:"))
sdouble=salaire*2
augmentation =salaire*0.046
annee=0

while (salaire < sdouble):
    salaire=salaire+salaire*0.046
    annee=annee+1
    print(salaire)
print("le salaire a double au bout de",annee,"annees")
 
