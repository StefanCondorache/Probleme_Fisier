with open("globulete.txt","r") as g:
    alb=int(g.readline())
with open("bradut.txt","w") as b:
    rosii=alb+3
    alb_=(alb+rosii)-2
    suma=str(rosii+alb+alb_)
    b.write(suma)