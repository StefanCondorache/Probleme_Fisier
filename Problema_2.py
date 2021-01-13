with open("numere.txt","r") as n:
    x=int(n.readline())
    y=int(n.readline())
z_min=str(min(list((x,y)))*3)+'\n'
z_max=str(max(list((x,y)))*2)
with open("produs.txt","w") as p:
    p.write(z_min)
    p.write(z_max)