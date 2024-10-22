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

# Initialize global variables
reps = 0
timer = None

# ---------------------------- TIMER FUNCTION ------------------------------- # 
def reset_timer():
    """Resets the timer and UI elements."""
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tick_label.config(text="")
    reps = 0

def start_timer():
    """Starts the timer and manages the session types."""
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)

def count_down(count):
    """Countdown function to update timer display."""
    count_min = math.floor(count / 60)
    count_sec = count % 60
    count_sec = f"0{count_sec}" if count_sec < 10 else count_sec
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        update_ticks()

def update_ticks():
    """Update the ticks label with the number of completed work sessions."""
    work_sessions = math.floor(reps / 2)
    ticks = "✓" * work_sessions
    tick_label.config(text=ticks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
icon = PhotoImage(file="tomato.png")
window.iconphoto(True, icon)
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas setup
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1)

# Labels setup
timer_label = Label(window, text="Timer", font=("Courier", 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=0, column=1, padx=10, pady=10)

tick_label = Label(window, text="", font=("Courier", 15, "bold"), bg=YELLOW, fg=GREEN)
tick_label.grid(row=3, column=1, padx=10, pady=10)

# Buttons setup
start_button = Button(window, 
                      text="Start", 
                      command=start_timer,
                      activebackground="grey", 
                      activeforeground="white")
start_button.grid(row=3, column=0, padx=20, pady=20)

reset_button = Button(window, 
                      text="Reset", 
                      command=reset_timer,
                      activebackground="grey", 
                      activeforeground="white")
reset_button.grid(row=3, column=2, padx=20, pady=20)

window.mainloop()
