print("Enter a number less than 25")
a=int(input())
if a>25:
    print("Error")
else:
    while a<=25: 
        print("Inside the loop, my variable is",a)
        a+=1