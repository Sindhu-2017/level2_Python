import pytest
@pytest.fixture
def salary_data():

    return [
        {
            "basic_salary": 30000,
            "hra": 6000,
            "da": 3000,
            "bonus": 1500,
            "net_salary": 40500
        },
        {
            "basic_salary": 40000,
            "hra": 8000,
            "da": 4000,
            "bonus": 2000,
            "net_salary": 54000
        },
        {
            "basic_salary": 50000,
            "hra": 10000,
            "da": 5000,
            "bonus": 2500,
            "net_salary": 67500
        }
    ]