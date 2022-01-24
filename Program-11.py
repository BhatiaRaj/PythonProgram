# Write a program using a function to check whether the number is prime or not. (A prime number is a number that has no divisors.)

x = int(input('Enter an integer: ')) 
prime = True #initial set 
 
for i in range(2,x): 
        if x % i == 0: 
                prime = False 
                break 
 
if prime: 
        print(str(x) + ' is prime.') 
else: 
        print(str(x) + ' is not prime') 
