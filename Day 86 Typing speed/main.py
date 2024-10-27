import tkinter as tk
import random

userin = ''
COUNT = 20
SCORE = 0

#----------------TIMER----------------
def count_down(count):
    label_timer.configure(text=f'Time left: {count}')
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    if count == 0:
        label_words.grid_forget()
        entry_input.grid_forget()
        label_score.grid_forget()
        label_timer.grid_forget()
        label_final_score.config(text=f'Your final score is {score} words per minute with {round(score/i * 100)}% accuracy!')
        label_final_score.grid(column=0, row=1, columnspan=2)

        button_reset.config(text = "Do you want to try again?", command=reset)
        button_reset.grid(column=0, row=3)


#----------------WORDS-----------------
with open('words.txt', mode='r') as file:
    words = file.read().splitlines()
    random.shuffle(words)
    print(words)


def show_words(j):
    current_words.set(f'{words[j]} {words[j + 1]} {words[j + 2]} {words[j + 3]} {words[j + 4]}')

#-----------------CHECKING IF WORD WAS WRITTEN CORRECTLY----------------

def check(content, j):
    if content == ' ' + words[j]:
        return True

#------------------RESET-------------------

def reset():
    global i, score, count
    label_timer.grid(column=0, row=2)
    label_words.grid(column=0, row=0)
    label_score.grid(column=1, row=2)
    entry_input.grid(column=0, row=1)
    entry_input.focus()
    label_final_score.grid_forget()
    button_reset.grid_forget()

    i = 0
    score = SCORE
    count = COUNT
    label_timer.configure(text=f'Time left: {count}')
    label_score.config(text=f' Current score: {score}')

    random.shuffle(words)
    show_words(0)
#------------------GUI------------------
i = 0
score = SCORE
count = COUNT

window = tk.Tk()
window.title('Typing Speed App')
window.config(padx=200, pady=200)

# Current words variable
current_words = tk.StringVar()
show_words(0)

# Timer, words, score labels
label_timer = tk.Label(text=f'Time left: {count}')
label_timer.grid(column=0, row=2)

label_words = tk.Label(textvariable=current_words)
label_words.grid(column=0, row=0)

label_score = tk.Label(text=f' Current score: {score}')
label_score.grid(column=1, row=2)

label_final_score = tk.Label(text='')

# Button for later
button_reset  = tk.Button()

# entry input
entry_input = tk.Entry(textvariable=userin, width=50)
entry_input.grid(column=0, row=1)
entry_input.insert(0, ' ')
entry_input.focus()

def process(event=None):
    global i, score

    content = entry_input.get()
    entry_input.delete(0, 'end')

    if check(content, i) == True:
        score += 1
        label_score.config(text=f' Current score: {score}')

    show_words(i+1)
    i += 1
    #start the count_down after first word
    if i == 1:
        count_down(count)

entry_input.bind('<space>', process)
# here we do process function if space was hit

window.mainloop()

