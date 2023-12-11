from Database import *

class User(Database):
    def __init__(self, login, password):
        self.login = login
        self.password = password
    
    def GET_ID(user_login):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        select_id_user= "SELECT Id_User FROM users WHERE Login = ?"
        cursor.execute(select_id_user, (user_login))
        user_id = cursor.fetchone()
        return user_id
    
    def CheckUserExist(user_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            select_order_exist = "SELECT Id_User FROM users WHERE Id_User = ?"
            cursor.execute(select_order_exist, (user_id,))
            ifid = cursor.fetchone()
            return ifid
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()

    def SELECT_User():
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT Login, Password, Role FROM users")
            result = cursor.fetchall()
            print("Логин   Пароль   Роль")
            for row in result:
                print("%s      %s     %s"%(row[0], row[1], row[2]))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback() 

    def INSERT_User(user_login, user_password, user_role):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        user_info = [(user_login, user_password, user_role)]
        try:
            cursor.executemany("INSERT INTO users (Login, Password, Role) VALUES (?, ?, ?)", user_info)
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    
    def UPDATE_User_Login(user_id, user_login):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        user_id = user_id
        user_login = user_login
        upd_log_query = "UPDATE users SET Login = ? WHERE Id_User = ?"
        try:
            cursor.execute(upd_log_query, (user_login, user_id))
            conn.commit()
            print("Логин изменён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()

    def UPDATE_User_Password(user_id, user_password):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        user_id = user_id
        user_password = user_password
        upd_log_query = "UPDATE users SET Password = ? WHERE Id_User = ?"
        try:
            cursor.execute(upd_log_query, (user_password, user_id))
            conn.commit()
            print("Пароль изменён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()

    def UPDATE_User_Role(user_id, user_role):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        user_id = user_id
        user_role = user_role
        upd_log_query = "UPDATE users SET Role = ? WHERE Id_User = ?"
        try:
            cursor.execute(upd_log_query, (user_role, user_id[0]))
            conn.commit()
            print("Роль изменена")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def IF_DELETE_User(user_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            select_role = "SELECT Role FROM users WHERE Id_User = ?"
            cursor.execute(select_role, (user_id[0],))
            user_role = cursor.fetchone()
            if (user_role[0] == "Client"):
                delete_query = "DELETE FROM clients WHERE Id_User = ?"
                cursor.execute(delete_query, (user_id[0],))
                conn.commit()
                User.__DELETE_User(user_id)
            elif(user_role[0] == "Employee"):
                delete_query = "DELETE FROM staff WHERE Id_User = ?"
                cursor.execute(delete_query, (user_id[0],))
                conn.commit()
                User.__DELETE_User(user_id)
            elif(user_role[0] == "Admin"):
                print("Админа нельзя удалить")
            else:
                User.DELETE_User(user_id)
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def __DELETE_User(user_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            delete_query = "DELETE FROM users WHERE Id_User = ?"
            cursor.execute(delete_query, (user_id[0],))
            conn.commit()
            print("Пользователь удалён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
