def n1(tab):
    i = 0
    s = 0
    while i < 3:
        s = s + tab[i]
        i = i + 1
    return s

def n2(tab):
    i = 0
    s = 0
    while i < 3:
        s = s+(i + 1) * tab[i]
        i = i + 1
    return s

#prog principal

tab = [2,17,35,24,51]
if tab[3] == n1(tab) and tab[4] == n2(tab):
    print("Aucune erreur")
else:
    e = 0
    i = 0
    n11 = tab[3]
    n22 = tab[4]
    e = n11 - n1(tab)
    i = int((n22 - n2(tab)) / e)
    i = i - 1
    tab[i] = tab[i] + e
    print(tab)
