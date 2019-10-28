from math import*

def creliste(nbre):
    un=nbre%10
    nbre=(nbre-un)/10
    dix=nbre%10
    cent=(nbre-dix)/10

    return[cent,dix,un]

    
