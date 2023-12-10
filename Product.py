from Database import *

class Product(Database):
    def __init__(self, nameP, number, price):
        self.nameP = nameP
        self.number = number
        self.price = price
    
    def INSERT_Product(ifname, ifnumber, ifprice):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        product_info = [(ifname, ifnumber, ifprice)]
        try:
            cursor.executemany("INSERT INTO products (NameP, Number, Price) VALUES (?, ?, ?)", product_info)
            conn.commit()
            print("Продукт добавлен")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    

    def SELECT_ALL():
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT NameP, Price, Number, Id_Product FROM products")
            result = cursor.fetchall()
            print("Название          Цена(руб)   Кол-во  Артикул")
            for row in result:
                print("%s      %d     %d    %d"%(row[0], row[1], row[2], row[3]))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def SELECT_BY_PRICE():
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT NameP, Price, Number, Id_Product FROM products order by Price")
            result = cursor.fetchall()
            print("Название          Цена(руб)   Кол-во  Артикул")
            for row in result:
                print("%s      %d     %d    %d"%(row[0], row[1], row[2], row[3]))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def SELECT_BY_NAME():
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT NameP, Price, Number, Id_Product FROM products order by NameP")
            result = cursor.fetchall()
            print("Название          Цена(руб)   Кол-во  Артикул")
            for row in result:
                print("%s      %d     %d    %d"%(row[0], row[1], row[2], row[3]))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    def SELECT_BY_NUMBER():
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT NameP, Price, Number, Id_Product FROM products order by Number")
            result = cursor.fetchall()
            print("Название          Цена(руб)   Кол-во  Артикул")
            for row in result:
                print("%s      %d     %d    %d"%(row[0], row[1], row[2], row[3]))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    
    def SHOW_ORDER(client_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        summ = 0
        try:
            select_order_query = '''SELECT NameP, Price, products.Id_Product 
            FROM products 
            INNER JOIN orders 
            ON products.Id_Product = orders.Id_Product
            WHERE Id_Client = ?;'''
            cursor.execute(select_order_query, (client_id))
            result = cursor.fetchall() 
            print("Название          Цена(руб)   Артикул")
            for row in result: 
                print("%s      %d     %d"%(row[0], row[1], row[2]))
                summ = summ + row[1]
            print(f"Сумма заказа: {summ} руб.")
            conn.commit() 
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()

    def Enough_Products(product_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        select_number= "SELECT Number FROM products WHERE Id_Product = ?"
        cursor.execute(select_number, (product_id))
        number = cursor.fetchone()
        if (number[0]>0):
            return True
        else:
            return False
    def Reduce_Product(product_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        try:
            select_number= "SELECT Number FROM products WHERE Id_Product = ?"
            cursor.execute(select_number, (product_id))
            number = cursor.fetchone()
            new_number = (number[0]-1)
            reduce_query = "UPDATE products SET Number = ? WHERE Id_Product = ?"
            cursor.execute(reduce_query, (new_number, product_id[0]))
            conn.commit()
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    
    def INSERT_Order(client_id, product_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        order_info = [(client_id[0], product_id[0])]
        try:
            cursor.executemany("INSERT INTO orders (Id_Client, Id_Product) VALUES (?, ?)", order_info)
            conn.commit()
            print("Товар добавлен в заказ")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    
    def DELETE_In_Order(client_id, product_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        delete_query = "DELETE FROM orders WHERE Id_Product = ? AND Id_Client = ?"
        try:
            cursor.execute(delete_query, (product_id[0], client_id[0]))
            conn.commit()
            print("Товар удалён из заказа")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()
    
    def DELETE_Product(product_id):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        delete_query = "DELETE FROM products WHERE Id_Product = ?"
        try:
            cursor.execute(delete_query, (product_id[0],))
            conn.commit()
            print("Товар удалён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()

    def UPDATE_Product_Name(product_id, product_name):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        upd_namep_query = "UPDATE products SET NameP = ? WHERE Id_Product = ?"
        try:
            cursor.execute(upd_namep_query, (product_name, product_id[0]))
            conn.commit()
            print("Товар изменён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()

    def UPDATE_Product_Number(product_id, product_number):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        upd_number_query = "UPDATE products SET Number = ? WHERE Id_Product = ?"
        try:
            cursor.execute(upd_number_query, (product_number, product_id[0]))
            conn.commit()
            print("Товар изменён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()

    def UPDATE_Product_Price(product_id, product_price):
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        upd_price_query = "UPDATE products SET Price = ? WHERE Id_Product = ?"
        try:
            cursor.execute(upd_price_query, (product_price, product_id[0]))
            conn.commit()
            print("Товар изменён")
        except sqlite3.Error as e:
            print(f"Error: {e}")
            conn.rollback()