# import tkinter as tk
# from tkinter import ttk

# def set_price(event):
#     selected_item = item_combobox.get()
#     price = item_prices[selected_item]
#     price_entry.config(state="normal")
#     price_entry.delete(0, tk.END)
#     price_entry.insert(0, str(price))
#     price_entry.config(state="disabled")

# def add_item():
#     item = item_combobox.get()
#     price = item_prices[item]
#     quantity = int(quantity_combobox.get())
#     total_price[0] += price * quantity
#     items.append((item, price, quantity))

#     display_text.insert(tk.END, f"{item}\t\t{price}\t\t{quantity}\n")
#     total_var.set(str(total_price[0]))

# def generate_bill():
#     bill = f"Item\t\tPrice\t\tQuantity\n"
#     for item, price, quantity in items:
#         bill += f"{item}\t\t{price}\t\t{quantity}\n"
#     bill += f"\nTotal Price: {total_price[0]}"
#     print(bill)  # You can also save this bill to a file if you want

# # Create main window
# root = tk.Tk()
# root.title("Sweet Shop Bill Generator")

# items = []  # List to store items
# total_price = [0]  # Variable to store total price

# # Predefined items and their prices
# item_prices = {
#     "Gulab Jamun": 200,
#     "Ras Malai": 250,
#     "Lassi": 20,
#     "Paneer": 170,
#     "Ice Cream": 100,
#     "Chocolate": 150,
#     "Cake": 200
# }

# # Labels
# item_label = tk.Label(root, text="Item:")
# item_label.grid(row=0, column=0, padx=10, pady=5)

# price_label = tk.Label(root, text="Price:")
# price_label.grid(row=0, column=1, padx=10, pady=5)

# quantity_label = tk.Label(root, text="Quantity:")
# quantity_label.grid(row=0, column=2, padx=10, pady=5)

# # Dropdown list for items
# item_combobox = ttk.Combobox(root, values=list(item_prices.keys()))
# item_combobox.grid(row=1, column=0, padx=10, pady=5)
# item_combobox.bind("<<ComboboxSelected>>", set_price)

# # Entry field for price (disabled)
# price_entry = tk.Entry(root, state="disabled")
# price_entry.grid(row=1, column=1, padx=10, pady=5)

# # Dropdown list for quantity
# quantity_combobox = ttk.Combobox(root, values=[str(i) for i in range(1, 11)])
# quantity_combobox.grid(row=1, column=2, padx=10, pady=5)

# # Add button
# add_button = tk.Button(root, text="Add Item", command=add_item)
# add_button.grid(row=1, column=3, padx=10, pady=5)

# # Display area for items and total price
# display_text = tk.Text(root, height=10, width=50)
# display_text.grid(row=2, column=0, columnspan=4, padx=10, pady=5)
# display_text.insert(tk.END, "Items\t\tPrice\t\tQuantity\n")

# # Total price label
# total_label = tk.Label(root, text="Total Price:")
# total_label.grid(row=3, column=0, padx=10, pady=5)

# total_var = tk.StringVar()
# total_var.set("0")
# total_price_label = tk.Label(root, textvariable=total_var)
# total_price_label.grid(row=3, column=1, padx=10, pady=5)

# # Generate bill button
# generate_button = tk.Button(root, text="Generate Bill", command=generate_bill)
# generate_button.grid(row=4, column=0, columnspan=4, padx=10, pady=5)

# root.mainloop()




from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image

root = Tk()
root.title("ORDER ONLINE")
root.geometry("600x600")

def calc_cost():
    global cost
    cost = 40
    for order in orders:
        cost += order[3]

def remove(rmv):
    global cost
    orders.pop(int(rmv)-1)
    top.destroy()
    show_cart(2)

def show_cart(h):
    global top
    top = Toplevel(root)  # Changed here
    top.geometry("300x300")
    top.title("CART")
    n = 0
    i = 1
    for order in orders:
        my_label1 = Label(top, text=str(i)+". "+order[1]).grid(row=n, column=0, sticky="w")
        my_label2 = Label(top, text="\tRs."+str(order[3])+"\n").grid(row=n, column=2, sticky="w")
        n += 2
        i += 1
    deliv = Label(top, text="Delivery: Rs.40")
    deliv.grid(row=n+1, column=2, sticky="e")
    calc_cost()
    total = Label(top, text="TOTAL: Rs."+str(cost))
    total.grid(row=n+2, column=2, sticky="e")
    remove_btn = Button(top, text="Remove Item", command=lambda: remove(remove_entry.get()))
    remove_btn.grid(row=n+3, column=0, sticky="w", columnspan=1)
    global remove_entry
    remove_entry = Entry(top, width=5, borderwidth=2)
    remove_entry.grid(row=n+3, column=1, sticky="w")
    back1_btn = Button(top, text="Back", command=lambda: top.destroy())
    back1_btn.grid(row=n+4, column=0, sticky="w", pady=10)

def cart(id):
    conn = sqlite3.connect('database_new.db')
    c = conn.cursor()
    c.execute("SELECT *,rowid FROM "+city+" WHERE rowid="+str(id))
    selected = c.fetchall()
    conn.commit()
    conn.close()
    orders.append(selected[0]) 
    if(len(orders)): 
        show_cart_btn["state"] = NORMAL

