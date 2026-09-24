# 8. Menu-Based Number Analyzer 
# Create:
# ===== NUMBER ANALYZER =====

# 1. Check Even/Odd
# 2. Check Prime
# 3. Check Palindrome
# 4. Check Armstrong
# 5. Reverse Number
# 6. Sum of Digits
# 7. Exit
# Use:
# while 
# match-case 
# if/elif/else 
# functions if already covered 
# break 
# This is a good transition from individual programs to small application development.

import math
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

def palindromeCheck(n):
    rev = reverse(n)
    if n == rev:
        return "a palidrome"
    else:
        return "not a palindrome"

def armstrongCheck(n):
    count = calculateDigit(n)
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

def primeCheck(n):
    isPrime = False
    for i in range(2,math.floor(math.sqrt(n))+1):
        if n % i == 0:
            isPrime = True
            break

    if isPrime :
        return "a Prime"
    else:
        return "not a Prime"

while True :
    print ("1. Check Even/Odd")
    print ("2. Check Prime")
    print ("3. Check Palindrome")
    print ("4. Check Armstrong")
    print ("5. Reverse Number")
    print ("6. Sum of Digits")
    print ("7. Exit")
    choice = int(input("Enter your choice :"))

    match choice :
        case 1:
            print("1 - Odd/Even check")
            number = int(input ("Enter the number :"))
            print(number ,"is an",oddEvenCheck(number) ,"number")

        case 2:
            print("2 - Prime check")
            number = int(input ("Enter the number :"))
            print(number,"is",primeCheck(number),"number")
            
        case 3:
            print (" 3- Palidrome check")
            number = int(input ("Enter the number :"))
            print(number ,"is",palindromeCheck(number) ,"number")

        case 4:
            print (" 4 - Armstrong Check")
            number = int(input ("Enter the number :"))
            print(number,"is",armstrongCheck(number),"number")

        case 5:
            print("5-Reverse number")
            number = int(input ("Enter the number :"))
            print("Reversed :" ,reverse(number))

        case 6:
            print("6 - Sum of digits")
            number = int(input ("Enter the number :"))
            print("Sum of digits :" ,sumDigit(number))

        case 7:
            print("Exiting ...")
            break

        case _:
            print("Invalid choice")








