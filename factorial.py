def factorial(n):  
    if n == 1:  
        return n  
    else:  
        return n*factorial(n-1)  
      
number = int(input("Enter a number: "))  
   
if number < 0:  
    print("Sorry, factorial does not exist for negative numbers")  
elif number == 0:  
    print("The factorial of 0 is 1")  
else:  
    print("The factorial of",number,"is",factorial(number))
