import re
nume=str(input("Introdu numele si prenumele: "))
a, b=nume.split()
c=0
f=0
if (a.title()==a):
    for i in a:
        if (ord(i)<=122) and (ord(i)>=65):
            c=0
        else:
            c=1
else:
    c=1
    
if (b.title()==b) :
    for e in b:
        if (ord(e)<=122) and (ord(e)>=65):
            f=0
        else:
            f=1
else:
    f=1

if (c==0) and (f==0):
    print("Corect")
elif (c==1) and (f==1):
    print("Error")