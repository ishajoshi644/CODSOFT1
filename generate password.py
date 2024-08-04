import random;                          
le=[]

len = int(input("Enter the length of password->>  "))  
for i in range(0,len):                         
    a=random.randint(0,165)
    if(a==35 or a==64):
        b=chr(a)
        le.append(b)
    elif(a>=48 and a<=57):
        b=chr(a)
        le.append(b)
    elif(a>=65 and a<=90):
        b=chr(a)
        le.append(b)
    elif(a>=97 and a<=122):
        b=chr(a)
        le.append(b)
    else:
        a=random.randint(0,9)
        le.append(a)
    


print("Your password is - >  ")         
for j in le:                                     
    print(j,end="")                                 # print final password

    