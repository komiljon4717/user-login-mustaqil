
import mysql.connector
import os

mydb = mysql.connector.connect(
            host="localhost",
            user="ali",
            passwd="123456789",
            database="DANG"
)




class User:
    def __init__(self, name=None, login=None, password=None, age=None):
        self.name = name
        self.login = login
        self.password = password
        self.age = age
        self.choose = ['1', '2']
        self.password_min_len = 6

    def entering_system(self):
        self.choose_parts()
        reg_or_log = input("[1/2]:").strip()

        while reg_or_log not in self.choose:
            self.clear_everything()
            print("Noto'g'ri belgi kiritdingiz. Iltimos quyidagi belgilardan birini tanlang:")
            self.choose_parts()
            reg_or_log = input("[1/2]:").strip()

        if reg_or_log is self.choose[0]:
                self.register()
        else:
                self.log_in()

    def choose_parts(self):
        print(f"""
                Tizimga kirish:
                Register    [{self.choose[0]}]
                Login       [{self.choose[1]}]
                """)


        # Registratsiya qismi


    def register(self):
        get_name = input("Ismingizni kiriting: ").capitalize().strip()
        while not get_name.isalpha():
            self.clear_everything()
            print("Noto'g'ri belgi kiritdingiz. Iltimos faqat harflardan foydalaning")
            get_name = input("Ismingizni kiriting: ").capitalize().strip()

        get_login = input("Login kiriting: ").strip()
        while not get_login.isalnum() or self.user_exists(get_login) or self.is_srt_empty(get_login):
            self.clear_everything()
            print("Noto'g'ri belgi kiritdingiz")
            print("-Loginda faqat harf yoki/va raqamlar bo'lishi kerak")
            print("-Bu login mavjud")
            get_login = input("Login kiriting: ").strip()

        get_password = input("Parolni kiriting: ").strip()
        check_password = input("Yana bir bor parolni kiriting: ").strip()
        while self.is_srt_empty(get_password) or len(get_password) < self.password_min_len or get_password != check_password:
            self.clear_everything()
            print("Noto'g'ri belgi kiritdingiz.")
            print("-Kiritilgan parol bo'sh")
            print("-Kiritilgan parollar bir xil emas")
            print(f"-Parol {self.password_min_len} dan kam bo'lmasligi kerak")

            get_password = input("Parolni kiriting: ").strip()
            check_password = input("Yana bir bor parolni kiriting: ").strip()


        get_age = input("Yoshingizni kiriting: ").strip()
        while not get_age.isnumeric():
            self.clear_everything()
            print("Noto'g'ri qiymat kiritdingiz. Iltimos faqat raqm kiriting:")
            get_age = input("Yoshingizni kiriting: ").strip()

        self.add_class(get_name, get_login, get_password, get_age)
        self.write_to_base()

    def add_class(self, get_name, get_login, get_password, get_age):
        self.name = get_name
        self.login = get_login
        self.password = get_password
        self.age = get_age

    def write_to_base(self):
        mycursor = mydb.cursor()
        mycursor.execute(f"insert into users values (null, '{self.name}', '{self.login}', '{self.password}', '{self.age}')")
        mydb.commit()

        self.mass_log_out()

        # log_in qismi


    def log_in(self):
        get_login = input("Login kiriting: ").strip().lower()
        while not self.user_exists(get_login):
            self.clear_everything()
            print("Noto'g'ri login kiritdingiz!")
            get_login = input("Login kiriting: ").strip().lower()

        get_password = input("Parolni kiriting: ").strip()
        while not self.is_all_match(get_login, get_password):
            self.clear_everything()
            print("Noto'g'ri parol kiritdingiz!: ")
            get_password = input("Parolni kiriting: ").strip()

        self.login = get_login
        self.password = get_password









        self.clear_everything()
        self.mass_update_log_or_pass()
        up_log_or_pass = input("[1/2]:").strip()
        while up_log_or_pass not in self.choose:
            self.clear_everything()
            print("Noto'g'ri belgi kiritdingiz. Iltimos quyidagi belgilardan birini tanlang:")
            self.mass_update_log_or_pass()
            up_log_or_pass = input("[1/2]:").strip()

        if up_log_or_pass is self.choose[0]:
            self.update_login()
        else:
            self.update_password()

    def mass_update_log_or_pass(self):
        print(f"""
                Tizimga hush kelibsiz:
                Login yoki parolni yangilashni hoxlaysizmi?
                Loginni o'zgartirish    [{self.choose[0]}]
                Parolni o'zgartirish    [{self.choose[1]}]
                """)

    def log_out(self):
        os.system("exit")

    def update_login(self):
        new_login = input("Yangi loginni kiriting: ").strip().lower()
        while not new_login.isalnum() or self.user_exists(new_login):
            self.clear_everything()
            print("Noto'g'ri belgi kiritdingiz")
            print("-Loginda faqat harf yoki/va raqamlar bo'lishi kerak")
            print("-Bu login mavjud")
            new_login = input("Login kiriting: ").strip()

        mycursor = mydb.cursor()
        mycursor.execute(f"update users set login='{new_login}' where login='{self.login}'")
        mydb.commit()

        self.mass_log_out()

    def user_exists(self, input_login):
        mycursor = mydb.cursor()
        mycursor.execute(f"select login from users where login = '{input_login}'")
        all_data = mycursor.fetchall()
        if all_data:
            return True
        else:
            return False

    def update_password(self):
        new_password = input("Yangi parolni kiriting: ").strip()
        check_password = input("Yangi parolni yana bir bor parolni kiriting: ").strip()
        while self.is_srt_empty(new_password) or len(
                new_password) < self.password_min_len or new_password != check_password:
            self.clear_everything()
            print("Noto'g'ri belgi kiritdingiz.")
            print("-Kiritilgan parol bo'sh")
            print("-Kiritilgan parollar bir xil emas")
            print(f"-Parol {self.password_min_len} dan kam bo'lmasligi kerak")

            new_password = input("Parolni kiriting: ").strip()
            check_password = input("Yana bir bor parolni kiriting: ").strip()

        mycursor = mydb.cursor()
        mycursor.execute(f"update users set password='{new_password}' where password='{self.password}'")
        mydb.commit()

        self.mass_log_out()

    def delete_account(self):
        self.clear_everything()
        get_password = input("Parolni kiriting: ").strip()
        mycursor = mydb.cursor()
        mycursor.execute(f"select ID from users where password='{get_password}'")
        all_data = str(mycursor.fetchall())

        while self.is_srt_empty(all_data):
            self.clear_everything()
            print("Parol xato qaytadan kiriting")
            get_password = input("Parolni kiriting: ").strip()

        mycursor = mydb.cursor()
        mycursor.execute(f"DELETE FROM users WHERE password = '{get_password}'")
        mydb.commit()

    @staticmethod
    def clear_everything():
        os.system("clear")

    @staticmethod
    def is_srt_empty(string):
        return not string

    def is_all_match(self, get_login, get_password):
        mycursor = mydb.cursor()
        mycursor.execute(f"select name from users where login = '{get_login}' and password='{get_password}'")
        all_data = mycursor.fetchall()
        if all_data:
            return True
        else:
            return False

    def mass_log_out(self):
        self.clear_everything()
        print(f"""
        
        Tizimdan chiqishni hoxlaysizmi 
        yoki accountni o'chirasizmi?
        
        Tizimdan chiqish        [{self.choose[0]}]
        Akkountni o'chirish     [{self.choose[1]}]
        
        """)
        logout_or_del = input("[1/2]:").strip()
        while logout_or_del not in self.choose:
            self.clear_everything()
            print("Noto'g'ri belgi kiritdingiz. Iltimos quyidagi belgilardan birini tanlang:")
            logout_or_del = input("[1/2]:").strip()

        if logout_or_del is self.choose[0]:
            self.log_out()
        else:
            self.delete_account()




person = User()
person.entering_system()

os.system("clear")
print("Siz tizimdan chiqdingiz")

