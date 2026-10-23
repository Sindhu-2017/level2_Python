class EmployeeNotFoundError(Exception):
    def __init__(self, employee_id):
        self.employee_id = employee_id
        message = f"Employee with ID {employee_id} not found."
        super().__init__(message)


class InvalidSalaryError(Exception):

    def __init__(self, message):
        super().__init__(message)


class DataFileError(Exception):

    def __init__(self, message):
        super().__init__(message)
