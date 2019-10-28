def nbracine(a,b,c):
    delta=b*b-4*a*c
    if delta > 0 :
        return 2 
    else:
        return 0
#Programme principal :
a=float (input('a ?'))
b=float (input('b ?'))
c=float (input('c ?'))
print ("Il y a ",nbracine(a,b,c),"racines")
