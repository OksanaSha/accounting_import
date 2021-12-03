from datetime import datetime
from application.db.people import get_employees
from application.salary import calculate_salary

if __name__ == '__main__':
    print(f'start main.py on {datetime.today().strftime("%d-%m-%Y")}')
    calculate_salary()
    get_employees()

