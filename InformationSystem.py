import os.path
from Database import *
from User import *
from Employee import *
from Admin import *
from Product import *
from Client import *

Database.DBCreate()
conn = sqlite3.connect('RecordStudio.db')
cursor = conn.cursor()
iflogin = str
ifpassword = str
ifname = str
ifsurname = str
ifsalary = str
ifid = str
ifemail = str
ifnumber = str
ifprice = str
choice = str
smth_to_lookup = str
mail_to_lookup = str
order_to_lookup = str
employee_to_lookup = str
user_to_lookup = str
def CHOOSE_ROLE(user_login):
    conn = sqlite3.connect('RecordStudio.db')
    cursor = conn.cursor()
    select_role = "SELECT Role FROM users WHERE Login = ?"
    cursor.execute(select_role, (user_login))
    user_role = cursor.fetchone()
    if (user_role[0] == "Admin"):
        return AdminInterface(user_login)
    elif (user_role[0] == "Employee"):
        return StaffInterface(user_login)
    elif (user_role[0] == "Client"):
        return ClientInterface(user_login)
    elif (user_role[0] == "User"):
        return UserInterface(user_login)

def IFLogin():
    global iflogin
    print("Введите логин:")
    iflogin=str(input())
    if ((iflogin.isalnum()) and (len(iflogin)>=5) and (len(iflogin)<=15)):
        return iflogin
    else:
        print("Логин должен состоять только из букв и цифр, а также содержать от 5 до 15 символов")
        IFLogin()
def IFPassword():
    global ifpassword
    print("Введите пароль:")
    ifpassword=str(input())
    if ((len(ifpassword)>=8) and (not set(".,:;!_*-+()/#¤%&)").isdisjoint(ifpassword)) and (not set("1234567890").isdisjoint(ifpassword))):
        return ifpassword
    else:
        print("Пароль должен содержать цифры, специальные знаки и быть длиннее 8 символов")
        IFPassword()
def IFName():
    global ifname
    print("Введите имя:")
    ifname=str(input())
    if (ifname.isalpha()):
        ifname = ifname.title()
        return ifname
    else:
        print("Имя должно состоять только из букв")
        IFName()
def IFSurname():
    global ifsurname
    print("Введите фамилию:")
    ifsurname=str(input())
    if (ifsurname.isalpha()):
        ifsurname = ifsurname.title()
        return ifsurname
    else:
        print("Фамилия должна состоять только из букв")
        IFName()
def IFSalary():
    global ifsalary
    print("Введите зарплату:")
    ifsalary=str(input())
    if (ifsalary.isdigit()):
        return int(ifsalary)
    else:
        print("Зарплата должна состоять только из цифр")
        IFSalary()
def IFId():
    global ifid
    print("Введите ID:")
    ifid=str(input())
    if (ifid.isdigit()):
        return int(ifid)
    else:
        print("ID должен состоять только из цифр")
        IFId()
def IFNumber():
    global ifnumber
    print("Введите количество товара:")
    ifnumber=str(input())
    if (ifnumber.isdigit()):
        return int(ifnumber)
    else:
        print("Количество должно состоять только из цифр")
        IFNumber()
def IFPrice():
    global ifprice
    print("Введите цену:")
    ifprice=str(input())
    if (ifprice.isdigit()):
        return int(ifprice)
    else:
        print("Цена должна состоять только из цифр")
        IFPrice()
def IFEmail():
    global ifemail
    print("Введите почту:")
    ifemail=str(input())
    if (not set(".@").isdisjoint(ifemail)):
        return ifemail
    else:
        print("Почта должна иметь собачку и точку")
        IFEmail()

def EnterFirst():
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    if users:
        Enter()
    else:
        print("Вы впервые вошли в программу, добавьте админа:")
        admin = Admin(IFLogin(), IFPassword(), IFName(), IFSurname(), IFSalary())
        Admin.INSERT_Admin(iflogin, ifpassword, ifname, ifsurname, ifsalary)
        Enter()

def Enter():
    print("1. Войти\n2. Зарегестрироваться (Права сотрудника выдаёт админ)")
    if (IFChoice2() == '1'):
        LogIn_login()
    else:
        Registration_login()

def CheckLogin():
    global smth_to_lookup
    try:
        smth_to_lookup = IFLogin()
        select_login_exist = "SELECT Login FROM users WHERE Login = ?"
        cursor.execute(select_login_exist, (smth_to_lookup,))
        user_login = cursor.fetchone()
        return user_login
    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
