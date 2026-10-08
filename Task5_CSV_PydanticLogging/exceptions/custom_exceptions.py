class EmployeeNotFoundError(Exception):
    def __init__(self, employee_id):
        self.employee_id = employee_id
        super().__init__(f"Employee with ID {employee_id} was not found.")


class InvalidSalaryError(Exception):
    def __init__(self, salary):
        self.salary = salary
        super().__init__(f"Invalid salary: {salary}. Salary must be greater than 0.")


class DataFileError(Exception):
    def __init__(self, file_name):
        self.file_name = file_name
        super().__init__(f"Data file not found: {file_name}")