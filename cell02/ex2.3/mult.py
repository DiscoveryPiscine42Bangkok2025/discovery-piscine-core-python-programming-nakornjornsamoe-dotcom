print("Enter the first number: ")
a=int(input)
print("Enter the second number: ")
b=int(input)
r=a*b
print(a,"x",b,"=",r)
if r>0:
    print("The result is positive.")
elif r<0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")