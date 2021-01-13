with open("input.txt","r") as i:
    x=int(i.readline())
list1=list((str(x-2)+' ',str(x-1)+' ',str(x)+' ',str(x+1)+' ',str(x+2)))
with open("output.txt","w") as o:
    for y in list1:    
        o.write(y)