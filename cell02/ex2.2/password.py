print("Enter the frist number:")
a=int(input())
print("Enter the second number:")
b=int(input())
r=a*b
if r<0:
    print(a,"x",b,"=",r)
    print("The result is negative.")
elif r>0:
    print(a,"x",b,"=",r)
    print("The result is positive.")
else:
    print(a,"x",b,"=",r)
    print("The result is positive and negative.")