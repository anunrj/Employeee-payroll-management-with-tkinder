from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management System-Fanshawe Collage")

        # =======================Variables===============================
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_designation = StringVar()
        self.var_email = StringVar()
        self.var_address = StringVar()
        self.var_phone = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_idproofcomb = StringVar()
        self.var_combstate = StringVar()
        self.var_salary = StringVar()

        lbl_title = Label(root, text="Employee Management System-:Fanshawe Collage", font=('times new roman', 28, 'bold'), fg='darkblue', bg='white')
        lbl_title.place(x=0, y=0, width=1530, height=50)

        # ============================LOGO====================================
        img_logo = Image.open('logof.png')
        img_logo = img_logo.resize((50, 50))
        self.photo1 = ImageTk.PhotoImage(img_logo)
        self.logo = Label(root, image=self.photo1)
        self.logo.place(x=270, y=0, width=50, height=50)

        # =========================IMAGE FRAME========================
        img_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        img_frame.place(x=0, y=50, width=1530, height=160)

        # ===========================first image==============================
        img1 = Image.open('image1.jpeg')
        img1 = img1.resize((540, 160))
        self.photo2 = ImageTk.PhotoImage(img1)
        self.img_1 = Label(img_frame, image=self.photo2)
        self.img_1.place(x=0, y=0, width=510, height=160)

        # ==========================second image==================================
        img2 = Image.open('image1.jpeg')
        img2 = img2.resize((540, 160))
        self.photo3 = ImageTk.PhotoImage(img2)
        self.img_2 = Label(img_frame, image=self.photo3)
        self.img_2.place(x=540, y=0, width=510, height=160)

        # ===========================third image===================================
        img3 = Image.open('image1.jpeg')
        img3 = img3.resize((540, 160))
        self.photo4 = ImageTk.PhotoImage(img3)
        self.img_3 = Label(img_frame, image=self.photo4)
        self.img_3.place(x=1000, y=0, width=510, height=160)

        # =========================main frame=====================================
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        main_frame.place(x=10, y=210, width=1500, height=560)

        # =====================upper frame======================================
        upper_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text='Employee Information', font=('times new roman', 11, 'bold'), fg='red', bg='white')
        upper_frame.place(x=10, y=10, width=1480, height=270)

        # ==========================labels and entry fields===============================
        lbl_dep = Label(upper_frame, text='Department', font=('ariel', 11, 'bold'), bg='white')
        lbl_dep.grid(row=0, column=0, padx=2, sticky=W)

        combo_dep = ttk.Combobox(upper_frame, textvariable=self.var_dep, font=('times new roman', 11, 'bold'), width=17, state='readonly')
        combo_dep['values'] = ('Select Department', 'HR', 'Software', 'Manager', 'Finance')
        combo_dep.current(0)
        combo_dep.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Name
        lbl_name = Label(upper_frame, text='Name', font=('ariel', 11, 'bold'), bg='white')
        lbl_name.grid(row=0, column=2, sticky=W, padx=2, pady=7)

        txt_name = ttk.Entry(upper_frame, textvariable=self.var_name, width=22, font=('ariel', 11, 'bold'))
        txt_name.grid(row=0, column=3, padx=2, pady=7)

        # Designation
        lbl_designation = Label(upper_frame, text='Designation', font=('ariel', 11, 'bold'), bg='white')
        lbl_designation.grid(row=1, column=0, sticky=W, padx=2, pady=7)

        txt_designation = ttk.Entry(upper_frame, textvariable=self.var_designation, width=22, font=('ariel', 11, 'bold'))
        txt_designation.grid(row=1, column=1, padx=2, pady=7)

        # Email
        lbl_email = Label(upper_frame, text='Email', font=('ariel', 11, 'bold'), bg='white')
        lbl_email.grid(row=1, column=2, sticky=W, padx=2, pady=7)

        txt_email = ttk.Entry(upper_frame, textvariable=self.var_email, width=22, font=('ariel', 11, 'bold'))
        txt_email.grid(row=1, column=3, padx=2, pady=7)

        # DOB
        lbl_dob = Label(upper_frame, text='DOB', font=('ariel', 11, 'bold'), bg='white')
        lbl_dob.grid(row=3, column=0, sticky=W, padx=2, pady=7)

        txt_dob = ttk.Entry(upper_frame, textvariable=self.var_dob, width=22, font=('ariel', 11, 'bold'))
        txt_dob.grid(row=3, column=1, padx=2, pady=7)

        # DOJ
        lbl_doj = Label(upper_frame, text='DOJ', font=('ariel', 11, 'bold'), bg='white')
        lbl_doj.grid(row=3, column=2, sticky=W, padx=2, pady=7)

        txt_doj = ttk.Entry(upper_frame, textvariable=self.var_doj, width=22, font=('ariel', 11, 'bold'))
        txt_doj.grid(row=3, column=3, padx=2, pady=7)

        # ID Proof
        lbl_id = Label(upper_frame, text='ID Proof', font=('ariel', 11, 'bold'), bg='white')
        lbl_id.grid(row=4, column=0, padx=2, sticky=W)
        com_txt_id = ttk.Combobox(upper_frame, textvariable=self.var_idproofcomb, state="readonly", font=('ariel', 11, 'bold'), width=17)
        com_txt_id['values'] = ('Select your ID', 'Licence', 'SIN Number')
        com_txt_id.current(0)
        com_txt_id.grid(row=4, column=1, sticky=W, padx=2, pady=7)

        # Address
        lbl_address = Label(upper_frame, text='Address', font=('ariel', 11, 'bold'), bg='white')
        lbl_address.grid(row=2, column=0, sticky=W, padx=2, pady=7)
        txt_address = ttk.Entry(upper_frame, textvariable=self.var_address, width=22, font=('ariel', 11, 'bold'))
        txt_address.grid(row=2, column=1, padx=2, pady=7)

        # Phone
        lbl_phone = Label(upper_frame, text='Phone:', font=('ariel', 11, 'bold'), bg='white')
        lbl_phone.grid(row=2, column=2, sticky=W, padx=2, pady=7)
        txt_phone = ttk.Entry(upper_frame, textvariable=self.var_phone, width=22, font=('ariel', 11, 'bold'))
        txt_phone.grid(row=2, column=3, padx=2, pady=7)

        # Employment Type
        lbl_full = Label(upper_frame, text='State', font=('ariel', 11, 'bold'), bg='white')
        lbl_full.grid(row=4, column=2, padx=2, sticky=W)
        com_txt_full = ttk.Combobox(upper_frame, textvariable=self.var_combstate, state="readonly", font=('ariel', 11, 'bold'), width=17)
        com_txt_full['values'] = ('Select full/part(time)', 'Full Time', 'Part Time')
        com_txt_full.current(0)
        com_txt_full.grid(row=4, column=3, sticky=W, padx=2, pady=7)

        # Salary
        lbl_sal = Label(upper_frame, text='Salary', font=('ariel', 11, 'bold'), bg='white')
        lbl_sal.grid(row=2, column=4, sticky=W, padx=2, pady=7)
        txt_sal = ttk.Entry(upper_frame, textvariable=self.var_salary, width=22, font=('ariel', 11, 'bold'))
        txt_sal.grid(row=2, column=5, padx=2, pady=7)
        #===========================image==============================================================
        img4 = Image.open('fanshawe.png')
        img4 = img4.resize((540, 160))
        self.photo5 = ImageTk.PhotoImage(img4)
        self.img_4 = Label(upper_frame, image=self.photo5)
        self.img_4.place(x=800, y=0, width=400, height=250)

        # Button frame
        button_frame = Frame(upper_frame, bd=2, relief=RIDGE, bg='white')
        button_frame.place(x=1250, y=0, width=170, height=200)

        # Save button
        btn_save = Button(button_frame, text='Save', command=self.add_data, font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_save.grid(row=0, column=0, pady=5)

        # Update button
        btn_update = Button(button_frame, text='Update',command=self.update_data, font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_update.grid(row=1, column=0, pady=5)

        # Delete button
        btn_delete = Button(button_frame, text='Delete',command=self.delete_data, font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_delete.grid(row=2, column=0, pady=5)

        # Clear button
        btn_clear = Button(button_frame, text='Clear',command=self.reset_data, font=('arial', 15, 'bold'), width=13, bg='blue', fg='white')
        btn_clear.grid(row=3, column=0, pady=5)

        # ==========================lower frame=============================
        lower_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, bg='white', text='Employee Information Table', font=('times new roman', 11, 'bold'), fg='red')
        lower_frame.place(x=10, y=280, width=1480, height=270)

        # Search frame
        search_frame = LabelFrame(lower_frame, bd=2, relief=RIDGE, bg='white', text='Search Employee Information', font=('times new roman', 11, 'bold'), fg='red')
        search_frame.place(x=0, y=0, width=1470, height=60)

        # Search by label
        search_by = Label(search_frame, font=('arial', 11, 'bold'), text='Search By:', fg='white', bg='red')
        search_by.grid(row=0, column=0, sticky=W, padx=5)

        # Search option
        
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(search_frame, textvariable=self.var_com_search, state="readonly", font=('arial', 12, 'bold'), width=18)
        com_txt_search['values'] = ('Select Option', 'Phone')
        com_txt_search.current(0)
        com_txt_search.grid(row=0, column=1, sticky=W, padx=5)

        # Search text entry
        self.var_search = StringVar()
        txt_search = ttk.Entry(search_frame, textvariable=self.var_search, width=22, font=('arial', 10, 'bold'))
        txt_search.grid(row=0, column=2, padx=5)

        # Search button
        btn_search = Button(search_frame, text='Search', command=self.search_data,font=('arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_search.grid(row=0, column=3, padx=5)

        # Show All button
        btn_showall = Button(search_frame, text='Show All', command=self.fetch_data,font=('arial', 13, 'bold'), width=14, bg='blue', fg='white')
        btn_showall.grid(row=0, column=4, padx=5)

        # Table frame
        table_frame = Frame(lower_frame, bd=3, relief=RIDGE)
        table_frame.place(x=0, y=60, width=1470, height=170)

        # Scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, column=('dep', 'name', 'degi', 'email','address','phone', 'dob', 'doj', 'idproof', 'state', 'salary'), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep', text='Department')
        self.employee_table.heading('name', text='Name')
        self.employee_table.heading('degi', text='Designation')
        self.employee_table.heading('email', text='Email')
        self.employee_table.heading('address', text='Address')
        self.employee_table.heading('dob', text='DOB')
        self.employee_table.heading('doj', text='DOJ')
        self.employee_table.heading('idproof', text='ID Proof')
        
        self.employee_table.heading('phone', text='Phone')
        self.employee_table.heading('state', text='State')
        self.employee_table.heading('salary', text='Salary')

        self.employee_table['show'] = 'headings'

        self.employee_table.column('dep', width=100)
        self.employee_table.column('name', width=100)
        self.employee_table.column('degi', width=100)
        self.employee_table.column('email', width=100)
        self.employee_table.column('address', width=100)
        self.employee_table.column('dob', width=100)
        self.employee_table.column('doj', width=100)
        self.employee_table.column('idproof', width=100)
        
        self.employee_table.column('phone', width=100)
        self.employee_table.column('state', width=100)
        self.employee_table.column('salary', width=100)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_dep.get() == "" or self.var_email.get() == "":
            messagebox.showerror('Error', 'All fields are required')
        else:
            try:
                conn = mysql.connector.connect(host='localhost', username='root', password='', database='mydata')
                my_cursor = conn.cursor()
                my_cursor.execute('INSERT INTO emp1 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', (
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_designation.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_phone.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idproofcomb.get(),
                    
                    self.var_combstate.get(),
                    self.var_salary.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee has been added successfully')
            except Exception as es:
                messagebox.showerror('Error', f'Due to: {str(es)}',parent=self.root)
        
    def fetch_data(self):
        conn = mysql.connector.connect(host='localhost', username='root', password='', database='mydata')
        my_cursor = conn.cursor()
        my_cursor.execute('SELECT * FROM emp1')
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('', 'end', values=row)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row = self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        row=content['values']
        self.var_dep.set(row[0])
        self.var_name.set(row[1])
        self.var_designation.set(row[2])
        self.var_email.set(row[3])
        self.var_address.set(row[4])
        self.var_phone.set(row[5])
        self.var_dob.set(row[6])
        self.var_doj.set(row[7])
        self.var_idproofcomb.set(row[8])
        self.var_combstate.set(row[9])
        self.var_salary.set(row[10])

#======================update========================================
    def update_data(self):
     if self.var_dep.get() == "" or self.var_email.get() == "":
        messagebox.showerror('Error', 'All fields are required')
     else:
        try:
            update = messagebox.askyesno('Update', 'Do you want to update this employee', parent=self.root)
            if update > 0:
                conn = mysql.connector.connect(host='localhost', username='root', password='', database='mydata')
                my_cursor = conn.cursor()
                my_cursor.execute('''
                    UPDATE emp1 
                    SET Department=%s, Name=%s, Designation=%s, Email=%s, Address=%s, Phone=%s, Dob=%s, Doj=%s, State=%s, Salary=%s 
                    WHERE Idproof=%s
                ''', (
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_designation.get(),
                    self.var_email.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                     self.var_idproofcomb.get(),
                    self.var_address.get(),
                    self.var_phone.get(),
                    
                    
                    self.var_combstate.get(),
                    self.var_salary.get()
                    
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success', 'Employee updated successfully', parent=self.root)
            else:
                return
        except Exception as es:
            messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)

    #===========================delete function=======================================
    def delete_data(self):
     if self.var_idproofcomb.get() == "":
        messagebox.showerror('Error', 'Please select an employee to delete', parent=self.root)
     else:
        try:
            delete = messagebox.askyesno('Delete', 'Do you want to delete this employee?', parent=self.root)
            if delete > 0:
                conn = mysql.connector.connect(host='localhost', username='root', password='', database='mydata')
                my_cursor = conn.cursor()
                my_cursor.execute('DELETE FROM emp1 WHERE Idproof=%s', (self.var_idproofcomb.get(),))
                
                conn.commit()
                conn.close()
                messagebox.showinfo('Deleted', 'Employee deleted successfully', parent=self.root)
            else:
                return
        except Exception as es:
            messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)

#=========================reset function===========================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designation.set("Select Designation")
        self.var_email.set("")
        self.var_address.set("")
        self.var_phone.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_combstate.set("Select State")
        self.var_salary.set("")
        self.var_idproofcomb.set("")

    #======================search button==========================================
    def search_data(self):
     if self.var_com_search.get() == "" or self.var_search.get() == "":
        messagebox.showerror('Error', 'Please select an option and enter a value', parent=self.root)
     else:
        try:
            conn = mysql.connector.connect(host='localhost', username='root', password='', database='mydata')
            my_cursor = conn.cursor()
            query = f"SELECT * FROM emp1 WHERE {self.var_com_search.get()} LIKE %s"
            value = f"%{self.var_search.get()}%"
            my_cursor.execute(query, (value,))
            rows = my_cursor.fetchall()
            if len(rows) != 0:
                self.employee_table.delete(*self.employee_table.get_children())
                for row in rows:
                    self.employee_table.insert('', END, values=row)
                conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror('Error', f'Due to: {str(es)}', parent=self.root)




    

        





if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
