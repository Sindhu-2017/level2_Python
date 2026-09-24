import math

# Even or Odd check
def check_even_odd( number : int ) -> int:

    return "Even" if number % 2 == 0 else "Odd"

# Prime number check
def prime_check( number : int ) -> int:

    if number < 2:
        return "Not a Prime"

    if number == "2":
        return "Prime"

    for i in range( 2 , math.floor(math.sqrt(number))+1 ):
        if number % i == 0:
            return "Not a Prime"

    return "Prime"

# Reverse number
def reverse( number : int ) -> int:

    reversed_number = 0

    while number > 0:
        remainder = number % 10
        reversed_number = reversed_number * 10 + remainder
        number = number // 10

    return reversed_number

# Palindrome Check
def palindrome_check ( number : int ) -> int:

    reversed_number = reverse(number)

    return "a Palindrome" if number == reversed_number else "Not a Palindrome"

# Calculating digits
def calculate_digits(number : int) -> int :
    
    count = 0

    while number > 0:
        number = number // 10
        count += 1

    return count


#Armstrong check
def armstrongCheck(number : int) -> int:

    count = calculate_digits(number)
    temp = number
    sum = 0

    while (temp > 0):
        remainder = temp % 10
        sum += remainder ** count
        temp = temp // 10

    return "an Armstrong" if sum == number else "Not an Armstrong"


# Sum of digits
def sum_of_digits (number : int) -> int :

    sum = 0

    while number > 0:
        remainder = number % 10
        sum = sum + remainder
        number = number // 10

    return sum



while True :
    print ("1. Check Even/Odd")
    print ("2. Check Prime")
    print ("3. Reverse Number")
    print ("4. Check Palindrome")
    print ("5. Check Armstrong")
    print ("6. Sum of Digits")
    print ("7. Exit")
    choice = int(input("Enter your choice :"))

    match choice :
        case 1:
            print("1 - Check Even/Odd")
            number = int(input ("Enter the number :"))
            print( f"{ number } is an { check_even_odd(number) } number" )

        case 2:
            print("2 - Prime check")
            number = int(input ("Enter the number :"))
            print(f" {number} is {prime_check(number)} number")

        case 3:
            print("5-Reverse number")
            number = int(input ("Enter the number :"))
            print("Reversed :" ,reverse(number))
            
        case 4:
            print (" 3- Palidrome check")
            number = int(input ("Enter the number :"))
            print(f" {number} is {palindrome_check(number)} number")

        case 5:
            print (" 4 - Armstrong Check")
            number = int(input ("Enter the number :"))
            print(f" {number} is {armstrongCheck(number)} number")
        

        case 6:
            print("6 - Sum of digits")
            number = int(input ("Enter the number :"))
            print(f" Sum of digits : {sum_of_digits(number)}")

        case 7:
            print("Exiting ...")
            break

        case _:
            print("Invalid choice")