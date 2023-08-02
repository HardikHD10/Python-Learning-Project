from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(250,100)
window.config(pady=20,padx=20)

# input
input = Entry(width=10,font=("Georgia",12,"bold"))
input.grid(row=0,column=1)

def milestokm():
    miles = float(input.get())
    y = 1.60934 * miles
    km = round(y, 2)
    return km

# label 1
label_1 = Label(text="Miles",font=("Georgia",12,"bold"))
label_1.grid(row=0,column=2)

# label 2
label_2 = Label(text="is equal to",font=("Georgia",12,"bold"))
label_2.grid(row=1,column=0)

# label 3
label_3 = Label(font=("Georgia",12,"bold"))
label_3.grid(row=1,column=1)

# label 4
label_4= Label(text="KM",font=("Georgia",12,"bold"))
label_4.grid(row=1,column=2)


# button
def buttonpressed():
        label_3.config(text=milestokm())

button = Button(text="Calculate",font=("Georgia",12,"bold"),command=buttonpressed)
button.grid(row=2,column=1)
window.mainloop()