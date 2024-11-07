import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from collections import Counter
import pandas as pd

path = './static/Screenshot_from_2024-11-01_11-27-40.png'
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
print(top_colors)
dff = pd.DataFrame(top_colors)
# print(dff.name)

print(int(dff.iloc[2].name[0]))

print((int(dff.iloc[0].name[0]), int(dff.iloc[0].name[1]), int(dff.iloc[0].name[2])))

print('#%02x%02x%02x' % (24, 24, 27))


