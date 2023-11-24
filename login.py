import tkinter as tk
from tkinter import *
from tkinter import font

class orderSystem:
    def __init__(first, main):
        def on_entry_click(event):
            if first.passEnter.get() == "":
                first.passEnter.delete(0, tk.END)
                first.passEnter.config(show='*')
        def on_focus_out(event):
            if not first.passEnter.get():
                first.passEnter.insert(0, "")
                first.passEnter.config(show='*')
        def show_password():
            if var.get():
                # If the checkbox is checked, show the password
                first.passEnter.config(show='')
            else:
                # If the checkbox is unchecked, hide the password
                first.passEnter.config(show='*')
        #main root
        first.main=main
        first.main.title("CRISPY CROWNS")
        first.main.geometry('1440x1024')
        first.main.iconbitmap('icon.ico')
        first.main.config(bg='#C98895')
        #label for text
        first.cClabel= tk.Label(main,text="Crispy Crowns",font=("times new roman",60,'bold'),bg='#EEB8C3',fg='gray2',padx=200,pady=5)
        first.cClabel.pack(padx=5,pady=50)
        first.uNLabel= tk.Label(main,text="USERNAME",font=("times new roman",20,'bold'),bg='#C98895',fg='gray2',padx=5,pady=5)
        first.uNLabel.place(x=298.29,y=250)
        first.passLabel= tk.Label(main,text="PASSWORD",font=("times new roman",20,'bold'),bg='#C98895',fg='gray2',padx=5,pady=5)
        first.passLabel.place(x=298.29,y=360)
        var = tk.BooleanVar()
        show_password_checkbox = tk.Checkbutton(main, text="Show Password", font=("times new roman",15,'normal'),variable=var, command=show_password, bg='#C98895')
        show_password_checkbox.place(x=920, y=455) #checkbox for the show password
        first.newUser= tk.Label(main,text="New User?",font=("times new roman",20,'normal'),bg='#C98895',fg='gray2',padx=5,pady=5)
        first.newUser.place(x=550,y=595)
        #Enter username
        fonts = font.Font(size=30) 
        first.unEnter = tk.Entry(main, width=35, font=fonts)
        first.unEnter.config(bg='#EEB8C3')
        first.unEnter.place(x=305, y=290)
        #Enter password
        fonts = font.Font(size=30)  # Adjust the size as needed
        first.passEnter = tk.Entry(main, width=35, font=fonts, show='*')
        first.passEnter.config(bg='#EEB8C3')
        first.passEnter.bind("<FocusIn>", on_entry_click)
        first.passEnter.bind("<FocusOut>", on_focus_out)
        first.passEnter.place(x=305, y=400)
        #log in&signup button
        first.loginButton = tk.Button(main,text="LOG IN",font=("times new roman",30,'bold'),bg='#EEB8C3',fg='gray2',padx=200,pady=5,command=first.login)
        first.loginButton.place(x=400,y=500)
        first.signUpButton = tk.Button(main,text="SIGN UP",font=("times new roman",15,'normal'),bg='#EEB8C3',fg='gray2',padx=15,pady=5,command=first.signUp)
        first.signUpButton.place(x=700,y=595)
        #image
        first.imgDonut = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\a.png"
        first.img = tk.PhotoImage(file=first.imgDonut)
        first.imageLabel = tk.Label(main, image=first.img,padx=0,pady=0,bg='#C98895')
        first.imageLabel.place(x=1200,y=-200)
        first.don = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\a.png"
        first.imgDon = tk.PhotoImage(file=first.don)
        first.donlabel = tk.Label(main, image=first.imgDon,padx=0,pady=0,bg='#C98895')
        first.donlabel.place(x=-186,y=550)

    def login(first):
        print("login")
        """mag lagay here for log in para maka enter na dayon sa fakeng sshit nga system"""
        
    def signUp(first):
        print("SIGNUYP")
        """mag lagay here for sign up para maka sign in sila sa system """

def main():
    root = tk.Tk()
    orderSys = orderSystem(root)
    root.mainloop()
if __name__ == "__main__":
    main()