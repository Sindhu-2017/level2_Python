from services.salary_service import SalaryService

def test_calculate_hra(salary_data):
    salary_service = SalaryService(None)
    for data in salary_data:
        result = salary_service.calculate_hra(data["basic_salary"])
        assert result == data["hra"]

def test_calculate_da(salary_data):
    salary_service = SalaryService(None)
    for data in salary_data:
        result = salary_service.calculate_da(data["basic_salary"])
        assert result == data["da"]


def test_calculate_bonus(salary_data):
    salary_service = SalaryService(None)
    for data in salary_data:
        result = salary_service.calculate_bonus(data["basic_salary"])
        assert result == data["bonus"]


def test_calculate_net_salary(salary_data):
    salary_service = SalaryService(None)
    for data in salary_data:
        result = salary_service.calculate_net_salary(
            data["basic_salary"],
            data["hra"],
            data["da"],
            data["bonus"]
        )

        assert result == data["net_salary"]