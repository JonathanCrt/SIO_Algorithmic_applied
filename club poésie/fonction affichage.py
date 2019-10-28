from math import *
from random import *

def affichage (ch1,ch2):
    print(ch1," passera ",ch2)



def tirage_rang ():
    premier= rand(inscrits)
    return premier

    


#Programme principal

inscrits = ["amed","antoine","arthur","charlotte","damien","eliane",
            "françoise","kirthana","lucas","maxime",
            "maimouma","sathya","tiphaine"]
jour =["lundi","mardi","mercredi","jeudi","vendredi"]

for i in range(13):
    tirage_rang()
    affichage(tirage_rang(i),jour[i%4])
    
