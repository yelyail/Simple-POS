import tkinter as tk
from tkinter import font,messagebox
from register import signin 
from main import mainFrame
import mysql.connector

class MainClassLogIn():
    def __init__(self, main):
        def show_password():
            if var.get():
                # If the checkbox is checked, show the password
                self.passEnter.config(show='')
            else:
                # If the checkbox is unchecked, hide the password
                self.passEnter.config(show='*')
        #main root
        self.main=main
        self.main.title("CRISPY CROWNS")
        self.main.geometry('1440x1024')
        self.main.iconbitmap('icon.ico')
        self.main.config(bg='#C98895')
        #label for text
        self.cClabel= tk.Label(main,text="CRISPY CROWNS",font=("times new roman",60,'bold'),bg='#EEB8C3',fg='black',padx=160,pady=5)
        self.cClabel.pack(padx=5,pady=50)
        self.uNLabel= tk.Label(main,text="USERNAME",font=("times new roman",20,'bold'),bg='#C98895',fg='gray2',padx=5,pady=5)
        self.uNLabel.place(x=298.29,y=330)
        self.uNLabel= tk.Label(main,text="USER ID",font=("times new roman",20,'bold'),bg='#C98895',fg='gray2',padx=5,pady=5)
        self.uNLabel.place(x=298.29,y=240)
        self.passLabel= tk.Label(main,text="PASSWORD",font=("times new roman",20,'bold'),bg='#C98895',fg='gray2',padx=5,pady=5)
        self.passLabel.place(x=298.29,y=420)
        var = tk.BooleanVar()
        show_password_checkbox = tk.Checkbutton(main, text="Show Password", font=("times new roman",15,'normal'),variable=var, command=show_password, bg='#C98895')
        show_password_checkbox.place(x=920, y=510) 
        self.newUser= tk.Label(main,text="Don't have an Account?",font=("times new roman",15,'normal'),bg='#C98895',fg='gray2',padx=5,pady=5)
        self.newUser.place(x=490,y=660)
        #Enter username
        fonts = font.Font(size=30) 
        self.unEnter = tk.Entry(main, width=35, font=fonts)
        self.unEnter.config(bg='#EEB8C3')
        self.unEnter.place(x=305, y=370)
        #Enter userID
        fonts = font.Font(size=30) 
        self.userIDEnter = tk.Entry(main, width=35, font=fonts)
        self.userIDEnter.config(bg='#EEB8C3')
        self.userIDEnter.place(x=305, y=280)
        #log in&signup button
        self.loginButton = tk.Button(main,text="SIGN IN",font=("times new roman",30,'bold'),bg='#EEB8C3',fg='gray2',padx=200,pady=5,command=lambda: self.login())
        self.loginButton.place(x=400,y=560)
        self.signUpButton = tk.Button(main,text="Register Here",font=("times new roman",15,'normal'),bg='#EEB8C3',fg='gray2',padx=10,pady=5,command=lambda: self.signup())
        self.signUpButton.place(x=700,y=660)
        #image
        self.imgDonut = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\a.png"
        self.img = tk.PhotoImage(file=self.imgDonut)
        self.imageLabel = tk.Label(main, image=self.img,padx=0,pady=0,bg='#C98895')
        self.imageLabel.place(x=1200,y=-200)
        self.don = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\a.png"
        self.imgDon = tk.PhotoImage(file=self.don)
        self.donlabel = tk.Label(main, image=self.imgDon,padx=0,pady=0,bg='#C98895')
        self.donlabel.place(x=-186,y=550)

        fonts = font.Font(size=30)
        self.passEnter = tk.Entry(self.main, width=35, font=fonts, show='*')
        self.passEnter.config(bg='#EEB8C3')
        self.passEnter.place(x=305, y=460)

        self.connectDatabase()  
        self.cursor = self.conn.cursor()
        self.attempt = 0
        self.attempt_1 = 3
    def login(self):
        success = self.read()
        if success:
            self.main.withdraw()
            main_frame_instance = mainFrame(self.main)
            self.main.wait_window(main_frame_instance)
    def signup(self):
        self.main.withdraw()
        signin_instance = signin(self.main)
        self.main.wait_window(signin_instance)
    def connectDatabase(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='donuts')
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            raise
    def read(self):
        while self.attempt <= self.attempt_1:
            userID = self.userIDEnter.get()
            userName = self.unEnter.get()
            password = self.passEnter.get()
            try:
                if " " in userName: 
                    messagebox.showinfo("ERROR!", "USERNAME MUST NOT CONTAIN WHITE SPACES")
                    return False
                elif self.loginCheck(userID, userName, password):
                    # code for success
                    messagebox.showinfo("Successful", f"Welcome to the system, {userName.upper()}!")
                    return True 
                else:
                    # code for attempt failed
                    messagebox.showinfo("Attempt Failed!", "Invalid inputs. Please try again and check your User ID, Username, and password\nAttempt Failed! There are only 3 attempts allowed")
                    self.attempt += 1
                    break 
            except mysql.connector.Error as e:
                messagebox.showinfo("ERROR!", f"An error occurred: {e}")
                self.conn.rollback()
                return False
        if self.attempt >= self.attempt_1:
            messagebox.showinfo("ERROR!", "Maximum login attempts reached. Please try again later.")
            self.conn.close()
            self.main.withdraw()
        # Clear entries after the loop
        self.userIDEnter.delete(0, tk.END)
        self.unEnter.delete(0, tk.END)
        self.passEnter.delete(0, tk.END)
        return False
    def loginCheck(self, userID, userName, password):
        # connect to mysql
        sql = 'SELECT userID, userName, password FROM register WHERE userID=%s AND userName=%s AND password=%s'
        vals = (userID, userName, password)  # rows in database
        self.cursor.execute(sql, vals)
        result = self.cursor.fetchone()  # Fetch one row
        return result is not None
def main():
    root = tk.Tk()
    root.resizable(False,False)
    orderSys = MainClassLogIn(root)
    root.mainloop()
if __name__ == "__main__":
    main()