def CheckPassword(user_login):
    try:
        password_to_check = IFPassword()
        select_password_exist = "SELECT Password FROM users WHERE Password = ? AND Login = ?"
        cursor.execute(select_password_exist, (password_to_check, user_login[0]))
        user_password = cursor.fetchone()
        return user_password
    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
def CheckEmail():
    try:
        mail_to_lookup = IFEmail()
        select_mail_exist = "SELECT Email FROM clients WHERE Email = ?"
        cursor.execute(select_mail_exist, (mail_to_lookup,))
        ifemail = cursor.fetchone()
        if not ifemail:
            return mail_to_lookup
        else:
            print("Такая почта уже занята, выберете другую")
            CheckEmail()
    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
def CheckProducts():
    try:
        smth_to_lookup = IFId()
        select_product_exist = "SELECT Id_Product FROM products WHERE Id_Product = ?"
        cursor.execute(select_product_exist, (smth_to_lookup,))
        ifid = cursor.fetchone()
        return ifid
    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
def CheckOrderExist():
    try:
        order_to_lookup = IFId()
        select_order_exist = "SELECT Id_Orders FROM orders WHERE Id_Orders = ?"
        cursor.execute(select_order_exist, (order_to_lookup,))
        ifid = cursor.fetchone()
        return ifid
    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
def CheckEmployeeExist():
    try:
        employee_to_lookup = IFId()
        select_employee_exist = "SELECT Id_Staff FROM staff WHERE Id_Staff = ?"
        cursor.execute(select_employee_exist, (employee_to_lookup,))
        ifid = cursor.fetchone()
        return ifid
    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
def CheckUserExist():
    try:
        user_to_lookup = IFId()
        select_user_exist = "SELECT Id_User FROM users WHERE Id_User = ?"
        cursor.execute(select_user_exist, (user_to_lookup,))
        ifid = cursor.fetchone()
        return ifid
    except sqlite3.Error as e:
        print(f"Error: {e}")
        conn.rollback()
def LogIn_login():
    user_login = CheckLogin()
    if user_login:
        LogIn_password(user_login)
    else:
        print("Пользователь не найден")
        LogIn_login()
def LogIn_password(user_login):
    user_password = CheckPassword(user_login)
    if user_password:
        print("Вы успешно вошли!")
        CHOOSE_ROLE(user_login)
    else:
        print("Пароль неверный")
        LogIn_password(user_login)
        
def Registration_login():
    global smth_to_lookup
    user_login = CheckLogin()
    if not user_login:
        user_login = smth_to_lookup
        Registration_password(user_login)
    else:
        print("Такой пользователь уже существует, выберете другой логин")
        Registration_login()
def Registration_password(user_login):
    user_password = IFPassword()
    user_role = "User"
    User.INSERT_User(user_login, user_password, user_role)
    print("Вы успешно зарегестрировались как юзер!")
    EnterFirst()

def IFChoice2():
    global choice
    choice = str(input())
    if ((choice == '1') or (choice == '2')):
        return choice
    else:
        print("Выбор должен быть 1 или 2")
        IFChoice2()
def IFChoice4():
    global choice
    choice = str(input())
    if ((choice == '1') or (choice == '2') or (choice == '3') or (choice == '4')):
        return choice
    else:
        print("Выбор должен быть цифрой от 1 до 4")
        IFChoice4()
def IFChoice5():
    global choice
    choice = str(input())
    if ((choice == '1') or (choice == '2') or (choice == '3') or (choice == '4') or (choice == '5')):
        return choice
    else:
        print("Выбор должен быть цифрой от 1 до 5")
        IFChoice5()

