# Assignment1 Simple Python Programs
# 1)Python Program to Check Whether a Given Number is Even or Odd using Recursion
def oddEven_recur(n):
    if n==0:
        return True
    elif n==1:
        return False
    else:
        return oddEven_recur(n-2)

num=int(input("Enter a number to check even/odd"))
if oddEven_recur(num):
    print(num,"is even")
else:
    print(num,"is odd")
# Enter a number to check even /odd: 10
# 10 is even.


# 2)Python Program to Check Whether a Number is Positive or Negative
n=int(input("Enter number: "))
if(n>0):
    print("Number is positive")
else:
    print("Number is negative")
# Output

# Enter number: 45
# Number is positive
 

# Enter number: -30
# Number is negative


# 3)Python Program to Print All Odd Numbers in a Range
lower=int(input("Enter the lower limit for the range:"))
upper=int(input("Enter the upper limit for the range:"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)
# Output
# Enter the lower limit for the range:1
# Enter the upper limit for the range:16
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15


# 4)Python Program to Check if a Number is a Palindrome using Built-in Function
# Palindrome Program in Python using Built-in Function
 
def is_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))
 
# Get the number from the user
n = int(input("Enter number: "))
 
# Check if the number is a palindrome
if is_palindrome(n):
  print("The number is a palindrome!")
else:
  print("The number is not a palindrome.")

# OutPut
# Enter number:12321
# The number is a palindrome!


# 5 Python Program to Find the Fibonacci Series Without using Recursion
a=int(input("Enter the first number of the series "))
b=int(input("Enter the second number of the series "))
n=int(input("Enter the number of terms needed "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1

# output
# Enter the first number of the series 0
# Enter the second number of the series 1
# Enter the number of terms needed 4
# 0 1 1 2 
 

# Enter the first number of the series 2
# Enter the second number of the series 4
# Enter the number of terms needed 5
# 2 4 6 10 16