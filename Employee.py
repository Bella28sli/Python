from Database import *
from User import *

class Employee(User):
    def __init__(self, login, password, nameE, surnameE, salary):
        super().__init__(login, password)
        self.nameE = nameE
        self.surnameE = surnameE
        self.salary = salary
    
    def SELECT_Staff():
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            select_staff_query = '''SELECT staff.Name, staff.Surname, staff.Salary, users.Login
            FROM (staff
            INNER JOIN users ON staff.Id_User = users.Id_User);'''
            cursor.execute(select_staff_query)
            result = cursor.fetchall()
            print("Имя  Фамилия  Зарплата  Аккаунт")
            for row in result:
                print("%s      %s      %d     %s"%(row[0], row[1], row[2], row[3]))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()

    def INSERT_Staff(employee_name, employee_surname, employee_salary, user_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        employee_info = [(employee_name, employee_surname, employee_salary, user_id)]
        try:
            cursor.executemany("INSERT INTO staff (Name, Surname, Salary, Id_User) VALUES (?, ?, ?, ?)", employee_info)
            ifid = User.CheckUserExist(user_id)
            if ifid:
                upd_log_query = "UPDATE users SET Role = 'Employee' WHERE Id_User = ?"
                try:
                    cursor.execute(upd_log_query, (ifid))
                    conn.commit()
                except sqlite3.Error as e:
                    print(f"Error: {e}")
                    conn.rollback()
            else:
                pass
            print("Сотрудник добавлен")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def UPDATE_Staff_Salary(user_id, ifsalary):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        user_id = user_id
        employee_salary = ifsalary
        upd_salary_query = "UPDATE staff SET Salary = ? WHERE Id_User = ?"
        try:
            cursor.execute(upd_salary_query, (employee_salary, user_id[0]))
            conn.commit()
            print("Зарплата изменена")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def UPDATE_Staff_Name(employee_id, ifname):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        upd_name_query = "UPDATE staff SET Name = ? WHERE Id_Staff = ?"
        try:
            cursor.execute(upd_name_query, (ifname, employee_id[0]))
            conn.commit()
            print("Имя изменено")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def UPDATE_Staff_Surname(employee_id, ifsurname):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        upd_surname_query = "UPDATE staff SET Surname = ? WHERE Id_Staff = ?"
        try:
            cursor.execute(upd_surname_query, (ifsurname, employee_id[0]))
            conn.commit()
            print("Фамилия изменена")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def UPDATE_Staff_User(employee_id, user_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        upd_name_query = "UPDATE staff SET Id_User = ? WHERE Id_Staff = ?"
        try:
            cursor.execute(upd_name_query, (user_id, employee_id[0]))
            ifid = User.CheckUserExist(user_id)
            if ifid:
                upd_log_query = "UPDATE users SET Role = 'Employee' WHERE Id_User = ?"
                try:
                    cursor.execute(upd_log_query, (ifid))
                    conn.commit()
                except sqlite3.Error as e:
                    print(f"Error: {e}")
                    conn.rollback()
            else:
                pass
            conn.commit()
            print("Аккаунт изменён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def DELETE_Staff(employee_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            select_id_user= "SELECT Id_User FROM staff WHERE Id_Staff = ?"
            cursor.execute(select_id_user, (employee_id[0],))
            user_id = cursor.fetchone()
            upd_log_query = "UPDATE users SET Role = 'User' WHERE Id_User = ?"
            cursor.execute(upd_log_query, (user_id))
            delete_query = "DELETE FROM staff WHERE Id_Staff = ?"
            cursor.execute(delete_query, (employee_id[0],))
            conn.commit()
            print("Сотрудник удалён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()