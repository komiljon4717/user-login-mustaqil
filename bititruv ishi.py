
# name
# login
# password
# age
import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            user="ali",
            passwd="123456789",
            database="DANG"
)
import os



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

    def register(self):
        get_name = input("Ismingizni kiriting: ").capitalize().strip()
        while not get_name.isalpha():
            self.clear_everything()
            print("Noto'g'ri belgi kiritdingiz. Iltimos faqat harflardan foydalaning")
            get_name = input("Ismingizni kiriting: ").capitalize().strip()

        get_login = input("Login kiriting: ").strip()
        while not get_login.isalnum() or self.user_exists(get_login):
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


        
    def log_in(self):
        print("login part")

    def log_out(self):
        pass

    def update_login(self):
        pass

    def user_exists(self, input_login):
        mycursor = mydb.cursor()
        mycursor.execute(f"select login from users where login = '{input_login}'")
        all_data = mycursor.fetchall()
        if all_data:
            return True
        else:
            return False

    def update_password(self):
        pass

    def delete_account(self):
        pass
    @staticmethod
    def clear_everything():
        os.system("clear")

    @staticmethod
    def is_srt_empty(string):
        return not string




person = User()
person.entering_system()