def rstrnt(z, x):
    for widget in root.winfo_children():
        widget.grid_forget()
    sel_rstrnt = ''
    for item in items:
        y = str(item[6])
        if(z == y):
            sel_rstrnt = item[0]

    conn = sqlite3.connect('database_new.db')
    c = conn.cursor()
    c.execute("SELECT *,rowid FROM "+city+" WHERE r_name="+f"'{sel_rstrnt}'")
    menu = c.fetchall()
    conn.commit()
    conn.close()

    my_label = Label(root, text=sel_rstrnt+"\n", font=(50))
    my_label.grid(row=0, column=0)
    khana = StringVar()
    n = 0
    for food in menu:
        k = 50 - len(food[1])
        Radiobutton(root, text=food[1]+(k*("."))+"Rs."+str(food[3]), value=food[6], variable=khana).grid(column=0, pady=4, sticky="w")
        n += 1
    khana.set(z)
    add_cart = Button(root, text="Add Item", command=lambda: cart(khana.get()))
    add_cart.grid(row=2*n+2, column=3, sticky="e")
    back_btn = Button(root, text="Back", command=lambda: dish_category(x))
    back_btn.grid(row=2*n+2, column=1, sticky="w")
    global show_cart_btn
    show_cart_btn = Button(root, text="Show Cart", command=lambda: show_cart(1))
    show_cart_btn.grid(row=2*n+2, column=4)
    if(len(orders) == 0):
        show_cart_btn["state"] = DISABLED

def open_window():  # Renamed function name
    top = Toplevel(root)  # City selection window
    top.geometry("200x150")
    def get_city():
        global city
        city = clicked.get()
        print(city)
        top.destroy()
        main_window()  # Call main_window() after city selection

    myLabel = Label(top, text="Please!! Select your city")
    myLabel.grid(row=0, column=2)

    option = [
        "Jalandhar",
        "Chandigarh",
        "Patiala",
        "Bathinda",
        "Firozpur",
        "Amritsar",
        "Ludhiana"
    ]
    clicked = StringVar()
    clicked.set(option[0])

    drop = OptionMenu(top, clicked, *option)
    drop.grid(row=2, column=2, padx=50)

    my_button = Button(top, text="OK", command=get_city)
    my_button.grid(row=4, column=2)

def dish_category(x):
    orders.clear()
    cost = 0
    print(city)
    for widget in root.winfo_children():
        widget.grid_forget()
    conn = sqlite3.connect('database_new.db')
    c = conn.cursor()
    c.execute("SELECT *,rowid FROM "+city+" WHERE d_category="+f"'{x}'")
    global items
    items = c.fetchall()
    conn.commit()
    conn.close()

    dish = StringVar()
    n = 0
    for item in items:
        Radiobutton(root, text=item[1], value=item[6], variable=dish).grid(column=0, sticky="w")
        label1 = Label(root, text=item[0]+"\t\t\t      "+"Rs."+str(item[3])).grid(column=3, stick="e")
        n += 1
    dish.set(items[0][6])

    open_rstrnt = Button(root, text="Open Restaurant", command=lambda: rstrnt(dish.get(), x))
    open_rstrnt.grid(row=2*n+2, column=3, sticky="e")

def main_window():
    pizza_img = PhotoImage(file="C:/Users/Danish/OneDrive/Documents/Python Project/images/WhatsApp Image 2024-04-19 at 21.34.18_f91f7faf.png")
    img_label = Label(image=pizza_img)

    pizza_btn = Button(root, text="pizza", command=lambda: dish_category("pizza"), pady=50, padx=50)
    pizza_btn.grid(row=1, column=0, pady=20, padx=20)
    burger_btn = Button(root, text="BURGERS", command=lambda: dish_category("burger"), pady=50, padx=50)
    burger_btn.grid(row=1, column=1, padx=20)
    NOODLES_btn = Button(root, text="NOODLES", command=lambda: dish_category("noodles"), pady=50, padx=48)
    NOODLES_btn.grid(row=1, column=2, padx=20)
    pasta_btn = Button(root, text="PASTA", command=lambda: dish_category("pasta"), pady=50, padx=52)
    pasta_btn.grid(row=2, column=0, pady=20, padx=20)
    sandwich_btn = Button(root, text="SANDWICH", command=lambda: dish_category("sandwich"), pady=50, padx=55)
    sandwich_btn.grid(row=2, column=1, padx=20)
    thali_btn = Button(root, text="THALI", command=lambda: dish_category("thali"), pady=50, padx=59)
    thali_btn.grid(row=2, column=2, padx=20)
    soup_btn = Button(root, text="SOUP", command=lambda: dish_category("soup"), pady=50, padx=55)
    soup_btn.grid(row=3, column=0, pady=20, padx=20)
    beverages_btn = Button(root, text="BEVERAGES", command=lambda: dish_category("beverages"), pady=50, padx=45)
    beverages_btn.grid(row=3, column=1, padx=20)

open_window()  # Call open_window() first
root.mainloop()

