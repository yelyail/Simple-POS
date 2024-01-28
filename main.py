import tkinter as tk
from tkinter import *
from tkinter import messagebox,simpledialog
from datetime import datetime
import mysql.connector

class mainFrame(tk.Toplevel):
    def __init__(self, main):
        super().__init__(main)
        #main root
        self.main=main
        self.title("CRISPY CROWNS")
        self.geometry('1440x1024')
        self.iconbitmap('icon.ico')
        self.config(bg='#C98895')
        self.resizable(False,False)
        
        #image
        self.don = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\a.png"
        self.imgDon = tk.PhotoImage(file=self.don)
        self.donlabel = tk.Label(self, image=self.imgDon,padx=0,pady=0,bg='#C98895')
        self.donlabel.place(x=-186,y=550)
        #label for name
        self.cClabel= tk.Label(self,text="Crispy Crowns",font=("times new roman",40,'bold'),bg='#EEB8C3',fg='gray2',padx=100,pady=2)
        self.cClabel.place(x=150,y=10)
        # Create rectangle
        firstRect = tk.Canvas(self, width=700, height=1024)
        firstRect.place(x=830,y=0)
        firstRect.create_rectangle(0, 0, 1200, 1024, fill="#EFC4CA")
        self.firstImg = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\a.png"
        self.firstImg_1 = tk.PhotoImage(file=self.firstImg)
        self.firstLabel = tk.Label(self, image=self.firstImg_1,padx=0,pady=0,bg='#EFC4CA')
        self.firstLabel.place(x=1200,y=-220)
        #method for the images of the donuts
        self.donuts_Image()
        self.other_button()
        self.add_button()
        self.conn = None
        self.cursor = None
        self.ttLabel = None
    def other_button(self):
        #text widget
        self.total =tk.Entry(self,width=20,font=('Arial',20),state=DISABLED)
        self.total.place(x=1110,y=660)
        #label
        self.orderLabel= tk.Label(self,text="ORDER LIST",font=("times new roman",25,'bold'),bg='#EFC4CA',fg='gray2')
        self.orderLabel.place(x=854,y=60)
        self.totalLabel= tk.Label(self,text="TOTAL PRICE: PHP",font=("times new roman",20,'bold'),bg='#EFC4CA',fg='gray2')
        self.totalLabel.place(x=850,y=660)
        #receipt & logout button
        self.receiptButton = tk.Button(self,text="PRINT RECEIPT",font=("times new roman",20,'bold'),bg='#EEB8C3',fg='gray2',padx=150,pady=4,command=lambda: self.totalPrice())
        self.receiptButton.place(x=870,y=715)
        self.logoutButton = tk.Button(self,text="Sign Out",font=("times new roman",12,'bold'),bg='#FF2400',fg='gray2',padx=5,pady=4,command=lambda: self.log_out())
        self.logoutButton.place(x=1340,y=10)
        self.editButton = tk.Button(self,text="EDIT",font=("times new roman",20,'bold'),bg='#F59CAE',fg='gray2',padx=5,pady=4,command=lambda: self.edit())
        self.editButton.place(x=1197,y=570)
        self.clearButton = tk.Button(self,text="CLEAR",font=("times new roman",20,'bold'),bg='#F59CAE',fg='gray2',padx=5,pady=4,command=lambda: self.clear())
        self.clearButton.place(x=1300,y=570)
        self.allowEdit = False
        self.cartCleared = False
    def add_button(self):    
        #for addButton
        self.add_1 = tk.Button(self,text="ADD",font=("times new roman",12,'bold'),bg='#D9D9D9',fg='gray2',padx=5,pady=4,command=lambda: self.quantityOfOrder("Nutella"))
        self.add_1.place(x=170,y=270)
        self.add_2 = tk.Button(self,text="ADD",font=("times new roman",12,'bold'),bg='#D9D9D9',fg='gray2',padx=5,pady=4,command=lambda: self.quantityOfOrder("Alcapone"))
        self.add_2.place(x=170,y=486)
        self.add_3 = tk.Button(self,text="ADD",font=("times new roman",12,'bold'),bg='#D9D9D9',fg='gray2',padx=5,pady=4,command=lambda: self.quantityOfOrder("Strawberry"))
        self.add_3.place(x=170,y=700)
        self.add_4 = tk.Button(self,text="ADD",font=("times new roman",12,'bold'),bg='#D9D9D9',fg='gray2',padx=5,pady=4,command=lambda: self.quantityOfOrder("Glaze"))
        self.add_4.place(x=453,y=270)
        self.add_5 = tk.Button(self,text="ADD",font=("times new roman",12,'bold'),bg='#D9D9D9',fg='gray2',padx=5,pady=4,command=lambda: self.quantityOfOrder("Chocomallow"))
        self.add_5.place(x=453,y=486)
        self.add_6 = tk.Button(self,text="ADD",font=("times new roman",12,'bold'),bg='#D9D9D9',fg='gray2',padx=5,pady=4,command=lambda: self.quantityOfOrder("Classic"))
        self.add_6.place(x=453,y=700)
        self.add_7 = tk.Button(self,text="ADD",font=("times new roman",12,'bold'),bg='#D9D9D9',fg='gray2',padx=5,pady=4,command=lambda: self.quantityOfOrder("Snowwhite"))
        self.add_7.place(x=723,y=270)
        self.add_8 = tk.Button(self,text="ADD",font=("times new roman",12,'bold'),bg='#D9D9D9',fg='gray2',padx=5,pady=4,command=lambda: self.quantityOfOrder("Choco"))
        self.add_8.place(x=723,y=486)
        self.add_9 = tk.Button(self, text="ADD", font=("times new roman", 12, 'bold'), bg='#D9D9D9', fg='gray2', padx=5, pady=4, command=lambda: self.quantityOfOrder("Sprinkles"))
        self.add_9.place(x=723, y=700)
        # Create a Text widget for receipt
        self.receiptBox = tk.Text(self, height=20, width=50, font=('Arial', 15),state=DISABLED)
        self.receiptBox.place(x=860, y=100)
        self.foodList =[]
    def quantityOfOrder(self, foodType):
        self.Quantity = tk.Toplevel()
        self.Quantity.title(f"Enter {foodType} Quantity")
        self.Quantity.iconbitmap('icon.ico')  
        self.Quantity.geometry('300x80') 

        quantity_label = tk.Label(self.Quantity, text="Enter Quantity:")
        quantity_label.place(x=10, y=10)
            
        quantity_entry = tk.Entry(self.Quantity, font=('Arial', 12))
        quantity_entry.place(x=100, y=10)
    
        confirm_button = tk.Button(self.Quantity, text="Confirm", font=("times new roman", 12, 'bold'), bg='#D9D9D9', fg='gray2', padx=5, pady=4,command=lambda: self.addFood(foodType, int(quantity_entry.get())))
        confirm_button.place(x=130,y=40)
    def addFood(self, foodType, quantity):
        foodItem = None
        if quantity > 0:
            if foodType == "Nutella":
                foodItem = {"name": "Nutella", "price": 15, "quantity": quantity}
            elif foodType == "Alcapone":
                foodItem = {"name": "Alcapone", "price": 20, "quantity": quantity}
            elif foodType == "Strawberry":
                foodItem = {"name": "Strawberry", "price": 12, "quantity": quantity}
            elif foodType == "Glaze":
                foodItem = {"name": "Glaze", "price": 15, "quantity": quantity}
            elif foodType == "Chocomallow":
                foodItem = {"name": "Chocomallow", "price": 13, "quantity": quantity}
            elif foodType == "Classic":
                foodItem = {"name": "Classic", "price": 10, "quantity": quantity}
            elif foodType == "Snowwhite":
                foodItem = {"name": "Snow White", "price": 10, "quantity": quantity}
            elif foodType == "Choco":
                foodItem = {"name": "Choco Choco", "price": 14, "quantity": quantity}
            elif foodType == "Sprinkles":
                foodItem = {"name": "Sprinkles", "price": 15, "quantity": quantity}
                
                if self.cartCleared:
                    self.receiptBox.delete("1.0", tk.END)
                    self.allowEdit = False
        else:
            messagebox.showinfo("BACK", "Input a number greater than 0")
            return
        
        self.foodList.append(foodItem)
        self.donCOn()
        self.Quantity.destroy()
        self.selectedItem = None
    def donCOn(self):
        try:
            self.connectDatabase()
            if self.cursor is not None:
                for food_list in self.foodList:
                    values = (food_list["name"], food_list["price"], food_list["quantity"])
                    self.cursor.execute('INSERT INTO product (productName, price, qty) VALUES (%s, %s, %s)', values)
                self.conn.commit()
                self.displayFoodItems()
            else:
                messagebox.showerror("Error", "Database connection not established.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.closeDatabase()
    def displayFoodItems(self):
        self.receiptBox.config(state=tk.NORMAL)
        self.receiptBox.delete("1.0", tk.END)
        for food_item in self.foodList:
            self.name = food_item["name"]
            self.price = food_item["price"]
            self.quantity = food_item.get("quantity", 1)
            self.totalItemPrice = self.price * self.quantity
            text_to_insert = f"{self.name}        Php {self.price:.2f}      Quantity: {self.quantity}     Php {self.totalItemPrice:.2f}\n"
            self.receiptBox.insert(tk.END, text_to_insert)
        self.receiptBox.config(state=tk.DISABLED)
    def donuts_Image(self):
        secondRect = tk.Canvas(self, width=180, height=180)
        secondRect.place(x=49,y=130)
        secondRect.create_rectangle(0, 0, 600, 1024, fill="#EFC4CA")
        self.secondImg = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\1.png"
        self.secondImg_1 = tk.PhotoImage(file=self.secondImg)
        self.secondLabel = tk.Label(self, image=self.secondImg_1,bg='#EFC4CA')
        self.secondLabel.place(x=75,y=135)
        self.Label_1_1= tk.Label(self,text="Php 15",font=("times new roman",12,'normal'),bg='#EFC4CA',fg='gray2')
        self.Label_1_1.place(x=60,y=280) 
        self.Label_1= tk.Label(self,text="Nutella",font=("times new roman",18,'bold'),bg='#EFC4CA',fg='gray2')
        self.Label_1.place(x=60,y=255) 
    
        thirdRect = tk.Canvas(self, width=180, height=180)
        thirdRect.place(x=49,y=346)
        thirdRect.create_rectangle(0, 0, 600, 1024, fill="#EFC4CA")
        self.thirdImg = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\f.png"
        self.thirdImg_1 = tk.PhotoImage(file=self.thirdImg)
        self.thirdLabel = tk.Label(self, image=self.thirdImg_1,bg='#EFC4CA')
        self.thirdLabel.place(x=75,y=350) 
        self.Label_2= tk.Label(self,text="Php 20",font=("times new roman",12,'normal'),bg='#EFC4CA',fg='gray2')
        self.Label_2.place(x=56,y=500)
        self.Label_2= tk.Label(self,text="Alcapone",font=("times new roman",18,'bold'),bg='#EFC4CA',fg='gray2')
        self.Label_2.place(x=54,y=470) 

        fourthRect = tk.Canvas(self, width=180, height=180) 
        fourthRect.place(x=49,y=560)
        fourthRect.create_rectangle(0, 0, 600, 1024, fill="#EFC4CA")
        self.Label_3_1= tk.Label(self,text="Php 12",font=("times new roman",12,'normal'),bg='#EFC4CA',fg='gray2')
        self.Label_3_1.place(x=53,y=710) 
        self.Label_3= tk.Label(self,text="Strawberry",font=("times new roman",16,'bold'),bg='#EFC4CA',fg='gray2')
        self.Label_3.place(x=50,y=685) 
        self.fourthIMG = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\h.png"
        self.fourthIMG_1 = tk.PhotoImage(file=self.fourthIMG)
        self.fourthLabel = tk.Label(self, image=self.fourthIMG_1,bg='#EFC4CA')
        self.fourthLabel.place(x=75,y=570) 
        #create a square for the self three square sa center
        fifthRect = tk.Canvas(self, width=180, height=180)
        fifthRect.place(x=330,y=130)
        fifthRect.create_rectangle(0, 0, 600, 1024, fill="#EFC4CA")
        self.Label_4= tk.Label(self,text="Glaze",font=("times new roman",20,'bold'),bg='#EFC4CA',fg='gray2')
        self.Label_4.place(x=340,y=250) 
        self.Label_4_1= tk.Label(self,text="Php 15",font=("times new roman",12,'normal'),bg='#EFC4CA',fg='gray2')
        self.Label_4_1.place(x=343,y=280)
        self.fifthIMG = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\i.png"
        self.fifthIMG_1 = tk.PhotoImage(file=self.fifthIMG)
        self.fifthLabel = tk.Label(self, image=self.fifthIMG_1,bg='#EFC4CA')
        self.fifthLabel.place(x=360,y=135) 

        sixRect = tk.Canvas(self, width=180, height=180)
        sixRect.place(x=330,y=346)
        sixRect.create_rectangle(0, 0, 600, 1024, fill="#EFC4CA")
        self.Label_5_1= tk.Label(self,text="Php 13",font=("times new roman",12,'normal'),bg='#EFC4CA',fg='gray2')
        self.Label_5_1.place(x=334,y=499) 
        self.Label_5= tk.Label(self,text="Chocomallow",font=("times new roman",15,'bold'),bg='#EFC4CA',fg='gray2')
        self.Label_5.place(x=334,y=475) 
        self.sixIMG = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\g.png"
        self.sixIMG_1 = tk.PhotoImage(file=self.sixIMG)
        self.sixLabel = tk.Label(self, image=self.sixIMG_1,bg='#EFC4CA')
        self.sixLabel.place(x=360,y=350) 
        
        sevenRect = tk.Canvas(self, width=180, height=180)
        sevenRect.place(x=330,y=560)
        sevenRect.create_rectangle(0, 0, 600, 1024, fill="#EFC4CA")
        self.Label_6= tk.Label(self,text="Classic",font=("times new roman",18,'bold'),bg='#EFC4CA',fg='gray2')
        self.Label_6.place(x=334,y=685)
        self.Label_6= tk.Label(self,text="Php 10",font=("times new roman",12,'normal'),bg='#EFC4CA',fg='gray2')
        self.Label_6.place(x=338,y=710)
        self.sevenIMG = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\d.png"
        self.sevenIMG_1 = tk.PhotoImage(file=self.sevenIMG)
        self.sevenLabel = tk.Label(self, image=self.sevenIMG_1,bg='#EFC4CA')
        self.sevenLabel.place(x=360,y=565) 
        #create a square for the self three square sa right
        eightRect = tk.Canvas(self, width=180, height=180)
        eightRect.place(x=600,y=130)
        eightRect.create_rectangle(0, 0, 600, 1024, fill="#EFC4CA")
        self.Label_7= tk.Label(self,text="Php 10",font=("times new roman",12,'normal'),bg='#EFC4CA',fg='gray2')
        self.Label_7.place(x=605,y=286)
        self.Label_7_1= tk.Label(self,text="Snow White",font=("times new roman",16,'bold'),bg='#EFC4CA',fg='gray2')
        self.Label_7_1.place(x=603,y=260)
        self.eightIMG = "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\j.png"
        self.eightIMG_1 = tk.PhotoImage(file=self.eightIMG)
        self.eightLabel = tk.Label(self, image=self.eightIMG_1,bg='#EFC4CA')
        self.eightLabel.place(x=630,y=135) 

        nineRect = tk.Canvas(self, width=180, height=180)
        nineRect.place(x=600,y=346)
        nineRect.create_rectangle(0, 0, 600, 1024, fill="#EFC4CA")
        self.nineIMG= "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\c.png"
        self.nineIMG_1 = tk.PhotoImage(file=self.nineIMG)
        self.nineLabel = tk.Label(self, image=self.nineIMG_1,bg='#EFC4CA')
        self.nineLabel.place(x=630,y=350) 
        self.Label_8= tk.Label(self,text="Choco Choco",font=("times new roman",15,'bold'),bg='#EFC4CA',fg='gray2')
        self.Label_8.place(x=603,y=475)
        self.Label_8_1= tk.Label(self,text="Php 14",font=("times new roman",12,'normal'),bg='#EFC4CA',fg='gray2')
        self.Label_8_1.place(x=605,y=500)

        tenthRect = tk.Canvas(self, width=180, height=180)
        tenthRect.place(x=600,y=560)
        tenthRect.create_rectangle(0, 0, 600, 1024, fill="#EFC4CA")
        self.tenImg= "C:\\Users\\Acer\\OneDrive\\Documents\\AssignmentsActivities Files\\IT5\\flowchart\\2.png"
        self.tenImg_1 = tk.PhotoImage(file=self.tenImg)
        self.tenLabel = tk.Label(self, image=self.tenImg_1,bg='#EFC4CA')
        self.tenLabel.place(x=630,y=565) 
        self.Label_9= tk.Label(self,text="Sprinkles",font=("times new roman",16,'bold'),bg='#EFC4CA',fg='gray2')
        self.Label_9.place(x=603,y=690)
        self.Label_9_1= tk.Label(self,text="Php 15",font=("times new roman",12,'normal'),bg='#EFC4CA',fg='gray2')
        self.Label_9_1.place(x=605,y=715)
    def log_out(self): 
        result = messagebox.askyesno("Log Out", "Are you sure you want to log out?")
        if result:
            self.destroy() 
        else:
            pass 
    def edit(self):
        if not self.foodList:
            messagebox.showinfo("Edit Error", "There are no items in the order to edit.")
            return
        item_names = [item["name"] for item in self.foodList]
        selected_item = simpledialog.askstring("Select Item", "Select the item to edit:", initialvalue=item_names[0], parent=self)

        if selected_item:
            self.qtyOfOrder(selected_item)
    def qtyOfOrder(self, foodType):
        self.selected_item = next((item for item in self.foodList if item["name"] == foodType), None)
        if self.selected_item:
            self.Quantity = tk.Toplevel()
            self.Quantity.title(f"Edit Quantity for {foodType}")
            self.Quantity.iconbitmap('icon.ico')
            self.Quantity.geometry('300x80')
            quantity_label = tk.Label(self.Quantity, text="Enter Quantity:")
            quantity_label.place(x=10, y=10)
            quantity_entry = tk.Entry(self.Quantity, font=('Arial', 12))
            quantity_entry.place(x=100, y=10)
            quantity_entry.insert(tk.END, str(self.selected_item.get("quantity", 1)))

            item_id = self.selected_item.get("name")

            confirm_button = tk.Button(self.Quantity, text="Confirm", font=("times new roman", 12, 'bold'),bg='#D9D9D9', fg='gray2', padx=5, pady=4,command=lambda: self.updateDatabase(item_id, int(quantity_entry.get())))
            confirm_button.place(x=130, y=40)
        else:
            messagebox.showerror("Error", "Item not found in the order list.")
    def updateDatabase(self, item_id, new_quantity):
        try:
            self.connectDatabase()
            updateSQL = "UPDATE product SET qty = %s WHERE productName = %s"
            self.cursor.execute(updateSQL, (new_quantity, item_id))
            self.conn.commit()

            messagebox.showinfo("Success", "Item updated successfully!")
            self.Quantity.destroy()
            for food_item in self.foodList:
                if food_item["name"] == item_id:
                    food_item["quantity"] = new_quantity
                    food_item["totalItemPrice"] = food_item["price"] * new_quantity
            self.displayFoodItems()
        except Exception as e:
            print(e)
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            self.closeDatabase()
    def totalPrice(self):
        self.total.config(state=tk.NORMAL)
        self.total.delete(0, tk.END)
        self.total_price = 0
        for food_item in self.foodList:
            self.total_price += food_item["price"] * food_item.get("quantity", 1)
        self.total.insert(tk.END, f"{self.total_price:.2f}")
        ques = messagebox.askyesno("Print Receipt", "Are you sure you want to print the receipt?")
        if ques:
            self.printReceipt() 
        else:
            pass 
    def clear(self):
        self.cartCleared = True
        self.foodList = []

        self.receiptBox.config(state=tk.NORMAL) 
        self.receiptBox.delete("1.0", tk.END)
        cart = "CART IS EMPTY"
        self.receiptBox.insert(tk.END, cart)
        self.receiptBox.config(state=tk.DISABLED) 
    def connectDatabase(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='donuts')
            self.cursor = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to connect to the database: {e}")
    def closeDatabase(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
    def printReceipt(self):
        #money
        self.money()
        #design
        messagebox.showinfo("PRINT RECEIPT", "Receipt printed successfully!")
        self.receipt = tk.Toplevel()
        self.receipt.title("Receipt")
        self.receipt.iconbitmap('icon.ico') 
        self.receipt.geometry('400x700')
        self.receipt.config(bg='#C98895')
        self.center(self.receipt, 400, 700)
        self.receipt.protocol("WM_DELETE_WINDOW", self.receiptClose) 

        self.crisLabel= tk.Label(self.receipt,text="Crispy Crowns",font=("times new roman",40,'bold'),bg='#C98895',fg='gray2')
        self.crisLabel.place(x=30,y=5)
        self.addressLabel= tk.Label(self.receipt,text="Address: University of Mindanao",font=("times new roman",16,'normal'),bg='#C98895',fg='gray2')
        self.addressLabel.place(x=65,y=70)
        self.addressLabel_1= tk.Label(self.receipt,text="(Matina Campus)",font=("times new roman",16,'normal'),bg='#C98895',fg='gray2')
        self.addressLabel_1.place(x=135,y=97)
        self.teleLabel= tk.Label(self.receipt,text="Telephone: 1234 567 89",font=("times new roman",12,'normal'),bg='#C98895',fg='gray2')
        self.teleLabel.place(x=130,y=120)
        self.desLabel= tk.Label(self.receipt,text="****************************************",font=("times new roman",16,'normal'),bg='#C98895',fg='gray2')
        self.desLabel.place(x=0,y=140)
        self.sampleLabel= tk.Label(self.receipt,text="SAMPLE RECEIPT",font=("times new roman",20,'bold'),bg='#C98895',fg='gray2')
        self.sampleLabel.place(x=85,y=155)
        self.desLabel_1= tk.Label(self.receipt,text="****************************************",font=("times new roman",16,'normal'),bg='#C98895',fg='gray2')
        self.desLabel_1.place(x=0,y=185)
        self.desLabel_2= tk.Label(self.receipt,text="****************************************",font=("times new roman",16,'normal'),bg='#C98895',fg='gray2')
        self.desLabel_2.place(x=0,y=600)
        self.desLabel_3= tk.Label(self.receipt,text="****************************************",font=("times new roman",16,'normal'),bg='#C98895',fg='gray2')
        self.desLabel_3.place(x=0,y=650)

        self.rBox = tk.Text(self.receipt, height=17, width=42, font=('Arial', 12),state=DISABLED,bg='#C98895')
        self.rBox.place(x=10, y=210)

        self.ttLabel = tk.Label(self.receipt, text="TOTAL:     PHP {:.2f}".format(self.total_price),bg='#C98895',font=("Arial",20,'bold'))
        self.ttLabel.place(x=20,y=528)

        self.cashLabel = tk.Label(self.receipt, text="CASH:           PHP {:.2f}".format(self.moneyEnter),bg='#C98895',font=("Arial",14,'normal'))
        self.cashLabel.place(x=20,y=556)

        self.changeLabel = tk.Label(self.receipt, text="CHANGE:     PHP {:.2f}".format(self.change),bg='#C98895',font=("Arial",14,'normal'))
        self.changeLabel.place(x=20,y=580)
        
        self.tyLabel= tk.Label(self.receipt,text="THANK YOU!",font=("times new roman",20,'bold'),bg='#C98895',fg='gray2')
        self.tyLabel.place(x=110,y=620)
        self.dateLabel= tk.Label(self.receipt,text="",font=("times new roman",15,'normal'),bg='#C98895',fg='gray2')
        self.dateLabel.place(x=10,y=665)
        #date
        currentDATETIME = datetime.now()
        CDTS = currentDATETIME.strftime("%Y-%m-%d %H:%M:%S")
        self.dateLabel.config(text=""+CDTS)
        #receipt
        self.rBox.config(state=tk.NORMAL)
        transactions = self.receiptTransact()
        for transaction_str in transactions:
            self.rBox.insert(tk.END, transaction_str)
        self.rBox.config(state=tk.DISABLED)
        self.receipt.mainloop()
    def receiptClose(self):
        self.receipt.destroy()
        self.clear()
        self.upTWid(0)
    def upTWid(self,amount):
        self.receiptBox.config(state=tk.NORMAL) 
        self.total.delete(0, tk.END)
        self.total.insert(tk.END, f"{amount:.2f}")
    def center(self, window, width, height):
        widthScreen = window.winfo_screenwidth()
        heightScreen = window.winfo_screenheight()
        x = (widthScreen - width) // 2
        y = (heightScreen - height) // 2
        window.geometry(f"{width}x{height}+{x}+{y}")
    def receiptTransact(self):
        try:
            transact = []
            for productData in self.foodList:
                product = "{:<5} {:<45}     Php {:>5}.00\n".format(
                            productData.get('quantity', 'N/A'),
                            productData.get('name', 'N/A'),
                            productData.get('price', 'N/A')*productData.get('quantity', 'N/A'))
                transact.append(product)
            return transact
        except Exception as e:
            print(f"Error during receiptTransact: {e}")
            return []
    def money(self):
        try:
            total = "{:.2f}".format(self.total_price)
            ttl = float(total)
            self.moneyEnter = simpledialog.askfloat("Enter Money", f"Total Php: {total}\nEnter amount:")
            if self.moneyEnter is not None:
                if self.moneyEnter > ttl or self.moneyEnter == ttl:
                    self.change = self.moneyEnter - ttl
                    if self.ttLabel is not None:
                        self.ttLabel.config(text="TOTAL:   PHP {:.2f}".format(ttl))
                        self.cashLabel.config(text="CASH:   PHP {:.2f}".format(self.moneyEnter))
                        self.changeLabel.config(text="CHANGE:   PHP {:.2f}".format(self.change))
                        self.printReceipt()
                        print("Receipt printed successfully.")
                else:
                    messagebox.showwarning("Insufficient Payment", "Please pay the full amount.")
                    self.money()
        except Exception as e:
            print(f"Error during money: {e}")