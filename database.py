from tkinter import *
import sqlite3

root=Tk()
root.title("ORDER ONLINE")
root.iconbitmap("C:/Users/Danish/Downloads/discussion_talk_conversation_interview_icon_262575 (1).ico")
root.geometry("805x400")

def delete():
    # create a database or connect to one
    conn=sqlite3.connect('database_new.db')
    # create cursor
    c=conn.cursor()
    # Delete a record
    c.execute("DELETE from "+city.get()+" WHERE oid="+delete_box.get())
    # commit change
    conn.commit()
    # close connection
    conn.close()
    delete_box.delete(0,END)

# show restaurants
def query():
    # query_label.grid_forget(0,END)
    # create a database or connect to one
    conn=sqlite3.connect('database_new.db')
    # create cursor
    c=conn.cursor()
    # show results
    print_records=''
    c.execute("SELECT *,rowid FROM "+city.get()+ " ORDER BY r_name")
    records=c.fetchall()
    for record in records:
        print_records +=str(record) + "\n"

    query_label=Label(root,text=print_records)
    query_label.grid(row=9,column=0,columnspan=10)
    
    # commit change
    conn.commit()

    # close connection
    conn.close()

def submit():
    # create a database or connect to one
    conn=sqlite3.connect('database_new.db')

    # create cursor
    c=conn.cursor()

    c.execute("INSERT INTO "+city.get()+" VALUES (:r_name,:d_name,:address,:d_cost,:city,:d_category)",
              {
               'r_name' :r_name.get(),
               'd_name':d_name.get(),
               'address':address.get(),
               'd_cost':d_cost.get(),
               'city':city.get(),
               'd_category':d_category.get()
              } )

    # commit change
    conn.commit()

    # close connection
    conn.close()

    d_name.delete(0,END)

    d_cost.delete(0,END)

# # Jalandhar Table
# # create a database or connect to one
# conn=sqlite3.connect('database_new.db')

# # create cursor
# c=conn.cursor()

# c.execute("""CREATE TABLE Jalandhar (
#           r_name text,
#           d_name text,
#           address text,
#           d_cost integer,
#           city text,
#           d_category text         
#     )""")

# # commit change
# conn.commit()

# # close connection
# conn.close()

# # Patiala Table
# # create a database or connect to one
# conn=sqlite3.connect('database_new.db')

# # create cursor
# c=conn.cursor()

# c.execute("""CREATE TABLE Patiala (
#           r_name text,
#           d_name text,
#           address text,
#           d_cost integer,
#           city text,
#           d_category text         
#     )""")

# # commit change
# conn.commit()

# # close connection
# conn.close()

# # # Bathinda Table
# # # create a database or connect to one
# conn=sqlite3.connect('database_new.db')

# # create cursor
# c=conn.cursor()

# c.execute("""CREATE TABLE Bathinda (
#           r_name text,
#           d_name text,
#           address text,
#           d_cost integer,
#           city text,
#           d_category text         
#     )""")

# # commit change
# conn.commit()

# # close connection
# conn.close()

# # # Firozpur Table
# # # create a database or connect to one
# conn=sqlite3.connect('database_new.db')

# # create cursor
# c=conn.cursor()

# c.execute("""CREATE TABLE Firozpur (
#           r_name text,
#           d_name text,
#           address text,
#           d_cost integer,
#           city text,
#           d_category text         
#     )""")

# # commit change
# conn.commit()

# # close connection
# conn.close()


# # # Amritsar Table
# # # create a database or connect to one
# conn=sqlite3.connect('database_new.db')

# # create cursor
# c=conn.cursor()

# c.execute("""CREATE TABLE Amritsar (
#           r_name text,
#           d_name text,
#           address text,
#           d_cost integer,
#           city text,
#           d_category text         
#     )""")

# # commit change
# conn.commit()

# # close connection
# conn.close()


# # # Ludhiana Table
# # # create a database or connect to one
# conn=sqlite3.connect('database_new.db')

# # create cursor
# c=conn.cursor()

# c.execute("""CREATE TABLE Ludhiana (
#           r_name text,
#           d_name text,
#           address text,
#           d_cost integer,
#           city text,
#           d_category text         
#     )""")

# # commit change
# conn.commit()

# close connection
# conn.close()

r_name_label=Label(root,text="Restaurant name")
r_name_label.grid(row=0,column=0)
d_name_label=Label(root,text="Dish name")
d_name_label.grid(row=1,column=0)
address_label=Label(root,text="address")
address_label.grid(row=2,column=0)
d_cost_label=Label(root,text="Dish Cost")
d_cost_label.grid(row=3,column=0)
city_label=Label(root,text="city name")
city_label.grid(row=4,column=0)
d_category_label=Label(root,text="Dish Category")
d_category_label.grid(row=5,column=0)

r_name=Entry(root,width=50)
r_name.grid(row=0,column=1,columnspan=2)
d_name=Entry(root,width=50)
d_name.grid(row=1,column=1,columnspan=2)
address=Entry(root,width=50)
address.grid(row=2,column=1,columnspan=2)
d_cost=Entry(root,width=50)
d_cost.grid(row=3,column=1,columnspan=2)
city=Entry(root,width=50)
city.grid(row=4,column=1,columnspan=2)
d_category=Entry(root,width=50)
d_category.grid(row=5,column=1,columnspan=2)
delete_box=Entry(root,width=30)
delete_box.grid(row=8,column=1,columnspan=2)

submit_btn=Button(root,text='Submit',padx=50,command=submit)
submit_btn.grid(row=6,column=1)

show_entries_btn=Button(root,text="Show Entries",command=lambda:query())
show_entries_btn.grid(row=7,column=1)

delete_btn=Button(root,text="DELETE Record",command=delete)
delete_btn.grid(row=8,column=0)

root.mainloop()
