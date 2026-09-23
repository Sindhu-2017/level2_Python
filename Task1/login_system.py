# 6. Login System 
# Create a simple login system.
# Requirements:
# Store username and password. 
# Allow maximum 3 attempts. 
# If credentials are correct → Login successful. 
# Otherwise → Display remaining attempts. 
# After 3 failed attempts → Account locked. 
# Use loops and conditions. 

username = "Sindhu123"
password = "1234@5678"

attempts = 0
max_attempts = 3

while attempts < max_attempts :
    attempts += 1
    username_input = input ("Enter the username :")
    password_input = input ("Enter the password :")

    if username_input == username and password_input == password:
        print ("Login successful")
        break
    else :
        print ("Only " , max_attempts -attempts," attempts are remaining")

if attempts == max_attempts :
    print ("Account locked")