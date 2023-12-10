import sqlite3 
from abc import ABC, abstractclassmethod

class Database(ABC):
    @staticmethod
    def DBCreate():
        conn = sqlite3.connect('RecordStudio.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                Id_User INTEGER PRIMARY KEY AUTOINCREMENT,
                Login TEXT NOT NULL,
                Password TEXT NOT NULL,
                Role TEXT NOT NULL
            )
        ''' )
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                Id_Product INTEGER PRIMARY KEY AUTOINCREMENT,
                NameP TEXT NOT NULL,
                Number INTEGER NOT NULL,
                Price INTEGER NOT NULL
            )
        ''' )
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS staff (
                Id_Staff INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Surname TEXT NOT NULL,
                Salary INTEGER NOT NULL,
                Id_User INTEGER UNIQUE,
                FOREIGN KEY (Id_User) REFERENCES users (Id_User)  
            )
        ''' )
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                Id_Client INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                Surname TEXT NOT NULL,
                Email TEXT NOT NULL,
                Id_User INTEGER UNIQUE,
                FOREIGN KEY (Id_User) REFERENCES users (Id_User)  
            )
        ''' )
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                Id_Orders INTEGER PRIMARY KEY AUTOINCREMENT,
                Id_Client INTEGER,
                Id_Product INTEGER,
                FOREIGN KEY (Id_Client) REFERENCES clients (Id_Client),
                FOREIGN KEY (Id_Product) REFERENCES products (Id_Product) 
            )
        ''' )
        conn.commit()
    