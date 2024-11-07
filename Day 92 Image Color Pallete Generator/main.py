import os
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename
from PIL import Image
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd

UPLOAD_FOLDER = './static/'
ALLOWED_EXTENSIONS = {'jpg', 'png'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#------------------FIND MOST COMMON COLORS-----------------
def most_common_colors(path):
    picture = Image.open(path)
    pic_array = np.array(picture)
    rows = pic_array.shape[0]
    columns = pic_array.shape[1]

    all_colors = []
    for i in range(0,rows):
        for j in range(0,columns):
            all_colors.append(pic_array[i,j,0:3].astype('int'))
            # print(pic_array[i,j,0:3])
    df = pd.DataFrame(all_colors)
    top_colors = df.groupby([0,1,2]).size().sort_values(ascending=False)[0:10]
    top_colors_df = pd.DataFrame(top_colors)
    print(top_colors_df)
    return top_colors_df


import seaborn as sns




@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['myFile']
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        if file:
            top_colors_df = most_common_colors(path)

            colors = []
            # iloc for getting hold of a row. Then because of grouping, those rows have names
            for i in range(0,10):
                rgb_color = (int(top_colors_df.iloc[i].name[0]), int(top_colors_df.iloc[i].name[1]), int(top_colors_df.iloc[i].name[2]))

                hex_color = '#%02x%02x%02x' % rgb_color
                colors.append(hex_color)

            # create plot
            print(colors)
            sns.palplot(colors, size=1.5)
            ax = plt.gca()
            plt.subplots_adjust(left=0)
            for i, name in enumerate(colors):
                ax.text(i-0.2, 0.62, name)
            plt.savefig('./static/img/plot.png')
            return render_template('generate.html', file=filename)
    return render_template('index.html')


@app.route('/delete/<file>')
def delete(file):
    os.remove(f'./static/{file}')
    return redirect('/')
@app.route('/generate')
def generate():
    return render_template('generate.html')
app.run(debug=True)