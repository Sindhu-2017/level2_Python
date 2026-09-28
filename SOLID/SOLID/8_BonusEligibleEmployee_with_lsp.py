class Employee:

    def calculate_salary(self):
        raise NotImplementedError


class BonusEligibleEmployee(Employee):

    def calculate_bonus(self):
        raise NotImplementedError


class PermanentEmployee(BonusEligibleEmployee):

    def calculate_salary(self):
        return 50000

    def calculate_bonus(self):
        return 5000


class Contractor(Employee):

    def calculate_salary(self):
        return 40000


def display_salary(employee):
    print("Salary:", employee.calculate_salary())


def display_bonus(employee):
    print("Bonus:", employee.calculate_bonus())


permanent = PermanentEmployee()
contractor = Contractor()

display_salary(permanent)
display_bonus(permanent)

display_salary(contractor)