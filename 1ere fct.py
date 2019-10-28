def f(x):
    if x >=-2 and x < 5 :
        return -3*x+2
    elif x>=5 and x<=12:
        return 5

print ("\t x \t | \t f(x) ")

for x in range (-2,13):
    print ("\t", x ,"\t|\t",f(x))
