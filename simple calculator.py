print("ARITHMETIC OPERATIONS")
a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
c=input("enter operation choice:")
if(c=="+"):
    print("addition of 2 numbers =",a+b)
elif(c=="-"):
    print("subtraction of 2 numbers =",a-b)
elif(c=="/"):
    print("division of 2 numbers =",a/b)
elif(c=="%"):
    print("remainder of 2 numbers =",a%b)
elif(c=="*"):
    print("multiplication of 2 numbers =",a*b)
else:
    print("error")
