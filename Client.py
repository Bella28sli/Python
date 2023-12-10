from Database import *
from User import *

class Client(User):
    def __init__(self, login, password, nameC, surnameC, mail):
        super().__init__(login, password)
        self.nameC = nameC
        self.surnameC = surnameC
        self.mail = mail

    def GET_Client_Id(user_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        select_id_user= "SELECT Id_Client FROM clients WHERE Id_User = ?"
        cursor.execute(select_id_user, (user_id))
        client_id = cursor.fetchone()
        return client_id
    
    def INSERT_Client_From_Admin(iflogin, ifpassword, ifname, ifsurname, ifemail):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        client_as_user = [(iflogin, ifpassword, 'Client')]
        try:
            cursor.executemany("INSERT INTO users (Login, Password, Role) VALUES (?, ?, ?)", client_as_user)

            userlogin_to_lookup = iflogin
            select_id_query = "SELECT Id_User FROM users WHERE Login =?"
            cursor.execute(select_id_query, (userlogin_to_lookup,))
            client_id = cursor.fetchone()

            client_as_client = [(ifname, ifsurname, ifemail, client_id[0])]
            cursor.executemany("INSERT INTO clients (Name, Surname, Email, Id_User) VALUES (?, ?, ?, ?)", client_as_client)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()

    def INSERT_Client_From_User(user_id, ifname, ifsurname, ifemail):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            cursor.executemany("UPDATE users SET Role = 'Client' WHERE Id_User = ?", (user_id,))


            client_as_client = [(ifname, ifsurname, ifemail, user_id[0])]
            cursor.executemany("INSERT INTO clients (Name, Surname, Email, Id_User) VALUES (?, ?, ?, ?)", client_as_client)
            print("Вы стали клиентом")
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    
    def UPDATE_Client_Name(user_id, ifname):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        user_id = user_id
        client_name = ifname
        upd_name_query = "UPDATE clients SET Name = ? WHERE Id_User = ?"
        try:
            cursor.execute(upd_name_query, (client_name, user_id))
            conn.commit()
            print("Имя изменено")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()

    def UPDATE_Client_Surname(user_id, ifsurname):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        user_id = user_id
        client_surname = ifsurname
        upd_name_query = "UPDATE clients SET Surname = ? WHERE Id_User = ?"
        try:
            cursor.execute(upd_name_query, (client_surname, user_id))
            conn.commit()
            print("Фвмилия изменена")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()

    def UPDATE_Client_Email(user_id, ifemail):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        user_id = user_id
        client_email = ifemail
        upd_name_query = "UPDATE clients SET Email = ? WHERE Id_User = ?"
        try:
            cursor.execute(upd_name_query, (client_email, user_id))
            conn.commit()
            print("Почта изменена")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()