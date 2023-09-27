from tkinter import *
from tkinter import messagebox as msg
import mysql.connector

root = Tk()
root.title("Hotel Management")
root.geometry("700x500")
root.resizable(False, False)


#===================================================Database connection function
def conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="hotel_management"
    )

#===================================================Registration window
xyz = ""
def check():
    check_root=Tk()
    check_root.title("Registration Box")
    check_root.geometry("300x300")
    check_root.resizable(False, False)
    var=StringVar()

    def register():
        register = Tk()
        register.title("Hotel Management System")
        register.geometry("500x500")
        register.resizable(False, False)
        

        def validate():
            con=conn()
            cursor = con.cursor()
            query = "insert into hotel_table values(%s, %s, %s, %s, %s, %s)"
            args = (YN_entry.get(), YA_entry.get(), YNUM_entry.get(), DN_entry.get(), room_entry.get(), Payment_entry.get())
            cursor.execute(query, args)
            con.commit()
            con.close()
            msg.showinfo("Status", "checkInn - successful")

        click = Label(register, text="you clicked on", font=("Arial 18 bold"))
        click.place(x=20, y=20)

        coma = Label(register, text=":", font=("Arial 18 bold"))
        coma.place(x=260, y=20)

        checkinn = Label(register, text="CheckInn", font=("Arial 18 bold"))
        checkinn.place(x=340, y=20)

        Your_Name = Label(register, text="Enter Your Name            : ", font=("Arial 14 bold"))
        Your_Name.place(x=40, y=80)
        YN_entry = Entry(register)
        YN_entry.place(x=320, y=85)

        Your_address = Label(register, text="Enter Your Address     : ", font=("Arial 14 bold"))
        Your_address.place(x=40, y=110)
        YA_entry = Entry(register)
        YA_entry.place(x=320, y=115)

        Your_number = Label(register, text="Enter Your Number        : ", font=("Arial 14 bold"))
        Your_number.place(x=40, y=140)
        
        YNUM_entry = Entry(register)
        YNUM_entry.place(x=320, y=145)
        

        Day_number = Label(register, text="Number Of Days           : ", font=("Arial 14 bold"))
        Day_number.place(x=40, y=170)
        DN_entry = Entry(register)
        DN_entry.place(x=320, y=175)

        room = Label(register, text="Choose Your Room:", font=("Arial 14 bold"))
        room.place(x=40, y=200)
        room_entry = Entry(register)
        room_entry.place(x=320, y=205)

        Payment = Label(register, text="Choose Payment:", font=("Arial 14 bold"))
        Payment.place(x=40, y=230)
        Payment_entry = Entry(register)
        Payment_entry.place(x=320, y=235)

        Submit = Button(register, text="Submit", bg='red', font=("Arial 10 bold"), command=validate)
        Submit.place(x=250, y=380)
#=============================================================================================================
    
    name_label = Label(check_root, text="Name*", font=("Arial 14 bold"))
    name_label.place(x=40, y=20)
    name_entry = Entry(check_root)
    name_entry.place(x=140, y=25)
    
    contact_label = Label(check_root, text="Contact*", font=("Arial 14 bold"))
    contact_label.place(x=40, y=45)
    contact_entry = Entry(check_root)
    contact_entry.place(x=140, y=50)

    email_label = Label(check_root, text="Email*", font=("Arial 14 bold"))
    email_label.place(x=40, y=70)
    email_entry = Entry(check_root)
    email_entry.place(x=140, y=75)
   
    city_label = Label(check_root, text="City*", font=("Arial 14 bold"))
    city_label.place(x=40, y=95)
    city_entry = Entry(check_root)
    city_entry.place(x=140, y=100)

    state_label = Label(check_root, text="State*", font=("Arial 14 bold"))
    state_label.place(x=40, y=120)
    state_entry = Entry(check_root)
    state_entry.place(x=140, y=125)

    register_button = Button(check_root, text="Register", bg='yellow', font=("Arial 10 bold"), command=register)
    register_button.place(x=150, y=180)
#==============================================================================================================
def guest():
    con=conn()
    cursor = con.cursor()
    query = "select * from hotel_table"
    cursor.execute(query)
    row = cursor.fetchall()
    
    guest1 = Tk()
    guest1.geometry("800x800")
    guest1.title("Guest list")
    k = 50
    for i in row:
        f = Label(guest1, text=i, font=("Arial 12"))
        f.place(x=20,y=k)
        k +=50
        
    con.commit()
    con.close()
    msg.showinfo("Status", "guest list")

