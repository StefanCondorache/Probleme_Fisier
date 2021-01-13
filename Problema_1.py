with open("numere.txt","r") as n:
    x=int(n.readline())
    y=int(n.readline())
z=min(list((x,y)))
with open("minim.txt","w") as m:
    m.write(str(z))