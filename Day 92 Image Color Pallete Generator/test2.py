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

list = []

a = np.array([1,1,1])
b = np.array([2,2,2])
c = pic_array[0,0,0:3]
d = np.array([1,2,3])

print(a.tolist())
list.append(a.tolist())
list.append(b.tolist())
print(list)

all_colors = []

for i in range(0,rows):
    for j in range(0,columns):
        all_colors.append(pic_array[i,j,0:3].astype('str'))

print(all_colors[0])
# print(all_colors.count([24,24,27]))

cnt = Counter(all_colors)