def AdminInterface(user_login):
    user_id = User.GET_ID(user_login)
    print(f"\nВы вошли как админ. Вам доступно просматривать, редактировать, добавлять и удалять сотрудников, пользователей и заказы. Вы не можете оформлять заказы с рабочего аккаунта :(")
    print("\nЧто вы хотите сделать?\n1. Изменить данные аккаунта\n2. Редактор заказов\n3. Редактор сотрудников\n4. Редактор пользователей\n5. Выйти из аккаунта")
    choice = IFChoice5()
    if (choice == '1'):
        print("Что вы хотите изменить?\n1. Логин\n2. Пароль\n3. Имя\n4. Фамилию\n5. Зарплату")
        choice = IFChoice5()
        if (choice == '1'):
            print("Вы уверены, что хотите сменить логин?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeLogin(user_login)
            elif (choice == '2'):
                StaffInterface(user_login)
        elif (choice == '2'):
            print("Вы уверены, что хотите сменить пароль?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangePassword(user_login)
            elif (choice == '2'):
                StaffInterface(user_login)    
        elif (choice == '3'):
            print("Вы уверены, что хотите сменить имя?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeName(user_id, user_login)
            elif (choice == '2'):
                StaffInterface(user_login)
        elif (choice == '4'):
            print("Вы уверены, что хотите сменить фамилию?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeSurname(user_id, user_login)
            elif (choice == '2'):
                StaffInterface(user_login)
        elif (choice == '5'):
            print("Вы уверены, что хотите сменить зарплату?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeSalary(user_id, user_login)
            elif (choice == '2'):
                AdminInterface(user_login)          
    elif (choice == '2'):
        ChangeOrders(user_login)
    elif (choice == '3'):
        ChangeStaff(user_login)
    elif (choice == '4'):
        ChangeUsers(user_login)
    elif (choice == '5'):
        print("Вы вышли из аккаунта")
        EnterFirst()
def StaffInterface(user_login):
    user_id = User.GET_ID(user_login)
    print(f"\nВы вошли как сотрудник. Вам доступно просматривать, редактировать, добавлять и удалять товары. Вы не можете оформлять заказы с рабочего аккаунта :(")
    print("\nЧто вы хотите сделать?\n1. Изменить данные аккаунта\n2. Просмотреть товары\n3. Редактор товаров\n4. Выйти из аккаунта")
    choice = IFChoice4()
    if (choice == '1'):
        print("Что вы хотите изменить?\n1. Логин\n2. Пароль\n3. Имя\n4. Фамилию")
        choice = IFChoice4()
        if (choice == '1'):
            print("Вы уверены, что хотите сменить логин?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeLogin(user_login)
            elif (choice == '2'):
                StaffInterface(user_login)
        elif (choice == '2'):
            print("Вы уверены, что хотите сменить пароль?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangePassword(user_login)
            elif (choice == '2'):
                StaffInterface(user_login)    
        elif (choice == '3'):
            print("Вы уверены, что хотите сменить имя?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeName(user_id, user_login)
            elif (choice == '2'):
                StaffInterface(user_login)
        elif (choice == '4'):
            print("Вы уверены, что хотите сменить фамилию?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeSurname(user_id, user_login)
            elif (choice == '2'):
                StaffInterface(user_login)        
    elif (choice == '2'):
        ShowProducts(user_login)
    elif (choice == '3'):
        ChangeProducts(user_login)
    elif (choice == '5'):
        print("Вы вышли из аккаунта")
        EnterFirst()

def ClientInterface(user_login):
    user_id = User.GET_ID(user_login)
    print(f"\nВы вошли как клиент. Вам доступно просматривать наши товары и добавлять их в заказ.")
    print("\nЧто вы хотите сделать?\n1. Изменить данные аккаунта\n2. Просмотреть товары\n3. Редактор заказа\n4. Выйти из аккаунта")
    choice = IFChoice4()
    if (choice == '1'):
        print("Что вы хотите изменить?\n1. Логин\n2. Пароль\n3. Имя\n4. Фамилию\n5. Почту")
        choice = IFChoice5()
        if (choice == '1'):
            print("Вы уверены, что хотите сменить логин?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeLogin(user_login)
            elif (choice == '2'):
                ClientInterface(user_login)
        elif (choice == '2'):
            print("Вы уверены, что хотите сменить пароль?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangePassword(user_login)
            elif (choice == '2'):
                ClientInterface(user_login)    
        elif (choice == '3'):
            print("Вы уверены, что хотите сменить имя?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeName(user_id, user_login)
            elif (choice == '2'):
                ClientInterface(user_login)
        elif (choice == '4'):
            print("Вы уверены, что хотите сменить фамилию?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeSurname(user_id, user_login)
            elif (choice == '2'):
                ClientInterface(user_login)   
        elif (choice == '5'):
            print("Вы уверены, что хотите сменить почту?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeEmail(user_id, user_login)
            elif (choice == '2'):
                ClientInterface(user_login)      
    elif (choice == '2'):
        ShowProducts(user_login)
    elif (choice == '3'):
        CheckOrder(user_login)
    elif (choice == '4'):
        print("Вы вышли из аккаунта")
        EnterFirst()

def UserInterface(user_login):
    print(f"\nВы вошли как юзер. Вам доступно просматривать наши товары.\nЧтобы оформить заказ - заполните дополнительную инфорамцию, нажав \"Стать клиентом\"")
    print("\nЧто вы хотите сделать?\n1. Изменить данные аккаунта\n2. Просмотреть товары\n3. Стать клиентом\n4. Выйти из аккаунта")
    choice = IFChoice4()
    if (choice == '1'):
        print("Что вы хотите изменить?\n1. Логин\n2. Пароль")
        choice = IFChoice2()
        if (choice == '1'):
            print("Вы уверены, что хотите сменить логин?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangeLogin(user_login)
            elif (choice == '2'):
                UserInterface(user_login)
        elif (choice == '2'):
            print("Вы уверены, что хотите сменить пароль?\n1. Да\n2. Нет")
            choice = IFChoice2()
            if (choice == '1'):
                ChangePassword(user_login)
            elif (choice == '2'):
                UserInterface(user_login)    
    elif (choice == '2'):
        ShowProducts(user_login)
    elif (choice == '3'):
        BecomeClient(user_login)
    elif (choice == '4'):
        print("Вы вышли из аккаунта")
        EnterFirst()

def ChangeLogin(user_login):
    old_login = user_login
    select_id_user= "SELECT Id_User FROM users WHERE Login = ?"
    cursor.execute(select_id_user, (old_login))
    user_id = cursor.fetchone()
    print("Введите новый логин")
    user_login = CheckLogin()
    if not user_login:
        user_login = smth_to_lookup   
        User.UPDATE_User_Login(user_id[0], user_login)
        CHOOSE_ROLE(tuple(user_login.split(',')))
    else:
        print("Такой пользователь уже существует")
        ChangeLogin(old_login)
def ChangePassword(user_login):
    user_id = User.GET_ID(user_login)
    print("Введите новый пароль")
    user_password = IFPassword()  
    User.UPDATE_User_Password(user_id[0], user_password)
    CHOOSE_ROLE(user_login)
def ChangeName(user_id, user_login):
    print("Введите новое имя:")
    ifname = IFName()
    Client.UPDATE_Client_Name(user_id[0], ifname)
    CHOOSE_ROLE(user_login)
def ChangeSurname(user_id, user_login):
    print("Введите новую фамилию:")
    ifsurname = IFSurname()
    Client.UPDATE_Client_Surname(user_id[0], ifsurname)
    CHOOSE_ROLE(user_login)
def ChangeEmail(user_id, user_login):
    print("Введите новую почту:")
    ifemail = CheckEmail()
    if not ifemail:
        ifemail = smth_to_lookup
    else:
        print("Такая почта уже занята, выберете другую")
        ChangeEmail(user_id, user_login)
    Client.UPDATE_Client_Email(user_id[0], ifemail)
    CHOOSE_ROLE(user_login)
def ChangeSalary(user_id, user_login):
    print("Введите новую зарплату:")
    ifsalary = IFSalary()
    Employee.UPDATE_Staff_Salary(user_id[0], ifsalary)
    CHOOSE_ROLE(user_login)

def ShowProducts(user_login):
    print("\n1. Просмотреть товары без фильтрации\n2. Отфильтровать по цене\n3. Отфильтровать по названию\n4. Отфильтровать по количеству на складе\n5. Выйти в меню")
    choice = IFChoice5()
    if (choice == '1'):
        Product.SELECT_ALL()
        CHOOSE_ROLE(user_login)
    elif (choice == '2'):
        Product.SELECT_BY_PRICE()
        CHOOSE_ROLE(user_login)
    elif (choice == '3'):
        Product.SELECT_BY_NAME()
        CHOOSE_ROLE(user_login)
    elif (choice == '4'):
        Product.SELECT_BY_NUMBER()
        CHOOSE_ROLE(user_login)
    elif (choice == '5'):
        CHOOSE_ROLE(user_login)

def BecomeClient(user_login):
    global smth_to_lookup
    print("Чтобы стать клиентом нужно указать личную информацию. Вы уверены?\n1. Да\n2. Нет")
    choice = IFChoice2()
    if (choice == '1'):
        select_id_user= "SELECT Id_User FROM users WHERE Login = ?"
        cursor.execute(select_id_user, (user_login))
        user_id = cursor.fetchone()
        ifname = IFName()
        ifsurname = IFSurname()
        ifemail = CheckEmail()
        Client.INSERT_Client_From_User(user_id, ifname, ifsurname, ifemail)
        ClientInterface(user_login)
    elif (choice == '2'):
        UserInterface(user_login)

def CheckOrder(user_login):
    print("\nЧто вы хотите сделать?\n1. Просмотреть заказ\n2. Добавить в заказ\n3. Удалить из заказа\n4. Вернуться в меню")
    choice = IFChoice4()
    user_id = User.GET_ID(user_login)
    client_id = Client.GET_Client_Id(user_id)
    if (choice =='1'):
        Product.SHOW_ORDER(client_id)
        CHOOSE_ROLE(user_login)
    elif (choice == '2'):
        product_id = CheckProducts()
        if product_id:
            if Product.Enough_Products(product_id):
                Product.INSERT_Order(client_id, product_id)
                Product.Reduce_Product(product_id)
                CheckOrder(user_login)
            else:
                print("На складе недостаточно товара, приносим свои извинения")
                CheckOrder(user_login)
        else:
            print("Такого товара не существует")
            CheckOrder(user_login)
    elif (choice == '3'):
        product_id = CheckProducts()
        if product_id:
            Product.DELETE_In_Order(client_id, product_id)
            CheckOrder(user_login)
        else:
            print("Такого товара не существует")
            CheckOrder(user_login)
    elif (choice == '4'):
        ClientInterface(user_login)

def ChangeProducts(user_login):
    print("\nЧто вы хотите сделать?\n1. Редактировать товар\n2. Добавить товар\n3. Удалить товар\n4. Вернуться в меню")
    choice = IFChoice4()
    if (choice =='1'):
        product_id = CheckProducts()
        if product_id:
            print("Что отредактировать?\n1. Название\n2. Количество\n3. Цену\n4. Выйти")
            choice = IFChoice4()
            if (choice == '1'):
                print("Введите имя")
                Product.UPDATE_Product_Name(product_id, str(input()))
                ChangeProducts(user_login)
            elif (choice == '2'):
                Product.UPDATE_Product_Number(product_id, IFNumber())
                ChangeProducts(user_login)
            elif (choice == '3'):
                Product.UPDATE_Product_Price(product_id, IFPrice())
                ChangeProducts(user_login)
            elif (choice == '4'):
                ChangeProducts(user_login)
        else:
            print("Такого товара не существует")
            ChangeProducts(user_login)
        ChangeProducts(user_login)
    elif (choice == '2'):
        print("Введите имя")
        Product.INSERT_Product(str(input()), IFNumber(), IFPrice())
        ChangeProducts(user_login)
    elif (choice == '3'):
        product_id = CheckProducts()
        if product_id:
            Product.DELETE_Product(product_id)
            ChangeProducts(user_login)
        else:
            print("Такого товара не существует")
            ChangeProducts(user_login)
        ChangeProducts(user_login)
    elif (choice == '4'):
        StaffInterface(user_login)

def ChangeOrders(user_login):
    global order_to_lookup
    print("\nЧто вы хотите сделать?\n1. Просмотреть заказы\n2. Редактировать заказ\n3. Добавить заказ\n4. Удалить заказ\n5. Вернуться в меню")
    choice = IFChoice5()
    if (choice == '1'):
        Admin.SELECT_Orders()
        ChangeOrders(user_login)
    if (choice =='2'):
        order_id = CheckOrderExist()
        if order_id:
            print("Что отредактировать?\n1. Клиента\n2. Товар")
            choice = IFChoice2()
            if (choice == '1'):
                Admin.UPDATE_ORDER_Client(order_id, IFId())
                ChangeOrders(user_login)
            elif (choice == '2'):
                Admin.UPDATE_ORDER_Product(order_id, IFId())
                ChangeOrders(user_login)
        else:
            print("Такого заказа не существует")
            ChangeOrders(user_login)
    elif (choice == '3'):
        Admin.INSERT_Order(IFId(), IFId())
        ChangeOrders(user_login)
    elif (choice == '4'):
        order_id = CheckOrderExist()
        if order_id:
            Admin.DELETE_Order(order_id)
            ChangeProducts(user_login)
        else:
            print("Такого заказа не существует")
            ChangeOrders(user_login)
        ChangeOrders(user_login)
    elif (choice == '5'):
        AdminInterface(user_login)
def ChangeStaff(user_login):
    print("\nЧто вы хотите сделать?\n1. Просмотреть сотрудников\n2. Редактировать сотрудника\n3. Добавить сотрудника\n4. Удалить сотрудника\n5. Вернуться в меню")
    choice = IFChoice5()
    if (choice == '1'):
        Employee.SELECT_Staff()
        ChangeStaff(user_login)
    if (choice =='2'):
        employee_id = CheckEmployeeExist()
        if employee_id:
            print("Что отредактировать?\n1. Имя\n2. Фамилию\n3. Зарплату\n4. Аккаунт")
            choice = IFChoice4()
            if (choice == '1'):
                Employee.UPDATE_Staff_Name(employee_id, IFName())
                ChangeStaff(user_login)
            elif (choice == '2'):
                Employee.UPDATE_Staff_Surname(employee_id, IFSurname())
                ChangeStaff(user_login)
            elif (choice == '3'):
                Employee.UPDATE_Staff_Salary(employee_id, IFSalary())
                ChangeStaff(user_login)
            elif (choice == '4'):
                Employee.UPDATE_Staff_User(employee_id, IFId())
                ChangeStaff(user_login)
        else:
            print("Такого сотрудника не существует")
            ChangeStaff(user_login)
    elif (choice == '3'):
        Employee.INSERT_Staff(IFName(), IFSurname(), IFSalary(), IFId())
        ChangeStaff(user_login)
    elif (choice == '4'):
        employee_id = CheckEmployeeExist()
        if employee_id:
            Employee.DELETE_Staff(employee_id)
            ChangeStaff(user_login)
        else:
            print("Такого сотрудника не существует")
            ChangeStaff(user_login)
        ChangeOrders(user_login)
    elif (choice == '5'):
        AdminInterface(user_login)
def ChangeUsers(user_login):
    print("\nЧто вы хотите сделать?\n1. Просмотреть пользователей\n2. Редактировать пользователя\n3. Добавить пользователя\n4. Удалить пользователя\n5. Вернуться в меню")
    choice = IFChoice5()
    if (choice == '1'):
        User.SELECT_User()
        ChangeUsers(user_login)
    if (choice =='2'):
        user_id = CheckUserExist()
        if user_id:
            print("Что отредактировать?\n1. Логин\n2. Пароль\n3. Роль\n4. Выйти")
            choice = IFChoice4()
            if (choice == '1'):
                User.UPDATE_User_Login(user_id, IFLogin())
                ChangeUsers(user_login)
            elif (choice == '2'):
                User.UPDATE_User_Password(user_id, IFPassword())
                ChangeUsers(user_login)
            elif (choice == '3'):
                print("Новая роль?\n1. Юзер\n2. Клиент\n3. Сотрудник\n4. Админ")
                choice = IFChoice4()
                if (choice =='1'):
                    user_role = 'User'
                if (choice =='2'):
                    user_role = 'Client'
                if (choice =='3'):
                    user_role = 'Employee'
                if (choice =='4'):
                    user_role = 'Admin'
                User.UPDATE_User_Role(user_id, user_role)
                ChangeUsers(user_login)
            elif (choice == '4'):
                ChangeUsers(user_login)
        else:
            print("Такого пользователя не существует")
            ChangeUsers(user_login)
    elif (choice == '3'):
        print("Роль пользователя?\n1. Юзер\n2. Клиент\n3. Сотрудник\n4. Админ")
        choice = IFChoice4()
        if (choice =='1'):
            user_role = 'User'
        if (choice =='2'):
            user_role = 'Client'
        if (choice =='3'):
            user_role = 'Employee'
        if (choice =='4'):
            user_role = 'Admin'
        User.INSERT_User(IFLogin(), IFPassword(), user_role)
        ChangeUsers(user_login)
    elif (choice == '4'):
        user_id = CheckUserExist()
        if user_id:
            User.IF_DELETE_User(user_id)
            ChangeUsers(user_login)
        else:
            print("Такого пользователя не существует")
            ChangeUsers(user_login)
        ChangeUsers(user_login)
    elif (choice == '5'):
        AdminInterface(user_login)
EnterFirst()