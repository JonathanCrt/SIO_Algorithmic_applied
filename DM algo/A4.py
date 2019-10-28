

def ISSNok(code8):
    N=0
    m=8
    for i in range (7):
        N=N+m*int(code8[i])
        m=m-1
    r=N%11
    key=0
    if(r==0):
        key=0
    elif(r==10):
        key='X'
    else:
        key=11-r
    if(key==int(code8[7])):
       return True
    else:
       return False

#Programme Principal

code8=str(input("Saissisez le code ISSN:"))

print(ISSNok(code8))

