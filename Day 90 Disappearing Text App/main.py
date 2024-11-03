import string
import tkinter as tk


nr_of_letters = 0
COUNT = 5
still_typing = False

#----------------WINDOW----------------
window = tk.Tk()
window.config(width=800, height=600, padx=50, pady=50)
window.title('Disappearing Text App')


#---------------Timer-------------------
def count_down(count):
    print(count)
    global nr_of_letters, still_typing

    # if we are still typing, start the timer from 0
    if still_typing:
        still_typing = False
        window.after(1000, count_down, 0)

    # else timer goes up
    elif count < COUNT:
        window.after(1000, count_down, count + 1)

    # and if it hits COUNT then we clear and reset nr of letters
    else:
        main_entry.delete(index1="1.0", index2='end')
        nr_of_letters = 0


#---------------Widgets------------------
main_label = tk.Label(text='Start typing. After 5 seconds the text will disappear:')
main_label.grid(column=0, row=0)

main_entry = tk.Text(width=50)
main_entry.focus()
main_entry.grid(column=0, row=1)

# event - any action input by user (so character, enter etc)
def check(event):
    global nr_of_letters, still_typing

    # if any ascii_letter or space is hit we increase nr of letters and set "still_typing" to true
    if event.char in string.ascii_letters or event.char == ' ':
        nr_of_letters += 1
        still_typing = True

    # starting timer after first letter is put
    if nr_of_letters == 1:
        count_down(0)

# binding text / entry widget to a key (any key in this case) and if the key is inserted, we call function 'check'
main_entry.bind('<Key>', check)


window.mainloop()