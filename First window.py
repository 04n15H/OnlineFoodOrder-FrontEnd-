from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import ImageTk,Image

root=Tk()
root.configure(bg="aquamarine")
root.title("ORDER ONLINE")
root.geometry("600x600")

def show_cart(h,z,x):
    top=Toplevel()
    top.geometry("300x300")
    top.title("CART")
    n=0
    for order in orders:
        my_label1=Label(top,text=order[1]).grid(row=n,column=0,sticky="w")
        my_label2=Label(top,text="\t\tRs."+str(order[3])+"\n").grid(row=n,column=5,sticky="w")
        n+=2
    back_btn=Button(top,text="Back",command=lambda:rstrnt(z,x))
    back_btn.grid(row=n+1,column=0)
    
    

def cart(id):
    # CALIING DATABASE
    # create a database or connect to one
    conn=sqlite3.connect('database_new.db')
    # create cursor
    c=conn.cursor()

    c.execute("SELECT *,rowid FROM "+city+" WHERE rowid="+str(id))
    selected=c.fetchall()
    print(selected)
    # commit change
    conn.commit()
    # close connection
    conn.close()
    print(selected[0])
    orders.append(selected[0]) 
    global cost
    cost+=selected[0][3]
    if(len(orders)): 
        show_cart_btn["state"]=NORMAL


def rstrnt(z,x):
    print(type(z))
    for widget in root.winfo_children():
        widget.grid_forget()
    sel_rstrnt=''

    for item in items:
        y=str(item[6])
        if(z==y):
            sel_rstrnt=item[0]
            print(sel_rstrnt)

    # CALIING DATABASE
    # create a database or connect to one
    conn=sqlite3.connect('database_new.db')
    # create cursor
    c=conn.cursor()
    # Query the database
    c.execute("SELECT *,rowid FROM "+city+" WHERE r_name="+f"'{sel_rstrnt}'")
    menu=c.fetchall()
    print(menu)
    # commit change
    conn.commit()
    # close connection
    conn.close()

    my_label=Label(root,text=sel_rstrnt+"\n",font=(50))
    my_label.grid(row=0,column=0)

    khana=StringVar()
    n=0
    for food in menu:
        k=50-len(food[1])
        Radiobutton(root,text=food[1]+(k*("."))+"Rs."+str(food[3]),value=food[6],variable=khana).grid(column=0,pady=4,sticky="w")
        n+=1

    add_cart=Button(root,text="Add Item",command=lambda:cart(khana.get()))
    add_cart.grid(row=2*n+2,column=3,sticky="e")

    back_btn=Button(root,text="Back",command=lambda:dish_category(x))
    back_btn.grid(row=2*n+2,column=1,sticky="w")

    global show_cart_btn
    show_cart_btn=Button(root,text="Show Cart",command=lambda:show_cart(1,z,x))
    show_cart_btn.grid(row=2*n+2,column=4)
    
    if(len(orders)==0):
        show_cart_btn["state"]=DISABLED
def open():
    for widget in root.winfo_children():
         widget.grid_forget()
    root.geometry("200x150")
    def get_city():
        global city
        city=clicked.get()
        print(city)
        main_window()



    
    myLabel=Label(root,text="Please!! Select your city")
    myLabel.grid(row=0,column=2)


    option=[
        "Jalandhar",
        "Chandigarh",
        "Patiala",
        "Bathinda",
        "Firozpur",
        "Amritsar",
        "Ludhiana"
    ]
    clicked=StringVar()
    clicked.set(option[0])

    drop=OptionMenu(root,clicked,*option)
    drop.grid(row=2,column=2,padx=50)

    my_button=Button(root,text="OK",command=get_city)
    my_button.grid(row=4,column=2)


def dish_category(x):
    orders.clear()
    cost=0
    print(city)
    
    for widget in root.winfo_children():
        widget.grid_forget()

    # CALIING DATABASE
    # create a database or connect to one
    conn=sqlite3.connect('database_new.db')
    # create cursor
    c=conn.cursor()
    # Query the database
    c.execute("SELECT *,rowid FROM "+city+" WHERE d_category="+f"'{x}'")
    global items
    items=c.fetchall()
    print(items)
    # commit change
    conn.commit()
    # close connection
    conn.close()

    dish=StringVar()
    n=0
    for item in items:
        Radiobutton(root,text=item[1],value=item[6],variable=dish).grid(column=0,sticky="w")
        label1=Label(root,text=item[0]+"\t\t\t      "+"Rs."+str(item[3])).grid(column=3,stick="e")
        n+=1
    # dish.set(item[1]+"\tRs."+str(item[3])+"\t\t\t\t"+item[0])
    
    
    open_rstrnt=Button(root,text="Open Restaurant",command=lambda:rstrnt(dish.get(),x))
    open_rstrnt.grid(row=2*n+2,column=3,sticky="e")


def main_window():
    for widget in root.winfo_children():
        widget.grid_forget()
    root.geometry("500x510")
    pizza_img=PhotoImage(file="C:/Users/Danish/OneDrive/Documents/Python Project/images/WhatsApp Image 2024-04-19 at 21.34.18_f91f7faf.png")
    img_label=Label(image=pizza_img)

    #CREATE BUTTONS
    pizza_btn=Button(root,text="pizza",command=lambda: dish_category("pizza"),pady=50,padx=50,borderwidth=0,bg='aquamarine')
    pizza_btn.grid(row=1,column=0,pady=20,padx=20)
    burger_btn=Button(root,text="BURGERS",command=lambda: dish_category("burger"),pady=50,padx=50)
    burger_btn.grid(row=1,column=1,padx=20)
    NOODLES_btn=Button(root,text="NOODLES",command=lambda: dish_category("noodles"),pady=50,padx=48)
    NOODLES_btn.grid(row=1,column=2,padx=20)
    pasta_btn=Button(root,text="PASTA",command=lambda: dish_category("pasta"),pady=50,padx=52)
    pasta_btn.grid(row=2,column=0,pady=20,padx=20)
    sandwich_btn=Button(root,text="SANDWICH",command=lambda: dish_category("sandwich"),pady=50,padx=55)
    sandwich_btn.grid(row=2,column=1,padx=20)
    thali_btn=Button(root,text="THALI",command=lambda: dish_category("thali"),pady=50,padx=59)
    thali_btn.grid(row=2,column=2,padx=20)
    soup_btn=Button(root,text="SOUP",command=lambda: dish_category("soup"),pady=50,padx=55)
    soup_btn.grid(row=3,column=0,pady=20,padx=20)
    beverages_btn=Button(root,text="BEVERAGES",command=lambda: dish_category("beverages"),pady=50,padx=45)
    beverages_btn.grid(row=3,column=1,padx=20)


open()
global orders
orders=[]
global cost
cost=0











root.mainloop()

