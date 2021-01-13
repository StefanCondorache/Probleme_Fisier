with open("numar.txt","r") as n:
    x=int(n.readline())
with open("inmultire.txt","w") as i:
    for k in range(11): 
        z=str(x)+' * '+str(k)+' = '+str(k*x)+'\n'
        i.write(z)