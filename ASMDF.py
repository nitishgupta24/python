import os
os.system("CLS")
a=0
while(a!="0"):
        a=input("enter + for additon \nenter - for subtraction\n enter / for division\n enter * for multiplication\n enter // for floor division\n enter 0 to closa a program")
        if(a=="+"):
            os.system("CLS")
            s=int(input("enter the number"))
            d=int(input("enter the number 2"))
            print(s+d)
        elif(a=="-"):
            os.system("CLS")
            s=int(input("enter the number"))
            d=int(input("enter the number 2"))
            print(s-d)
            
        elif(a=="/"):
            os.system("CLS")
            s=int(input("enter the number"))
            d=int(input("enter the number 2"))
            print(s/d)
        elif(a=="*"):
            os.system("CLS")
            s=int(input("enter the number"))
            d=int(input("enter the number 2"))
            print(s*d)
        elif(a=="//"):
            os.system("CLS")
            s=int(input("enter the number"))
            d=int(input("enter the number 2"))
            print(s//d)
        elif(a=="0"):
            break
        else:
            os.system("CLS")
            print("wrong entry")    
os.system("CLS")
print("program terminated succesfully")            
