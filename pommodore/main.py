from tkinter import *
import math
from gtts import gTTS
import subprocess

# ---------------------------- CONSTANTS ------------------------------- #
DARK_BLUE = "#213555"
LIGHT_BLUE = "#4F709C"
GRAY = "#F0F0F0"
ORANGE = "#F7B168"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
mark = 0
repetitions = 0
timer = None

# ----------------------------- VOICE OBJECTS ---------------------------- #

language = 'en'  # Language code (e.g., 'en' for English)
slow = False     # Set to True for slower speech

short_break_voice = "Five minute break"
long_break_voice = "Twenty minute break"
focus_time_voice = "time to focus"

short_break_tts = gTTS(short_break_voice, lang=language, slow=slow)
short_break_mp3 = "short_break.mp3"
short_break_tts.save(short_break_mp3)

long_break_tts = gTTS(long_break_voice, lang=language, slow=slow)
long_break_mp3 = "long_break.mp3"
long_break_tts.save(long_break_mp3)

focus_time_tts = gTTS(focus_time_voice, lang=language, slow=slow)
focus_time_mp3 = "focus_time.mp3"
focus_time_tts.save(focus_time_mp3)


# ---------------------- BRING WINDOW TO THE FRONT OF SCREEN -------- #


# ---------------------- VOICE FUNCTIONS ---------------------------- #
def short_break_time():
    sound_file = "short_break.mp3"  # Replace with the path to your audio file
    subprocess.call(["afplay", sound_file])


def long_break_time():
    sound_file = "long_break.mp3"  # Replace with the path to your audio file
    subprocess.call(["afplay", sound_file])


def focus_time():
    sound_file = "focus_time.mp3"
    subprocess.call(["afplay", sound_file])


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(text_timer, text="00:00")
    label_timer.config(text="Focus Countdown", fg=DARK_BLUE)
    check.config(text="Turns: \n\n0/4")
    start_button.config(state="normal")
    global repetitions
    repetitions = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global repetitions
    repetitions += 1

    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if repetitions % 8 == 0:
        count_down(long_break)
        long_break_time()
        label_timer.config(text="20min Break", fg=DARK_BLUE)

    elif repetitions % 2 == 0:
        count_down(short_break)
        short_break_time()
        label_timer.config(text="5min Break", fg=DARK_BLUE)
    else:
        count_down(work_time)
        focus_time()
        label_timer.config(text="Time to focus", fg=DARK_BLUE)

    start_button.config(state="disabled")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global repetitions, mark

    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(text_timer, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        reps_done = math.floor(repetitions/2)
        for _ in range(reps_done):
            mark += 1
        check.config(text=f"{mark}/4")

# ---------------------------- UI SETUP ------------------------------- #


# create window
window = Tk()
window.title("Focus timer App")
window.config(padx=70, pady=40, bg=GRAY)

# first label for "Timer"
label_timer = Label(text="Focus countdown", font=(FONT_NAME, 46, "normal", "bold"))
label_timer.grid(column=1, row=0)
label_timer.config(bg=GRAY, fg=LIGHT_BLUE, pady=10)

# create the canvas image
canvas = Canvas(width=210, height=234, bg=GRAY, highlightthickness=0)
tomato = PhotoImage(file="pommodore/timer.png")
canvas.create_image(100, 112, image=tomato)
text_timer = canvas.create_text(98, 155, text="00:00", fill=ORANGE, font=(FONT_NAME, 40, "bold"))
canvas.grid(column=1, row=1)


# start button
start_button = Button(text="Start", highlightthickness=0, borderwidth=0, command=start_timer, highlightbackground=GRAY,
                      width=7, height=2)
start_button.grid(column=0, row=3)


# second label for "check"
check = Label(text=f"Turns: \n\n{mark}/4", font=(FONT_NAME, 24, "normal"), fg=DARK_BLUE, bg=GRAY)
check.grid(column=1, row=4)

# reset button
reset_button = Button(text="Reset", highlightthickness=0, borderwidth=0, command=reset_timer, highlightbackground=GRAY,
                      width=7, height=2)
reset_button.grid(column=2, row=3)


# make sure it runs non-stop
window.mainloop()
