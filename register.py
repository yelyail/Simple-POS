import tkinter as tk
from tkinter import *
from tkinter import font, messagebox
import mysql.connector

class signin(tk.Toplevel):
    def __init__(self, main): 
        super().__init__(main)
        def show_password():
            if var.get():
                self.passEnter.config(show='')
            else:
                self.passEnter.config(show='*')
        def show_password_1():
            if var_1.get():
                self.passEnter_1.config(show='')
            else:
                self.passEnter_1.config(show='*')
        #main root
        self.main=main
        self.title("CRISPY CROWNS")
        self.title("CRISPY CROWNS")
        self.geometry('1440x1024')
        self.iconbitmap('icon.ico')
        self.config(bg='#C98895')
        self.resizable(False,False)
        # Entry field for password
        font_password = font.Font(size=30)
        self.passEnter_1 = tk.Entry(self, width=35, font=font_password, show='*')
        self.passEnter_1.config(bg='#EEB8C3')
        self.passEnter_1.place(x=330, y=441)
        #CHECKBOX FOR PASSWORD
        var = tk.BooleanVar()
        var_1 = tk.BooleanVar()
        show_password_passWOrd = tk.Checkbutton(self, text="Show Password", font=("times new roman",15,'normal'),variable=var_1, command=show_password_1, bg='#C98895')
        show_password_passWOrd.place(x=950, y=490) 
        show_password_ConfirmPass = tk.Checkbutton(self, text="Show Password", font=("times new roman",15,'normal'),variable=var, command=show_password, bg='#C98895')
        show_password_ConfirmPass.place(x=950, y=580) 
        # Entry field for confirm password
        font_confirm_password = font.Font(size=30)
        self.passEnter = tk.Entry(self, width=35, font=font_confirm_password, show='*')
        self.passEnter.config(bg='#EEB8C3')
        self.passEnter.place(x=330, y=535)

        self.label()
        self.connectDatabase()  
        self.cursor = self.conn.cursor()
    def label(self):
        #create account and Sign in button
        self.createAccButton = tk.Button(self,text="SIGN UP",font=("times new roman",20,'bold'),bg='#EEB8C3',fg='gray2',padx=150,pady=5,command=self.createAcc)
        self.createAccButton.place(x=510,y=620)
        self.signInButton = tk.Button(self,text="SIGN IN",font=("times new roman",15,'normal'),bg='#EEB8C3',fg='gray2',padx=15,pady=5,command=self.signin)
        self.signInButton.place(x=770,y=690)
        #label for name
        self.cClabel= tk.Label(self,text="CREATE AN ACCOUNT",font=("times new roman",50,'bold'),bg='#EEB8C3',fg='black',padx=100,pady=5)
        self.cClabel.pack(padx=5,pady=50)
        #label for the details
        self.fNLabel= tk.Label(self,text="User ID",font=("times new roman",20,'bold'),bg='#C98895',fg='gray2',padx=5,pady=5)
        self.fNLabel.place(x=330,y=210)
        self.unLabel= tk.Label(self,text="Username",font=("times new roman",20,'bold'),bg='#C98895',fg='gray2',padx=5,pady=5)
        self.unLabel.place(x=330,y=300)
        self.eALabel= tk.Label(self,text="Password",font=("times new roman",20,'bold'),bg='#C98895',fg='gray2',padx=5,pady=5)
        self.eALabel.place(x=330,y=397)
        self.passLabel= tk.Label(self,text="Confirm Password",font=("times new roman",20,'bold'),bg='#C98895',fg='gray2',padx=5,pady=5)
        self.passLabel.place(x=330,y=490)
        self.newUser= tk.Label(self,text="Already have an account?",font=("times new roman",15,'normal'),bg='#C98895',fg='gray2',padx=5,pady=5)
        self.newUser.place(x=550,y=695)
        #image
        self.imgDonut = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\a.png"
        self.img = tk.PhotoImage(file=self.imgDonut)
        self.imageLabel = tk.Label(self, image=self.img,padx=0,pady=0,bg='#C98895')
        self.imageLabel.place(x=1200,y=-200)
        self.don = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\a.png"
        self.imgDon = tk.PhotoImage(file=self.don)
        self.donlabel = tk.Label(self, image=self.imgDon,padx=0,pady=0,bg='#C98895')
        self.donlabel.place(x=-186,y=550)
        #Enter userID
        fonts = font.Font(size=30) 
        self.fnEnter = tk.Entry(self, width=35, font=fonts)
        self.fnEnter.config(bg='#EEB8C3')
        self.fnEnter.place(x=330, y=250)
        #Enter userName
        fonts = font.Font(size=30) 
        self.unEnter = tk.Entry(self, width=35, font=fonts)
        self.unEnter.config(bg='#EEB8C3')
        self.unEnter.place(x=330, y=340)
    def signin(self):
        self.destroy()
        self.main.deiconify()
    def connectDatabase(self):
        self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='donuts')
        self.cursor = self.conn.cursor()
    def createAcc(self):
        userID = self.fnEnter.get()
        userName = self.unEnter.get()
        password = self.passEnter_1.get()
        confirmPass = self.passEnter.get()

        try:
            if (userID == "" or userID == " ") or (userName == "" or userName == " ") or (
                    password == "" or password == "") or (confirmPass == "" or confirmPass == " "):
                messagebox.showinfo("ERROR", "Please fill up the blank")
                return
            elif not password == confirmPass:
                messagebox.showinfo("ERROR!", "Password didn't match")
            elif " " in userName:
                messagebox.showinfo("ERROR!", "USERNAME MUST NOT CONTAIN WHITE SPACES")
            else:
                sql = 'INSERT INTO register(userID, userName, password, confirmPass) VALUES(%s, %s, %s, %s)'
                vals = (userID, userName, password, confirmPass)
                self.cursor.execute(sql, vals)
                self.conn.commit()
                messagebox.showinfo("SUCCESS!", "You registered successfully!")
                self.fnEnter.delete(0, tk.END)
                self.unEnter.delete(0, tk.END)
                self.passEnter_1.delete(0, tk.END)
                self.passEnter.delete(0, tk.END)
                messagebox.showinfo("SUCCESS!", "Restarting the Program!")
                self.main.destroy()
        except mysql.connector.Error as e:
            if "Duplicate entry" in str(e):
                messagebox.showinfo("ERROR!", "Duplicate User ID, please try again with a different one")
            else:
                messagebox.showinfo("ERROR!", f"An error occurred: {e}")
            self.conn.rollback()