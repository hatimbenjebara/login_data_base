

import pandas as pd
df = pd.read_csv("login.csv")
print("if this your first time you need to to create your email, if not entre your email".capitalize())
introduction = input("answer by Y or N, is this your first visite? : ".capitalize())
while True:
    if introduction =="Y" or introduction== "y":
        print("Welcome to our program. This is your first visit. You need to create your login.: \n".capitalize())
        name=input("give me your name :")
        age=input("give me your age:")
        while True:
            email=input("give me a email:")
            if "@" not in email:
                print("invalid email adress please include @ symbol")
            elif email in df["email"]:
                print("email already exist. Please entre a different email adress")
            else:
                print("valid email")
                break
        while True: 
            password= input("Entre your password at least 8 characters:")
            if len(password)<8:
                print("password must be at least 8 characters long")
            else:
                print("password is valid")
                break
        new_row = pd.DataFrame({"name": [name], "age": [age], "email":[email], "password":[password]})
        df=pd.concat([df, new_row], ignore_index= True)
        df.to_csv("login.csv", index = False)
    elif introduction=="N" or introduction=="n": 
        print("welcome back, you have a login saves please entre your email and password:\n")
        while True :
            email= input("entre you email:")
            password = input("entre your password:")
            if email in df["email"].values:
                print("this email exist in dataset")
                correct_password= df.loc[df["email"] == email, "password"].values[0]
                if password ==correct_password:
                    print("password valid")
                    print("welcome back ", df.loc[df["email"]== email , "name"] .values[0])
                    break
                else: 
                    print("sorry wrong password")
                    break
            else:
                print("email does not exist in dataset. please entre a valid email")
    else:
        print("wrong you put the wrong character")
        print("please ansear by y or n ")
        break
#method2 : oop 
import pandas as pd
class LoginSystem:
    def __init__(self):
        self.df = pd.read_csv("login.csv")   
    def create_account(self):
        print("Welcome to our program. This is your first visit. You need to create your login.")
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        while True:
            email = input("Enter your email: ")
            if "@" not in email:
                print("Invalid email address. Please include '@' symbol.")
            elif email in self.df["email"].values:
                print("Email already exists. Please enter a different email address.")
            else:
                print("Valid email.")
                break
        while True:
            password = input("Enter your password (at least 8 characters): ")
            if len(password) < 8:
                print("Password must be at least 8 characters long.")
            else:
                print("Valid password.")
                break
        new_row = pd.DataFrame({"name": [name], "age": [age], "email": [email], "password": [password]})
        self.df = pd.concat([self.df, new_row], ignore_index=True)
        self.df.to_csv("login.csv", index=False)
        print("Account created successfully!")
    def login(self):
        print("Welcome back. You have a login saved. Please enter your email and password.")
        while True:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            if email in self.df["email"].values:
                print("This email exists in the dataset.")
                correct_password = self.df.loc[self.df["email"] == email, "password"].values[0]
                if password == correct_password:
                    print("Password valid.")
                    print("Welcome back, ", self.df.loc[self.df["email"] == email, "name"].values[0], "!")
                    break
                else:
                    print("Sorry, wrong password.")
                    break
            else:
                print("Email does not exist in the dataset. Please enter a valid email.")
    def run(self):
        print(self.df)
        print("Hello! This program is for... If this is your first time, you need to create your email. If not, enter your email.")
        introduction = input("Answer by Y or N, is this your first time: ").upper()
        while True:
            if introduction == "Y":
                self.create_account()
                break
            elif introduction == "N":
                self.login()
                break
            else:
                print("Wrong input. Please answer by Y or N.")
                introduction = input("Is this your first time? ").upper()
                continue
login_system = LoginSystem()
login_system.run()