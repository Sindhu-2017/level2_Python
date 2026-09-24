# 7. Number Analyzer 
# Given a number, display:
# Number of digits
# Sum of digits
# Product of digits
# Reverse
# Even/Odd
# Prime/Not Prime
# Palindrome/Not Palindrome
# Armstrong/Not Armstrong

def calculateDigit(n):
    count = 0
    while n > 0:
        n = n // 10
        count += 1
    return count

def sumDigit (n) :
    sum = 0
    while n > 0:
        rem = n % 10
        sum = sum + rem
        n = n // 10
    return sum

def productDigit (n):
    product = 1
    while n > 0:
        rem = n % 10
        product = product * rem
        n = n // 10
    return product

def reverse(n):
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev

def oddEvenCheck(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

def palindromeCheck(n,rev):
    if n == rev:
        return "a palidrome"
    else:
        return "not a palindrome"

def armstrongCheck(n,count):
    temp = n
    sum = 0
    while (temp > 0):
        rem = temp % 10
        sum += rem ** count
        temp = temp // 10

    if sum == n:
        return "an Armstrong"
    else :
        return "not an Armstrong"

number = int(input ("Enter the number :"))
digits=calculateDigit(number)
print("Number of digits :" ,digits)
print("Sum of digits :" ,sumDigit(number))
print("Product of digits :" ,productDigit(number))
reversed = reverse(number)
print("Reversed :" ,reversed)
print(number ,"is an",oddEvenCheck(number) ,"number")
print(number ,"is",palindromeCheck(number,reversed) ,"number")
print(number,"is",armstrongCheck(number,digits),"number")



