from abc import ABC, abstractclassmethod
from Database import *
from Employee import *
class Admin(Employee):
    def __init__(self, login, password, nameE, surnameE, salary):
        super().__init__(login, password, nameE, surnameE, salary)
    
    def INSERT_Admin(iflogin, ifpassword, ifname, ifsurname, ifsalary):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        admin_as_user = [(iflogin, ifpassword, 'Admin')]
        try:
            cursor.executemany("INSERT INTO users (Login, Password, Role) VALUES (?, ?, ?)", admin_as_user)

            userlogin_to_lookup = iflogin
            select_id_query = "SELECT Id_User FROM users WHERE Login =?"
            cursor.execute(select_id_query, (userlogin_to_lookup,))
            admin_id = cursor.fetchone()

            admin_as_employee = [(ifname, ifsurname, ifsalary, admin_id[0])]
            cursor.executemany("INSERT INTO staff (Name, Surname, Salary, Id_User) VALUES (?, ?, ?, ?)", admin_as_employee)

            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    
    def SELECT_Orders():
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            select_orders_query = '''SELECT clients.Email, products.NameP
            FROM ((orders
            INNER JOIN clients ON orders.Id_Client = clients.Id_Client)
            INNER JOIN products ON orders.Id_Product = products.ID_Product);'''
            cursor.execute(select_orders_query)
            result = cursor.fetchall()
            print("Почта заказчика   Название товара")
            for row in result:
                print("%s      %s"%(row[0], row[1]))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    
    def INSERT_Order(client_id, product_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        order_info=[(client_id, product_id)]
        try:
            cursor.executemany("INSERT INTO orders (Id_Client, Id_Product) VALUES (?, ?)", order_info)
            conn.commit()
            print("Заказ добавлен")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def UPDATE_ORDER_Client(order_id, client_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        upd_log_query = "UPDATE orders SET Id_Client = ? WHERE Id_Orders = ?"
        try:
            cursor.execute(upd_log_query, (client_id, order_id[0]))
            conn.commit()
            print("Клиент заказа изменён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def UPDATE_ORDER_Product(order_id, product_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        upd_log_query = "UPDATE orders SET Id_Product = ? WHERE Id_Orders = ?"
        try:
            cursor.execute(upd_log_query, (product_id, order_id[0]))
            conn.commit()
            print("Продукт заказа изменён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def DELETE_Order(order_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        delete_query = "DELETE FROM orders WHERE Id_Orders = ?"
        try:
            cursor.execute(delete_query, (order_id[0],))
            conn.commit()
            print("Заказ удалён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()



