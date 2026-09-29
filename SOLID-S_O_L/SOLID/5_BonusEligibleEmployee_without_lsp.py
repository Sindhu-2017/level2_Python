class Employee:

    def calculate_salary(self):
        pass

    def calculate_bonus(self):
        pass


class PermanentEmployee(Employee):

    def calculate_salary(self):
        return 50000

    def calculate_bonus(self):
        return 5000


class Contractor(Employee):

    def calculate_salary(self):
        return 40000

    def calculate_bonus(self):
        raise NotImplementedError(
            "Contractors are not eligible for bonus"
        )


def display_employee_details(employee):

    print("Salary:", employee.calculate_salary())
    print("Bonus:", employee.calculate_bonus())


permanent = PermanentEmployee()
display_employee_details(permanent)

contractor = Contractor()
display_employee_details(contractor)