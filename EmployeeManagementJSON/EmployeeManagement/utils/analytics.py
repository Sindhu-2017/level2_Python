def display_employees(employees: list[dict]) -> None:

    for number, employee in enumerate(employees, start=1):

        print(
            f"{number}. "
            f"ID: {employee['employee_id']} - "
            f"{employee['employee_name']} - "
            f"{employee['department']} - "
            f"Experience: {employee['experience']}"
        )


def get_departments(employees: list[dict]) -> set[str]:

    return {
        employee["department"]
        for employee in employees
    }


def sort_by_salary(employees: list[dict]) -> list[dict]:

    return sorted(
        employees,
        key=lambda employee: employee["net_salary"],
        reverse=True
    )


def sort_by_experience(employees: list[dict]) -> list[dict]:

    return sorted(
        employees,
        key=lambda employee: employee["experience"],
        reverse=True
    )


def get_highest_salary_employee(
    employees: list[dict]
) -> dict | None:

    if not employees:
        return None

    return max(
        employees,
        key=lambda employee: employee["net_salary"]
    )


def get_department_employees(
    employees: list[dict],
    department: str
) -> list[dict]:

    return [
        employee
        for employee in employees
        if employee["department"].lower() == department.lower()
    ]


def get_experienced_employees(
    employees: list[dict],
    minimum_experience: int
) -> list[dict]:

    return [
        employee
        for employee in employees
        if employee["experience"] >= minimum_experience
    ]


def calculate_average_salary(
    employees: list[dict]
) -> float:

    if not employees:
        return 0.0

    return sum(
        employee["net_salary"]
        for employee in employees
    ) / len(employees)


def check_salary_condition(
    employees: list[dict]
) -> None:

    salaries: list[float] = [
        employee["net_salary"]
        for employee in employees
    ]

    print(
        "All employees have salary above 30000:",
        all(salary > 30000 for salary in salaries)
    )

    print(
        "At least one employee has salary above 60000:",
        any(salary > 60000 for salary in salaries)
    )