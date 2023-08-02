from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("POMODORO")
window.config(padx=100,pady=50,bg=YELLOW)

# label 1
label_1 = Label(text="Timer",font=(FONT_NAME,35,"bold"),bg=YELLOW,fg=GREEN)
label_1.grid(column=1,row=0)


canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text = canvas.create_text(100,130,text="00 : 00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global reps,timer
    count_minute = math.floor(count / 60)
    count_second = count % 60
    if count_minute < 10:
        count_minute = f"0{count_minute}"
    if count_second < 10:
        count_second = f"0{count_second}"
    canvas.itemconfig(timer_text,text=f"{count_minute}:{count_second}")
    if count > 0 :
        timer = window.after(1000,countdown,count - 1)
    else:
        Start_timer()
        marks =""
        for _ in range(math.floor(reps/2)):
            marks += "✅"
            label_2.config(text=marks)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def Start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    if reps % 2 != 0 :
        countdown(work_sec)
        label_1.config(text="Work",font=(FONT_NAME,35,"bold"),bg=YELLOW,fg=GREEN)
    elif reps % 8 == 0 :
        countdown(long_break)
        label_1.config(text="Long Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED)
    else:
        countdown(short_break)
        label_1.config(text="Short Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global timer,reps
    window.after_cancel(timer)
    label_1.config(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    label_2.config(text="")
    reps = 0


# label 2
label_2 = Label(font=(FONT_NAME,10,"bold"),bg=YELLOW)
label_2.grid(column=1,row=3)

# button 1
button_1 = Button(text="Start",font=(FONT_NAME,10,"bold"),bg=YELLOW,highlightthickness=0,command=Start_timer)
button_1.grid(column=0,row=2)

# button 2
button_2 = Button(text="Reset",font=(FONT_NAME,10,"bold"),bg=YELLOW,highlightthickness=0,command=reset_timer)
button_2.grid(column=2,row=2)



window.mainloop()