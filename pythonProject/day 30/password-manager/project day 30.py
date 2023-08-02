from tkinter import *
from tkinter import messagebox
import pyperclip
import pandas
import random
import json
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= 5
    nr_symbols = 5
    nr_numbers = 5

    password_list = []

    for char in range (1, nr_letters + 1):
        r_c = random.choice(letters)
        password_list.append(r_c)

    for sym in range (1, nr_symbols + 1):
        r_s = random.choice(symbols)
        password_list.append(r_s)

    for num in range(1,nr_numbers + 1):
        r_n = random.choice(numbers)
        password_list.append(r_n)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    entry_3.delete(0,END)
    entry_3.insert(0,password)
    pyperclip.copy(password)
    pyperclip.paste()
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website_name = entry_1.get()
    email = entry_2.get()
    password = entry_3.get()
    new_data = {
        website_name : {
        "email":email,
        "password":password,
    }
    }
    if website_name == "":
        messagebox.showerror(title="Error",message="Website name is empty !")
    elif email == "":
        messagebox.showerror(title="Error",message="Email is empty !")
    elif password == "":
        messagebox.showerror(title="Error", message="Password is empty !")
    else:
        is_ok = messagebox.askokcancel(title="Save", message="Do you want to save the information?")
        if is_ok:
            try :
                with open("password_file.json", mode="r") as file:
                   data = json.load(file)

            except FileNotFoundError :
                with open("password_file.json", mode="w") as file:
                   json.dump(new_data, file, indent=4)

            else:
                with open("password_file.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)

                with open("password_file.json", mode="w") as file:
                    json.dump(data, file, indent=4)

            finally:
                entry_1.delete(0,END)
                entry_2.delete(0,END)
                entry_3.delete(0,END)

def Search():
    website = entry_1.get()
    try:
        with open("password_file.json") as file:
            data = json.load(file)
    except FileNotFoundError:
            messagebox.showerror(title="Error",message="No Data File Found!")
    else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"Email/Username: {email}\nPassword: {password}")
            else:
                messagebox.showerror(title="Error", message=f"No Details of {website} currently exists!")

            # ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(pady=50,padx=50)
window.title("Password Manager")

canvas = Canvas(width=200,height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(column=1,row=0)

#label 1
label_1 = Label(text="Website:")
label_1.grid(column=0,row=1)
#label 2
label_2 = Label(text="Email/Username:")
label_2.grid(column=0,row=2)
#label 3
label_3 = Label(text="Password:")
label_3.grid(column=0,row=3)

# entry 1
entry_1 = Entry(width=21)
entry_1.grid(row=1,column=1,columnspan=1)
entry_1.focus()
# entry 2
entry_2 = Entry(width=35)
entry_2.grid(row=2,column=1,columnspan=2)
# entry 3
entry_3 = Entry(width=21)
entry_3.grid(row=3,column=1,columnspan=1)

# button 1
button_1 = Button(text="Generate Password",command=password_generator)
button_1.grid(row=3,column=2,columnspan=1)
# button 2
button_2 = Button(text="Add",width=36,command=add)
button_2.grid(row=4,column=1,columnspan=2)
#button 3
button_3 = Button(text="Search",command=Search,width=13,bg="#0000FF")
button_3.grid(row=1,column=2,columnspan=1)

window.mainloop()