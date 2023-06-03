import os
os.system("CLS")
l=[2,1,3,5,0,7]
a=max(l)
print(a)
for i in range(len(l)+1):
    for j in range(len(l)):
        if(l[j]!=a):
            l[j]+=1
            print(" - ",end="")
        else:
            
            print(" * ",end="")
    print("\n")            
        