# 2. Employee Salary Analyzer
#
# Accept:
#
# Employee name
#
# Basic salary
#
# Experience
#
# Calculate:
#
# HRA
#
# DA
#
# Gross salary
#
# Bonus based on experience
#
# Final salary category

employee_name = input("Enter employee name: ")
basic_salary = float(input("Enter basic salary: "))
experience = float(input("Enter experience: "))
da = 0
hra = 0
if basic_salary > 20000:
    da = basic_salary * 58.5/100
    hra = basic_salary * 15.0/100
elif basic_salary > 15000:
    da = basic_salary * 0.46/100
    hra = basic_salary * 0.12/100
else:
    da= basic_salary * 0.425
    hra= 1500

gross_salary = basic_salary + hra + da
bonus = 0

if experience >= 10:
    bonus = 20000
elif experience >= 5:
    bonus = 12000
elif experience >= 2:
    bonus = 8000
else:
    bonus = 2000

final_salary = gross_salary + bonus

salary_category = ""
if gross_salary >= 100000 :
    salary_category = "High Salary"
elif gross_salary >= 50000 :
    salary_category = "Medium Salary"
else:
    salary_category = "Low Salary"

print("Employee Name : ",employee_name)
print("Basic Salary : ",basic_salary)
print("Experience : ",experience)
print("HRA : ",hra)
print("DA : ",da)
print("Grade : ",salary_category)
print("Bonus : ",bonus)
print("Final Salary",final_salary)