#=============================================================================================================
def out():
    g = Tk()
    g.geometry("350x350")
    g.title("checkout")
    out = Label(g, text="Enter Mobile Number")
    out.place(x=40,y=80)
    out1=Entry(g,)
    out1.place(x=140,y=80)
    def new():
        con=conn()
        cursor = con.cursor()
        query1="select number from hotel_table where number=%s"
        args1=(out1.get(),)
        cursor.execute(query1,args1)
        contact_num=cursor.fetchall()
        print(contact_num)
        try:
            val_str=contact_num[0]
            print("tuple : ",val_str[0])
            query = "delete from hotel_table where number = %s"
            args=(out1.get(),)
            if out1.get() == val_str[0]:
                cursor.execute(query,args) 
                con.commit()
                con.close()
                msg.showinfo("Status", "checkout successful please do not come again")
            else:
                con.commit()
                con.close()
                msg.showinfo("Status", "contact num not found")
        except:
            msg.showinfo("Status", "contact not found ")
    btn=Button(g, text="check_out", font=('Arial 12 bold'), command=new)
    btn.place(x=90,y=140)

#==================================================================================
def info():
    i = Tk()
    i.geometry("700x700")
    i.title("Information")

    def get_info():
        con=conn()
        cursor = con.cursor()
        query="select * from hotel_table where number=%s"
        args=(YNUM_entry.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            for i in row:
                YN_entry.insert(0,i[0])
                YA_entry.insert(0,i[1])
                DN_entry.insert(0,i[3])
                room_entry.insert(0,i[4])
                Payment_entry.insert(0,i[5])
        con.commit()
        con.close()

    Your_Name = Label(i, text="Enter Your Name            : ", font=("Arial 14 bold"))
    Your_Name.place(x=40, y=80)
    YN_entry = Entry(i)
    YN_entry.place(x=320, y=85)

    Your_address = Label(i, text="Enter Your Address     : ", font=("Arial 14 bold"))
    Your_address.place(x=40, y=110)
    YA_entry = Entry(i)
    YA_entry.place(x=320, y=115)

    Your_number = Label(i, text="Enter Your Number        : ", font=("Arial 14 bold"))
    Your_number.place(x=40, y=140)
        
    YNUM_entry = Entry(i)
    YNUM_entry.place(x=320, y=145)
        

    Day_number = Label(i, text="Number Of Days           : ", font=("Arial 14 bold"))
    Day_number.place(x=40, y=170)
    DN_entry = Entry(i)
    DN_entry.place(x=320, y=175)

    room = Label(i, text="Choose Your Room:", font=("Arial 14 bold"))
    room.place(x=40, y=200)
    room_entry = Entry(i)
    room_entry.place(x=320, y=205)

    Payment = Label(i, text="Choose Payment:", font=("Arial 14 bold"))
    Payment.place(x=40, y=230)
    Payment_entry = Entry(i)
    Payment_entry.place(x=320, y=235)

    Submit = Button(i, text="Submit", bg='red', font=("Arial 10 bold"),command=get_info)
    Submit.place(x=250, y=380)
    
#============================================================================================

def exit_data():
    exit()
#========================================================================Main menu
welcome_label = Label(root, text="WELCOME", font=("Arial 20 bold"))
welcome_label.place(x=270, y=20)

hotel_label = Label(root, text="HOTEL MANAGEMENT", font=("impact 26"))
hotel_label.place(x=380, y=80)

python_label = Label(root, text="PYTHON TKINTER", font=("impact 30"))
python_label.place(x=385, y=140)

gui_label = Label(root, text="GUI", font=("impact 60"))
gui_label.place(x=460, y=200)

btn1 = Button(root, text="1. CHECK INN", font=("Arial 15"), command=check)
btn1.place(x=70, y=80)

btn2 = Button(root, text="2. SHOW GUEST LIST", font=("Arial 15"), command=guest)
btn2.place(x=70, y=130)

btn3 = Button(root, text="3. CHECK OUT", font=("Arial 15"), command=out)
btn3.place(x=70, y=180)

btn4 = Button(root, text="4. GET INFO OF ANY GUEST", font=("Arial 15"), command=info)
btn4.place(x=70, y=230)

btn5 = Button(root, text="5. EXIT", font=("Arial 15"), command=exit_data)
btn5.place(x=70, y=280)

root.mainloop()
