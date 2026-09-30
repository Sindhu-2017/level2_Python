from services.salary_service import SalaryService

def test_calculate_hra():
    salary_service = SalaryService(None)
    result = salary_service.calculate_hra(30000)
    assert result == 6000


def test_calculate_da():
    salary_service = SalaryService(None)
    result = salary_service.calculate_da(30000)
    assert result == 3000


def test_calculate_bonus():
    salary_service = SalaryService(None)
    result = salary_service.calculate_bonus(30000)
    assert result == 1500


def test_calculate_net_salary():
    salary_service = SalaryService(None)
    result = salary_service.calculate_net_salary(30000,6000,3000,1500)
    assert result == 40500