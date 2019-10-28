notes=[5,12,13.5,10,8] #liste 
compt=0 #on intiale le compteur
for i in range(len(notes)):
    print("-",notes[i])
    if notes[i] >11:
        compt=compt+1
print()
print("Il y a",compt,"notes supéreieures a 11")
#moyenne des notes :
Moyenne=sum(notes)/len(notes)
print("la moyenne des notes est :",Moyenne)
