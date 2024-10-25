from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog


#----------------- WATERMARK ------------

def generate(str):
    global combined

    im = Image.open(filename).convert('RGBA')
    txt = entry_text.get()
    position = (int(entry_position.get().split(',')[0]), int(entry_position.get().split(',')[1]))
    opacity = int(int(entry_opacity.get())/100*255)

    text = Image.new('RGBA', im.size, (225, 255, 255, 0)) #text as new image with 0 opacity and size of initial picture

    font = ImageFont.truetype("Tests/fonts/NotoSans-Regular.ttf", 42)

    d = ImageDraw.Draw(text) # drawing on the text image
    d.text(position, text=txt, fill=(255, 0, 0, opacity), font=font)
    combined = Image.alpha_composite(im, text) #composing two pictures

    combined.show()

def upload_file(event=None):
    global filename
    filename = filedialog.askopenfilename()

    im = Image.open(filename)

    label_info = tk.Label(text=f'Your image has size {im.size}')
    label_info.grid(column=1, row=0)

def save_file():
    directory = filename.split('.')[-2]
    name = directory.split('/')[-1]
    new_directory = directory + '_edited.' + filename.split('.')[-1]

    combined.save(new_directory)


window = tk.Tk()
window.config(padx=50, pady=50)
window.title('Watermarking Desktop App')

button_choose = tk.Button(text='Choose file', command=upload_file)
button_choose.grid(column=0, row=0)

label_text = tk.Label(text='Choose text for your watermark:')
label_text.grid(column=0, row=1)

entry_text = tk.Entry()
entry_text.grid(column=1, row=1)

label_opacity = tk.Label(text='Choose the opacity (0-100)%:')
label_opacity.grid(column=0, row=2)

entry_opacity = tk.Entry()
entry_opacity.grid(column=1, row=2)

label_position = tk.Label(text='Choose the position as (x,y):')
label_position.grid(column=0, row=3)

entry_position = tk.Entry()
entry_position.grid(column=1, row=3)

button_generate = tk.Button(text='Generate image', command=lambda: generate(filename)) #putting arguments into function (not need here)
button_generate.grid(column=1, row=4)

button_save = tk.Button(text='Save your image', command=save_file)
button_save.grid(column=1, row=5)

window.mainloop()









