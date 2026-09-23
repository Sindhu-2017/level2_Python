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



number = int(input ("Enter the number :"))
print("Number of digits :" ,calculateDigit(number))
print("Sum of digits :" ,sumDigit(number))
print("Product of digits :" ,productDigit(number))
print("Reversed :" ,reverse(number))

