#Programme qui indique la parité du nb saisi

p,i='',''

pari=input("pair(p) ou impair(i):")
nb=input("Saisir un nombre entier :")

if (pari == 'p' and nb%2 ==0 or pari=='i' and nb%2 != 0  ):
        print("Gagné")
else : 
     print("perdu")



