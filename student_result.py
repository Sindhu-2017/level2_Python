# 1. Student Result Analyzer  

# Create a program that: 

# Accepts student name.  

# Accepts marks for 5 subjects.  

# Calculates total.  

# Calculates average.  

# Determines grade.  

# Determines Pass/Fail.  

# Validates that marks are between 0 and 100.  

student_name = input(" Enter student name : ")
tamil_mark = int (input("Enter the mark for Tamil :"))
english_mark = int (input("Enter the mark for English :"))
maths_mark = int (input("Enter the mark for Maths :"))
science_mark = int (input("Enter the mark for Science :"))
social_mark = int (input("Enter the mark for Social :"))

marks = [ tamil_mark , english_mark , maths_mark , science_mark , social_mark ]
total = 0
for mark in marks :
    if mark < 0 or mark > 100 :
        print ("Invalid marks")

    total = total + mark

average = total / 5
grade = ""
result = ""

if average >= 90:
    grade = "A"
    result = "PASS"

elif average >= 80:
    result = "PASS"
    grade = "B"

elif average >= 70:
    grade = "C"
    result = "PASS"

elif average >= 60:
    grade = "D"
    result = "PASS"

elif average >= 40:
    grade = "E"
    result = "PASS"

else:
    grade = "F"
    result = "FAIL"

print ("Student Name :" , student_name)
print()
print("Tamil : ",tamil_mark)
print("English : ",english_mark)
print("Maths : ",maths_mark)
print("Science : ",science_mark)
print("Social : ",social_mark)
print()
print("Total :",total)
print("Average : ",average)
print("Grade : ",grade)
print("Result : ",result)



    
