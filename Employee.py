from Database import *
from User import *

class Employee(User):
    def __init__(self, login, password, nameE, surnameE, salary):
        super().__init__(login, password)
        self.nameE = nameE
        self.surnameE = surnameE
        self.salary = salary
    
    def UPDATE_Staff_Salary(user_id, ifsalary):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        user_id = user_id
        employee_salary = ifsalary
        upd_salary_query = "UPDATE staff SET Salary = ? WHERE Id_User = ?"
        try:
            cursor.execute(upd_salary_query, (employee_salary, user_id))
            conn.commit()
            print("Зарплата изменена")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()